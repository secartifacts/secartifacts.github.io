---
title: Tips
order: 40
---

The following guides will be useful when preparing your artifact:
- [HOWTO for AEC Submitters](https://docs.google.com/document/d/1pqzPtLVIvwLwJsZwCb2r7yzWMaifudHe1Xvn42T4CcA/edit),
  by Dan Barowy, Charlie Curtsinger, Emma Tosch, John Vilk, and Emery Berger
- [Artifact Evaluation: Tips for Authors](https://blog.padhye.org/Artifact-Evaluation-Tips-for-Authors/),
  by Rohan Padhye

Here are some general tips to make life easier for both artifact authors and evaluators:

- **Automate as much as possible**, you will save a lot of time in the end from not having to re-run experiments that suffered from human error.
  This is feasible even for artifacts that need multiple nodes or to replicate configuration in multiple places.
  See [this repository](https://github.com/SolalPirelli/docker-artifact-eval) for an example of artifact automation with Docker.

- **Try out your own artifact on a blank environment**, following the steps you documented.
  One lightweight way to do this is to create a Docker container from a base OS image, such as `ubuntu:latest`.
  You can also use a virtual machine or even provision a real machine if you have the infrastructure to do so.

- **Log both successes and failures**, so that users know that something happened.
  Avoid logging unnecessary or confusing information, such as verbose output or failures that are actually expected.
  Log potential issues, such as an optional but recommended library not being present.

- **Measure resource use** using tools such as `mpstat`, `iostat`, `vmstat`, and `ifstat` to measure CPU, I/O, memory, and network use respectively on Linux,
  or `/usr/bin/time -v` to measures the time and memory used by a command also on Linux.
  This lets users know what to expect.

## Checklists

Unfortunately, artifacts sometimes miss badges because they were not tested on a
clean setup, or not documented enough, or because running experiments is too
error-prone due to complex manual steps. **This year, we provide checklists for authors and evaluators**
to help prepare and evaluate artifacts, minimizing the
risk of an artifact unnecessarily missing a badge.


### Artifact Available

- The artifact is available on a public website with a specific version such as a git commit
- The artifact has a "read me" file with a reference to the paper
- Ideally, the artifact should have a license that at least allows use for comparison purposes

Artifacts must meet these criteria _at the time of evaluation_.
Promises of future availability, such as artifacts "temporarily" gated behind credentials given to evaluators, are not enough.

### Artifact Functional

- The artifact has a "read me" file with high-level documentation:
  - A description, such as which folders correspond to code, benchmarks, data, ...
  - A list of supported environments, including OS, specific hardware if necessary, ...
  - Compilation and running instructions, including dependencies and pre-installation steps,
    with a reasonable degree of automation such as scripts to download and build exotic dependencies
  - Configuration instructions, such as selecting IP addresses or disks
  - Usage instructions, such as analyzing a new data set
  - Instructions for a "minimal working example"
- The artifact has documentation explaining the high-level organization of modules, and code comments explaining non-obvious code,
  such that other researchers can fully understand it
- The artifact contains all components the paper describes using the same terminology as the paper, and no obsolete code/data
- If the artifact includes a container/VM, it must also contain a script to create it from scratch

Artifacts must be usable on other machines than the authors', though they may require hardware such as specific network cards.
Information such as IP addresses must not be hardcoded.

### Results Reproduced

- The artifact has a "read me" file that documents:
  - The exact environment the authors used, including OS version and any special hardware
  - The exact commands to run to reproduce each claim from the paper
  - The approximate resources used per claim, such as "5 minutes, 1 GB of disk space"
  - The scripts to reproduce claims are documented, allowing researchers to ensure they correspond to the claims;
    merely producing the right output is not enough
- The artifact's external dependencies are fetched from well-known sources such as official websites or GitHub repositories
  - Changes to such dependencies should be clearly separated, such as using a patch file or a repository fork with a clear commit history

The amount of manual work, such as writing configuration files, should be reasonably minimized.
In particular, there should be no redundant manual steps such as writing the same configuration values in multiple places, as this inevitably leads to human error.