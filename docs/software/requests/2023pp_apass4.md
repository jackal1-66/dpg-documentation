# Software updates for 2023 pp apass4 MC processing
# label on github: async-2023-pp-apass4

**Starting tags when stable-async was rebased to dev/master for apass1:**

- O2: async-20231204.4
- O2DPG: async-20231204.4-1
- O2Physics: O2Physics::async-20231204.1-4
- QualityControl: v1.126.1
- alidist: O2PDPSuite-daily-20231204-0100

** Tag diverged by stable async and continued strting from 20th March (below), from now on only MC continues **


### Latest requested changes:
| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|

### 19 April 2024:

Special tag for pp 2023 apass3. 

Starting point is the tag for pp 2023 apass4, plus two additional fixes. Tag for MC created too.

O2: async-20240229.pp.2

O2DPG: async-20240229.pp.2


[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/135/)

JIRA: [comment](https://its.cern.ch/jira/browse/O2-3970?focusedId=6289480&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-6289480)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 19.04.2024 | F. Mazzaschi | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1598) | MC | Enable strangeness tracking by default | - |yes | | |
| 19.04.2024| F. Mazzaschi | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1488) | MC | Update pythia gun generator for hypernuclei | - |yes | | |
| 19.04.2024| F. Mazzaschi | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1484) | MC | Add gun for hypernuclei in Pb--Pb | - |yes | | |
| 19.04.2024| D. Krupova | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1468) | MC, needs updated QC | MFT track task for MC | - | yes| | |
| 19.04.2024| O. Schmidt | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1467) | MC, might need updated QC | Will run additional QC task for MC productions which are already enabled for data | - |yes | | |
| 19.04.2024| M. Hemmer | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12490) | MC | The mcCaloCellLabelCursor now won't have initial values (0,0) to reduce size of the table and remove unwanted (0,0) entries  | [EMCAL-889](https://its.cern.ch/jira/browse/EMCAL-889) | yes| | |
|  19.04.2024| S. Wenzel, B. Volkel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/13000) | MC | Digitization: Fix timestamps for querying CCDB when using BasicCCDBManager | - | yes | | |
|  19.04.2024| F. Grosa | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1587) | MC | Fix options for collision context creation in (old) embedding path | - | yes | | |
| 19.04.2024 | N. Jacazio | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1580) | MC | Update injection scheme for resonances produced by pythia | - | yes | | |
| 19.04.2024 | N. Jacazio | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1534) | MC | Update injection scheme for resonances produced by pythia | - | yes | | |


### 20 March 2024 (for apass4 pp  MC)
#### starting from O2: async-20240229.2a and tagging O2: async-20240229.2a.trd with TRD Geo Fix

O2: async-20240229.2a.trd

O2DPG: async-20240229.2

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/125/)

