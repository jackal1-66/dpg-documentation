# Operator documentation

## If something does not work and some important things

Assume there is for whatever reasons a problem with this tool and you have to cherry-pick manually, please always use

```bash
git cherry-pick -x <commit>
```

The `-x` is the super important part that also this tool uses. It adds the original commit hash to the commit message once the original commit has been cherry-picked. In this way, it will always be possible to trace back where cherry-picked commits come from.

In fact, the documentation update explained [here](#push-the-tags) and [here](#update-the-documentation) would still work, except for operator and label connections.

Also, never cherry-pick commits that are not on the default branch of a repository.

## Update software tags

This is a description of some tooling that supports the following procedure:

1. cherry-pick new software requests,
1. tag related packages,
1. create requested tags,
1. push these tags to the corresponding upstream repos,
1. update the documentation page.

The tool is located at `<top-dir-of-this-repo>/src/utils/o2dpg_async_update.py`. The following steps should be done one after the other.

For this documentation, we will **assume** that the script is located in the directory `${ASYNC_BIN}`. You can of course export
```bash
export ASYNC_BIN=<top-dir-of-this-repo>/src/utils
```
to be able to exactly follow the examples.

**NOTE** that for consistency, tags must start with `async-`. Otherwise, the toll will abort.

## Don't be confused

At the end, you will read about [updating the documentation](#update-the-documentation). Although it will also fetch this repository from remote, **it is not the same copy of the repository you run this code from**.
So you have to clone it once somewhere simply to run the tool which is described here.
For everything the tool does there is absolutely no need to fetch anything yourself. In fact, it is highly discouraged to even do that.
Just let the tool do what it does.

## Run in a dedicated directory

**It is strongly recommended** to run all of the following in a **dedicated working directory** since running it creates additional output files.
All repos that are cloned and used should be seen as part of the tool's data. Do not do any developments in these local repos since they are manipulated and any local developments that are there otherwise might be lost.

## Directly diving into it

This is more of a quick guide. More info is provided further down.

### Initialise

To be done once

```bash
${ASYNC_BIN}/o2dpg_async_update.py init --operator "Firstname Lastname"
```

If you need to have the latest stage of the repositories already available at this point (e.g. to browse or to check when a PR has multiple commits), they can be cloned/updated wth

```bash
${ASYNC_BIN}/o2dpg_async_update.py init --fetch
```

### Get a template for the config to work with

This can be done for each new cherry-picking session and copies a template `template_cherry_pick.yml` into the current working directory.

```bash
${ASYNC_BIN}/o2dpg_async_update.py init --template
```

Inside the template, there are 2 examples. The first one specifically shows how to tag all packages always with the same tag. This we do specifically for everything that goes on top of the branch `async-v1-01-branch`. Always all packages are tagged.

In other cases, the new tags are usually based on previous tags.

### Fill the template

Each package is identified by its `name` and wants to know where to `start_from` (this could be an existing tag or branch) and which `target_tag` should be applied once everything in the `commits` list has been cherry-picked. In addition, each such config file needs the list of `labels`.
This means that each such config file corresponds to a new software build.

By the way, don't worry about

* the order of commits when filling the list since they will be ordered in any case,
* whether you use the long hashes of the short once; they will always be extended to the long hashes to be consistent.

### Run the cherry-picking

Once the config is complete, run

```bash
${ASYNC_BIN}/o2dpg_async_update.py cherry-pick <path-to-yaml-config>
```

In the beginning, it will clone or update the concerned packages. Therefore, since everything is communicated via `ssh`, you might need to enter your password (multiple times, once per package) to unlock your private key.

After that, it will attempt to apply all commits on top of where you chose to `start_from`. If it fails, it will let you know.
In any case, as the last message, it will let you know where the corresponding log file of this run is located.

### Push the tags

Since during cherry-picking things can always go wrong, pushing the tags is a dedicated step. To push all tags that have just been created, run

```bash
${ASYNC_BIN}/o2dpg_async_update.py push <the-same-path-to-yaml-config-that-you-just-used-before>
```

This will push all tags and as the last step, it will update the online documentation to contain commits that have been cherry-picked, in which tags they were seen for the first time etc. Since also here, all repositories are accessed via `ssh`, a password for your private key might be necessary.

### DONE

That's it.

Now comes some more info.

## General info

### Help

To get first-level help, run

```bash
${ASYNC_BIN}/o2dpg_async_update.py --help
```

to see all available sub-commands.

Also, for each sub-command, there is a dedicated help message with

```bash
${ASYNC_BIN}/o2dpg_async_update.py <sub-command> --help
```

### Packages concerned

This tool handles by default the following packages:

* O2,
* O2DPG,
* O2Physics,
* QualityControl.

It does currently not support any other packages. However, an extension in that direction would be relatively trivial.

### Log files

Log files are always created. They contain the same information that is written in the terminal but also more, for instance all output when a git command is issued.
As you will see below, there are various sub-commands that can be run. The log file name will be printed at the end of the execution and has the form of `o2dpg_cherry_picks_logs/<called-function>_<timestamp>.log`.

### To be always up-to-date

Accessing the upstream repos is done via `ssh`. If your private key is password protected, you might need to enter your password from time to time whenever a repo is cloned or the local ones are updated.
Note that it is extremely important that - when running any cherry-picking and tagging - we make sure to really have the absolute latest and greatest state synced with upstream.
This is why cloning and resetting of local history to the upstream repo is mandatory each time you cherry-pick or something else is updated.

## Specifying the operator

For each step, the operator must be known. To set the operator permanently, run
```bash
${ASYNC_BIN}/o2dpg_async_update.py init --operator "Firstname Lastname"
```

To overwrite or set the operator for a specific action, run any other command with
```bash
${ASYNC_BIN}/o2dpg_async_update.py <command> --operator "Firstname Lastname" [<other-options>]
```

## Cherry-pick and tag

### You cannot cherry-pick everything

The commits that are chosen to cherry-pick have to live in the history of the default branch. If they don't, the tool will abort.
This is done for consistency reasons and to always keep the connection to the default branch of each package.

### Force retagging

Sometimes, you created a tag but then you realise, that a commit is missing or similar. In that case, do
```bash
${ASYNC_BIN}/o2dpg_async_update.py tag <input_config> --retag <pkg1> <pkg2>
```
and mention there all the package you would like to retag after changing the list of commits in the config.

**This is not recommended!** The better way would be to always create a new tag. Especially if the tag was already pushed, there is nothing you can do about it as far as this tool is concerned.


## Update the documentation

There are 3 different types of pages that will be created or modified during this step:

1. **per package** a list of commits that have been cherry-picked associated to tags, operators, labels and timestamps,
1. **per package** a history of tags and what they are based on,
1. a list of labels that is mapped to the **latest tags** of the packages associated with each label.

A documentation updated happens whenever the `push` command is executed. So there should be no need to manually do that.

**Although it is not recommended** to do the following nor should it be necessary, two other ways to update the documentation are available.

### Via a list of configuration files

By providing a list of `YAML` configuration files, one can run

```bash
${ASYNC_BIN}/o2dpg_async_update.py update-doc --from-configs <config1> <config2> ...
```

This will only work if everything in the configs has been pushed before. It will not work by simply creating such a config and then run the above.
This is somewhat safe to do because it can recognise the connection between tags, commits, labels and operators.

### Recollect the cherry-picked commits from scratch

**This should not be necessary** but it is possible to collect all cherry-picked commits again. Everything that was possible to connect to operators, labels etc. will again be associated with those.
This is possible as long as the file in `data/async_software_logging/tagging_history.yml` is intact. If that is messed up or does not exist, the connection between commits, operators etc. will be lost.
The file `data/async_software_logging/commits.yml` is really only a cache file to speed up the creation of the documentation. And this is the file that would be written again from scratch when the following is run:

```bash
${ASYNC_BIN}/o2dpg_async_update.py update-doc --recreate-commits
```

### Just update everything and you don't care

First a **disclaimer**: Please be careful here!

It is in fact possible to update the entire documentation for all of the packages. However, in that case, no further operator or label information will be added and only the operator and label information that is currently available can be used. For new tags it might not be possible to derive such information if they haven't been added via this tool.

Doing this simply browses through the repositories tags and collects all commits that belong/were introduced with a certain tag. If operator/label information is available, great. Otherwise commits will be added with `UNKNOWN LABEL` and `UNKNOWN OPERATOR` annotations.

If you are still convinced, run

```bash
${ASYNC_BIN}/o2dpg_async_update.py update-doc
```
