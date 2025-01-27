---
title: Submission instructions
order: 30
---

Artifact Evaluation (AE) in USENIX Security '25 will be conducted in two phases: (1) a **mandatory AE phase for _artifact availability_** after main paper acceptance and before the final camera-ready papers are due (Phase-1); (2) an **optional AE phase for _functionality and reproducibility_** checks after final papers are due (Phase-2). In both cases, the submitted artifacts will be reviewed by the Artifact Evaluation Committee (AEC). Artifacts should be submitted in the same cycle as the accepted paper. All authors are encouraged to check the separate deadlines for both phases in the [Call for Artifacts](https://www.usenix.org/conference/usenixsecurity25/call-for-artifacts). Having two separate deadlines ensures that authors have additional time to prepare their artifacts for the more advanced and optional ["Artifact Functional" and "Results Reproducible"](badges) badges in Phase-2. Please note that papers that have been "Accepted" after "Shepherd Approval" or after being "Invited for Major Revision" have a slightly later deadline for Phase-1.
Also note that the AE process is *single-blind*, so you do not need to anonymize your submission (neither artifacts nor paper).


For each cycle, a single HotCRP instance will be used to manage the AE for both phases.

**HotCRP links for artifact submission:**

* Cycle-1: [https://sec25cycle1ae.usenix.hotcrp.com](https://sec25cycle1ae.usenix.hotcrp.com/)
* Cycle-2 (link will be made available later)


The following describes what the authors are expected to do prior to each deadline.


## Phase-1: Artifacts Available

**Phase-1 AE is mandatory for all papers that get accepted to USENIX Security '25**. In this phase, the AEC will assess and ensure that the artifacts are in compliance with the ["Artifacts Available"](badge) badge requirements. The authors need to submit a **permanent link to their artifacts** hosted on recommended platforms (e.g., [Zenodo](https://zenodo.org/), [FigShare](https://figshare.com/), [Dryad](https://datadryad.org/stash/), [Software Heritage](https://archive.softwareheritage.org/)). The AEC will ensure that all the artifacts that were promised to be made available in the ["Open-Science" section](https://www.usenix.org/conference/usenixsecurity25/submission-policies-and-instructions#:~:text=of%20the%20paper%2C-,one%20additional%20page,-for%20discussing%20ethics) of the submitted paper were made available publicly and permanently. This evaluation will be completed _before the camera-ready versions of the main paper are due_.

Upon successful completion of the AE -- availability verification, the authors have to include:
- the permanent link to their artifacts repository in the camera-ready version of their paper;
- the "Artifacts Available" badge on the camera-ready version of their paper.



## Phase-2: Artifacts Functional / Results Reproducible

Once the AE process for the mandatory Phase-1 is completed and "Artifacts Available" badge decisions are made, the AE chairs will reopen the HotCRP submission site for Phase-2. **Phase-2 of the AE is optional** and is meant for authors who intend to receive one or both of the following additional badges for their artifacts: ["Artifacts Functional" and "Results Reproducible"](badges). The submission deadline for this phase is _after the camera-ready deadline of the main paper_ to allow the authors some additional time to revise their artifacts for the more stringent requirements of these two badges. However, **we highly recommend that all interested authors start preparing their artifacts for this phase as soon as they receive their paper acceptance notification to allow for sufficient time.**

Most of the duration of this phase involves a single-blinded discussion period between the authors and AEC members. During this, the AEC members will work with the authors to help them improve the quality of their artifacts and make them amenable to the badges that they apply for. The AE timeline was set up to ensure approximately four weeks of time are allotted for this important discussion period. Throughout this period, the authors are expected to be available and improve their artifacts as per the feedback from the AEC. To kickstart this evaluation, _authors can **initially** make the artifacts for this phase available on software development repositories (such as [GitHub](https://github.com/) or [GitLab](https://about.gitlab.com/)) or Internet-accessible hardware owned/leased by the authors, containers/VMs, or any other reasonable format that enables evaluation_. **An important requirement for this phase is the submission of an [artifact-appendix](#artifact-appendix) document in HotCRP**. The HotCRP submission site will feature additional text fields to help in the AEC assignment process (such as the "artifact-access type" for evaluation), which the authors are expected to update prior to the deadline for Phase 2.


After the discussion period, the AEC members will deliberate on the latest state of the artifacts and write reviews explaining their stance on each of the two badges. After this, the badge notifications will be sent, and the final reviews from the AEC will be released to the authors. The authors will then have about a week of time to consider and incorporate any final suggestions from the AEC's reviews to improve the artifacts as well as the artifact appendix. **The final artifact appendix should then be submitted by the authors and include a link to the evolved artifacts. At this stage, the artifacts should be hosted on recommended platforms that support _permanent storage_** (e.g., Zenodo, FigShare, Dryad, etc., but ***not* GitHub, GitLab, or personal websites**). **Compliance with these policies is mandatory for issuing the "Artifacts Functional" / "Results Reproducible" badges.**  We highly recommend the authors use the "version control" features available on all the recommended platforms such as [Zenodo](https://help.zenodo.org/docs/deposit/manage-versions/), [FigShare](https://help.figshare.com/article/can-i-edit-or-delete-my-research-after-it-has-been-made-public), [Dryad](https://blog.datadryad.org/2024/07/09/for-authors-keep-your-data-current-with-dryads-data-versioning-feature/) for this purpose. As Phase-2 begins only after the main camera-ready paper is due, the use of these versioning features allows future readers of the main paper with links to the initial version to still be able to access the final artifacts. At the same time, this website will also be updated to provide direct links to the final versions of artifacts as well as camera-ready versions of the artifact appendices.


### Packaging

Artifacts must be packaged to ease evaluation. All submissions for "Artifacts Functional" and "Results Reproducible" badges must include an [artifact appendix](#artifact-appendix). Packaging is not only about evaluation but about future use of the artifact by other researchers who may want to build on top of it or use it as a baseline. In addition, consider how you plan to distribute your artifact.

If you have any questions about how best to package your artifact, contact [the
AEC chairs](mailto:sec25aec@usenix.org).

**Destructive Artifacts**: Some artifacts may attempt to perform malicious or
destructive operations by design. These cases should be boldly and explicitly
flagged in detail at artifact submission time so that the AEC can take appropriate precautions before installing and running these artifacts. Please check the relevant box in the submission form and contact the AEC chairs if you believe that your artifacts fall into this category.

**Camera-Ready Submission Instructions**: For all artifacts that receive either "Artifacts Functional" or "Results Reproducible" badges, after the artifact evaluation is concluded, we will collect a camera-ready version of the artifact appendix. This includes information about the finalized artifact location, the appendix, and similar supplemental material. The instructions will be shared via email when the badge decisions are announced.

Your artifact package must include an obvious "read me" document containing
suitable instructions and documentation. A tool without a quick tutorial is
generally very difficult to use. Similarly, a dataset is useless without an
explanation of how to browse the data. Please see the [badges](badges) page for
more details on what the instructions should contain.

Authors should consider one of the following methods to package the software
components of their artifacts (although the AEC is open to other reasonable
formats as well):

- *Source code:* If your artifact has few dependencies and can be installed
  easily on several operating systems, you may submit source code and build
  scripts. However, if your artifact has a long list of dependencies, please use
  one of the other formats below.

- *Container/virtual machine:* We recommend using a format that is easy for
  evaluators to work with, such as Docker images. In any case, the Dockerfile or
  script used to initialize the virtual machine should be available. Consider
  preparing the right toolchain and runtime environment.

- *Live instance on the Web:* Ensure that it is available during the artifact
  evaluation process.

- *Internet-accessible hardware:* If your artifact requires special hardware
  (e.g., SGX or another trusted execution environment), or if your artifact is
  actually a piece of hardware; please make sure that evaluators can access the
  device. VPN/SSH-based access to the device might be an option (in that case,
  please provide the SSH private access key directly in your submission to
  reduce time to gain access to hardware).
  Use the "Artifact access type" item on the submission form to indicate whether you will make compute resources available.


### Artifact Storage

Great artifacts are easy to find and stored for a long time. **The new "Open-Science policy" of USENIX Security mandates the sharing of final artifacts on a platform that supports permanent access.** For this purpose, we recommend [Zenodo](https://zenodo.org/). Other valid hosting options include institutional and third-party digital repositories (e.g., [FigShare](https://figshare.com/), [Dryad](https://datadryad.org/stash/), [Software Heritage](https://archive.softwareheritage.org/)). Since the artifacts can potentially evolve during the evaluation to address feedback from the reviewers, one stable reference can be collected for artifact submission and another (potentially different) one for the final version of the artifact. We intend to utilize the versioning features supported by the above platforms for this purpose.


### Artifact Appendix

The artifact appendix is a self-contained document that describes a roadmap for
evaluators. This includes a description of the hardware, software, and
configuration requirements, as well as the major claims made by the paper and
how to reproduce each claim through your artifact. Linking the claims of the
paper to the artifact is a necessary step that ultimately allows artifact
evaluators to reproduce your results. It is of foremost importance that you
state your paper's key results and claims clearly. This is especially important
if you think that these claims differ from the expectations set up by your
paper. If possible, the appendix should also describe how to compare the results
of a reproduced experiment to the ones found in the paper (e.g., by providing
access to the underlying dataset of the results).

The intention for the artifact appendix is to be published in conjunction with your artifact. A template for the artifact appendix and additional instructions for formatting it will be made available here later.

**Artifact Appendices are recommended to be at most 3 pages.**
