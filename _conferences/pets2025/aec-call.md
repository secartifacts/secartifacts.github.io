---
title: Call for Artifacts
order: 10
---

## Artifact Submission Guidelines

- All submitted artifacts should be relevant to their corresponding PoPETs
  paper.
- Please upload a copy of your paper.
- Many papers have several artifacts (e.g., multiple source code repositories,
  datasets, build environments), which is great! Please keep in mind that we'll
  need a single link to put on the PETS website and that all artifacts
  associated with your paper should be discoverable from that one link.
- Please include a README.md file with your submission that briefly explains the
  type and purpose of the artifact. At a prominent position in the README.md
  file make clear to which paper the artifact belongs and how the artifact is
  relevant to the paper.
- Please include the [ARTIFACT-EVALUATION.md](/pets2025/ARTIFACT-EVALUATION.md) file in
  your artifact (either include it in the README.md file or add it as a separate
  file.). It is important for the reviewers during the reviewing process.
  Provide a direct link to that file at the submission page.

### Source Code Submissions

- All source code should be accompanied by a README.md or other documentation
  that describes how to build and/or run the code. Reviewers will provide
  feedback on the clarity of the instructions and attempt to follow them and
  build and/or run the code.
- Any source code submissions should be accompanied with a build environment
  such as a virtual machine or a Docker container that has been configured with
  all the dependencies and prerequisites necessary to build the code. If you use
  a virtual machine, please state how many resources it will consume and any
  configuration steps that are required. Your virtual machine should not usually
  have to download additional dependencies when you run your install scripts. If
  that is the case, reassess your build process and consider making changes to
  limit the amount of network resources needed. You can also use one of the VM
  images provided by us, which you can spawn from within HotCRP. In this case
  please provide the name of the used image. Please keep in mind that our VMs
  are only available to the reviewers and you, to ease the process, and they are
  not available to the public. Your artifact, however, should also be runnable
  and helpful for the general public. Hence, your descriptions and scripts
  should be as generic as possible. If your artifact runs on compute providers,
  like AWS or similar, state the amount of money/coins required to run the
  experiments and provide account credentials with enough coins. Our reviewers
  won't invest their money or credit cards to setup accounts. If this cannot be
  provided, provide an alternative way of running your artifact. If this is not
  possible, reconsider your choices of badges (see below).
- If the code is in a compiled language, the code should compile in the provided
  build environment by performing the provided instructions.
- Compilation and setup should be automated as much as possible. Ideally, there
  will be one script that builds your software, runs your tests, and produces
  the results in a comprehensible way.
- Please ensure that your code has a license and clearly states this
  information. The following resources may help you to choose a license:
  - For a clear, easy to follow guide see: [https://choosealicense.com/](https://choosealicense.com/).
  - For more in-depth detail on open source and copy-left licenses, see
    [https://www.gnu.org/licenses/license-list.en.html](https://www.gnu.org/licenses/license-list.en.html) and
    [https://opensource.org/licenses](https://opensource.org/licenses).
- Our goal is that the artifacts are useful for as long as possible. Some tips
  on improving the longevity of your source code artifact are:
  - Include the versions of your software's dependencies wherever possible.
  - Mention specific hashes of git commits that match the state your artifact
    was in at the time of submission.
  - Virtual machines and Docker images will last longer than Docker files and
    allow researchers to more accurately reproduce your exact execution
    environment (though the trade off is that they will be larger).
  - Artifacts are not required to be able to run on all hardwares and OSes. If
    your artifact requires any particular hardware/OS, please make it clear in
    the submission.

### Dataset Submissions

- All datasets should be clearly documented in a way that allows researchers
  working on similar problems to re-use the dataset for their work.
- If the dataset includes survey results, please provide a copy of the original
  survey with raw results. This is vital for replication studies and helping
  researchers interpret the context of your results.
- Please state the sizes of datasets in the documentation.
- It's encouraged to accompany the data with processing scripts that produce the
  graphs or statistical output that appear in the paper.

## Artifact Badges

See [badges](/pets2025/badges).

## What Makes a Good Submission

To ensure a smooth submission process, please follow the following important
guidelines. Firstly, authors should fill out the
[ARTIFACT-EVALUATION.md](/pets2025/ARTIFACT-EVALUATION.md) file provided and
include it in their artifact (either in the README.md file or as a separate
file). Mention the badges you deem reasonable for your artifact and, if
necessary, describe which stages are simplified or skipped and why. This will
help the reviewer better understand your work and ensure a seamless review
process. Secondly, prompt communication is essential. Authors are kindly
requested to respond to reviews and comments within a time span of two weeks.
This will facilitate constructive discussions and allow for timely feedback
incorporation. Lastly, in the event that changes are requested during the review
process, we kindly ask authors to endeavor to incorporate them, at least
partially, within two weeks after the request. Your cooperation in adhering to
these guidelines will greatly contribute to the efficiency and effectiveness of
our submission and review process. We eagerly anticipate receiving your
high-quality contributions and look forward to showcasing your research!

## What Makes a Good Review

The goal of our artifact evaluation is to ensure the artifacts are as useful as
possible. Towards this goal, artifact evaluation process is interactive and we
expect the authors to take into account the reviewers' comments and modify their
artifacts accordingly. As such, the reviews should contain sufficient details
for the authors to make the appropriate changes; for example, if the code fails,
then the review should include the environment that it is run on and the error
messages. After the authors have fixed the issues, they will add a comment on
the submission site, at which point the reviewers can either approve the
artifact or provide additional comments for another rounds of revision.