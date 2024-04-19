# Software updates for 2023 PbPb apass3 MC processing
# label on github: async-2023-pbpb-apass3

**Starting tags when stable-async was rebased to dev/master for apass1:**

- O2: async-20231204.4
- O2DPG: async-20231204.4-1
- O2Physics: O2Physics::async-20231204.1-4
- QualityControl: v1.126.1
- alidist: O2PDPSuite-daily-20231204-0100

** Tag diverged by stable async and continued strting from 5th April (below), from now on only MC continues **


### Latest requested changes:
| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|

### 18 April 2024:

Special tag for PbPb 2023 apass3. 

Starting point is the tag for pp 2023 apass4, plus two additional fixes. Tag for MC created too.

O2: async-20240229.pbpb.2

O2DPG: async-20240229.pbpb.2


[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/134/)

JIRA: [comment](https://its.cern.ch/jira/browse/O2-3970?focusedId=6289480&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-6289480)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 18.04.2024 | F. Mazzaschi | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1598) | MC | Enable strangeness tracking by default | - | yes| | |
| 18.04.2024| F. Mazzaschi | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1488) | MC | Update pythia gun generator for hypernuclei | - |yes | | |
|18.04.2024 | F. Mazzaschi | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1484) | MC | Add gun for hypernuclei in Pb--Pb | - |yes | | |
| 18.04.2024| D. Krupova | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1468) | MC, needs updated QC | MFT track task for MC | - | yes| | |
|18.04.2024 | O. Schmidt | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1467) | MC, might need updated QC | Will run additional QC task for MC productions which are already enabled for data | - |yes | | |
| 18.04.2024| M. Hemmer | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12490) | MC | The mcCaloCellLabelCursor now won't have initial values (0,0) to reduce size of the table and remove unwanted (0,0) entries  | [EMCAL-889](https://its.cern.ch/jira/browse/EMCAL-889) |yes | | |
| 18.04.2024 | S. Wenzel, B. Volkel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/13000) | MC | Digitization: Fix timestamps for querying CCDB when using BasicCCDBManager | - | yes | | |
| 18.04.2024 | F. Grosa | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1587) | MC | Fix options for collision context creation in (old) embedding path | - | yes | | |
| 18.04.2024 | N. Jacazio | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1580) | MC | Update injection scheme for resonances produced by pythia | - | yes | | |
| 18.04.2024 | N. Jacazio | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1534) | MC | Update injection scheme for resonances produced by pythia | - | yes | | |


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
