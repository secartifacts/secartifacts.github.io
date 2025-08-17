---
title: Badges
order: 20
custom_css: pets-badges
---

Each accepted artifact can be granted up to three badges. During submission,
authors must select which badges they want their artifacts to be evaluated
against. As we detail below, in general, all submitted artifact should apply at
least for "Artifact Available" badge, unless doing so would endanger someone. To
ease reviewing effort, we encourage authors to apply appropriately to all the
badges for which they believe requirements are met by their artifact. Our
interpretation of the individual badges is aligned with the one of [other
conferences](https://secartifacts.github.io/). If you have questions about which
badges to apply for, first go through the FAQ below and then please contact the
artifact evaluation chairs directly.

## Artifact Available <a class="pets-artifact-badge">Artifact: Available</a>

For the "Artifact Available" badge, the reviewers check that the artifact is
publicly accessible, has a license and is relevant to the paper.

Your artifact should be publicly accessible at a permanent location; it should
_not_ be behind any kind of paywall or restricted access or private repository.
If the artifact requires you as an author to manually approve requests for
access, it is not public and will not qualify for the "Artifact Available"
badge. Note that all components of your artifact should be publicly available
(e.g. source code, datasets, etc.).

Valid hosting options are institutional and third-party digital repositories
(e.g., GitHub, Gitlab, BitBucket, Zenodo, Figshare, etc.). Do _not_ use personal
web pages or cloud storage services like Google Drive, Dropbox, etc.

**All submitted artifacts should apply at least for "Artifact Available"**,
unless for some specific unusual situations when doing so could endanger
someone. For instance, if the artifact demonstrates exploiting a vulnerability
and the possible harms from releasing a proof of concept would outweigh the
benefits of making it available as part of a responsible disclosure process. In
this case, authors could apply for just the "Functional and Reproduced Badges".
If you wish to commercialize your project, you can and should still submit your
artifact for this badge, under restricted licensing, as discussed in the FAQ
below.

The FAQ also provides resources on licensing, dealing with large files, and
linking to multiple repositories.

### Checklist for "Available Badge":

- [ ] Publicly available artifact with a single link.
- [ ] Presence of a license.
- [ ] Relevance to paper.
- [ ] Corresponding content from `ARTIFACT-APPENDIX.md` completed.

This badge does _not_ mean that the reviewers have checked that the code
executes or that they have reproduced the results of the paper.


## Artifact Functional <a class="pets-artifact-badge">Artifact: Functional</a>


To be awarded the "Artifact Functional" badge the artifact should satisfy these
criteria:

- Documentation: The artifact clearly documents how it should be used (i.e.,
  installation + execution).
- Completeness: It includes all key components described in the paper.
- Exercisability: It includes the scripts and data needed to run the experiments
  described in the paper. The software must successfully execute in the provided
  environment.

**Documentation:** The `ARTIFACT-APPENDIX.md` file within all source code
artifacts should describe how to build and/or run the code. Reviewers will
provide feedback on the clarity of the instructions and attempt to follow them
and build and run the code.

**Completeness:** Consider the experiments in your artifact as arranged in a
pipeline of multiple stages, such as data collection, data processing, and
producing plots or tables for the paper. The "Completeness" criteria requires
each stage to be represented. For instance, an artifact may have a proprietary
machine learning model as a key component of the system, and so, achieving
completeness may be difficult. If you are unable to represent any stage, then
represent it in either a simplified manner or run it on dummy data, in order for
reviewers to check the functionality of the stage. Provide the expected outcome
of the fully run stage such that preceding stages are performed on 'real' data.
Under the FAQ, we have examples on how authors can still prepare their artifact
for the "Artifact Functional" badge in cases that involve licensing issues,
time, or resource constraints.

**Exercisability:** All source code should be accompanied by a build environment
such as a Dockerfile or a virtual machine (VM) install script, with all the
dependencies (software _and_ datasets) necessary to build the code. Include and
pin the versions of your software dependencies. If the code is in a compiled
language, the code should compile in the provided build environment by running
the provided instructions. Compilation and setup should be automated as much as
possible. Ideally, there will be one script that builds your software, runs your
tests, and produces the results in a comprehensible way.

To receive this badge, artifacts are _not_ required to be able to run on all
hardware and OSes.

### Checklist for "Functional Badge":

- [ ] Meets "Available Badge" requirements (except for unusual situations
  discussed previously).
- [ ] Clear documentation is provided.
- [ ] Completeness criterion fulfilled (with potential limitations reasonably
      argued).
- [ ] Exercisability criterion fulfilled (with potential limitations reasonably
      argued).
- [ ] Corresponding content from `ARTIFACT-APPENDIX.md` completed.

## Artifact Reproduced <a class="pets-artifact-badge">Artifact: Reproduced</a>


The "Artifact Reproduced" badge requires the main claims of the paper to be
reproduced by the reviewers. Implicitly, an artifact awarded the "Artifact
Reproduced" badge needs to also meet the requirements of the "Artifact
Functional" badge.

Authors must specify the commands to run the artifacts clearly and describe how
to reproduce each main claim of the paper. Best practice is to point out which
part of the paper is reproduced by a given script, e.g., name the table or
figure. Also, the authors must highlight which results of the paper are not
reproducible with the given artifact and explain why. Authors are encouraged to
contemplate how their artifact could be re-used by others in the future and
describe potential ways for improvement, etc.

Authors are asked to automate as much of the execution of the experiments as
possible; manual effort from reviewers to run and interpret the results should
be minimized. For instance, if an experiment is performing a swap across
different parameters, a script automating it should be provided. Ideally,
results should also be automatically parsed and output in a comprehensible way,
as close to the output in the paper as possible (table or figure, etc.).

To award the "Artifact Reproduced" badge, reviewers must be able to reproduce
the main claims of the paper with the provided artifact. As a rule of thumb, a
quantitative claim should generally be considered reproducible if the results
obtained by reviewers are within 5% of the reported value in the paper. That
being said, some artifact-specific factors may prevent this; in these cases,
artifact reviewers should also consider if the results that they obtain align
qualitatively with the claims made in the paper. It is the reviewer's role to
enforce that these quantitative and/or qualitative expectations are met before
awarding the "Artifact Reproduced" badge.

Additionally, some experiments may by nature be harder to fully reproduced
during the timeframe of the artifact evaluation: e.g., take a while to run, need
several iterations, train a model on a large dataset, etc. In these cases,
authors should still provide the instructions and expected results for the
"long" version of the experiment, and also for a simplified one (e.g., fewer
iterations, smaller dataset, etc.). Indeed, even on a simplified version or
fewer runs, reviewers should still somewhat be able to look at the results and
the standard deviation, and check that results from the paper can be reproduced.

Finally, some artifacts, such as longitudinal studies or hardware-based
contributions, may be infeasible for the “Artifact Reproduced” badge (see FAQ
below), as reviewers have limited time and only commodity hardware available.
Nevertheless, these authors can and should still prepare their artifacts for the
“Artifact Functional” badge.

### Checklist for "Reproduced Badge":

- [ ] Meets "Functional Badge" requirements.
- [ ] List of the core contributions and claims of the paper identified.
- [ ] Clear mapping between claims, experiments, and results provided.
- [ ] Minimal amount of manual effort required from reviewers, i.e., fair amount
      of automation.
- [ ] Reviewers obtain reproducible results quantitatively (i.e., within 5% of
      the claimed value) and/or qualitatively.
- [ ] Corresponding content from `ARTIFACT-APPENDIX.md` completed.