---
title: Badges
order: 20
custom_css: pets-badges
---

Each accepted artifact can be granted up to three badges. During the submission,
the authors must select which badges they want their artifacts to be evaluated
against. We encourage the authors to choose the badges appropriately, to ease
the reviewing effort. Our understanding of the individual badges is aligned with
other conferences, e.g., [USENIX Security
Symposium](https://secartifacts.github.io/usenixsec2023/badges)

## Artifact Available <a class="pets-artifact-badge">Artifact: Available</a>

The "Artifact Available" badge indicates that the artifact is publicly available
at a permanent location (not be behind any kind of paywall or restricted
access). If the artifact requires you as an author to manually approve requests
for access, it is not public and will not qualify for the "Artifact Available"
badge. If you have concerns or questions about this badge please contact us
directly. Valid hosting options are institutional and third-party digital
repositories. Please do not use personal web pages. The link should be
persistent; for repositories that evolve over time (e.g., Git repositories),
please specify a specific commit-id or tag to be evaluated. The reviewers check
that the artifact can be retrieved, and that it includes a license. The
reviewers check that the artifact is relevant to the paper. This badge does
*not* mean that the reviewers have reproduced the results or checked that the
code executes or that they have reproduced the results for full functionality.

## Artifact Functional <a class="pets-artifact-badge">Artifact: Functional</a>

For the "Artifact Functional" badge the artifact should satisfy these criteria:

- Documentation: It clearly documents how it relates to the paper, and how it
  should be used.
- Completeness: It includes all the core contributions described in the paper.
- Exercisability: It includes the scripts and data needed to run the experiments
  described in the paper. The software must be successfully executable?

Some artifacts may not, by definition, be able to satisfy the completeness or
exercisability criteria. For instance, an artifact may have a proprietary
machine learning model as a key component of the system, and so, achieving
completeness may be difficult. Artifacts may rely on datasets that are too large
to be included, or contain personally identifiable information, and so,
satisfying exercisability is difficult. We guide authors below, using some
examples, on how they can still prepare their artifact to achieve this badge.
Additionally, some artifacts, such as longitudinal studies or hardware-based
contributions, may be infeasible for the Artifact Reproduced badge (see below),
as reviewers have limited time and only commodity hardware available.
Nevertheless, these authors can prepare their artifacts for the Artifact
Functional badge, as described in the examples: Examples

Consider the experiments in your artifact as arranged in a pipeline of multiple
stages, such as data collection, data processing, and producing plots or tables
for the paper. The “Completeness” and “Exercisability” criteria require each
stage to be represented. Our key advice is to present each stage, including the
ones that cannot be fully run. These can be represented in either a simplified
manner or run on dummy data to check the functionality of the stage. If
possible, provide the expected outcome of the fully run stage such that
preceeding stages are performed on 'real' data again. In the following we
present some examples:

- **Tools based on large machine learning (ML) models.** If an ML model is required
  to execute the presented tool, the authors should provide it, unless it is
  proprietary. Authors may use `git-lfs` to commit large model files to their
  repository. If they can not share the model, we expect them to share a dummy
  model, which may perhaps perform worse, but which can be used to test the
  principle functionality of the presented tool. Ideally, authors should provide
  the code to train the original model, though depending on the contributions of
  the paper, it need not be executed.
- **Lengthy experiment runtimes.** Similar to the point above, even if the
  experiment requires days or weeks of compute time on commodity hardware, the
  "Artifact Functional" badge can be achieved. In such cases the authors should
  also provide a simplified version of the experiment, which may run on less
  training data or for fewer epochs of time, in order to enable the reviewers to
  check the functionality of that stage. Authors should additionally provide
  results of the full experiments in the repository, so that reviewers can
  verify the functionality of the later stages with these results.
- **User studies, longitudinal studies and crawls.** Some studies cannot be repeated
  within the reviewing process. However, the authors should provide the
  evaluation scripts to reproduce the main results of the paper. Pseudonymized
  raw data should also be provided, unless forbidden by legal requirements,
  privacy, or ethical concerns. In such cases, a data set with dummy data should
  be included. Reviewers should be able to execute the evaluation scripts on
  either the pseudonymized raw data or dummy data.
- **Hardware-based contributions.** If the artifact requires certain hardware,
  please request for it within the "hardware requirement" section in the
  [ARTIFACT-EVALUATION.md](/pets2025/ARTIFACT-EVALUATION.md) template. If
  special physical setups are required, the authors may simulate the hardware.
  Authors should publish the raw results of the experiments, so that reviewers
  can verify the remaining stages as functional.

## Artifact Reproduced <a class="pets-artifact-badge">Artifact: Reproduced</a>

The "Artifact Reproduced" badge requires the core contributions of the paper to
be reproduced by the reviewers. Authors must specify the commands to run the
artifacts clearly and describe how to reproduce each core finding of the paper.
Best practice is to point out which part of the paper is reproduced by a given
script, e.g., name the table or figure. Also, the authors must highlight which
results of the paper are not reproducible with the given artifacts and argue
why. Note that minor additional experiments that do not significantly contribute
to the paper may not be included in the artifact.
