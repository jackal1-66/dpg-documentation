# Software for 2022 pp apass4, Simulation

For pp 2022 there are 2 branches

* O2: [https://github.com/AliceO2Group/AliceO2/tree/async-2022-apass4-pp-mc](https://github.com/AliceO2Group/AliceO2/tree/async-2022-apass4-pp-mc)
* O2DPG: [https://github.com/AliceO2Group/O2DPG/tree/async-2022-apass4-pp-mc](https://github.com/AliceO2Group/O2DPG/tree/async-2022-apass4-pp-mc)
* alisw/alidist async-2022-apass4-pp-mc.1

and tags for pp 2022 are created from those branches.

## Development and testing

Any changes that need to be back-ported shall be introduced via PRs to those branches.

For [O2@async-2022-apass4-pp-mc](https://github.com/AliceO2Group/AliceO2/tree/async-2022-apass4-pp-mc) there is already a CI in place based on [ali-bot](https://github.com/alisw/ali-bot/blob/master/ci/repo-config/mesosci/slc8-gpu/o2-fullci-2022pp-apass4.env).


## Additional comments

* O2: A few commits were cherry-picked on top of tag: [async-20230706.1a](https://github.com/AliceO2Group/AliceO2/tree/async-20230706.1a) that mostly consolidate the AODProducer. We had various issues that were related to segfaults. These should all be under control now.
* O2DPG: Here I cherry-picked everything starting from  [async-20230515.1](https://github.com/AliceO2Group/O2DPG/tree/async-20230515.1) up to upstream/master (just a few days ago). So the latest commit in O2DPG currently is (this is from upstream/master): [https://github.com/AliceO2Group/O2DPG/commit/6f4eb9199b22b41aa1e778f877e887384cdc7b98](https://github.com/AliceO2Group/O2DPG/commit/6f4eb9199b22b41aa1e778f877e887384cdc7b98)
* all other sw versions are untouched, so basically
    * O2Physics: [async-20230515.1](https://github.com/AliceO2Group/O2Physics/tree/async-20230515.1)
    * QC: [v1.101.1](https://github.com/AliceO2Group/QualityControl/tree/v1.101.1)
    * alidist: [O2PDPSuite-nightly-20230515](https://github.com/alisw/alidist/tree/O2PDPSuite-nightly-20230515)

Tests for initial cherry-picking in O2 and O2DPG were run with [https://gitlab.cern.ch/o2simulationtools/alice-dpg-tests/-/tree/main/reco-2022/20231122?ref_type=heads](https://gitlab.cern.ch/o2simulationtools/alice-dpg-tests/-/tree/main/reco-2022/20231122?ref_type=heads).

# Requested changes:
| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |   
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|


# 12.04.2024

O2: async-2022-apass4-pp-mc.4c

O2DPG: async-2022-apass4-pp-mc.4c

Retagging also O2

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/133/)

[JIRA] (https://its.cern.ch/jira/browse/O2-3970?focusedId=6306700&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-6306700)


| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |   
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 12.04.2024 | F. Grosa | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1587) | MC | Fix options for collision context creation in (old) embedding path | - | yes | | |
| 12.04.2024 | S. Wenzel, B. Volkel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/13000) | MC | Digitization: Fix timestamps for querying CCDB when using BasicCCDBManager | - | yes | | |
| 12.04.2024 | N. Jacazio | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1580) | MC | Update injection scheme for resonances produced by pythia | - | yes | | |
| 12.04.2024 | N. Jacazio | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1534) | MC | Update injection scheme for resonances produced by pythia | - | yes | | |


# 04.04.2024

O2: async-2022-apass4-pp-mc.4b

O2DPG: async-2022-apass4-pp-mc.4b

Retagging also O2

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/128/)

[JIRA] (https://its.cern.ch/jira/browse/O2-3970?focusedId=6306700&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-6306700)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |   
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 02.04.2024 | F. Noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/commit/a3142359b3b535f0654077234eeeadc1c313b64e) | MC |  Option for PreHadron pruning in Pythia8 events |  | yes | 
| 02.04.2024 | F. Catalano | O2DPG | reverting [PR](https://github.com/AliceO2Group/O2DPG/commit/5bce1d49d451269dd04f0851a1f07bfc0b4dca1a) | MC |  Add bash script for D2H anchored MC |  | reverted | 
| 02.04.2024 | F. Catalano | O2DPG | reverting [PR](https://github.com/AliceO2Group/O2DPG/commit/90920b3036117d80e9849a08576fa9c4b3fb637b) | MC | Remove unsupported option  | | reverted | 

# 28.03.2024

O2: async-2022-apass4-pp-mc.4a

O2DPG: async-2022-apass4-pp-mc.4a

Retagging also O2

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/127/)

[JIRA] (https://its.cern.ch/jira/browse/O2-3970?focusedId=6306700&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-6306700)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |   
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| N/A | M. Fasel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12729) | MC | Load CTP configuration per run, instead of hard coded object | | NO, since too many missing deps | 
| 28.03.2024 | F. Grosa | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1552) | MC |  Enhance fraction of D+ to KKpi in D2H MC + new configuration #1552 | | yes | 
| 28.03.2024 | F. Grosa | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1553) | MC |  PWGHF: Add configuration for sim with pT-hard bins (no gap) #1553 | | yes | 
| 28.03.2024 | F. Catalano | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/commit/5bce1d49d451269dd04f0851a1f07bfc0b4dca1a) | MC |  Add bash script for D2H anchored MC |  | yes | 
| 28.03.2024 | F. Catalano | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/commit/90920b3036117d80e9849a08576fa9c4b3fb637b) | MC | Remove unsupported option  | | yes | 

# 11.03.2024

O2: async-2022-apass4-pp-mc.4

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/120/)

[JIRA] (https://its.cern.ch/jira/browse/O2-3970?focusedId=6306700&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-6306700)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |   
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 11.03.2024 | C. Zampolli | O2 | [PR](https://github.com/AliceO2Group/AliceO2/blob/async-2022-apass4-pp-mc.1/DataFormats/Parameters/src/GRPObject.cxx) | MC | Fixing a missing conversion factor for sqrt(S) | [link](https://its.cern.ch/jira/browse/O2-4271?focusedId=6306629&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-6306629) | yes | | | 

## 01.03.2024

O2: async-2022-apass4-pp-mc.3

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/119/)

[JIRA](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=310310&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-310310)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |   
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
|  | F. Noferini | alidist | 250b3729b557761daf015f812f9cac2e3adff147 | MC | Install OpenSSL's pkgconfig files (#5271) |  | no |  |  |
| 01.03.2024 | F. Noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/commit/a0433b890dc7cbf517252168f06ca331b6874d28) | MC|  TRD geometry fix |  | yes | |  |
| 01.03.2024 | F. Noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/11661) 36caf2d3f7da5c4eb83b18ede706dd07b19f3901 | MC|   TRD new structure for Tracklet64 (#11661) |  | yes | |  |
| 01.03.2024 | F. Noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/commit/7aa359fd58df6b99d67791e5cba6e38a434093a0) 7aa359fd58df6b99d67791e5cba6e38a434093a0 | MC| TRD tracklet pad column lookup fix |  | yes | |  |
| 01.03.2024 | A. Molander | O2 | [PR](https://github.com/AliceO2Group/AliceO2/commit/8330214543c5feb248dcea540a0950cffeef3c11) 8330214543c5feb248dcea540a0950cffeef3c11 | MC| FIT: Base TOF for sim hits on hit pos instead of fixed detector pos |  | yes | |  |
| 01.03.2024 | A. Molander, F. Noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/11650) 8872f73f824a3ef867d4228c09b1fc5f25a8417e | MC| FITRaw: refactoring + new raw data metric feature (#11650) |  | yes | |  |
| N/A | J. Liu | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1444) | MC |  moving MC QC from test ccdb to qcdb |  | no |  |  |

## 20.12.2023

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/102/)

[JIRA](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=310310&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-310310)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |   
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 20.12.2023 | J. Liu | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1369) | MC | Don't go to test CCDB in QC in MC |  | yes | NO, DOES NOT APPLY, NEEDS FURTHER CHECKS |  |
| 20.12.2023 | M. Fasel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12463) | MC | EMCAL trigger simulation |  | yes | yes |  |
