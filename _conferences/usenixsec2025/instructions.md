---
title: Submission instructions
order: 30
---

Artifacts must be packaged to ease evaluation. All submissions for "Artifacts Functional" and "Results Reproducbile" badges must include an [artifact
appendix](#artifact-appendix). Packaging is not only about evaluation but about
future use of the artifact by other researchers who may want to build on top of
it or use it as a baseline. In addition, consider how you plan to distribute
your artifact.

If you have any questions about how best to package your artifact, contact [the
AEC chairs](mailto:sec25aec@usenix.org).

*Destructive Artifacts*: Some artifacts may attempt to perform malicious or
destructive operations by design. These cases should be boldly and explicitly
flagged in detail at artifact submission time so the AEC can take appropriate
precautions before installing and running these artifacts. Please check the
relevant box in the submission form, and contact the
AEC chairs if you believe that your artifacts fall into this category.

*Camera-Ready Submission Instructions*: After the artifact evaluation is concluded,
we will collect a camera-ready version of the artifact appendix for all artifacts receiving at least one
of the follwing badges: "Artifacts Functional" and "Results Reproducbile". This includes information about the artifact location, the appendix,
and similar supplemental material. The instructions will be shared via email
when the badge decisions are announced.

## Packaging

Your artifact package must include an obvious "read me" document containing
suitable instructions and documentation. A tool without a quick tutorial is
generally very difficult to use. Similarly, a dataset is useless without some
explanation on how to browse the data. Please see the [badges](badges) page for
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

- *Live instance on the web:* Ensure that it is available during the artifact
  evaluation process.

- *Internet-accessible hardware:* If your artifact requires special hardware
  (e.g., SGX or another trusted execution environment), or if your artifact is
  actually a piece of hardware, please make sure that evaluators can access the
  device. VPN/SSH-based access to the device might be an option (in that case,
  please provide the SSH private access key directly in your submission to
  reduce time to gain access to hardware).
  Use the "Artifact access type" item on the submission form to indicate whether you will make compute resources available.

## Artifact Storage

Great artifacts are easy to find and stored for a long time. The new Open Science policy of USENIX Security mandates sharing of artifacts on a platform that supports permanent access. For this purpose, we recommend
[Zenodo](https://zenodo.org/). Other valid hosting options include institutional and third-party
digital repositories (e.g., [FigShare](https://figshare.com/), [Dryad](https://datadryad.org/stash/),
[Software Heritage](https://archive.softwareheritage.org/). During artifact submission time, the authors are expected to submit stable references to hosted on such platforms. Please note that artifacts hosted on personal websites or software development repositories such as GitHub are not acceptable for submission.  Since the artifact can potentially evolve during
the evaluation to address feedback from the reviewers, another (potentially
different) stable reference will be later collected for the final version of the
artifact. We intend to utilize the versioning features supported by the above platforms for this purpose. 

## Artifact Appendix

The artifact appendix is a self-contained document which describes a roadmap for
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

The intention for the artifact appendix is to be published in conjunction with
your artifact. A template for the artifact appendix and additional instructions for formatting it will be made available later.

**Artifact Appendices are recommended to be at most 3 pages.**
