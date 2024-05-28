#!/usr/bin/env python3

import sys
import argparse
from os.path import exists, join
from os import makedirs, listdir
from time import time
import yaml
from subprocess import Popen, PIPE, STDOUT
from shlex import split as sh_split


### Some defaults

# per package
DEFAULTS_O2 = {'upstream': 'git@github.com:AliceO2Group/AliceO2.git',
               'http': 'https://github.com/AliceO2Group/AliceO2',
               'dir': 'O2',
               'default_branch': 'dev'}

DEFAULTS_O2DPG = {'upstream': 'git@github.com:AliceO2Group/O2DPG.git',
                  'http': 'https://github.com/AliceO2Group/O2DPG',
                  'dir': 'O2DPG',
                  'default_branch': 'master'}

DEFAULTS_O2PHYSICS = {'upstream': 'git@github.com:AliceO2Group/O2Physics.git',
                      'http': 'https://github.com/AliceO2Group/O2Physics',
                      'dir': 'O2Physics',
                      'default_branch': 'master'}

DEFAULTS_QC = {'upstream': 'git@github.com:AliceO2Group/QualityCOntrol.git',
               'http': 'https://github.com/AliceO2Group/QualityControl',
               'dir': 'QualityControl',
               'default_branch': 'master'}

DPG_DOCS = {'name': 'dpg-docs',
            'upstream': 'git@github.com:AliceO2Group/dpg-documentation.git',
            'dir': 'dpg-documentation',
            'default_branch': 'main'}


# collect everything together
DEFAULTS = {'AliceO2': DEFAULTS_O2,
            'O2DPG': DEFAULTS_O2DPG,
            'O2Physics': DEFAULTS_O2PHYSICS,
            'QualityControl': DEFAULTS_QC}

for package_defaults in DEFAULTS.values():
    # provide an empty list of commits
    package_defaults['commits'] = []
    # to flag if successful, None indicates that nothing has been done yet
    package_defaults['status_cherry_pick'] = None


# Aliases
PACKAGE_ALIASES = {'O2': 'AliceO2',
                   'QC': 'QualityControl'}

### Expected keys for each package
REQUIRED_KEYS = ['name', 'upstream', 'start_from', 'target_tag']

# Play a trick here to be able to use a global log file which will be the single element of this list
LOG_FILE = []


####################
# Global utilities #
####################
def run_command(cmd, log_file=None, cwd=None, stdout_list=None):
    """
    Run a command

    Write to logfile or each line to a list
    """
    if not log_file and LOG_FILE:
        log_file = LOG_FILE[0]

    stdout, stderr = (None, None) if not log_file and stdout_list is None else (PIPE, STDOUT)
    p = Popen(sh_split(cmd), cwd=cwd, stdout=stdout, stderr=stderr, universal_newlines=True)

    if log_file:
        log_file = open(log_file, 'a')
        log_file.write(f'{cmd}\n')

    if log_file or stdout_list is not None:
        for line in p.stdout:
            if log_file:
                log_file.write(line)
            if stdout_list is not None:
                stdout_list.append(line.strip())

    p.wait()

    if log_file:
        log_file.close()

    return p.returncode


def read_yaml(path):
    """
    Read YAML into a dictionary
    """
    try:
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    except Exception:
        return None


def write_yaml(d, out_file):
    """
    Write dictionary to YAML
    """
    with open(out_file, 'w') as f:
        yaml.safe_dump(d, f)

    return None


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
        print('WARNING: Unknown package name. Available packages:')
        for package_name in DEFAULTS:
            print(f'  - {package_name}')
    return {}


def complete_package_config(package, labels=None):
    """
    Add some default values if not set
    This works inline on the package dict
    """
    # First, let's set the name to the GitHub upstream repo name in case of aliases
    package['name'] = PACKAGE_ALIASES.get(package['name'], package['name'])
    package['labels'] = labels or []
    package['commits_cherry_picked'] = {'success': [], 'skipped': [], 'failed': []}
    package_defaults = get_default(package['name'])
    for key, default_value in package_defaults.items():
        package[key] = package.get(key, default_value)


def check_package_config(package):
    """
    Check a package config, for instance if it is complete
    """
    print(f'INFO: Check configuration of package {package["name"]}')
    is_sane = True
    for key in REQUIRED_KEYS:
        if key not in package:
            is_sane = False
            print(f"ERROR: {key} not in package configuration.")

    return is_sane


def get_packages(config):
    """
    Get the package dicts from config dict
    """
    try:
        return config['packages']
    except KeyError:
        print('ERROR: Cannot find packages. Make sure to specify a list of packages under the key "packages.')
    return None


def get_labels(config):
    """
    Get the labels from config dict
    """
    try:
        return config['labels']
    except KeyError:
        print('ERROR: Cannot get labels. Make sure to specify a list of labels under the key "labels".')


#########################
# Git-related utilities #
#########################
def clone(package):
    """
    Clone from remote
    """
    cwd = package['dir']
    if not exists(cwd) and run_command(f'git clone {package["upstream"]} {cwd}') != 0:
        print(f'ERROR: Failed to clone repo from {package["upstream"]} to {cwd}.')
        return False
    return True


def fetch(package):
    """
    Fetch everything from remote including tags
    """
    cwd = package['dir']
    if not exists(cwd):
        return clone(package)
    return run_command('git fetch origin --tags', cwd=cwd) == 0


def update_default_branch(package):
    """
    Update the default branch of a package

    1. Fetch
    2. hard reset (assuming we don't care about local changes)
    """
    cwd = package['dir']
    default_branch = package['default_branch']
    return fetch(package) and run_command(f'git checkout {default_branch}', cwd=cwd) == 0 and run_command(f'git reset --hard origin/{default_branch}', cwd=cwd) == 0


def checkout(package, fetch_again=False):
    """
    Checkout a repo at a certain branch or tag

    1. If the repo does not yet exist locally, clone.
    2. Fetch everything (including tags) if requested
    3. Checkout branch/revision

    If a branch is requested to be checked-out, do so but for now move to a temporary branch
    """
    print(f'INFO: Checkout {package["name"]}')

    if not clone(package):
        return False

    cwd = package['dir']

    if fetch_again and not fetch(package):
        return False

    # checkout this
    ref_co = package['start_from']

    if run_command(f'git checkout {ref_co}', cwd=cwd) != 0:
        print(f'ERROR: Cannot checkout {ref_co} in {cwd}.')
        return False

    out = []
    is_detached = False
    run_command('git status', cwd=cwd, stdout_list=out)
    for line in out:
        if 'HEAD detached at' in line:
            is_detached = True
            break

    package['head_detached'] = is_detached

    if not is_detached:
        # we are on a branch, create a temporary one where to start
        branch_tmp = f'{package["start_from"]}-for-{package["target_tag"]}'
        package['start_from_cache'] = package["start_from"]
        package['start_from'] = branch_tmp
        if run_command(f'git checkout -B {branch_tmp}', cwd=cwd) != 0:
            print(f'ERROR: Cannot create temporary branch {branch_tmp} in {cwd}.')
            return False

    return True


def cherry_pick_single(cwd, commit):
    """
    Utility to cherry-pick per commit
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
    package_name = package['name']

    print(f'INFO: Cherry-pick {package_name}')

    if not package['commits']:
        print(f'WARNING: No commits found to cherry-pick for package {package_name}')
        return True

    commits_success = package['commits_cherry_picked']['success']
    commits_failed = package['commits_cherry_picked']['failed']
    commits_skipped = package['commits_cherry_picked']['skipped']

    cwd = package['dir']

    for commit in package['commits']:
        print(f"Cherry-picking {commit}")
        ret = cherry_pick_single(cwd, commit)
        if isinstance(ret, list):
            print(f"ERROR: There was a problem cherry-picking {commit}")
            for line in ret:
                print(f'  {line}')
            print('Try to continue')
            commits_failed.append(commit)
            continue
        if ret < 0:
            commits_skipped.append(commit)
            continue
        commits_success.append(commit)

    print(f"Cherry-picking\n  SUCCESS: {len(commits_success)}\n  SKIPPED: {len(commits_skipped)}\n  FAILED: {len(commits_failed)}")

    # set the status
    package['status_cherry_pick'] = not commits_failed

    if commits_failed:
        # Reset to initial SHA of start tag or branch
        run_command(f'git reset --hard HEAD~{len(commits_success)}', cwd=cwd)
        return False

    return True


def git_tag(package, retag=False):
    """
    Tag a package
    """
    package_name = package["name"]
    tag = package['target_tag']

    print(f'INFO: Tag {package_name} with {tag}')

    cwd = package['dir']

    if run_command(f'git rev-parse --verify {tag}', cwd=cwd) == 0:
        if retag and run_command(f'git tag -d {tag}', cwd=cwd) != 0:
            print(f'ERROR: Was asked to retag package {package_name} with {tag}.')
            return False

    if run_command(f'git tag {tag}', cwd=cwd) != 0:
        run_command(f'git reset --hard HEAD~{len(package["commits_cherry_picked"]["success"])}', cwd=cwd)
        print(f'ERROR: Cannot tag {cwd} with tag {tag}')
        return False

    return True


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
    rev = package['target_tag'] if not rev else rev
    cwd = package['dir']
    return run_command(f'git rev-parse --verify {rev}', cwd=cwd) == 0


###################################################
# Additional helpers for the cherry-pick workflow #
###################################################
def write_summary(package, out_dir):
    if not exists(out_dir):
        makedirs(out_dir)
    out_file = join(out_dir, f'{package["name"]}_{package["target_tag"]}.yaml')
    write_yaml(package, out_file)


def closure(package):
    """
    Conduct kind of a closure test to see if all commits went in
    """
    cwd = package['dir']
    tag = package['target_tag']
    package_name = package['name']

    print(f'INFO: Verify {package_name}')

    if run_command(f'git rev-parse --verify {tag}', cwd=cwd) != 0:
        print(f'ERROR: Package {package_name} does not contain tag {tag} which was requested')
        return False

    # check if HEAD is at the target tag
    rev_target_tag = []
    run_command(f'git rev-parse {tag}', cwd=cwd, stdout_list=rev_target_tag)
    rev_target_head = []
    run_command('git rev-parse HEAD', cwd=cwd, stdout_list=rev_target_head)

    if rev_target_tag[0] != rev_target_head[0]:
        print(f'ERROR: Hashes of HEAD and {tag} are different: {rev_target_tag[0]} != {rev_target_head[0]}')
        return False

    if package['commits_cherry_picked']['failed']:
        print(f'ERROR: Package {package_name} has failed commits.')
        return False

    commits_success = package['commits_cherry_picked']['success']

    if not commits_success and package['commits_cherry_picked']['skipped']:
        print(f'WARNING: All proposed commits were found to be skipped for package {package_name}. However, the tag {tag} is where it is supposed to be, so it should be fine.')
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
            print(f'ERROR: During the verification, the commit {commit} was apparently not cherry-picked.')
            return False

    return True


def finalise(package):
    """
    Some final actions/afterburner steps after cherry-picking
    """
    subjects = []
    package['commits_success_subjects'] = subjects
    cwd = package['dir']
    for commit in package['commits_cherry_picked']['success']:
        out = []
        run_command(f'git log --pretty="%s" -n1 {commit}', cwd=cwd, stdout_list=out)
        subjects.append(out[0])

    if 'start_from_cache' not in package:
        return

    cwd = package['dir']
    run_command(f'git checkout -B {package["start_from_cache"]}', cwd=cwd)
    run_command(f'git branch -D {package["start_from"]}', cwd=cwd)
    package["start_from"] = package["start_from_cache"]
    del package["start_from_cache"]


def push_tagged(package):

    tag = package['target_tag']
    package_name = package['name']
    if not git_verify(package):
        print(f'ERROR: Package {package_name} does not seem to contain tag {tag}.')
        return

    tag = package['target_tag']
    cwd = package['dir']

    out = []

    if run_command(f'git push origin {tag}', cwd=cwd, stdout_list=out) != 0:
        print(f'WARNING: Could not push tag {tag} due to')
        for line in out:
            print(line)
        return

    for line in out:
        if 'Everything up-to-date' in line:
            print(f'INFO: Tag {tag} of package {package_name} was already upstream')
            return

    print(f'INFO: Pushed tag {tag} of package {package_name}.')


#####################################################
# Additional helpers for updating the documentation #
#####################################################
def make_cherry_picked_markdown(package_name, commit_tuples, output_markdown):
    with open(output_markdown, 'w') as f:
        f.write(f'# Cherry-picked commits for {package_name}\n\n')
        f.write('| Commit subject | Tags first seen | Associated labels |\n| --- | --- | --- |\n')
        for commit_tuple in sorted(commit_tuples):
            # sorted by timestamp
            commit_link = f'{commit_tuple[1]}/commit/{commit_tuple[3]}'
            tag_links = [f'[{t}]({commit_tuple[1]}/tree/{t})' for t in list(set(commit_tuple[4]))]
            f.write(f'| [{commit_tuple[2]}]({commit_link}) | {", ".join(tag_links)} | {", ".join(list(set(commit_tuple[5])))} |\n')


##########################################
# main entrypoints steered from argparse #
##########################################
def run_cherry_pick_tag(args):
    """
    Entrypoint for cherry-picking and tagging
    """
    config = read_yaml(args.config)
    labels = get_labels(config)

    if not labels:
        print(f'ERROR: No labels given in {args.config}')
        return 1

    # this is where all git commands and stdout/stderr will go
    LOG_FILE.append(args.log_file or f'o2dpg_asyncSW_{"_".join(labels)}_cherry_pick.log')

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
        complete_package_config(package, labels)

        # check if the configuration is complete
        if not check_package_config(package):
            return 1
        else:
            print('==> Sane!')

        if not checkout(package):
            return 1
        else:
            print('==> Checked out!')

        # warn if this is tagged already with the target tag
        tagged = git_verify(package)
        if tagged and package["name"] not in packages_to_retag and "all" not in packages_to_retag:
            already_tagged.append(package)
            print(f'WARNING: Package {package["name"]} has the tag {package["target_tag"]} already. That might create problems if we re-tag. Run with --retag <pkg1> ... <pkgN> to force retagging.')
        else:
            to_tag.append(package)

    # now we should be in a position ready to cherry-pick and tag
    for package in to_tag:

        if not git_cherry_pick(package):
            return 1
        else:
            print('==> Cherry-picked!')

        if not git_tag(package, retag=args.retag):
            return 1
        else:
            print('==> Tagged!')

        if not closure(package):
            return 1
        else:
            print('==> Verified!')

        # finalise, for instance, if we have cherry-picked to a branch, this is so far a temporary branch which needs to be moved to the target branch
        finalise(package)
        # write the final summary to yaml for further processing
        write_summary(package, args.output)

    return 0


def run_push_tagged(args):
    """
    Entrypoint for pushing newly tagged packages
    """
    config = read_yaml(args.config)
    labels = get_labels(config)

    if not labels:
        print(f'ERROR: No labels given in {args.config}')
        return 1

    # this is where all git commands and stdout/stderr will go
    LOG_FILE.append(args.log_file or f'o2dpg_asyncSW_{"_".join(labels)}_push_tags.log')

    # First go through packages, clone them and checkout where we want to work with them
    for package in get_packages(config):

        # Add defaults for a few things if not given explicitly
        complete_package_config(package, labels)
        push_tagged(package)

    return 0


def run_update_doc(args):
    """
    Entrypoint for updating the documentation based on new cherry-picks and tags
    """
    # our documentation package
    # prepare
    clone(DPG_DOCS)
    update_default_branch(DPG_DOCS)

    # the directory where we store the YAML summary
    # This summary will always be extended and used to create a markdown table from
    git_log_file_dir = join('data', 'async_software_logging')
    log_file_dir = join(DPG_DOCS['dir'], git_log_file_dir)
    if not exists(log_file_dir):
        makedirs(log_file_dir)

    # the actual file with the entire summary
    git_log_file_path = join(git_log_file_dir, 'summary.yaml')
    log_file_path = join(log_file_dir, 'summary.yaml')

    # today from epoch, in ms; this is to sort so that we have always the latest commits on top
    # (even though some of them might have been applied to earlier tags associated with a different label)
    timestamp = int(time() * 1000)

    # we want to get the current summary that is already there
    packages_to_commit_summary = read_yaml(log_file_path)
    if not packages_to_commit_summary:
        packages_to_commit_summary = {}

    # go through all single package summary files that we can find
    # these have been created by run_cherry_pick_tag
    # we take each individual one, read it and add its commits, tags and labels to the overall summary
    for path in listdir(args.input):

        path = join(args.input, path)
        package = read_yaml(path)

        if not package:
            print(f'WARNING: Cannot read {path}, probably not a YAML file. Skip...')
            continue

        # this is a specific package
        package_name = package['name']
        # have a dictionary for it; key will be commit hashes and values a tuple where we collect information for this commit
        # the tuple related to a commit looks like
        # 0. timestamp (ms);
        # 1. http url of package to construct some links from it;
        # 2. commit subject;
        # 3. commit hash so that we have it available after when using the tuples independent of the original dictionary;
        # 4. list of tags this was cherry-picked in
        # 5. list of associated labels (although somewhat redundant to the tags, keep it for clarity)
        packages_to_commit_summary[package_name] = packages_to_commit_summary.get(package_name, {})
        d_package = packages_to_commit_summary[package_name]

        for subject, commit in zip(package['commits_success_subjects'], package['commits_cherry_picked']['success']):
            if commit not in d_package:
                # construct a tuple for this commit
                d_package[commit] = [timestamp, package['http'], subject, commit, [], []]
            # there is only one tag, so append
            tag = package['target_tag']
            if tag not in d_package[commit][4]:
                d_package[commit][4].append(tag)
            # there might be in general multiple labels associated with a tag, so extend
            for label in package['labels']:
                if label not in d_package[commit][5]:
                    d_package[commit][5].append(label)

    # this is the location where the markdowns will be written
    git_add_dir = join('docs', 'software', 'accepted')
    output_markdown_dir = join(DPG_DOCS['dir'], git_add_dir)
    if not exists(output_markdown_dir):
        makedirs(output_markdown_dir)


    # this is also where all git commands and stdout/stderr will go
    LOG_FILE.append('o2dpg_asyncSW_update_doc.log')

    # now we go through all (newly added and those that have been there before) commits per package
    # for each package we write a dedicated file
    for package_name, commit_dict in packages_to_commit_summary.items():
        # location of the markdown
        accepted_file_name = f'{package_name}_accepted.md'
        accepted_file_path = join(output_markdown_dir, accepted_file_name)
        make_cherry_picked_markdown(package_name, list(commit_dict.values()), accepted_file_path)
        # after creating/updating the file, add it
        git_add(DPG_DOCS, join(git_add_dir, accepted_file_name))

    # write and add the global summary YAML which will then be used again next time we cherry-pick
    write_yaml(packages_to_commit_summary, log_file_path)
    git_add(DPG_DOCS, git_log_file_path)

    # finish this by committing and pushing
    git_commit(DPG_DOCS, 'Update accepted cherry-picks')

    return 0
    git_push(DPG_DOCS)

    return 0


def run_fetch(args):
    for package in DEFAULTS.values():
        fetch(package)
    return 0


if __name__ == '__main__':

    # The main parser
    parser = argparse.ArgumentParser(description='Helping with asyncSW software deployment')

    # Use various sub-parsers
    sub_parsers = parser.add_subparsers(dest="command")

    # rel-val
    tag_parser = sub_parsers.add_parser("tag")
    tag_parser.add_argument("config", help="The input configuration")
    tag_parser.add_argument("--retag", nargs="*", help='whether or not to force retagging of packages')
    tag_parser.add_argument('--log-file', dest='log_file', help='Log file to output git commands and stdout/stderr to')
    tag_parser.add_argument('--output', help='Output directory where final YAML files will be written.', default='o2dpg_cherry_picks')
    tag_parser.set_defaults(func=run_cherry_pick_tag)

    push_parser = sub_parsers.add_parser("push")
    push_parser.add_argument("config", help="The input configuration")
    push_parser.add_argument('--log-file', dest='log_file', help='Log file to output git commands and stdout/stderr to')
    push_parser.set_defaults(func=run_push_tagged)

    update_doc_parser = sub_parsers.add_parser("update-doc")
    update_doc_parser.add_argument('--input', help='Input directory where final YAML files are written.', default='o2dpg_cherry_picks')
    update_doc_parser.set_defaults(func=run_update_doc)

    fetch_parser = sub_parsers.add_parser("fetch")
    fetch_parser.set_defaults(func=run_fetch)

    args = parser.parse_args()
    sys.exit(args.func(args))
