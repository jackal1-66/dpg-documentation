# Release Validation

The **ReleaseValidation** (RelVal) tool chain is used to validate the QC, AOD or Analysis output. Such validations are in the end comparisons of corresponding output that, for instance, come from using 2 different software versions, 2 different machine architectures, 2 different configurations etc.

The documentation is [here](https://aliceo2group.github.io/simulation/docs/relval/).

While everyone can run that, there are also official RelVal runs managed by the DPD and QC groups. They are steered to validate software changes or to test new features.

## Official RelVal

### Contacts (technical)

* Benedikt Volkel (benedikt.volkel@cern.ch),
* Zhenjun Xiong (zhenjun.xiong@cern.ch).

### Contacts (run)

* Zhenjun Xiong (zhenjun.xiong@cern.ch).

### Detector QC experts

The detector experts can be reached via dedicated e-groups `alice-dpg-async-qc-<det>`. To reach all experts at the same time, there is also [`alice-dpg-async-qc-det`](https://e-groups.cern.ch/e-groups/Egroup.do?egroupId=10608331).

### RelVal

At least one pair of QC files as well as one pair of AO2Ds must be compared.

In addition to the comparison, the results should be accompanied by a brief README.

The easiest at the moment is to pack an archive, upload it to CERNBox and share it with experts (see also [below](#jira)).

### JIRA

All official RelVal runs will be discussed in a dedicated JIRA ticket. The preparation of the ticket, running the RelVal as well as the follow-up is the responsibility of the [RelVal experts](#contacts-run).
The JIRA ticket shall have the components:

* O2DPG,
* Reconstruction,
* QC,
* Analysis.

The following steps need to be taken care of by the [RelVal experts](#contacts-run).

1. Run the validation.
1. A first overview shall be provided by the experts, such as
    * apparent anomalies,
    * detectors with only BAD or NON_COMPARABLE flags,
    * etc.
1. Provide a link to the results; easiest at the moment is to pack an archive, upload it to CERNBox and link it in the ticket.
1. Add the `alice-dpg-async-qc-det` to the watch list.
1. Start the discussion with the detector groups.
    * Ping specific detector groups if they are not responsive.

!!! example "JIRA template"

    A template for the initial description of the ticket:

    RelVal output on **LINK TO CERNBOX**.
    A README with what was compared is contained in the archive.

    **Compared QC files**

    1. dev: `<path/to/alien/QC.root>`,
    1. apass4: `<path/to/alien/QC.root>`

    **Compared AODs**

    1. dev: `<path/to/alien/AO2D.root>`,
    1. apass4: `<path/to/alien/AO2D.root>`

    **SW tags and descriptions**

    - dev: O2PDPSuite::daily-20240329-0100-1 (and specific versions of most important packages):
        - VO_ALICE@O2::daily-20240329-0100-1
        - VO_ALICE@O2DPG::daily-20240329-0100-1
        - VO_ALICE@O2Physics::daily-20240329-0100-1
        - VO_ALICE@QualityControl::daily-20240329-0100-1
    - apass4: O2PDPSuite::async-async-20240229.2a-slc7-alidist-O2PDPSuite-daily-20231208-0100-1, jq::v1.6-3  (and specific versions of most important packages):
        - VO_ALICE@O2::async-20240229.2a-1
        - VO_ALICE@O2DPG::async-20240229.2-1
        - VO_ALICE@O2Physics::async-20240207.1-10
        - VO_ALICE@QualityControl::v1.126.5-10

    To find the versions of specific software for each tag, please go to https://alimonitor.cern.ch/packages/ and search for the tag. There is also a link to "Full dependencies" which will show all versions of all software packages.

    **Detector list**

    Boxes to be ticked by detector experts if there are no issues.

    - [ ] ITS
    - [ ] MFT
    - [ ] TPC
    - [ ] TOF
    - [ ] FT0
    - [ ] MID
    - [ ] EMC
    - [ ] PHS
    - [ ] CPV
    - [ ] FDD
    - [ ] HMP
    - [ ] FV0
    - [ ] TRD
    - [ ] MCH
    - [ ] GLO

{% include list.liquid all=true %}
