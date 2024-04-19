# Software updates for 2023 pp apass and MC processing

## APass3

Creation of the tag is documented in the PbPb apass page, since it correspond to the starting tag for PbPb 2023 apass3: [link](https://gitlab.cern.ch/bvolkel/o2dpgdocs/-/blob/main/docs/software/requests/2023pbpb_apass.md#apass3)

## APass1

**Starting tags (for DATA):**
- O2PDPSuite: VO_ALICE@O2PDPSuite::async-async-20231103.1e-slc[7,8]-alidist-O2PDPSuite-daily-20231006-0200-3 with:
    - O2: async-20231103.1e
    - O2DPG: async-20231030.1c
    - O2Physics: async-20231025.1 
    - QualityControl: v1.119.0-33
    - [Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/92/)

Various patches to the software for data apass1 are discussed in:
- [JIRA comment](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=308365&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-308365)
- [JIRA comment](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=308369&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-308369)

For MC:
- [JIRA comment](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=309099&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-309099)
- [JIRA comment](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=309251&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-309251)
- [JIRA comment](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=309486&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-309486)
- [JIRA comment](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=309099&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-309099)
- [JIRA comment](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=309867&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-309867)

### Requested changes (for MC only, since data was completed with the tag above):

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |   
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| N/A | J. Liu | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1369) | MC | Don't go to test CCDB in QC in MC |  | yes | Did not apply in previous attempt, to be checked why at the next occasion |  |


#### 20.12.2023 - new build

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/105/)

[JIRA](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=310323&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-310323)

- O2: async-20231103.1g created

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |   
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 20.12.2023 | M. Fasel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12029) | MC | Use EMCAL simulation parameters from CCDB | [JIRA](https://alice.its.cern.ch/jira/browse/EMCAL-791)| | | Back-port, already in use in other productions |

#### 20.12.2023

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/103/)

[JIRA](https://alice.its.cern.ch/jira/browse/O2-3970?focusedId=310312&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-310312)

- O2: async-20231103.1f created

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |   
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 20.12.2023 | S. Wenzel, B. Volkel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12457) | MC | fix TPC memery leak | [JIRA](https://alice.its.cern.ch/jira/browse/O2-4494) |yes | yes| |
| 20.12.2023 | S. Wenzel, B. Volkel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12449) | MC | `BasicCCDBMAnager` assume infinite validity of locally created objects | | yes | yes | |
| 20.12.2023 | S. Wenzel, B. Volkel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12413) | MC | seeding fixes and improvements for `o2-sim` | |yes |yes | |
| 20.12.2023 | S. Wenzel, B. Volkel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12346) | MC | bring back reproducibility feature for Geant4 | |yes | yes | |
| 20.12.2023 | J. Liu | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1369) | MC | Don't go to test CCDB in QC in MC |  | yes | NO, DOES NOT APPLY |  |
