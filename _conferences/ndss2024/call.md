---
title: Call for Artifacts
order: 20
---

Before submitting your artifact, please check the information and submission guidelines below.

## Important Dates

*All AE-related deadlines are Anywhere on Earth (AoE).*

### Summer Deadline
* Paper notification to authors: Wed, 21 Jun 2023
* Artifact registration deadline: Wed, 28 Jun 2023
* Artifact submission deadline: Wed, 5 Jul 2023
* Kick-the-tires stage (answering AEC reviewer questions): Thu, 6 Jul to Fri, 14 Jul 2023
* Artifact decisions: Tue, 5 Sep 2023
* Camera-ready deadline for papers: Fri, 8 Sep 2023

Submission page: [https://ndss24ae-summer.hotcrp.com/](https://ndss24ae-summer.hotcrp.com/)

### Fall Deadline
* Paper notification to authors: Wed, 13 Sep 2023
* Artifact registration deadline: Wed, 20 Sep 2023
* Artifact submission deadline: Wed, 27 Sep 2023
* Kick-the-tires stage (answering AEC reviewer questions): Thu, 28 Sep to Fri, 6 Oct 2023
* Artifact decisions: Fri, 24 Nov 2023
* Camera-ready deadline for papers: Wed, 29 Nov 2023

Submission page: [https://ndss24ae-fall.hotcrp.com/](https://ndss24ae-fall.hotcrp.com/)

## Evaluation process

Authors are invited to submit artifacts soon after receiving the paper notification. At least one contact author must be reachable and respond to questions in a timely manner during the entire evaluation period to allow round trip communications between the AEC and the authors. Artifacts can be submitted only in the AE time frame associated with the paper submission round.

In addition to accepted papers, papers that receive a major or minor revision decision are eligible for AE: at artifact submission time, their authors should justify the necessary changes that they intend to carry out on the initially submitted paper and how such changes relate to the submitted artifact. 

At submission time, authors choose which [*badges*](badges) they want to be evaluated for. Members of the AEC will evaluate each artifact using the artifact appendix and instructions as guides, as detailed later in this page. Evaluators will communicate anonymously with authors through HotCRP to resolve minor issues and ask clarifying questions.

Evaluation starts with a *kick-the-tires* period during which evaluators ensure they can access their assigned artifacts and perform basic operations such as building and running a minimal working example. Artifact evaluations include feedback about the artifact, giving authors the option to address any significant blocking issues for AE work using this feedback. Communication after the kick-the-tires stage end can address interpretation concerns for the produced results or minor syntactic issues in the submitted materials.

For prospective authors: The target should be to present and document your artifact in a way that AEC members can use it and complete the evaluation successfully with minimal (and ideally no) interaction. To ensure that your instructions are complete, we suggest that you run through them on a fresh setup prior to submission, following exactly the instructions you have provided.

## Artifact details and requirements

Artifacts can be, e.g., software, datasets, models, test suites, or mechanized proofs. Paper proofs are not accepted, as evaluators lack the time and often the expertise to carefully review them. Physical objects, such as specialized computer hardware, are also not accepted, due to the difficulty of making them available to evaluators.

To ensure that the evaluation is practical for the AEC, the proposed experiments should take at most *1 day* and run on a *commodity desktop machine*. When the paper's research involves longer durations, the authors should design scaled-down experiments and properly justify how those can still significantly support the paper's analyses. A commodity desktop machine is defined as one with an x86-64 CPU with 8 cores and 16 GB of RAM running a recent Linux or Windows operating system and software obtainable free of charge. If this requirement cannot be met, the authors should make arrangements to provide (e.g., via SSH to their own infrastructure, or renting it from providers) anonymous access to the AEC. Hardware and software requirements must be stated when registering an artifact. If you intend to provide access to special hardware, you must reach out to the AE chair before the submission.

Artifact evaluation is single-blind. Each AEC member will independently test and review their assigned submissions. To maintain the anonymity of evaluators, artifact authors should not embed analytics or other tracking tools in any websites for their artifacts for the duration of the AE period. In cases where tracking is unavoidable, authors must notify the AE chair in advance so that AEC members can take adequate safeguards.

Submitting an artifact for evaluation does not give the AEC permission to make its contents public or to retain any part of it after evaluation. Thus, authors are free to include proprietary models, data files, or code in artifacts. Participating in the AE process does not require the public release of artifacts, though it is highly encouraged.

## Artifact preparation

Artifacts must be packaged to ease evaluation and use, including instructions for the evaluators and an artifact appendix to complement the paper. Packaging is not only about evaluation, but also about future use of the artifact by other researchers who may want to build on top of it or use it as a baseline.

Some artifacts may attempt to perform malicious or destructive operations by design. Such cases should be explicitly flagged in detail at submission time so that the AEC can take appropriate precautions before installing and running these artifacts.

### Instructions
An artifact package must include an _exhaustive_ "README" document containing adequate instructions and other documentation to present and explain the nature and functionality of the artifact and, if applicable, to conduct the required experiments for result reproduction.

When allowed by the characteristics of the artifact, authors are encouraged to provide a minimal working example. During the kick-the-tires stage, artifact evaluators will use it for preliminary functionality testing: doing so may anticipate issues that would otherwise only appear after a complete artifact evaluation attempt is conducted.

Along with badge descriptions, evaluator guides from AE efforts in related security and systems conferences can be very helpful for the authors to set their expectations on how well-prepared artifact instructions should look like. Several such resources are provided at the end of this page.

### Artifact appendix
The artifact appendix must be a self-contained document that describes a roadmap for evaluators. Alongside the description of the hardware, software, and other configuration requirements, the artifact appendix should enumerate the list of major **claims** made by the paper that can be reproduced through the artifact. The artifact appendix will be published in conjunction with the paper.

A template for the artifact appendix can be found here: [LaTeX Template](ndss_ae_appendix_template_v1.tex) (to be used in conjuction with the NDSS'24 template for research papers). Artifact appendices are limited in length to **2 pages**; contact the AE chair before submission to discuss well-motivated exceptions.

Linking the paper's claims to the artifact is a necessary step that allows artifact evaluators to reproduce results. Authors must state their paper's key results and claims clearly. Also, claims should be concrete, especially if these claims may differ from the expectations set by the paper. The AEC will still evaluate artifacts relatively to their paper, but an explanation can help setting expectations up front, especially in cases that might frustrate the evaluators without prior notice. For example, authors are encouraged to be transparent with the AEC about difficulties that evaluators might encounter in using the artifact or its maturity relative to the paper's content.

## Artifact packaging

Authors should consider one of the following methods to package the software components of their artifacts. Then, a link to access the package should be provided on the HotCRP submission form.

* Source code: When an artifact has few dependencies and can be installed easily on standard operating systems, authors may submit source code and build scripts. However, if an artifact has a long list of dependencies, please use one of the other formats below.

* Container/virtual machine: We recommend using a format that is easy for evaluators to work with, such as Docker images or an OVF virtual machine (e.g., to run it in VirtualBox). In any case, the Dockerfile or script used to initialize the virtual machine should be made available. A Docker image or virtual machine should already be set up with the right toolchain and runtime environment for the artifact.

* Live instance on the web: Authors must ensure it is available during the entire AE process.

* Internet-accessible hardware: If an artifact requires special hardware (e.g., SGX) or is actually a piece of hardware, the evaluators must be able to access the device. SSH-based access to the device might be an option.

Authors should reach out to the AE chair when other formats look more reasonable in their judgment.

## Resources
The following materials may be useful when preparing an artifact:
- [HOWTO for AEC Submitters](https://docs.google.com/document/d/1pqzPtLVIvwLwJsZwCb2r7yzWMaifudHe1Xvn42T4CcA/edit), by Dan Barowy, Charlie Curtsinger, Emma Tosch, John Vilk, and Emery Berger
- [Artifact Evaluation: Tips for Authors](https://blog.padhye.org/Artifact-Evaluation-Tips-for-Authors/), by Rohan Padhye
- [Evaluator Guide](https://sysartifacts.github.io/eurosys2022/guide), by the AE chairs of EuroSys '22
- [How Are Award-winning Systems Research Artifacts Prepared (Part 1)](https://www.sigops.org/2021/how-are-award-winning-systems-research-artifacts-prepared-part-1/), by Tianyin Xu
- [Systems Research Artifacts](https://sysartifacts.github.io/), a website collecting AE results for systems conferences

## Acknowledgements
The AE process at NDSS 2024 was inspired by similar endeavors in other systems and security conferences. This call for artifacts builds on materials from the AE process of EuroSys '23 and USENIX Security '23.
