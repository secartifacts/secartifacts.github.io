---
title: Artifact Evaluation
order: 0
---

A scientific paper consists of a constellation of artifacts that extend beyond the document itself: software, hardware, evaluation data and documentation, raw survey results, mechanized proofs, models, test suites, benchmarks, and so on. In some cases, the quality of these artifacts is as important as that of the document itself, yet many of our conferences offer no formal means to submit and evaluate anything but the paper itself. To address this shortcoming, [WOOT](https://wootconference.org/) organizes an optional artifact evaluation process, inspired by similar efforts in software engineering and security conferences.

## Benefits

We believe the dissemination of artifacts benefits our science and engineering as a whole, as well as the authors submitting them. Their availability improves replicability and reproducibility and enables authors to build on top of each other's work. It can also help more unambiguously resolve questions about cases not considered by the original authors. The authors receive recognition, leading to higher-impact papers, and also benefit themselves from making code reusable.

## Badges

Authors can choose to have their artifact evaluated against the following badges:

* __Open Research Objects (ORO)__: this badge indicates that the artifact is permanently archived in a public repository that assigns a global identifier and guarantees persistence, and is made available via standard open licenses that maximize artifact availability.
* __Research Objects Reviewed (ROR)__: this badge indicates that all relevant artifacts used in the research (including data and code) were reviewed and conformed to the expectations set by the paper.

We expect artifacts to be:
* consistent with the paper
* as complete as possible
* documented well
* easy to reuse, facilitating further research

Notice that the two badges can be issued independently.

## Artifact Details

To avoid excluding some papers, the AEC will try to accept any artifact that authors wish to submit. These can be software, hardware, data sets, survey results, test suites, mechanized proofs, etc. Given the experience in other communities, we decided to not accept paper proofs in the artifact evaluation process. The AEC lacks the time and often the expertise to carefully review paper proofs. Obviously, the better the artifact is packaged, the more likely the AEC can actually work with it during the evaluation process.

While we encourage open research, submission of an artifact does not contain tacit permission to make its content public. All AEC members will be instructed not to publicize any part of your artifact during or after the evaluation, nor retain any part after evaluation. Thus, you are free to include, e.g., models, data files, or proprietary binaries in your artifact. Also, note that participating in the AEC experiment does not require you to publish your artifacts unless you apply for the Open Research Objects (ORO) badge. Still, we strongly encourage you to do so.

We recognize that some artifacts may attempt to perform malicious operations by design. These cases should be boldly and explicitly flagged in detail in the readme so AEC members can take appropriate precautions before installing and running these artifacts. The evaluation of exploits and similar results might lead to additional hurdles where we still need to collect experience on how to handle this best. Please contact the AE chair if you have concerns, for example when evaluating bug-finding tools or other types of artifacts that need special requirements.