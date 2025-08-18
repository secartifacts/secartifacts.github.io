---
title: Frequently Asked Questions (FAQ)
order: 25
---

## I want to commercialize my artifact. Should I still apply for any badges?

IP protections and commercialization prospects should not inhibit authors from
applying for the "Artifact Available" badge. For instance, authors can choose
restrictive licenses that prohibit others from using their code. Alternately,
authors can design a smaller working prototype to demonstrate reproducibility of
the contributions of their paper.

## Which license should I choose for my artifact?

- For a clear, easy to follow guide see: [https://choosealicense.com/](https://choosealicense.com/)
- For more in-depth detail on open source and copy-left licenses, see
  [https://www.gnu.org/licenses/license-list.en.html]() and
  [https://opensource.org/licenses](https://opensource.org/licenses).
- Before you begin extending other authors' libraries, check that doing so would
  comply with the terms of the license.

## I need to upload a file that is larger than 100MB, but [GitHub does not allow that](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github#about-size-limits-on-github). How can I make my file available?

- If your file is at most 2GB, GitHub recommends
  [using Git LFS](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage).
- If your file is at most 50GB, then you should consider [hosting it as a record
  on
  Zenodo](https://support.zenodo.org/help/en-gb/1-upload-deposit/80-what-are-the-size-limitations-of-zenodo)
  for example. Artifacts have also used
  [Huggingface](https://huggingface.co/docs/hub/en/storage-limits) successfully
  to host large ML models.
- If directly uploading your (compressed) file to one of the aforementioned
  platforms does _not_ work, then you may split the file into multiple chunks.
  You can also contact the artifact chairs if you have trouble with this step.
- Do _not_ use Google Drive or Dropbox links; they are not version-controlled or
  persistent in any way.

## My paper has several artifacts, such as one source code repository and few datasets, or multiple source code repositories for different purposes. What link should I use and submit?

We will need a single link to put on the PETS website and all artifacts
associated with your paper should be discoverable from that one link.

- If you have several Git repositories, we suggest using
  [git submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules).
  Reference specific hashes of Git commits when using Git submodules.
- If you are using Zenodo (or similar service) to host your datasets and a Git
  repository for your code, ensure that your `README.md` in your Git repository
  includes a link to the Zenodo record, and you may submit the link to your Git
  repository for artifact evaluation.

## I have a user study. How can I get the "Artifact Available" badge?

An example of a
[good user study artifact](https://github.com/blues-lab/priv-eng-dataset/tree/ca35ffbb3c38ff7877c01ee92bfda29b2033ae6e)
is available here. Authors of papers with user studies can generally achieve the
"Artifact Available" badge, by including the following in their artifact:

- User study questionnaire.
- If participants were informed of, and consented to, _anonymized_ transcript or
  responses being released, explicitly mention this, and release these
  transcripts or questionnaire responses.
- We also recommend including demographics of your user study participants.

## I am designing a course or a game to teach privacy. How can I get the "Artifact Available" badge?

Here are examples of artifacts regarding
[an undergraduate course](https://github.com/MaishaB/undergraduate-privacy-curriculum/tree/0a7f27a8b4220298040323fb100daa658583717b)
and a
[game](https://github.com/DataSmithLab/Panopticon/tree/236b792058b2cc65a43c55b624bb4649b4bbd328)
to teach privacy.

For courses, thoroughly document the course structure, including the number of
lessons or modules, lesson titles, number and types of assessments. You should
also consider including:

  Written and programming exercises.
- Tutorials
- Assessments, including quizzes or exams.

For games, document the game mechanics, game materials, setup instructions as
well as per-round instructions. You may include videos to supplement, but not
replace, your documentation.

While in general we expect both game and course-related artifacts to be awarded
the "Artifact Available" badge, the aforementioned artifact included programming
exercises that could be fully exercised by the reviewers and was thus awarded
the "Artifact Functional" badge.

## I don't have time to write a Dockerfile to build my project. Do you have examples? Should I upload a Dockerfile or a Docker image or both?

Authors are encouraged to check out the [repository
examples](https://github.com/PoPETS-AEC/examples-and-other-resources) that have
been put together by the artifact evaluation chairs.

These examples are in the form of GitHub repositories that include:

- Dockerfiles for popular programming workflows, including Python-based
  projects.
- GitHub Action workflows to _automatically_ generate a Docker image based on
  the Dockerfile. Whenever the Dockerfile is changed, a new Docker image will be
  released. That way, authors can focus on writing and releasing their
  Dockerfile while reviewers can directly download the Docker image from the
  "GitHub Container Registry" (or another registry like DockerHub if authors
  follow resources we point to).

Authors can fork these repositories, and use the fork as a starting point for
their artifact. For example, for Python-based projects, authors should modify
the `Dockerfile` and add the pinned versions of their dependencies to a
`requirements.txt` (or similar) file.

Note that these resources are not comprehensive, so authors and reviewers are
not to interpret them as the only way to package an artifact; we also welcome
suggestions to these resources in the form of issues, pull requests, or direct
contributions.

## Should I go for VMs or Docker?

For most artifacts, we have found that a Dockerfile suffices. As in our response
to the question above, please check our [repository
examples](https://github.com/PoPETS-AEC/examples-and-other-resources) on GitHub.
If you use Docker:

- Always include the Dockerfile and other scripts used to build the Docker image
  in your artifact.
- Pin versions of dependencies as much as possible to avoid future breaking
  changes (e.g., specify a specific hash rather than a loose `latest` tag for
  the base image, same for dependencies versions).
- Note that if you do the above points, you do _not_ need to include both a
Dockerfile and a Docker image; we strongly prefer using a Dockerfile with pinned
versions.
- Finally, our example GitHub repository automatically generates a Docker image
from our (example) Dockerfile and publishes it as a "GitHub release", so you do
not need to worry about building and hosting the Docker image.

VMs could be a better fit for artifacts that require multiple nodes
communicating with each other (you could also explore [Docker
Compose](https://docs.docker.com/compose/) if that fits your use case). If you
include a VM:

- State the parameters used to create the VM, including the CPU architecture,
  number of expected CPU cores, the amount of RAM to be given, maximum size of
  the disk image that the VM was created with, BIOS/UEFI configuration. You
  should also list any external virtualized hardware that needs to be
  virtualized.
- Include the scripts or files required to build the VM image.
- Your VM should not usually have to download additional dependencies after you
  run your installation scripts. If that is the case, reassess your build
  process and consider making changes to limit the amount of network resources
  needed.
- We provide artifact reviewers with VM instances that can be spawn from HotCRP
  to perform the evaluation. Your artifact, however, should also be executable
  in general, and not only on these VMs. Hence, your descriptions and scripts
  should be as generic as possible.

## My artifact runs on cloud computing platforms such as AWS EC2, etc., and requires access credentials. How can I prepare my artifact for review?

Since PETS 2026, we have a dedicated submission field on HotCRP to allow authors
to specify account credentials, API access keys, etc. Authors should state the
amount of money/credits required to run the experiments and provide account
credentials with enough credits. Our reviewers are _not_ expected to invest
their money or provide their credit cards to set up accounts.

If any form of credentials cannot be provided, provide an alternative way of
running your artifact; you may communicate with the artifact chairs. If this is
not possible, reconsider your choices of badges, as it may be impossible to
assess your artifact for the "Artifact Functional or Reproduced" badges.

## My paper includes a dataset. How should I prepare the dataset?

- Document your dataset so that others can reuse it.
- Add scripts to automatically download the dataset (if necessary), parse the
  data, and produce the tables, graphs, or statistics that appear in the paper.
- If the dataset includes survey results, provide a copy of the original survey
  with raw results. This is vital for replication studies and helping
  researchers interpret the context of your results.

Please refer to the instructions under one of the previous FAQs on how to upload
large files to your repository.

## My paper involves a large machine learning (ML) model, or other such large files that are difficult to share. How can I get the "Artifact Functional" badge?

If a large ML model, or other file is required to execute the presented tool,
the authors should include it within their artifact, unless it is proprietary.
If the dataset or model is not included in the artifact, authors must share a
synthetic dataset or dummy model, which may, perhaps perform worse, but which
can be used by other researchers to test the principle functionality of the
artifact. Authors should provide the code to train the original model, though
depending on the contributions of the paper, it need not be executed.

Please refer to the instructions under one of the previous FAQs on how to upload
large files to your repository.

## My experiment has a lengthy runtime or requires a large amount of compute resources. How can I get the "Artifact Functional" badge?

Although experiments may require days or weeks of compute time on commodity
hardware, the "Artifact Functional" badge can usually still be achieved, by
following _each_ of the steps below.

- Provide a simplified version of the experiments, which may run on fewer data
  or fewer epochs of time, in order to enable the reviewers to check the
  functionality of that stage. If the results of the simplified experiments
  align with the ones reported in the paper, then authors can also aim for the
  "Artifact Reproduced" badge.
- Provide instructions and results of the full experiment in the repository, so
  that reviewers can verify the functionality of the later stages with these
  results.

## My paper involves a longitudinal study or crawl. How can I get the "Artifact Functional and Reproduced" badges?

Authors should provide:

- Anonymized raw data, unless forbidden by legal requirements, privacy, or
  ethical concerns. In this case, authors should include a dataset with dummy or
  synthetic data. Please follow the instructions above to upload large files to
  your artifact.
- Evaluation scripts to reproduce the results of the paper. Reviewers should be
  able to execute the evaluation scripts on either anonymized raw data or dummy
  data.

## My paper involves a hardware-based contribution. How can I prepare my artifact?

- If the artifact requires GPU VMs, Trusted Execution Environments, IoT devices
  and Smartphones, ensure that you indicate this at submission time.
- If other special hardware is required, then artifact chairs will attempt to
  procure the hardware from other artifact evaluation committee members. If this
  is not possible, then the artifact chairs may require authors to be involved
  in a video call to evaluate the artifact for the "Artifact Functional" and
  "Artifact Reproduced" badges.
- The authors may also simulate the hardware, though this can be challenging.
- Authors should additionally publish the raw results of the experiments, so
  that reviewers can verify the remaining stages as functional.

