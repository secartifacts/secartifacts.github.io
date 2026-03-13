---
title: Submission instructions
order: 30
---

We encourage authors of accepted papers (including Accepted on Shepherd Approval papers) to openly share their research artifacts by submitting them for AE verification before the artifact submission deadline.

Submitting an artifact is _optional_ for an accepted paper. However, during shepherding, reviewers may request access to the artifact to verify the paper's claims. If the artifact is requested but cannot be shared, a detailed justification must be provided and must be validated by the reviewers (i.e., if the reviewers disagree with the justification, the authors have to submit their artifacts, or their paper will be rejected).

Each artifact submission will be reviewed by at least two AEC members. The review is **single-blind** (i.e., no need to anonymize the artifacts, neither for availability verification nor for functionality and reproducibility assessments) and strictly confidential. All AEC members are instructed to treat the artifact confidentially during and after completing the evaluation and not to retain any part of the artifact after evaluation. Artifacts can include models, data files, proprietary binaries, exploits under embargo, etc. If your paper is under embargo during artifact evaluation, please let the AEC chairs know beforehand; you will still need to submit your artifacts for availability verification. Even if authors cannot make their artifacts publicly accessible (e.g., proprietary files), they could still apply for Artifacts Functional and Results Reproduced. Since we anticipate small glitches with installation and use, reviewers may communicate with authors during artifact evaluation to help resolve glitches while preserving reviewer anonymity. Please make sure that at least one of the authors is reachable to answer questions in a timely manner.

### Submission

Authors of accepted papers who wants to participate in artifact evaluation are expected to submit the following via the [artifact submission site](https://vehiclesec26ae.usenix.hotcrp.com/):

 * Title of the accepted paper
 * Abstract of the artifact submission
 * A PDF with the [Artifact Appendix](#artifact-appendix)
 * A PDF of the latest version of the accepted paper
 * Badges requested (available, functional and/or reproduced)

### Artifact Appendix

The artifact appendix is a self-contained document that describes a roadmap for evaluators. This includes a description of the hardware, software, and configuration requirements, as well as the major claims made by the paper and how to reproduce each claim through your artifact. Linking the claims of the paper to the artifact is a necessary step that ultimately allows artifact evaluators to reproduce your results. It is of foremost importance that you state your paper's key results and claims clearly. This is especially important if you think that these claims differ from the expectations set up by your paper. If possible, the appendix should also describe how to compare the results of a reproduced experiment to the ones found in the paper (e.g., by providing access to the underlying dataset of the results).

The intention for the artifact appendix is to be published in conjunction with your paper on the conference proceedings. A template for the artifact appendix can be found here: [LaTeX Template](appendix/usenix-vehiclesec-26-ae-latex.zip) and [PDF Example](appendix/usenix-vehiclesec-26-appendix.pdf).

**It is mandatory that all Artifact Appendix include the following fields:**
 - **Abstract:** a brief summary of the artifact's purpose, its components, and what claims it supports
 - **Description and Requirements**: describes the steps for setting up the evaluation environment and any concerns that might be of interest to the audience. This section should contain:
    - **Security, privacy, and ethical concerns**: outlines any risk or ethical consideration for the evaluators
    - **Access to the artifact**: A DOI or stable reference (e.g., Zenodo, FigShare, or OSF) to the code and the data. _Note: GitHub or personal websites are not accepted for final availability, but are accepted for the artifact evaluation phase (with a specific commit ID)._
    - **Badges**: List of the badges requested by the authors: https://secartifacts.github.io/usenixvehiclesec2026/badges
    - **Hardware dependencies**: Lists CPU, RAM, and GPU requirements (if any)
    - **Software dependencies**: Specifies OS, languages, and required libraries (if any)
    - **Benchmarks**: Lists datasets or test cases used for evaluation (if any)
  - **Set-up**: details installation steps and basic functionality tests to verify the environment
  - **Evaluation workflow**: Details the steps to reproduce the experiments presented in the paper. For each experiment, this section should highlight:
    - **Major claims**: Explicitly lists the scientific claims the artifact intends to prove
    - **Experiments**: Step-by-step instructions for running specific experiments, including estimated human and computing time
  - **Notes of reusability/version**: Contains information on how the artifact can be adapted and references the LaTeX template version used

## Badges for Artifact Appendix document 

The `usenixbadges` LaTeX style file affixes USENIX Artifact Evaluation badges to the front page of a USENIX-formatted paper. You must use it to add badges to your final (camera-ready) paper after AE evaluation, alongisde with the artifact appendix appended at the end. Download the [usenixbadges](appendix/usenix-security-26-badges.zip) package and follow theinstructions below.

#### Installation

Put `usenixbadges.sty` and the `usenixbadges-*.pdf` graphics files in the directory that contains the LaTeX source for your paper.  (Really, you can put them anywhere in LaTeX's search path, but the simplest thing is to put the files in the same directory as your paper's LaTeX source files.)

#### Usage

In the preamble of your LaTeX document, insert a line like this:

```
  \usepackage[<options>]{usenixbadges}
```

In the options, list the badges that have been awarded to your paper. The possible badges are:

  * `available`  --- affix the "Artifacts Available" badge
  * `functional` --- affix the "Artifacts Functional" badge
  * `reproduced` --- affix the "Results Reproduced" badge

Example:

```
  %% Affix the indicated badges to the paper.
  \usepackage[available,functional]{usenixbadges}
```

Tips:

* In your LaTeX document, the `\usepackage[...]{usenixbadges}` directive must come after `\documentclass` and before `\begin{document}`.

* If your LaTeX document has many `\usepackage` directives, put `\usepackage[...]{usenixbadges}` near the end of those.  This may avoid problems relating to conflicting options for the `graphicx` package.

