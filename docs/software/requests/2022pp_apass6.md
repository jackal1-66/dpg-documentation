# Software for 2022 pp apass6 and Pb-Pb apass2, Simulation
#label on github: async-2022-pp-apass6/pbpb-apass2

## Reference branches

* O2DPG [async-2022-apass6-pp](https://github.com/AliceO2Group/O2DPG/tree/async-2022-apass6-pp)
* O2 [async-2022-apass6-pp]()

# Requested changes:
| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|

### 19 April 2024, additional for MC
O2: async-20240115.6.trd

O2DPG: async-20240115.6.trd

O2Physics: async-20231213.1

JIRA: [comment O2](https://its.cern.ch/jira/browse/O2-3970?focusedId=5753780&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5753780), [comment O2DPG](https://its.cern.ch/jira/browse/O2-3970?focusedId=5754029&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5754029))

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/136/)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 19.04.2024 | F. Mazzaschi | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1598) | MC | Enable strangeness tracking by default | - |yes | | |

### 12 April 2024, additional for MC
O2: async-20240115.6.trd

O2DPG: async-20240115.5.trd

O2Physics: async-20231213.1

JIRA: [comment O2](https://its.cern.ch/jira/browse/O2-3970?focusedId=5753780&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5753780), [comment O2DPG](https://its.cern.ch/jira/browse/O2-3970?focusedId=5754029&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5754029))

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/132/)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 12.04.2024 | F. Mazzaschi | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1488) | MC | Update pythia gun generator for hypernuclei | - | yes | | |
| 12.04.2024 | F. Mazzaschi | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1484) | MC | Add gun for hypernuclei in Pb--Pb | - | yes | | |
| 12.04.2024 | F. Grosa | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1587) | MC | Fix options for collision context creation in (old) embedding path | - | yes | | |
| 12.04.2024 | S. Wenzel, B. Volkel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/13000) | MC | Digitization: Fix timestamps for querying CCDB when using BasicCCDBManager | - | yes | | |
| 12.04.2024 | N. Jacazio | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1580) | MC | Update injection scheme for resonances produced by pythia | - | yes | | |
| 12.04.2024 | N. Jacazio | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1534) | MC | Update injection scheme for resonances produced by pythia | - | yes | | |
| 12.04.2024 | F. Catalano | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1582) | MC | PWGHF: add xic+ in ini file and rename | | yes | | Yes |
| 12.04.2024 | F. Catalano | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1577) | MC | [Anchor] Remove exit | | yes | | Yes |
| 12.04.2024 | F. Catalano | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1539) | MC | Prototype decouple event gen from transport | [JIRA](https://its.cern.ch/jira/browse/O2-4754) | yes | | Yes |
| 12.04.2024 | F. Catalano | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1464) | MC | [Anchor] Add test for anchored MC | | yes | | Yes |
| 12.04.2024 | F. Catalano | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1384) | MC | [WF CI] Test also QC and AnalysisQC <br/> Two commits: eab175696e7dde819c8ef783e7c4001debbcc552, 61e60a4ccd9ab0748d7b7be87ad947b9a1862338 | | yes | | Yes |
| 12.04.2024 | F. Catalano | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1511) | MC | [Anchor] Add some more help messages | |yes  | | Yes |
| 12.04.2024 | F. Catalano | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1508) | MC | Running extraction of TPC time series in anchored MC | |yes  | | Yes |
| 12.04.2024 | F. Catalano | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1543) | MC | [SimWF] Recompute number of workers used in TFs | |yes  | | Yes |
| 12.04.2024 | F. Catalano | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1531) | MC | porting of MID aQC workflow to MC | |  |yes | Yes |
| 12.04.2024 | F. Catalano | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1402) | MC | Always take field for sim from CCDB | |  | yes| Yes |
| 12.04.2024 | F. Catalano | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1532) | MC | [WFRunner] Handle resource limits and CPU better | | yes | | Yes |
| 12.04.2024 | F. Catalano | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1413) | MC | [WF Runner] Fix when initial resources exceed boundaries | | yes | | Yes |
| 12.04.2024 | F. Catalano | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1329) | MC | [WFRunner] Estimate resources dynamically | | yes | | Yes |
| 12.04.2024 | F. Catalano | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12954) | MC | More consistent MCHeader forwarding when using GeneratorFromFile | [JIRA](https://its.cern.ch/jira/browse/O2-4754) |  |yes | Yes |
| 12.04.2024 | F. Catalano | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12920) | MC | More flexibel use of event setup from collisioncontext | [JIRA](https://its.cern.ch/jira/browse/O2-4754) |  |yes | Yes |
| 12.04.2024 | F. Catalano | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12899) | MC | Some changes needed to improve decoupling event generation from GEANT transport. <br/> Two commits: d6aa59738efe65730a08f98bbc87fa8ad9afc95f, 4619c835e283cb62c6bf23d6a0d1ba1f264beb60 | [JIRA](https://its.cern.ch/jira/browse/O2-4754) |  | yes| Yes |
| 12.04.2024 | F. Catalano | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12891) | MC | MCTrack: Calculate energy in double | [JIRA](https://its.cern.ch/jira/browse/O2-4754) |  |yes | Yes |


### 04 April 2024, additional for MC
O2: async-20240115.5.trd

O2DPG: async-20240115.4.trd

O2Physics: async-20231213.1

JIRA: [comment O2](https://its.cern.ch/jira/browse/O2-3970?focusedId=5753780&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5753780), [comment O2DPG](https://its.cern.ch/jira/browse/O2-3970?focusedId=5754029&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5754029))

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/126/)


| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |   
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 04.04.2024 | F. Grosa | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1552) | MC |  Enhance fraction of D+ to KKpi in D2H MC + new configuration #1552 | | yes | 
| 04.04.2024 | F. Grosa | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1553) | MC |  PWGHF: Add configuration for sim with pT-hard bins (no gap) #1553 | | yes | 

### 28 March 2024, additional for MC
O2: async-20240115.5.trd

O2DPG: async-20240115.3.trd

O2Physics: async-20231213.1

JIRA: [comment O2](https://its.cern.ch/jira/browse/O2-3970?focusedId=5753780&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5753780), [comment O2DPG](https://its.cern.ch/jira/browse/O2-3970?focusedId=5754029&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5754029))

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/129/)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 28.03.2024 | M. Fasel | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12729) | MC|  Fixes in CTP digitizer for anchored MC |  | yes| |  |
| 28.03.2024 | M. Hemmer | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12490) | MC|  AODProducerWorkflowSpec: Fix mcCaloCellLabelCursor filling scheme |  | yes| |  |


### 29 February 2024, additional for MC
O2: async-20240115.4.trd

O2DPG: async-20240115.3.trd

O2Physics: async-20231213.1

JIRA: [comment O2](https://its.cern.ch/jira/browse/O2-3970?focusedId=5753780&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5753780), [comment O2DPG](https://its.cern.ch/jira/browse/O2-3970?focusedId=5754029&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5754029))

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/116/)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 28.02.2024 | F. Noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12783) | MC|  Set mFirstOrbitTF before updateTimeDependentParams |  |yes | |  |
| 28.02.2024 | F. Noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12641) | MC|  Avoid static vars in the ITS/MFT digitizer |  | |yes |  |

### 27 February 2024, additional for MC
O2: async-20240115.3.trd

O2DPG: async-20240115.3.trd

O2Physics: async-20231213.1

JIRA: [comment O2](https://its.cern.ch/jira/browse/O2-3970?focusedId=5753780&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5753780), [comment O2DPG](https://its.cern.ch/jira/browse/O2-3970?focusedId=5754029&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5754029))

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/115/)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 27.02.2024 | F. Noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/commit/a0433b890dc7cbf517252168f06ca331b6874d28) | MC|  TRD geometry fix |  | yes| |  |
| 27.02.2024 | F. Noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/commit/d64f5657045c1babe0d937b3fd29886c776aad58) | MC| Seeding improvements of digitizers  |  | yes| |  |
| 27.02.2024 | F. Noferini, C. Ristea | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1365) | MC |  fix ft0 ctp input for pp case |  | | yes|  |

### 20 February 2024, additional for MC
O2: async-20240115.2.trd

O2DPG: async-20240115.2.trd

O2Physics: async-20231213.1

JIRA: [comment O2](https://its.cern.ch/jira/browse/O2-3970?focusedId=5753780&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5753780), [comment O2DPG](https://its.cern.ch/jira/browse/O2-3970?focusedId=5754029&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-5754029))

[Build](https://alijenkins.cern.ch/job/Build%20async%20reco%20O2%20for%20CPU+GPU/113/)

| Date of next tag | Requestor | Package | PR | Data or MC | Comment | JIRA (if it exists) | Accepted | In production | Validated by requestor |
| ---------------- | ------------ | ------- | --------------------------------------------------------:|:--------------------------------------------- | ------------------- | ---------------- | ------------- |-------------| ------------------|
| 20.02.2024 | sawenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1379) | MC |  Seed digitizers to TF seeds for reproducible operation |  | | |  |
| 20.02.2024 | sawenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1395) | MC |  Adjust mem estimates for sgnsim and tpcdigi |  | | |  |
| 20.02.2024 | benedikt-voelkel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1416) | MC |  [SimWF] Always set a process for Pythia8 |  | | |  |
| 20.02.2024 | catalinristea | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1340) | MC |  new anchoredMC.sh for nowadays productions |  | | |  |
| 20.02.2024 | njacazio | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1419) | MC |  Update hadronic cross section in injected MC  |  | | |  |
| 20.02.2024 | catalinristea | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1420) | MC |  Update anchorMC.sh - removing the use of ideal MFT/ITS alignments |  | | |  |
| 20.02.2024 | sawenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1432) | MC |  Possibility to take external config for Pythia8 |  | | |  |
| 20.02.2024 | benedikt-voelkel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1437) | MC |  [SimWF] Comments for anchored WF script |  | | |  |
| 20.02.2024 | sawenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1452) | MC |  Anchoring: Ability to get detector list from GRPECS |  | | |  |
| 20.02.2024 | sawenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1406) | MC |  Make TPC reco sensitive to TPCCorrMap param |  | | |  |
| 20.02.2024 | sawenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1412) | MC |  Fix passing some ConfigurableParams to sim_workflow |  | | |  |
| 20.02.2024 | benedikt-voelkel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1441) | MC |   [SimWF] Update reco and sources |  | | |  |
| 20.02.2024 | catalinristea | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1462) | MC |  Update anchorMC.sh - added proc arg |  | | |  |
| 20.02.2024 | benedikt-voelkel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1466) | MC |  Revert "Update anchorMC.sh - added proc arg" |  | | |  |
| 20.02.2024 | sawenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1443) | MC |  Fix type error in pipeline runner |  | | |  |
| 20.02.2024 | sawenzel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1471) | MC |  pipeline_runner: Fix script creation |  | | |  |
| 20.02.2024 | benedikt-voelkel | O2DPG | [PR](https://github.com/AliceO2Group/O2DPG/pull/1463) | MC |  [AnchorMC] Allow for any additional option for sim WF |  | | |  |
| 20.02.2024 | noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12691) | MC | Make hmp-matcher-workflow respect selected sources  |  | | |  |
| 20.02.2024 | noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12677) | MC | Force digitisation when not in GRP  |  | | |  |
| 20.02.2024 | noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12565) | MC | First orbit should be unsigned int  |  | | |  |
| 20.02.2024 | noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12525) | MC | ITSMFT time-evolving dead maps, builder and simulation  |  | | |  |
| 20.02.2024 | noferini | O2 | [PR](https://github.com/AliceO2Group/AliceO2/pull/12644) | MC | ITS MFT Time-evolving dead maps  |  | | |  |

