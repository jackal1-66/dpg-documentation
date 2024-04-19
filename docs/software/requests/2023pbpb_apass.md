# Software updates for 2023 pp and PbPb apass4 processing
# label on github: async-2023-pbpb-apass

**N.B.: **
- The software for PbPb apass1 was used also for apass2 of LHC23zs (pp 2023)
- The software for PbPb apass1 was used also for apass5 of the skimmed pp 2022 data

**Starting tags when stable-async was rebased to dev/master for apass1:**

- O2: async-20231204.4
- O2DPG: async-20231204.4-1
- O2Physics: O2Physics::async-20231204.1-4
- QualityControl: v1.126.1
- alidist: O2PDPSuite-daily-20231204-0100

## apass4 (only DATA), for MC pleas request in apass3 table -> 2023pbpb_apass3.md

### Latest requested changes:
| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| | C. Puggioni | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1520) | Data | Add new configuration file zdc_PbPb.json with new hitos bin compatible with calibration Use QC v1.135 | - | | | |
| | P. Cortese | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12712) | Data | Preserve numerical accuracy for calibrated signal amplitudes when creating AODs | - | | | |
values (0,0) to reduce size of the table and remove unwanted (0,0) entries  | [EMCAL-889](https://its.cern.ch/jira/browse/EMCAL-889) | | | |
| | C. Zampolli | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1526) | Data | Fixing for setting O2JOBID (for timeframes-rate-limit-ipcid) and SHMEMID |  | | | |


## apass3

### 05 April 2024:

Special tag for PbPb 2023 apass3. 

Starting point is the tag for pp 2023 apass4, plus two additional fixes. Tag for MC created too.

O2: async-20240229.2b (data), asycn-20240229.2b.trd (MC)

O2DPG: async-20240229.2a

[JIRA](https://its.cern.ch/jira/browse/O2-3970?focusedId=6337941&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-6337941)

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/130/)

[JIRA for MC](https://its.cern.ch/jira/browse/O2-3970?focusedId=6338206&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-6338206)

[Build for MC](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/131/)


| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 05.04.2024 | R. Shahoyan | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1575) | Data | Adjusting matching chi2 cut for PbPb 2023 apass3 | - | yes | yes | |
| 05.04.2024| R. Shahoyan | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12841) | Data | Adjust TRD forward pileup margin | - | yes | yes | |
| 05.04.2024| O. Schmidt | O2 | [commit](a0433b890dc7cbf517252168f06ca331b6874d28) | MC | To correct for TRD shift in MC (this commit is not in dev) | - | yes | yes | |


### 20 March 2024 (for apass4 pp  MC)
#### starting from O2: async-20240229.2a and tagging O2: async-20240229.2a.trd with TRD Geo Fix

O2: async-20240229.2a.trd

O2DPG: async-20240229.2

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/125/)


### 15 March 2024 (this is done only for pp 2023 apass3->apass4)
#### changes ported to stable-async and updating tag of 29/02

O2: async-20240229.2a

O2DPG: async-20240229.2

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/124/)

[Build for async-20240229.2 without F. Shlepper commit](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/123/)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 15.03.2024 | R. Shahoyan | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12872) | Data | Fix Z bias of TRD-matched tracks | - | | | |
| 15.03.2024 | D. Rohr | O2 | [commit](https://github.com/AliceO2Group/AliceO2/pull/12727/commits/c1ef553ea06e3aa061c5376fe84b1006bc797eb8) 4da6cbe7d3e6b4d1c39b088e711170f5080cd812 was already in stable-async | Data and MC, does not apply at the moment | Take only the commit in the link!!! fixes memory out of bounds | - | | | |
| 15.03.2024 | F. Schlepper | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12770) | Data | Add collinear DCAFitter and use it in SVertexer | - | | | |

### 14 March 2024:

O2: async-20240314.1

[Build]()

[JIRA](https://its.cern.ch/jira/browse/O2-3970?focusedId=6310597&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-6310597)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 14.03.2024 | P. Cortese | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12712) | Data | ZDC - Update of the intermediate reconstructed format | - | | | |
| 14.03.2024 | D. Rohr | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12843) | Data | Port all TPC Cluster Error changes from dev to stable-async + other needed commits | | yes | | | 



### 11 March 2024

O2: async-20240311.1

O2DPG: async-20240311.1

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/121/)

[JIRA](https://its.cern.ch/jira/browse/O2-3970?focusedId=6307003&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-6307003)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| | R. Shahoyan | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12841) | Data | Adjust TRD forward pileup margin | - | yes | | |
| | R. Shahoyan | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12792) | Data and MC | Discard afterburner tracks in ITS-TPC matching QC | - | yes | | |
| | M. Kleiner | O2 | [PR](https://github.com/AliceO2Group/AliceO2/commit/47d4b6660aff2563eb959435acaba8961b08cee1) | Data | fixes inverse for M-shape correction | - | yes | | |
| | M. Faggin | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1487) | Data/MC | Change eta cut for TPC tracks in GLO QC | - | | yes | |


### 29 February 2024:

O2: async-20240229.1 and async-20240229.1.trd (for MC)

O2DPG: async-20240229.1 and then also async-20240229.2 (since a commit was forgotten)

JIRA: [comment](https://its.cern.ch/jira/browse/O2-3970?focusedId=6289480&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-6289480), [comment](https://its.cern.ch/jira/browse/O2-3970?focusedId=6289659&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-6289659)

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/117/)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 29.02.2024 | C. Zampolli | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1509) | Data|  Sampling of trackQC table|  | yes | |  |
| 29.02.2024 | C. Zampolli | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1510) | Data|  Do not split metrics since it is too slow |  | yes | |  |
| 29.02.2024 | R. Shahoyan | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12783) | MC|  Set mFirstOrbitTF before updateTimeDependentParams |  | yes| |  |
| 29.02.2024 | C. Zampolli | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1508) | MC|  Adding time series in MC |  | yes | |  |
| 29.02.2024 | J. Liu | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1444) | MC |  moving MC QC from test ccdb to qcdb |  | yes |  |  |


### 26 February 2024, additional for MC
O2: async-20240219.2.trd

O2DPG: async-20240219.1.trd

O2Physics: async-20240207.1

JIRA: [comment O2](https://its.cern.ch/jira/browse/O2-3970?focusedId=5753780&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5753780), [comment O2DPG](https://its.cern.ch/jira/browse/O2-3970?focusedId=5754029&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5754029))

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/114/)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
|  | F. Noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/commit/a0433b890dc7cbf517252168f06ca331b6874d28) | MC|  TRD geometry fix (not ported in stable-async!) |  | | |  |
|  | F. Noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/commit/d64f5657045c1babe0d937b3fd29886c776aad58) | MC| Seeding improvements of digitizers  |  | | |  |


### 19 February 2024, additional for MC
O2: async-20240219.1.trd

O2DPG: async-20240219.1.trd

O2Physics: async-20240207.1

JIRA: [comment O2](https://its.cern.ch/jira/browse/O2-3970?focusedId=5753780&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5753780), [comment O2DPG](https://its.cern.ch/jira/browse/O2-3970?focusedId=5754029&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5754029))

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/112/)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 19.02.2024 | F. Noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/commit/a0433b890dc7cbf517252168f06ca331b6874d28) | MC|  TRD geometry fix (not ported in stable-async!) |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1358) | MC |  Align SOR and first orbit with CTPScalers |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12368) | MC |  Include SOR when calculating IR |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12449) | MC |  Re-enable caching property in BasicCCDBManager for digitization |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12457) | MC |  BasicCCDBManager: Assume infinite validity if header info is missing |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12565) | MC |  First orbit should be unsigned int |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12677) | MC |  Force digitisation when not in GRP |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12691) | MC |  Make hmp-matcher-workflow respect selected sources |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1340) | MC |  new anchoredMC.sh for nowadays productions |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1416) | MC |  [SimWF] Always set a process for Pythia8 |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1419) | MC |  Update hadronic cross section in injected MC |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1420) | MC |  Update anchorMC.sh - removing the use of ideal MFT/ITS alignments |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1432) | MC |  Possibility to take external config for Pythia8 |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1437) | MC |  Use consistent timestamp everywhere for anchored |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1452) | MC |  Anchoring: Ability to get detector list from GRPECS |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1441) | MC |  Update reco and sources, take correct workflow detectors that were active in data taking |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1463/files) | MC |  Anchor: Allow for any additional option for sim WF |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1443) | MC |  Fix type error in pipeline runner |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1471) | MC |  pipeline_runner: Fix script creation |  | | |  |
| 19.02.2024 | F. Noferini, C. Ristea | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1365) | MC |  fix ft0 ctp input for pp case |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1395) | MC |  Adjust mem estimates for sgnsim and tpcdigi |  | | |  |
| 19.02.2024 | B. Volkel, S. Wenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1379) | MC |  Seed digitizers to TF seeds for reproducible operation |  | | |  |


### 19 February 2024

O2: async-20240219.1

O2DPG: async-20240219.1

O2Physics: async-20240207.1

JIRA: [comment O2](https://its.cern.ch/jira/browse/O2-3970?focusedId=5753780&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5753780), [comment O2DPG](https://its.cern.ch/jira/browse/O2-3970?focusedId=5754029&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5754029))

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/111/)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 19.02.2024 | G. Volpe | O2 | [PR](https://github.com/AliceO2Group/O2/pull/12725) | DATA |  Adding chamber information in the AOD |  | yes | |  |
| 19.02.2024 | R. Shahoyan | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1470) | DATA |  Adjust matching chi2 cut and max c14 difference|  | yes | |  |
| 19.02.2024 | D. Rohr | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12718) | DATA | fixes a bug where clusters could be attached to the wrong track | | yes | |
| 19.02.2024 | D. Rohr | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12717) | DATA | fixes a bug where tracks were incorrectly constrained in Z | | yes | |
| 19.02.2024 | R. Shahoyan | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12715) | DATA | Fix missing HBFUtilsInitialize plugins in various reader workflows |  |yes | |  |
| 19.02.2024 | R. Shahoyan | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12687) | DATA | Enable TF throttling with readers, use in dpl-workflow |  | yes | |  |
| 19.02.2024 | R. Shahoyan | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1455) | DATA | Restore cluster syst errors for PbPb only |  | yes | |  |
| 19.02.2024 | C. Zampolli | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12680) | DATA | For the split wf | | yes | |
| 19.02.2024 | C. Zampolli | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1451) | DATA | For the split wf | | yes | |
| 19.02.2024 | R. Shahoyan | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12681) | DATA,MC | Suppress excessive logging in the TrackMethods/TPC QC |  | yes | |  |
|  19.02.2024  | N. Valle | O2 | [O2-12644](https://github.com/AliceO2Group/AliceO2/pull/12644) | Data and MC | Fixes and improvements in ITS, MFT efficiency maps | | yes | | |
| 19.02.2024 | N. Jacazio | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1419) | MC | Needed to allow xsection variation in MC |  | yes | |  |
| 19.02.2024 | F. Noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12672) | DATA | Bug fix in TOF diagnostic creation |  | yes | |  |



### 07 February 2024

O2: async-20240207.1

O2DPG: async-20240207.1 and then async-20240207.2

O2Physics: async-20240207.1

JIRA: [comment O2](https://its.cern.ch/jira/browse/O2-3970?focusedId=5753780&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5753780), [comment O2, 2nd part](https://its.cern.ch/jira/browse/O2-3970?focusedId=5754024&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5754024), [comment O2DPG](https://its.cern.ch/jira/browse/O2-3970?focusedId=5754029&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5754029), [comment O2Physics](https://its.cern.ch/jira/browse/O2-3970?focusedId=5754030&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5754030)

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/110/)


| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
|07.02.2024|R. Shahoyan|O2DPG|[PR](https://github.com/AliceO2Group/O2DPG/pull/1449#event-11734965588)|Data|Syst errors and ITS/TPC match params (plus use IDCs for scaling as default)|[JIRA](https://its.cern.ch/jira/browse/O2-4630)|yes|yes, in async-20240207.2||
|07.02.2024|R. Shahoyan|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12670),[PR](https://github.com/AliceO2Group/AliceO2/pull/12655), [PR](https://github.com/AliceO2Group/AliceO2/pull/12607),[PR](https://github.com/AliceO2Group/AliceO2/pull/12624),[PR](https://github.com/AliceO2Group/AliceO2/pull/12612)|Data,MC|Improve e.loss treatment, ITS/TPC matching|[JIRA](https://its.cern.ch/jira/browse/O2-4630)|yes|yes|
|07.02.2024|R. Shahoyan|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12649),[PR](https://github.com/AliceO2Group/AliceO2/pull/12653),[PR](https://github.com/AliceO2Group/AliceO2/pull/12665)|Data,MC|Always load CTP lumi+lumi-dependent errors|[JIRA](https://its.cern.ch/jira/browse/O2-4629)|yes|yes|
|07.02.2024|R. Shahoyan|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12640)|Data|Filter out TPC tracks with anomalous dedx properties|documented in the PR|yes|yes||
|07.02.2024|R. Shahoyan|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12641)|MC|Fix for ITS/MFT time-dependent dead maps|documented in the PR|yes|yes||
|07.02.2024|R. Shahoyan|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12527)|Data,MC|Fix for track L/T integral calculation| |yes|yes|
|07.02.2024|R. Shahoyan|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12488)|Data,MC|Fix in passing corr.maps options, meanLumiRef can be negative| |yes|yes|||
|07.02.2024|R. Shahoyan|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12485)|Data,MC|Optionally impose charge according to PID| |yes|Already merged on 21.12|
|07.02.2024|R.Shahoyan|O2DPG|[PR](https://github.com/AliceO2Group/O2DPG/pull/1440)|Data|Adjust TPC scaling options to O2 PR12653 (CTP lumi always loaded)||yes|yes|
|07.02.2024|R.Shahoyan|O2DPG|[PR](https://github.com/AliceO2Group/O2DPG/pull/1433)|Data|Enable M-shape correction by defualt if any correction is allowed||yes|yes|
|07.02.2024|R.Shahoyan|O2DPG|[PR](https://github.com/AliceO2Group/O2DPG/pull/1428)|Data|Enforce RANS_OPT=--ans-version compat for runs<544772||yes|yes|
|07.02.2024|R.Shahoyan|O2DPG|[PR](https://github.com/AliceO2Group/O2DPG/pull/1412)|MC|Fix passing some ConfigurableParams to sim_workflow||yes|yes|
|07.02.2024|N. Valle|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12525)|MC|Use time-dependent efficiency maps for ITS and MFT|[JIRA](https://its.cern.ch/jira/browse/O2-3676)|yes|yes||
|07.02.2024|F. Schlepper|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12566),[PR](https://github.com/AliceO2Group/AliceO2/pull/12598)|Data|Add GloQC Efficiency Plots. An issue observed only occuring in MC was fixed.|[JIRA](https://its.cern.ch/jira/browse/QC-1091)|yes|yes||
|07.02.2024|F. Noferini, N. Jacazio|O2Physics|[PR-4287](https://github.com/AliceO2Group/O2Physics/pull/4287),[PR-4387](https://github.com/AliceO2Group/O2Physics/pull/4387),[PR-4462](https://github.com/AliceO2Group/O2Physics/pull/4462)|Data|TOF pid QA|[AQC report](https://indico.cern.ch/event/1371938/contributions/5768192/attachments/2785835/4857205/TOFQC_23_01_2024.pdf)|yes|yes||
|07.02.2024|F. Noferini, N. Jacazio|O2DPG|[PR-1417](https://github.com/AliceO2Group/O2DPG/pull/1417),[PR-1425](https://github.com/AliceO2Group/O2DPG/pull/1425)|Data|TOF pid QA (one PR still missing)|[AQC report](https://indico.cern.ch/event/1371938/contributions/5768192/attachments/2785835/4857205/TOFQC_23_01_2024.pdf)|yes|yes||
|07.02.2024|A. Furs|QC|Use tag v1.126.3|Data|FT0 recoQC: more detailed performance plots|[AFIT-15](https://its.cern.ch/jira/browse/AFIT-15)|yes|Superseded by the request to have v1.126.5||
|07.02.2024|A. Furs|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12586)|Data|FT0 reco: rounding for mean times|[AFIT-3](https://its.cern.ch/jira/browse/AFIT-3)|yes|yes||
|07.02.2024|L. Serksnyte|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12452)|Data,MC|TPC QC: including cluster information per track to see the shared, reconstructed cluster distributions||yes|already in a previous tag (15 Dec)||
|07.02.2024|L. Serksnyte|O2DPG|[PR](https://github.com/AliceO2Group/O2DPG/pull/1424)|Data,MC|TPC QC: corresponding json updates for the cluster information per track task||yes|yes||
|07.02.2024|A. Furs|O2Physics|[PR-4476](https://github.com/AliceO2Group/O2Physics/pull/4476)|Data|FT0CorrectedTable: hotfix for dummy time filtering||yes|yes||
|07.02.2024 | A. Molander | O2DPG | [O2DPG/1423](https://github.com/AliceO2Group/O2DPG/pull/1423) | Data, MC, | Analysis QC for FT0 | [AFIT-74](https://its.cern.ch/jira/browse/AFIT-74) |yes |yes | |
|07.02.2024|L. Massacrier|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12614)|Data,MC|MCH: switch on the reading of BadChannels after including a protection in the code for Invalid Solar Id and Pad Id||yes|yes||
|07.02.2024|L. Serksnyte|QC|Use tag v1.126.4|Data,MC|TPC QC: including cluster information per track to see the shared, reconstructed cluster distributions||yes|Superseded by the request to have v1.126.5||
|07.02.2024|C. Zampolli|O2DPG|[PR](https://github.com/AliceO2Group/O2DPG/pull/1411), [PR](https://github.com/AliceO2Group/O2DPG/pull/1415), [PR](https://github.com/AliceO2Group/O2DPG/pull/1439), [PR](https://github.com/AliceO2Group/O2DPG/pull/1446)|Data|Change scaling fraction for skimmed data when running on skimmed CTFs||yes|yes||
|07.02.2024|C. Zampolli|O2DPG|[PR](https://github.com/AliceO2Group/O2DPG/pull/1410)|Data|Forbid AOD merging to fail||yes|yes||
|07.02.2024|D. Rohr|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12561)|Data|Fix issue in decoding TPC clusters||yes|yes| 
|07.02.2024|L. Serksnyte|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12630)|Data,MC|TPC QC: added PID hypothesis to TPC QC||yes|yes||
|07.02.2024|L. Serksnyte|QC|Use tag v1.126.5|Data,MC|TPC QC: added PID hypothesis to TPC QC||yes|yes||
|07.02.2024|Matthias, Marian|O2|https://github.com/AliceO2Group/AliceO2/pull/12615|Data,MC| Skimmed data udate - ||yes|yes|| 
|07.02.2024|Matthias, Marian|O2|https://github.com/AliceO2Group/AliceO2/pull/12637|Data,MC| Skimmed data udate PID for tracking - ||yes|yes|| 
|07.02.2024|Sandro, Marian|O2PDG|https://github.com/AliceO2Group/O2DPG/pull/1438|Data,MC| Skimmed data udate - ||yes|yes||
|07.02.2024|Matthias, Ruben |O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12439), [PR](https://github.com/AliceO2Group/AliceO2/pull/12628), [PR](https://github.com/AliceO2Group/AliceO2/pull/12631)  |Data| M-Shape correction ||yes|yes||
|07.02.2024|F. Schlepper|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12415), then [PR](https://github.com/AliceO2Group/AliceO2/pull/12664)|Data|Stop propagation of Tracks assoc. to V0 to PV||yes|yes||
|07.02.2024|Jens, David |O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12568), [PR](https://github.com/AliceO2Group/AliceO2/pull/12618), [PR](https://github.com/AliceO2Group/AliceO2/pull/12627)  |Data,MC| Use dead channel map in tracking ||yes|yes||

## apass2

### 15 January 2024

O2: async-20240115.1

O2DPG: async-20240115.1, and also async-20240115.1 including the change by Sandro below.

[JIRA](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=310804&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-310804)

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/108/)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
|15.01.2024|R. Shahoyan|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12507)|Data|Fix passing the options for derivative scaling to all devices||yes|yes||
|15.01.2024|M. Kleiner|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12506), [PR](https://github.com/AliceO2Group/AliceO2/pull/12512)|Data|Using weights to scale IDCs||yes|yes||
|15.01.2024|R. Shahoyan|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12516)|Data, MC|Fix for propagation of particles with q > 1||yes|yes||
|15.01.2024|M. Puccio|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12498), [O2](https://github.com/AliceO2Group/AliceO2/pull/12489), [O2DPG](https://github.com/AliceO2Group/O2DPG/pull/1407)|Data|ITS tracking improvements in terms of memory handling||yes|yes||
|15.01.2024|L. Massacrier|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12511)|Data (pp 2022 skimmed!!!)|Disable BadChannel CCDB usage||yes|yes||
|15.01.2024|S. Wenzel|O2DPG|[PR](https://github.com/AliceO2Group/O2DPG/pull/1406)|MC|Avoid that TPC distortions are used in reco of MC||yes|yes||
|15.01.2024|F. Noferini|O2DPG|[PR](https://github.com/AliceO2Group/O2DPG/pull/1408)|Data/MC|Update cuts for TOF QC||yes|yes||
|15.01.2024|B. Von Haller|QC|Use tag v1.126.2|Data/MC|Don't ignore errors when retrieving CCDB objects in QC||yes||




## apass1
### 22.12.2023

O2DPG: async-2023122.1

Final tag: "VO_ALICE@O2PDPSuite::async-async-20231221.1-slc[7,8]-alidist-O2PDPSuite-daily-20231208-0100-2"

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/107/)

[JIRA](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=310354&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-310354)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
|22.12.2023|M. Faggin|O2DPG|[PR](https://github.com/AliceO2Group/O2DPG/pull/1401)|Data/MC|Fix for the cut on the chi2/cluster||yes|yes||

### 21.12.2023

O2: async-2023121.1
O2DPG: async-2023121.1

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/106/)

[JIRA](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=310346&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-310346)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
|21.12.2023|R.Shahoyan|O2DPG|[PR](https://github.com/AliceO2Group/O2DPG/pull/1397)|Data|Decrease safety time margin for ITSTPC matching to 2ms||yes|yes||
|21.12.2023|R.Shahoyan|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12485)|Data|Optionally impose charge according to the PID, use in TPC output ||yes|yes||
|21.12.2023|R.Shahoyan|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12484)|Data|Fix CCDB DPL fetcher logging and refresh rate check ||yes|yes||
|21.12.2023|wiechula|O2|[PR](https://github.com/AliceO2Group/AliceO2/pull/12482)|Data|TPC: Add missing TF dependent ccdb update||yes|yes||

### 20.12.2023

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/104/)

[JIRA](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=310314&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-310314)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 20.12.2023 | D. Chinellato | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1391) | MC | Add TPC tracks to sec vtx sources. as in data |  | yes |  yes|  |
| 20.12.2023 | J. Liu | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1369) | MC | Don't go to test CCDB in QC in MC |  | yes | yes |  |
| 20.12.2023 | C. Zampolli | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1396) | data | Don't check O2trackqa table in sanity check, since it won't pass them, due to downsampling |  | yes | yes |  |


### 18 December 2023 - second tag

[Build #101](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/101/)

[JIRA comment](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=310198&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-310198)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 18.12.2023 | A.Molander | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1393) | MC | FIT: set digitizer gain settings | [O2-4379](https://alice.its.cern.ch/jira/browse/O2-4379) | yes | yes |  |

### 18 December 2023

[Build #100](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/100/)

[JIRA comment](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=310161&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-310161)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 18.12.2023 | F. Noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12477) | Data | Fix for TOF calib to be extracted in apass1 PbPb 2023 | | yes | yes |  |


### 16 December 2023

[Build #99](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/99/)

[JIRA comment](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=310149&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-310149), [other comment](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=310150&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-310150)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 16.12.2023 | R.Shahoyan | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12476) | Data | Eliminate extra conflict in global/local options name | | yes | yes |  |
| 16.12.2023 | R. Shahoyan | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12475) | Data | Eliminate conflict in global/local options name | | yes | yes |  |
| 16.12.2023 | C. Zampolli | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12474) | Data | Fix for unbound vars | | yes | yes |  |


### 15 December 2023

[Build #97](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/97/)

[JIRA comment](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=310140&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-310140)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 15.12.2023 | R. Shahoyan | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12473) | Data | Fixes for ITS/MFT deadmap producer | | yes | yes |  |
| 15.12.2023 | O. Schmidt | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12468) | Data | Fix PID assumption in the ITS extrapolation | | yes | yes |  |
| 15.12.2023 | N. Valle | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12471) | Data | Use std::maps for ITS/MFT deadmaps storage  | | yes | yes |  |
| 15.12.2023 | M. Fasel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12453) | MC | Include FIT trigger into EMCAL simulation | [EMCAL-1055](https://alice.its.cern.ch/jira/browse/EMCAL-1055)| yes | yes |  |
| 15.12.2023 | M. Coquet | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1382) | MC | Applying MFT alignment in anchored MC  | [O2-4470](https://alice.its.cern.ch/jira/browse/O2-4470) | yes | yes | yes |
| 15.12.2023 | L. Serksnyte | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1389) | Data | Moving window implementation | | yes |  yes |  |
| 15.12.2023 | L. Serksnyte | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12462) | Data | Fix in QC tracks task to have DCA for TPC| | yes |  yes |  |
| 15.12.2023 | L. Serksnyte | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12452) | Data | Shared cluster distribution implementation for TPC | | yes | yes  |  |
| 15.12.2023 | D. Grund     | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1392) | Data | MFT moving window            | | yes | yes  |  |
| 15.12.2023 | N. Valle | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12459) | Data | ITS, MFT efficiency maps | | yes| yes| |
| 15.12.2023 | A. Furs | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1390) | Data | Restoring previous reco PbPb config | | yes | yes  |  |


### 14 December 2023:

[Build #95](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/95/)

[JIRA comment](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=310041&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-310041)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 14.12.2023 | C. Zampolli | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1388) | MC | Hot fix for MC, otherwise tests won't work| | yes | yes  |  |
| 14.12.2023 | C. Zampolli | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1387) | Data | For split wf | | yes | yes  |  |

### 13 December 2023:

[Build #94](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/94/)

[JIRA comment](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=310015&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-310015)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 13.12.2023 | O. Schmidt | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12455) | Data | | | yes | yes  |  |
| 13.12.2023 | C. Zampolli | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12458) | Data | | | yes | yes |  |
| 13.12.2023 | M. Ivanov | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12387) | Data | TPC QA and PID information in the AO2D #12387 | | yes | yes |  |
| 13.12.2023 | C. Zampolli, F. Noferini | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1380) | Data | | | yes | yes |  |
| 13.12.2023 | D. Chinellato, F. Schlepper | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12420) | Data | | | yes | yes |  |
| 13.12.2023 | M. Concas | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12424) | MC | It does not directly affect Data as we use MatBud LUT, it would be needed for MC. | [JIRA](https://alice.its.cern.ch/jira/browse/O2-4488) | yes | yes |  |
| 13.12.2023 | J. Castillo, L. Massacrier | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12421) | Data | Add MCH track clusters table to AO2D | |yes | yes | yes |
| 13.12.2023 | M. Concas | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12410) | MC, Data | Reduce some of the persistent ITS memory footprint | | yes| yes | |
| 13.12.2023 | S. Wenzel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12449) | MC | Fix of TPC digi mem problem | | yes| yes | |
| 13.12.2023 | S. Wenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1381) | MC | MFT geometry setting | | yes| yes| |
| 13.12.2023 | R.Shahoyan| O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12409) | MC/Data | Prefer CCDB snaphot if it exists | |yes |yes | yes|
| 13.12.2023 | R.Shahoyan| O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12423) | Data | Pass sources to HMP matcher | |yes | yes| yes|
| 13.12.2023 | R.Shahoyan| O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12419) | Data/MC | Restore propagation of CCDB download failure error | |yes| yes | yes|
| 13.12.2023 | R.Shahoyan| O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12454) | Data/MC | per-sector selection of minTPCrow | |yes| yes| yes|
| 13.12.2023 | R.Shahoyan| O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12443) | Data/MC | Flag standard V0s / photons | |yes|yes | yes|
| 13.12.2023 | D.Chinelatto| O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12435) | Data/MC | Add V0 flag to AOD model | |yes| yes | yes|
| 13.12.2023 | D.Chinellato| O2Physics | [PR](https://github.com/AliceO2Group/O2Physics/pull/4151) | Data/MC | Fix V0s converter default V0type| |yes|yes | yes|
| 13.12.2023 | D.Chinellato| O2Physics | [PR](https://github.com/AliceO2Group/O2Physics/pull/4156) | Data/MC | V0 table producers switching  | |yes|yes | yes|
| 13.12.2023 | D.Chinellato| O2Physics | [PR](https://github.com/AliceO2Group/O2Physics/pull/4138) | Data/MC | V0 converter | |yes| yes| yes|
| 13.12.2023 | D.Rohr| O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12460) | Data/MC | Prevent accepting TPC tracks with failed fit | |yes| yes | yes|
| 13.12.2023   |  L. Šerkšnytė    | O2DPG    | [PR](https://github.com/AliceO2Group/O2DPG/pull/1383) |  MC | updated MC json file which was more than a year old and missing some new histos | | yes | yes | |
| 13.12.2023 | B. Volkel, S. Wenzel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12457) |  MC | solves a critical problem when cached CCDB objects shall be used by `BasicCCDBManager` with missing validity info | | yes | yes | |



### 08 December 2023:

[Build #91](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/91/)

[JIRA comment](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=309849&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-309849)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
|   8.12.2023   |  C. Zampolli     | O2DPG    | [PR](https://github.com/AliceO2Group/O2DPG/pull/1366) | Data  | |  |  yes | yes | yes |
|   8.12.2023   |  L. Šerkšnytė    | O2DPG    | [PR](https://github.com/AliceO2Group/O2DPG/pull/1367) |  Data |  | | yes | yes | yes|
|   8.12.2023   | D. Rohr           | O2      | [PR](https://github.com/AliceO2Group/AliceO2/pull/12407), [PR](https://github.com/AliceO2Group/AliceO2/pull/12412), [PR](https://github.com/AliceO2Group/AliceO2/pull/12414) | Data | | | yes | yes | |
|   8.12.2023   | D. Rohr           | O2DPG      | [PR](https://github.com/AliceO2Group/O2DPG/pull/1371), [PR]( https://github.com/AliceO2Group/O2DPG/pull/1374) | Data | | | yes| yes|
|   8.12.2023   | A. Isakov        | O2DPG    |[PR](https://github.com/AliceO2Group/O2DPG/pull/1197) | Data | | | yes |yes|
|  8.12.2023    | F. Noferini      | O2       | [PR](https://github.com/AliceO2Group/AliceO2/pull/12408) | Data | not super-urgent, it would impact only on one QC plot for TPConly TOF-matched tracks | | yes |yes| yes|
|   8.12.2023   |  S. Wenzel, B. Volkel | O2    | [PR](https://github.com/AliceO2Group/AliceO2/pull/12413) |MC | further statistical inconsistencies have been found in simulation | |yes |yes|
|   8.12.2023   |  S. Wenzel, B. Volkel | O2    | [PR](https://github.com/AliceO2Group/AliceO2/pull/12411) | MC | Make config params for FIT usable (some were `static constexpr` before) | | yes| yes|
|  8.12.2023    |  S. Wenzel, B. Volkel | alidist, AEGIS | [PR](https://github.com/alisw/alidist/pull/5277) | MC | Means moving to latest alidist | |yes | yes|
