# Software expert page

## Collecting the open requests

The open requests to be ported/cherry-picked, can be collected easily as markdown. To do so, run

* for O2: `${O2DPG_ROOT}/UTILS/o2dpg_make_github_pr_report.py --repo AliceO2`, this goes to the report `o2dpg_pr_report_AliceO2.md`,
* for O2DPG: `${O2DPG_ROOT}/UTILS/o2dpg_make_github_pr_report.py --repo O2DPG`, this goes to the report `o2dpg_pr_report_O2DPG.md`.

These can then be directly committed to this repository in the corresponding sub-pages [here](../requests_automtaic/index.md).

As a next step, it is foreseen to run it automatically in a GitLab pipeline and potentially even send an automatic email to the WP12/13 mailing list on Wednesdays at 12:00. With this email, people shall be notified about the upcoming discussion of open requests and get additional general information.

## Approving and marking PRs

All PRs shall be marked with a corresponding `<label>-accepted` label. This is foreseen to be done automatically.
What is foreseen is the following:

1. Cherry-picking shall be done with `cherry-pick -x <ref>`, so note the additional `-x`.
1. Pushing the branch with those cherry-picks back to the upstream repo.
1. GitHub shall automatically deduce everything and set the `<label>-accepted` labels, see also the related PR at https://github.com/alisw/ali-bot/pull/1300.
