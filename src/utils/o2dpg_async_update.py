#!/usr/bin/env python3

import sys
import argparse
from os.path import exists, join, abspath, dirname, expanduser
from os import makedirs
from time import time
from datetime import datetime
import yaml
from subprocess import Popen, PIPE, STDOUT
from shlex import split as sh_split
from shutil import copyfile
import logging


### Directories

# where the final YAMLs fo after cherry picking
PACKAGE_OUTPUT_DIRECTORY = 'o2dpg_cherry_picks'
# a directory that can be used to keep track
ASYNC_DIR = join(expanduser('~'), '.o2dpg_async_update')


### Package definitions

# the documentation package
DPG_DOCS = {'name': 'dpg-docs',
            'upstream': 'git@github.com:AliceO2Group/dpg-documentation.git',
            'dir': 'dpg-documentation',
            'default_branch': 'main'}


### Defaults for the concerned packages

# upstream: where the remote repository lives
# http: to be able to build urls
# name: the name of the repository
# dir: the directory where the repository will live locally
# default_branch: the default branch of the package to know where to cherry-pick from

# per package
DEFAULTS_O2 = {'upstream': 'git@github.com:AliceO2Group/AliceO2.git',
               'http': 'https://github.com/AliceO2Group/AliceO2',
               'name': 'O2',
               'dir': 'O2',
               'default_branch': 'dev'}

DEFAULTS_O2DPG = {'upstream': 'git@github.com:AliceO2Group/O2DPG.git',
                  'http': 'https://github.com/AliceO2Group/O2DPG',
                  'name': 'O2DPG',
                  'dir': 'O2DPG',
                  'default_branch': 'master'}

DEFAULTS_O2PHYSICS = {'upstream': 'git@github.com:AliceO2Group/O2Physics.git',
                      'http': 'https://github.com/AliceO2Group/O2Physics',
                      'name': 'O2Physics',
                      'dir': 'O2Physics',
                      'default_branch': 'master'}

DEFAULTS_QC = {'upstream': 'git@github.com:AliceO2Group/QualityControl.git',
               'http': 'https://github.com/AliceO2Group/QualityControl',
               'name': 'QualityControl',
               'dir': 'QualityControl',
               'default_branch': 'master'}


# put the defaults together into one dictionary that can be used if needed
DEFAULTS = {'AliceO2': DEFAULTS_O2,
            'O2DPG': DEFAULTS_O2DPG,
            'O2Physics': DEFAULTS_O2PHYSICS,
            'QualityControl': DEFAULTS_QC}

# add some common fields to the defaults
for package_defaults in DEFAULTS.values():
    # provide an empty list of commits
    package_defaults['commits'] = []
    # to flag if successful, None indicates that nothing has been done yet
    package_defaults['status_cherry_pick'] = None
    # a list of commits to be reverted first
    package_defaults['revert'] = []

# Aliases for packages that are often enough called like this
# use that to unify the naming across this tool
PACKAGE_ALIASES = {'O2': 'AliceO2',
                   'QC': 'QualityControl'}

# Required keys for each package
REQUIRED_KEYS = ['name', 'upstream', 'start_from', 'target_tag']


### Some more global variables that are useful
UNKNOWN_OPERATOR = 'UNKNOWN OPERATOR'
UNKNOWN_REVISION = 'UNKNOWN REVISION'
NO_LABEL = 'NO LABEL'
UNKNOWN_TIMESTAMP = 'UNKNWON TIMESTAMP'

# Play a trick here to be able to use a global log file which will be the single element of this list.
# By doing it like this, we can manipulate this list throughout runtime and changes will be visible to everyone
# (as long as we only append or pop)
LOG_FILE = []


#########################################
# Global and somewhat generic utilities #
#########################################
def get_logger():
    return logging.getLogger('async_sw_logger')


def run_command(cmd, cwd=None, stdout_list=None):
    """
    Run a command

    Write to logfile or each line to a list.

    NOTE: This will not handle pipes!
    """
    logger = get_logger()

    stdout, stderr = (None, None) if not logger and stdout_list is None else (PIPE, STDOUT)
    p = Popen(sh_split(cmd), cwd=cwd, stdout=stdout, stderr=stderr, universal_newlines=True)

    if logger:
        logger.debug(cmd)

    if logger or stdout_list:
        for line in p.stdout:
            line = line.strip()
            if logger:
                logger.debug(line)
            if stdout_list is not None:
                stdout_list.append(line)

    # always wait until it is finished
    p.wait()

    return p.returncode


def read_yaml(path):
    """
    Read YAML into a dictionary
    """
    logger = get_logger()
    logger.info('Read YAML file from %s', path)
    try:
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    except Exception:
        logger.error('Could not read file.')
        return None


def write_yaml(d, path):
    """
    Write dictionary to YAML
    """
    logger = get_logger()
    logger.info('Write YAML file to %s', path)
    with open(path, 'w') as f:
        yaml.safe_dump(d, f)


#########################################
# Package- and config-related utilities #
#########################################
def get_default(package_name):
    """
    Get the default dictionary of a package by name
    """
    try:
        return DEFAULTS[package_name]
    except KeyError:
        logger = get_logger()
        logger.warning('Unknown package name. Available packages:')
        for package_name in DEFAULTS:
            logger.warning('  - %s', package_name)
    return {}


def complete_package_config_with_defaults(package, labels=None):
    """
    Add some default values if not set
    This works inline on the package dict
    """
    # First, let's set the name to the GitHub upstream repo name in case of aliases
    try:
        package['name'] = PACKAGE_ALIASES.get(package['name'], package['name'])
    except KeyError:
        get_logger.error('Key "name" is missing in the package configuration')
        return False
    package['labels'] = labels or []
    package['commits_cherry_picked'] = {'success': [], 'skipped': [], 'failed': []}
    package_defaults = get_default(package['name'])
    for key, default_value in package_defaults.items():
        package[key] = package.get(key, default_value)

    return True


def check_package_config(package):
    """
    Check a package config

    1. If it is complete
    2. If certain criteria are met
    """
    logger = get_logger()
    logger.info('Check configuration of package %s.', package["name"])
    is_sane = True
    for key in REQUIRED_KEYS:
        if key not in package:
            is_sane = False
            logger.error('%s not in package configuration.', key)

    if not package.get('target_tag', "").startswith('async-'):
        is_sane = False
        logger.error('The target_tag must start with "async-", however, the name requested is "%s"', package.get('target_tag', ""))

    return is_sane


def get_packages(config):
    """
    Get the package dicts from config dict
    """
    try:
        return config['packages']
    except KeyError:
        get_logger().error('Cannot find packages. Make sure to specify a list of packages under the key "packages".')
    return None


def get_labels(config):
    """
    Get the labels from config dict
    """
    try:
        return config['labels']
    except KeyError:
        get_logger().error('Cannot get labels. Make sure to specify a list of labels under the key "labels".')
    return None


def check_tag_config_by_user(config, labels):
    """
    Ask the user again about their settings

    This is to give the user another chance to check their setting before they cherry-pick
    """
    logger = get_logger()
    logger.info('Cross-checking user config')
    logger.info('Are you sure you want to tag for the following labels [y/N]?\n%s', '\n'.join(labels))
    yes_no = input()

    if not yes_no or yes_no.lower() != 'y':
        logger.info('It seems you are not satisfied with your label settings.')
        return False

    for package in get_packages(config):
        logger.info('Do you want to tag the following package [y/N]?\nName: %s\nStart from: %s\nTarget tag: %s', package['name'], package['start_from'], package['target_tag'])
        yes_no = input()
        if not yes_no or yes_no.lower() != 'y':
            logger.info('It seems you are not satisfied with your tag settings.')
            return False

    return True


#################################
# Pure Git wrappers for package #
#################################
def git_add(package, paths):
    """
    Git wrapper for git add
    """
    return run_command(f'git add {paths}', cwd=package['dir']) == 0


def git_commit(package, message):
    """
    Git wrapper for git commit
    """
    return run_command(f'git commit -m "{message}"', cwd=package['dir']) == 0


def git_push(package):
    """
    Git wrapper for git push
    """
    return run_command(f'git push origin {package["default_branch"]}', cwd=package['dir']) == 0


def git_verify(package, rev=None):
    """
    Git wrapper for git rev-parse --verify
    """
    rev = rev or package['target_tag']
    return run_command(f'git rev-parse --verify {rev}', cwd=package['dir']) == 0


############################################################
# Git-related utilities with some additional functionality #
############################################################
def clone(package):
    """
    Clone from remote
    """
    logger = get_logger()
    logger.info('Cloning %s', package['name'])
    cwd = package['dir']
    if not exists(cwd) and run_command(f'git clone {package["upstream"]} {cwd}') != 0:
        logger.error('Failed to clone repo from %s to %s.', package['upstream'], cwd)
        return False
    return True


def fetch(package):
    """
    Fetch everything from remote including tags
    """
    get_logger().info('Fetching package %s', package['name'])
    cwd = package['dir']
    if not exists(cwd):
        return clone(package)
    return run_command('git fetch origin --tags', cwd=cwd) == 0


def update_branch_from_remote(package, branch=None):
    """
    Update the a branch of a package to the state of its corresponding upstream
    """
    logger = get_logger()
    branch = branch or package['default_branch']
    logger.info('Update branch %s from remote.', branch)
    cwd = package['dir']
    if run_command(f'git checkout {branch}', cwd=cwd) != 0 and run_command(f'git reset --hard origin/{branch}', cwd=cwd) != 0:
        logger.error('Cannot update default branch %s of package %s', branch, package['name'])
        return False
    return True


def expand_commit_hash(package, commit):
    """
    Always return the long commit hash
    """
    out = []
    run_command(f'git rev-parse {commit}', cwd=package['dir'], stdout_list=out)
    return out[0]


def get_full_history(package, branch=None):
    """
    Get the full commit history (hashes) from oldest to most recent
    """
    if not branch:
        branch = package['default_branch']

    out = []
    run_command(f'git rev-list {branch}', cwd=package['dir'], stdout_list=out)

    return list(reversed(out))


def sort_commits(package, according_to_list=None, commits=None, ignore_different_length=False):
    """
    Get the list of commits sorted from oldest to most recent
    """
    logger = get_logger()

    if not commits:
        commits = package['commits']

    commits = [expand_commit_hash(package, commit) for commit in commits]

    # remove potential duplicates
    commits = list(set(commits))

    logger.info('Sort commits from oldest to most recent')

    if according_to_list:
        out = according_to_list
    else:
        out = get_full_history(package)

    out = [o for o in out if o in list(set(commits))]

    if len(out) != len(commits) and not ignore_different_length:
        logger.error('During sorting, some of the original commits seem not to be recognised.')
        return None

    return out


################################
# Specific cherry-pick helpers #
################################
def prepare_for_cherry_pick(package):
    """
    Checkout a repo at a certain branch or tag

    1. If the repo does not yet exist locally, clone.
    2. Fetch everything (including tags) if requested
    3. Checkout branch/revision

    If a branch is requested to be checked-out, do so but for now move to a temporary branch
    """
    logger = get_logger()

    logger.info('Prepare for cherry-picking in package %s.', package['name'])

    # check this out
    revision_checkout = package['start_from']
    cwd = package['dir']

    if run_command(f'git checkout {revision_checkout}', cwd=cwd) != 0:
        logger.error('Cannot checkout %s in %s.', revision_checkout, cwd)
        return False

    # verify that all commits that we are about to cherry-pick live in history of the default branch
    commits_not_contained_in_default_branch = []
    for commit in package['commits']:
        if run_command(f'git branch {package["default_branch"]} --contains {commit}', cwd=cwd) != 0:
            commits_not_contained_in_default_branch.append(commit)

    if commits_not_contained_in_default_branch:
        logger.error('The following commits are not in the history of the default branch %s of package %s:\n%s', package['default_branch'], package['name'], '\n  '.join(commits_not_contained_in_default_branch))
        return False

    out = []
    is_detached = False
    run_command('git status', cwd=cwd, stdout_list=out)
    for line in out:
        if 'HEAD detached at' in line:
            is_detached = True
            break

    if not is_detached:
        # we are on a branch, create a temporary one where the work will be done
        # only when everything went fine we will reset the actual branch to the temporary one
        if not update_branch_from_remote(package, revision_checkout):
            return False
        branch_tmp = f'{revision_checkout}-for-{package["target_tag"]}'
        package['start_from_cache'] = revision_checkout
        # so for now we basically pretend as if this was the branch
        package['start_from'] = branch_tmp
        logger.info('Prepare temporary branch %s to work on', branch_tmp)
        if run_command(f'git checkout -B {branch_tmp}', cwd=cwd) != 0:
            logger.error('Cannot create temporary branch %s in %s.', branch_tmp, cwd)
            return False

    return True


def cherry_pick_single(cwd, commit):
    """
    Utility to cherry-pick one commit
    """
    cmd = f'git cherry-pick -x {commit}'
    stdout_lines = []
    if run_command(cmd, cwd=cwd, stdout_list=stdout_lines) != 0:
        search_for_skip = "nothing to commit, working tree clean"
        search_for_bad_object = "bad object"
        for line in stdout_lines:
            if search_for_skip in line:
                run_command("git cherry-pick --skip", cwd=cwd)
                return -1
            if search_for_bad_object in line:
                return stdout_lines
        run_command("git cherry-pick --abort", cwd=cwd)
        return stdout_lines
    return 0


def git_cherry_pick(package):
    """
    Cherry-pick for this package

    Go through a list of provided commits and try to apply them
    """
    logger = get_logger()

    package_name = package['name']

    logger.info('Run cherry-picking in package %s', package_name)

    if not package['commits']:
        logger.warning(f'No commits found to cherry-pick for package {package_name}')
        return True

    commits_success = package['commits_cherry_picked']['success']
    commits_failed = package['commits_cherry_picked']['failed']
    commits_skipped = package['commits_cherry_picked']['skipped']

    cwd = package['dir']

    sorted_commits = sort_commits(package)
    if sorted_commits is None:
        logger.error('Commits of package %s could not be sorted', package['name'])
        return False

    for commit in sorted_commits:
        # get the long hash to always use that for consistency
        ret = cherry_pick_single(cwd, commit)
        if isinstance(ret, list):
            logger.error('There was a problem cherry-picking %s', commit)
            for line in ret:
                print(f'  {line}')
            logger.info('Trying to continue')
            commits_failed.append(commit)
            continue
        if ret < 0:
            commits_skipped.append(commit)
            continue
        print("SUCCESS ", commit)
        commits_success.append(commit)

    logger.info('Cherry-picking\n  SUCCESS: %d\n  SKIPPED: %d\n  FAILED: %d', len(commits_success), len(commits_skipped), len(commits_failed))

    # set the status
    package['status_cherry_pick'] = not commits_failed

    if commits_failed:
        # Reset to initial SHA of start tag or branch
        logger.info('Cherry-picking has failed, resetting everything in package %s', package['name'])
        run_command(f'git reset --hard HEAD~{len(commits_success)}', cwd=cwd)
        return False

    return True


def git_tag(package, retag=False, reset=True):
    """
    Almost the same as simply tagging

    However, do some checks in addition and emit errors if any.
    Also, reset to where we started if tagging is not possible
    """
    package_name = package["name"]
    tag = package['target_tag']

    logger = get_logger()
    logger.info('Attempt to tag %s with %s', package_name, tag)

    cwd = package['dir']

    if run_command(f'git rev-parse --verify {tag}', cwd=cwd) == 0:
        if retag and run_command(f'git tag -d {tag}', cwd=cwd) != 0:
            logger.error('Was asked to re-tag package %s with %s, but failed to remove existing tag.', package_name, tag)
            return False

    if run_command(f'git tag {tag}', cwd=cwd) != 0:
        if reset:
            run_command(f'git reset --hard HEAD~{len(package["commits_cherry_picked"]["success"])}', cwd=cwd)
        logger.error('Cannot tag %s with tag %s, reset everything.', cwd, tag)
        return False

    return True


###################################################
# Additional helpers for the cherry-pick workflow #
###################################################
def build_single_package_identifier(package):
    """
    Short wrapper to get a well-defined identifier per package
    """
    return f'{package["name"]}_{package["start_from"]}_{package["target_tag"]}'


def make_package_summary_path(package, summary_dir):
    """
    Extend the wrapper by the YAML extension and prepend an output directory
    """
    return join(summary_dir, f'{build_single_package_identifier(package)}.yaml')


def write_single_summary(package, out_dir):
    """
    Write the package dictionary to YAML
    """
    if not exists(out_dir):
        makedirs(out_dir)
    out_file = make_package_summary_path(package, out_dir)
    write_yaml(package, out_file)


def closure(package):
    """
    Conduct kind of a closure test to see if all commits went in, tags are at the correct place
    """
    cwd = package['dir']
    tag = package['target_tag']
    package_name = package['name']

    logger = get_logger()

    logger.info('Verify %s.', package_name)

    if run_command(f'git rev-parse --verify {tag}', cwd=cwd) != 0:
        logger.error('Package %s does not contain tag %s which was requested', package_name, tag)
        return False

    # check if HEAD is at the target tag
    rev_target_tag = []
    run_command(f'git rev-parse {tag}', cwd=cwd, stdout_list=rev_target_tag)
    rev_target_head = []
    run_command('git rev-parse HEAD', cwd=cwd, stdout_list=rev_target_head)

    if rev_target_tag[0] != rev_target_head[0]:
        logger.error('Hashes of HEAD and %s are different: %s != %s', tag, rev_target_tag[0], rev_target_head[0])
        return False

    if package['commits_cherry_picked']['failed']:
        logger.error('Package %s has failed commits.', package_name)
        return False

    commits_success = package['commits_cherry_picked']['success']

    if not commits_success and package['commits_cherry_picked']['skipped']:
        logger.warning('All proposed commits were found to be skipped for package %s. However, the tag %s is where it is supposed to be, so it should be fine.', package_name, tag)
        return True

    # now go commit-by-commit to see if there have been taken in order
    for i, commit in enumerate(reversed(package['commits_cherry_picked']['success'])):
        out = []
        run_command(f'git log HEAD~{i + 1}..HEAD~{i}', cwd=cwd, stdout_list=out)
        # since we die cherry-pick - x, we should find the following
        search_for = f'cherry picked from commit {commit}'
        found = False
        for line in out:
            if search_for in line:
                found = True
                break
        if not found:
            logger.error('During the verification, the commit %s was apparently not cherry-picked.', commit)
            return False

    return True


def finalise(package, operator):
    """
    Some final actions/afterburner steps after cherry-picking

    1. If the work was done on a temporary branch, now is the point to update the actual branch
    2. Add the title of the commit for successful and skipped commits
    """
    # finally set the operator
    package['operator'] = operator
    # collect branches and tags to be pushed
    to_push = [package['target_tag']]
    package['push'] = to_push
    # keep this in the final package configuration so that for the user there is some information in addition to the bare commit hashes
    subjects = []
    package['commits_success_subjects'] = subjects

    cwd = package['dir']

    # collect the commit subjects for successful commits
    for commit in package['commits_cherry_picked']['success']:
        out = []
        run_command(f'git log --pretty="%s" -n1 {commit}', cwd=cwd, stdout_list=out)
        subjects.append(out[0])

    # collect the commit subjects for skipped commits
    subjects = []
    package['commits_skipped_subjects'] = subjects
    for commit in package['commits_cherry_picked']['skipped']:
        out = []
        run_command(f'git log --pretty="%s" -n1 {commit}', cwd=cwd, stdout_list=out)
        subjects.append(out[0])

    # set this so that in the next step we can check if it was indeed cherry-picked and tagged correctly
    package['cherry_picked_tagged'] = int(time())

    # done here since we are not working on a temporary branch
    if 'start_from_cache' not in package:
        return

    # we are on a temporary branch, so first, we checkout the actual branch that we cached and set it to the current history
    run_command(f'git checkout -B {package["start_from_cache"]}', cwd=cwd)
    # delete the temporary branch to keep it tidy
    run_command(f'git branch -D {package["start_from"]}', cwd=cwd)
    # resort the package's branch/start_from information to what it was initially
    package["start_from"] = package["start_from_cache"]
    del package["start_from_cache"]
    # this branch needs to be pushed as well
    to_push.append(package["start_from"])


def push_tagged(package):
    """
    Push tagged package to remote
    """
    logger = get_logger()

    tag = package['target_tag']
    package_name = package['name']

    if not package.get('cherry_picked_tagged', None):
        logger.error('Package %s does not seem to tagged, not pushing', package_name)
        return False

    if not git_verify(package):
        logger.error('Package %s does not seem to contain tag %s.', package_name, tag)
        return False

    for to_push in package['push']:
        logger.info('Attempt to push %s of package %s', to_push, package_name)
        out = []
        if run_command(f'git push origin {to_push}', cwd=package['dir'], stdout_list=out) != 0:
            logger.error('Could not push %s due to', to_push)
            for line in out:
                print(line)
            return False

        for line in out:
            if 'Everything up-to-date' in line:
                logger.info('%s of package %s was already upstream.', to_push, package_name)
                return True

        logger.info('Pushed %s of package %s.', to_push, package_name)

    return True


############################################################
# Helpers for updating the documentation, create markdowns #
############################################################
def make_cherry_picked_markdown(package_name, url, commit_tuples, output_markdown):
    """
    Create a markdown that contains all commits along with their operator, labels and timestamps
    """
    with open(output_markdown, 'w') as f:
        # write the headline and the header of the table
        f.write(f'# Cherry-picked commits for {package_name}\n\n')
        f.write('| Commit subject | Tags first seen / associated labels |\n| --- | --- |\n')

        for commit_tuple in commit_tuples:
            commit_link = f'{url}/commit/{commit_tuple[1]}'
            tag_links = []
            for tag, label, operator, timestamp in zip(commit_tuple[3], commit_tuple[4], commit_tuple[5], commit_tuple[6]):
                # if the timestamp can be converted, great
                try:
                    timestamp = datetime.fromtimestamp(int(timestamp)).strftime("%Y-%m-%d %H:%M")
                except ValueError:
                    timestamp = UNKNOWN_TIMESTAMP

                tag_links.append(f'[{tag}]({url}/tree/{tag}) ({label}, {timestamp}, {operator})')

            f.write(f'| [{commit_tuple[2]}]({commit_link}) | {"<br>".join(tag_links)} |\n')


def make_history_markdown(package_name, url, history_list, output_markdown):
    """
    Create a markdown that contains the history of tags and what they are based on
    """
    with open(output_markdown, 'w') as f:
        # write the headline and the header of the table
        f.write(f'# Tagging history for {package_name}\n\n')
        f.write('| Started from | Created tag | Operator | Associated labels | Date |\n| --- | --- | --- | --- | --- |\n')

        for tag_step in history_list:
            # if the timestamp can be converted, great
            try:
                timestamp = datetime.fromtimestamp(int(tag_step[0])).strftime("%Y-%m-%d %H:%M")
            except ValueError:
                timestamp = UNKNOWN_TIMESTAMP

            start_from = f'[{tag_step[1]}]({url}/tree/{tag_step[1]})'
            tag = f'[{tag_step[2]}]({url}/tree/{tag_step[2]})'

            f.write(f'| {start_from} | {tag} | {tag_step[4]} | {"<br>".join(tag_step[3])} | {timestamp} |\n')


def make_label_markdown(labels_to_tag_package_map, output_markdown):
    """
    Create a markdown that contains the latest tags per label
    """
    with open(output_markdown, 'w') as f:
        # write the headline and the header of the table
        f.write('# Latest tags per label\n\n')
        f.write('| Label | Package, tags |\n| --- | --- |\n')

        for label, tags_per_package in labels_to_tag_package_map.items():

            if label == NO_LABEL:
                # if there is no label, skip it since it does not make sense
                continue

            package_write_string = []

            for package_name, package_tuple in tags_per_package.items():
                # if the timestamp can be converted, great
                try:
                    timestamp = datetime.fromtimestamp(int(package_tuple[0])).strftime("%Y-%m-%d %H:%M")
                except ValueError:
                    timestamp = UNKNOWN_TIMESTAMP
                package_write_string.append(f'{package_name}, [{package_tuple[1]}]({package_tuple[3]}/tree/{package_tuple[1]}), ({package_tuple[2]}, {timestamp})')

            f.write(f'| {label} | {"<br>".join(package_write_string)} |\n')


def collect_cherry_picked_commits(log_messages_to_check):
    """
    expect a list of logs from git

    find commit that each of the present commits originated from through cherry-picking
    """
    commits_cherry_picked = []

    search_for = 'cherry picked from commit'
    for line in log_messages_to_check:
        if search_for not in line:
            continue
        line = line.strip('\n').strip().split()
        commits_cherry_picked.append(line[-1][:-1])

    return commits_cherry_picked


def update_doc_impl(package, recreate_commits=False):
    """
    Update the documentation for one package
    """
    logger = get_logger()

    logger.info('Updating the documentation for package %s', package['name'])

    if not package['pushed']:
        logger.warning('Package %s has not been pushed')
        return False

    # the name of the package that we are working on
    package_name = package['name']

    # the directory where we store the YAML caches
    # These will always be extended and will at the end be used to create a markdown tables of commits and tags
    git_cache_dir_path = join('data', 'async_software_logging')
    cache_dir_path = join(DPG_DOCS['dir'], git_cache_dir_path)
    if not exists(cache_dir_path):
        makedirs(cache_dir_path)

    # the tag history is cached here
    git_tagging_history_file_path = join(git_cache_dir_path, 'tagging_history.yml')
    tagging_history_file_path = join(DPG_DOCS['dir'], git_tagging_history_file_path)

    # it has the tag history per package
    history_dict = read_yaml(tagging_history_file_path) or {key: {} for key in DEFAULTS.keys()}
    # and now we take the dictionary of the package we are working on
    history_package = history_dict[package_name]

    # there are 2 scenarios
    # 1. the package has a 'target_tag' field; this indicates that it comes from a cherry-pick session and we should add this tag and the information we have for that;
    #    in this case we set add_tag to that tag name
    # 2. the package does not have that field; so the only thing we can do is to collect tags and their commits without operator, label or 'start_from' information
    add_tag = None
    if 'target_tag' in package:
        add_tag = package['target_tag']
        # at the timestamp according to when this package was pushed
        # note that the timestamp is converted to a string to be compatible with what we get when we query a timestamp from git
        history_package[package['target_tag']] = [str(package['pushed']), package['start_from'], package['target_tag'], package['labels'], package['operator']]

    # get the dictionary for the commit history
    git_commit_file_path = join(git_cache_dir_path, 'commits.yml')
    commit_file_path = join(DPG_DOCS['dir'], git_commit_file_path)
    commits_tags_first_seen_map = read_yaml(commit_file_path) or {key: {} for key in DEFAULTS.keys()}

    if recreate_commits:
        # set to empty dictionary if file does not exist or if requested
        commits_tags_first_seen_map[package_name] = {}
    commits_tags_first_seen_map_package = commits_tags_first_seen_map[package_name]

    # collect all async-* tags in this package
    all_tags = []
    run_command('git for-each-ref --sort=creatordate --format \'%(refname) %(creatordate:unix)\' refs/tags', cwd=package['dir'], stdout_list=all_tags)
    all_tags = [at for at in all_tags if 'refs/tags/async-' in at]

    # run through all of these tags
    for tag_date in all_tags:
        # from the aobve git query, we have the tag and the timestamp. This timestamp is in fact the commit timestamp and not the tag's timestamp
        # since in most cases we do not have annotated tags which have no time attached
        tag_date = tag_date.split()
        # split into the tag name and the timestamp
        tag = tag_date[0][len('refs/tags/'):]
        created = tag_date[1]

        if tag in history_package and add_tag != tag and not recreate_commits:
            # if this tag is known already and if it is also not to be added, skip this assuming that we have everything already.
            # however, we go on if the commit history is requested to be recreated
            continue
        elif tag not in history_package:
            # only add this tag, if it is not there to not potentially overwrite one we want to add
            tag_history_tuple = [created, UNKNOWN_REVISION, tag, [NO_LABEL], UNKNOWN_OPERATOR]
            history_package[tag] = tag_history_tuple
        else:
            tag_history_tuple = history_package[tag]

        # collect all logs from the tag; these will be passed on to collect all commit hashes of the previously cherry-picked commits
        logs_to_check = []
        run_command(f'git log {tag} --grep "cherry picked from commit"', cwd=package['dir'], stdout_list=logs_to_check)
        # we use cherry-pick -x <commit> so we can in fact trace the cherry-picked commit back to where it came from on teh default branch
        commits_from_default_branch = collect_cherry_picked_commits(logs_to_check)

        # we assign labels separately to the commits, so extract them here
        labels = tag_history_tuple[3]

        for commit in commits_from_default_branch:

            if commit not in commits_tags_first_seen_map_package:
                # new commit, extract the commit subject and prepare a tuple that we can use later
                out = []
                run_command(f'git log --pretty="%s" -n1 {commit}', cwd=package['dir'], stdout_list=out)
                # the commit tuple
                # 0. tag created (this is to sort)
                # 1. commit hash
                # 2. commit subject
                # 3. list of target tags it went into
                # 4. list of labels
                # 5. list of operators
                # 6. list of created timestamps
                commits_tags_first_seen_map_package[commit] = [tag_history_tuple[0], commit, out[0], [], [], [], []]

            for label in labels:
                if label in commits_tags_first_seen_map_package[commit][4]:
                    # if this label is already there, there should also be a tag associated with this label. So this commit is known to be there for this label already
                    # ==> continue
                    continue

                # update the tuple of this commit with tag, label, operator and tag timestamp
                commits_tags_first_seen_map_package[commit][3].append(tag_history_tuple[2])
                commits_tags_first_seen_map_package[commit][4].append(label)
                commits_tags_first_seen_map_package[commit][5].append(tag_history_tuple[4])
                commits_tags_first_seen_map_package[commit][6].append(tag_history_tuple[0])

    # write the tag and commit histories, basically cache so that next time everything is faster
    write_yaml(history_dict, tagging_history_file_path)
    git_add(DPG_DOCS, git_tagging_history_file_path)
    write_yaml(commits_tags_first_seen_map, commit_file_path)
    git_add(DPG_DOCS, git_commit_file_path)

    # all following markdown files will go into this directory
    git_history_dir_path = join('docs', 'software', 'accepted')
    history_dir_path = join(DPG_DOCS['dir'], git_history_dir_path)
    if not exists(history_dir_path):
        makedirs(history_dir_path)

    # make the tag history page
    history_file_name = f'{package_name}_tag_history.md'
    output_markdown = join(history_dir_path, history_file_name)
    history_package_list = list(history_package.values())
    history_package_list.sort(reverse=True)
    make_history_markdown(package_name, package['http'], history_package_list, output_markdown)
    git_add(DPG_DOCS, join(git_history_dir_path, history_file_name))

    # make a commit history page; it lists all commits with the info in which tag they were first seen
    # this is the location where the markdowns will be written
    accepted_file_name = f'{package_name}_accepted.md'
    accepted_file_path = join(history_dir_path, accepted_file_name)
    commits_tags_first_seen_list = list(commits_tags_first_seen_map_package.values())
    commits_tags_first_seen_list.sort(reverse=True)
    make_cherry_picked_markdown(package_name, package['http'], commits_tags_first_seen_list, accepted_file_path)
    git_add(DPG_DOCS, join(git_history_dir_path, accepted_file_name))

    # make a page that maps the labels to the latest tags that are associated with them
    # this is a bit cumbersome since we have to re-arrange the dictionaries we have created earlier
    labels_to_tag_package_map = {}
    for package_name_history, history_package in history_dict.items():
        tag_tuple_list = list(history_package.values())
        tag_tuple_list.sort(reverse=True)
        for tag_tuple in tag_tuple_list:
            for label in tag_tuple[3]:
                if label not in labels_to_tag_package_map:
                    labels_to_tag_package_map[label] = {}
                if package_name_history in labels_to_tag_package_map[label]:
                    continue
                labels_to_tag_package_map[label][package_name_history] = (tag_tuple[0], tag_tuple[2], tag_tuple[4], DEFAULTS[package_name_history]['http'])

    latest_tags_file_name = 'latest_tags.md'
    make_label_markdown(labels_to_tag_package_map, join(history_dir_path, latest_tags_file_name))
    git_add(DPG_DOCS, join(git_history_dir_path, latest_tags_file_name))

    # commit everything
    git_commit(DPG_DOCS, f'Update accepted cherry-picks {package_name}')

    return True


def update_doc_all(recreate_commits=False):
    """
    Run a documentation update for all packages
    """
    logger = get_logger()

    logger.info('Run entire documentation update')

    if not fetch(DPG_DOCS) or not update_branch_from_remote(DPG_DOCS):
        logger.error('Cannot update package %s', DPG_DOCS['name'])
        return 1

    for package in DEFAULTS.values():
        if not fetch(package) or not update_branch_from_remote(package) or not complete_package_config_with_defaults(package):
            logger.error('Cannot initialise package %s', package['name'])
            continue
        # mimic being pushed
        package['pushed'] = UNKNOWN_TIMESTAMP

        update_doc_impl(package, recreate_commits)

    git_push(DPG_DOCS)

    return 0


def update_doc_from_configs(config_paths):
    """
    Run documentation update for a list of configs
    """
    logger = get_logger()

    if not fetch(DPG_DOCS) or not update_branch_from_remote(DPG_DOCS):
        logger.error('Cannot update package %s', DPG_DOCS['name'])
        return 1

    for config_path in config_paths:

        config = read_yaml(config_path)
        labels = get_labels(config)

        return_value = 0

        if not labels:
            logger.error('No labels given in %s, not updating anything', config_path)
            return_value = 1
            continue

        for package_initial in get_packages(config):
            # Add defaults for a few things if not given explicitly
            if not complete_package_config_with_defaults(package_initial, labels):
                return_value = 1
                continue
            summary_package_path = make_package_summary_path(package_initial, PACKAGE_OUTPUT_DIRECTORY)
            # now actually, we take what was written in the summary because that has some information we might need
            package_final = read_yaml(summary_package_path)
            if not package_final:
                logger.error('It seems no tagging has been done for package %s, skipping', package_initial['name'])
                return_value = 1
                continue
            # and from that we push
            if not update_doc_impl(package_final):
                logger.error('Documentation could not be updated for package %s, skipping', package_final['name'])
                return_value = 1

    git_push(DPG_DOCS)

    return return_value


##########################################
# main entrypoints steered from argparse #
##########################################
def run_init(args):
    """
    To explicitly initialise
    """

    logger = get_logger()

    if args.fetch:
        # fetch everything already, e.g. if people would like to check things inside before moving to the actual tagging task
        for package_name, package in DEFAULTS.items():
            logger.info('Fetch %s', package_name)
            fetch(package)

    if args.template:
        template_path = join(dirname(abspath(sys.argv[0])), 'template_cherry_pick.yml')
        copyfile(template_path, 'template_cherry_pick.yml')
        logger.info('Copied a template to template_cherry_pick.yml')

    if not args.operator:
        return 0

    init_config_path = join(ASYNC_DIR, 'config.yaml')

    if exists(init_config_path):
        logger.warning('Overwriting the global configuration.')

    init_config = {'operator': args.operator}

    write_yaml(init_config, init_config_path)

    return 0


def run_cherry_pick_tag(args):
    """
    Entrypoint for cherry-picking and tagging
    """
    logger = get_logger()

    config = read_yaml(args.config)
    labels = get_labels(config)

    if not labels:
        logger.error('No labels given in %s', args.config)
        return 1

    if not check_tag_config_by_user(config, labels):
        # ask the user again to make sure they have a second chance to check their config before proceeding
        return 1

    # find out whether to retag something
    packages_to_retag = []
    if args.retag:
        for package_name in args.retag:
            packages_to_retag.append(PACKAGE_ALIASES.get(package_name, package_name))

    already_tagged = []
    to_tag = []

    # First go through packages, clone them and checkout where we want to work with them
    for package in get_packages(config):

        # Add defaults for a few things if not given explicitly
        if not complete_package_config_with_defaults(package, labels):
            return 1

        # check if the configuration is complete
        if not check_package_config(package):
            return 1
        else:
            logger.info('==> Config is sane!')

        if not fetch(package) or not prepare_for_cherry_pick(package):
            return 1
        else:
            logger.info('==> Checked out!')

        # warn if this is tagged already with the target tag
        tagged = git_verify(package)
        if tagged and package['name'] not in packages_to_retag and 'all' not in packages_to_retag:
            # if we found this to be done already, take it
            already_tagged.append(package)
            logger.warning('Package %s has the tag %s already. That might create problems if we re-tag. Run with --retag <pkg1> ... <pkgN> to force re-tagging.', package['name'], package['target_tag'])
        else:
            to_tag.append(package)

    # now we should be in a position ready to cherry-pick
    # do only the cherry-picking first so that we can see if that works. Only if all packages were successful, we move on with tagging
    for package in to_tag:

        if not git_cherry_pick(package):
            return 1
        else:
            logger.info('==> Cherry-picked!')

    for package in to_tag:
        if not git_tag(package, retag=args.retag):
            return 1
        else:
            logger.info('==> Tagged!')

        if not closure(package):
            return 1
        else:
            logger.info('==> Verified!')

        # finalise, for instance, if we have cherry-picked to a branch, this is so far a temporary branch which needs to be moved to the target branch
        finalise(package, args.operator)
        # write the final summary to yaml for further processing
        write_single_summary(package, PACKAGE_OUTPUT_DIRECTORY)

    return 0


def run_push_tagged(args):
    """
    Entrypoint for pushing newly tagged packages
    """
    config = read_yaml(args.config)
    labels = get_labels(config)

    logger = get_logger()

    if not labels:
        logger.error('No labels given in %s', args.config)
        return 1

    # Try to do as much as possible, so cache the return value
    return_value = 0

    # collect packages for which the we want to update the documentation
    update_packages_documentation = []

    # First go through packages, clone them and checkout where we want to work with them
    for package_initial in get_packages(config):
        # Add defaults for a few things if not given explicitly
        if not complete_package_config_with_defaults(package_initial, labels):
            return_value = 1
            continue
        summary_package_path = make_package_summary_path(package_initial, PACKAGE_OUTPUT_DIRECTORY)
        # now actually, we take what was written in the summary because that has some information we might need
        package_final = read_yaml(summary_package_path)
        if not package_final:
            logger.error('It seems no tagging has been done for package %s', package_initial['name'])
            return_value = 1
            continue
        # and from that we push
        if not push_tagged(package_final) and not package_final.get('pushed', False):
            logger.error('Package %s has not been pushed it seems but it could also not be pushed now.', package_final['name'])
            # finally return with 1
            return_value = 1
            continue
        # Flag as being pushed so we can look that up later when needed.
        package_final['pushed'] = int(time())
        # make this flagging persistent by writing again the package summary
        write_yaml(package_final, summary_package_path)
        # mark this for documentation update
        update_packages_documentation.append(package_final)

    logger.info('Now updating the documentation')

    if not fetch(DPG_DOCS) or not update_branch_from_remote(DPG_DOCS):
        logger.error('Cannot fetch documentation package')
        return 1

    for package in update_packages_documentation:
        update_doc_impl(package)

    git_push(DPG_DOCS)
    logger.info('Documentation updated')

    return return_value


def run_update_doc(args):
    """
    Update the documentation for all packages.
    This is not recommended since it does not account for any operator or label information for instance.
    """

    logger = get_logger()

    if args.from_configs and args.recreate_commits:
        logger.error('Can either make the documentation of commits from configs or recreate it from the tag history file')
        return 1

    if not args.from_configs:
        logger.warning('Are you sure that you want to updated the documentation independently of some package update?\nThis will not take any operator or label information into account!\nOtherwise, please specify the configs from which this update should be done with --from-configs <pkg1> <pkg2> ...\n[y/N]')

        yes_no = input()
        if not yes_no or yes_no.lower() != 'y':
            logger.info('Nothing was updated')
            return 1

        return update_doc_all(args.recreate_commits)

    return update_doc_from_configs(args.from_configs)


def run(args):
    """
    Global entrypoint

    Do some preparation and call the actual function to be executed
    """
    # first, setup the logger
    logging_directory = join('o2dpg_cherry_picks_logs', datetime.fromtimestamp(int(time())).strftime("%Y%m%d"))
    if not exists(logging_directory):
        makedirs(logging_directory)
    formatter = logging.Formatter('%(levelname)s: %(message)s')
    logger = get_logger()
    # basically report everything
    logger.setLevel(logging.DEBUG)
    # we want the output to go to the terminal...
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    # ...as well as to a file
    log_file_path = join(logging_directory, f'{args.func.__name__}_{int(time())}.log')
    file_handler = logging.FileHandler(log_file_path, 'w')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    # make this file known globally so that it can potentially be written to by other parties
    LOG_FILE.append(log_file_path)

    # The internal config directory
    if not exists(ASYNC_DIR):
        makedirs(ASYNC_DIR)

    # The run_init function gets a special treatment
    if args.func.__name__ == 'run_init':
        return args.func(args)

    # and the config file
    init_config_path = join(ASYNC_DIR, 'config.yaml')

    if not exists(init_config_path) and not args.operator:
        logger.error('You need to specify the operator with --operator "Firstname Lastname" for a sub-command or run with sub-command init --operator "Firstname Lastname" once.')
        return 1

    init_config = read_yaml(init_config_path)
    # if given explicitly, that operator takes precedence over the one in the global configuration
    args.operator = args.operator or init_config['operator']

    # now finally do what the user wanted all along. Don't return immediately so that we can tell our user where the final log file went.
    return_value = args.func(args)

    print(f'==> Log file is at {log_file_path}.')

    return return_value


if __name__ == '__main__':

    common_operator_parser = argparse.ArgumentParser(add_help=False)
    common_operator_parser.add_argument('--operator', help='The name of the operator')

    # The main parser
    parser = argparse.ArgumentParser(description='Helping with asyncSW software deployment')

    # Use various sub-parsers
    sub_parsers = parser.add_subparsers(dest="command")

    # init
    init_parser = sub_parsers.add_parser('init', parents=[common_operator_parser])
    init_parser.add_argument('--fetch', action='store_true', help='Fetch already the default packages once')
    init_parser.add_argument('--template', action='store_true', help='copy a configuration template to the current working directory')
    init_parser.set_defaults(func=run_init)

    # cherry-picking and tagging
    tag_parser = sub_parsers.add_parser("tag", parents=[common_operator_parser])
    tag_parser.add_argument("config", help="The input configuration")
    tag_parser.add_argument("--retag", nargs="*", help='whether or not to force re-tagging of packages')
    tag_parser.set_defaults(func=run_cherry_pick_tag)

    # push tagged packages
    push_parser = sub_parsers.add_parser("push", parents=[common_operator_parser])
    push_parser.add_argument("config", help="The input configuration")
    push_parser.set_defaults(func=run_push_tagged)

    # update documentation with what has been tagged and pushed
    update_doc_parser = sub_parsers.add_parser("update-doc", parents=[common_operator_parser])
    update_doc_parser.add_argument('--from-configs', dest='from_configs', nargs='*', help='Give a list of configs; these would be the same used during cherry-picking and tagging')
    update_doc_parser.add_argument('--recreate-commits', dest='recreate_commits', action='store_true', help='recreate the commit history entirely from the tag/operator history')
    update_doc_parser.set_defaults(func=run_update_doc)

    args = parser.parse_args()
    sys.exit(run(args))
