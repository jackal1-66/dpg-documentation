# Operator documentation

## Update software tags

This is a description of some tooling that supports the following procedure:

1. cherry-pick new software requests,
1. tag related packages,
1. create requested tags,
1. push these tags to the corresponding upstream repo,
1. update the documentation page

The [tool](o2dpg_async_update.py) is written in python. The following steps should be done one after the other.

In the following, we will assume that the script is located in the directory `${ASYNC_BIN}`.

It is strongly recommended to run all of the following in a **dedicated working directory** since running it creates additional output files.
In addition, it checks out the git packages it works with. Since it manipulates them as well, there should not be any personal work done in those local packages.

Some additional default values of packages are defined for

* O2,
* O2DPG,
* O2Physics,
* QualityControl.

For those, the script knows for instance where to find the upstream repositories.

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

To run this, a `YAML` configuration like the following must be prepared per label (or a group of labels since sometimes, a tag is associated to multiple labels at the same time):

```yaml
labels:
  - <label1> # e.g. async-2022-pp-apass6-2023-PbPb-apass2

packages:
    - name: first package # e.g. O2DPG
      start_from: <branch-or-tag> # e.g. async-v1-01-branch or async-20240115.7.trd
      target_tag: <target-tag> # e.g. async-20240115.8.trd
      commits:
      - <commit1>
      - <commit2>
      - ...
      - <commitN>
    - name: second package # e.g. O2
      start_from: <branch-or-tag> # e.g. async-v1-01-branch or async-20240115.7.trd
      target_tag: <target-tag> # e.g. async-20240115.8.trd
      commits:
      - <commit1>
      - <commit2>
      - ...
      - <commitN>
    - name: third package # e.g. QualityControl
      start_from: <branch-or-tag> # e.g. async-v1-01-branch or async-20240115.7.trd
      target_tag: <target-tag> # e.g. async-20240115.8.trd
      commits:
      - <commit1>
      - <commit2>
      - ...
      - <commitN>
```

In this case we are hence interested in

1. cherry-picking **per package** a list of commits,
1. subsequently, we wish to add the corresponding `<target-tag>` to each package.

This is all done by issuing the following command
```bash
${ASYNC_BIN}/o2dpg_async_update.py tag <input_config>
```

If this goes wrong at any point, everything will be reset and one can start over after fixing potential merge conflict or similar.

### Force retagging

Sometimes, you created a tag but then you realise, that a commit is missing or similar. In that case, do
```bash
${ASYNC_BIN}/o2dpg_async_update.py tag <input_config> --retag <pkg1> <pkg2>
```
and mention there all the package you would like to retag after changing the list of commits in the config.

## Push tagged packages

Once the previous step has been run successfully on the configuration `<input_config>`, run
```bash
${ASYNC_BIN}/o2dpg_async_update.py push <input_config>
```
to push all packages' tags to their remote repository.

## Update the documentation

Now comes the step that is crucial for our bookkeeping. This should be run once after all packages for all labels have been cherry-picked and pushed.
Run
```bash
${ASYNC_BIN}/o2dpg_async_update.py update-doc
```
to update the documentation.

This will

1. Clone or fetch the documentation repository if it is not yet there,
1. reset the local default branch to the upstream history,
1. update a summary YAML (internal use) with everything that has been done in the previous steps,
1. compile a markdown with everything that has ever been cherry-picked; each commit will be mapped to the tags it was first seen in and associated labels will also be added for completeness.
