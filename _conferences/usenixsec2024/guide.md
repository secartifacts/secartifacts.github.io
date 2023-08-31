---
title: Evaluator guide
order: 45
---

This document is a guide through the artifact evaluation process for evaluators.

If you have general questions, please contact the artifact evaluation chairs. If
you have a question about a specific artifact, see below for instructions on
asking the authors.

## Your Goal as a Reviewer

The goal of artifact evaluation is to help science by ensuring that published
papers are accompanied by high-quality artifacts (e.g., software, hardware,
datasets, etc.) that can be reused and extended by others. Authors submit their
artifacts (and the artifact appendix) after the camera-ready version has been
finalized (possibly in an earlier cycle) and are incentivized to participate
through the awarding of badges. Moreover, the best artifacts that excel in all
the evaluated dimensions will be rewarded with a Distinguished Artifact Award.

Your main goal is to read the paper and judge how well the artifact matches the
expectations set by it. We expect artifacts to be (i) consistent with the paper,
(ii) as complete as possible, (iii) documented well, and (iv) easy to reuse for
further research.

Keep in mind that all artifacts, reviews, and discussions are confidential. Some
artifacts may even contain embargoed material (e.g., exploits) due to
vulnerability disclosure. As such, we trust you will treat all the AE material
as confidential and also delete the artifact after the evaluation has finished
(although most authors will publish the artifact upon publication of the paper).

Also keep in mind that artifact evaluation is a cooperative process. Artifacts
that initially do not meet the requirements for badges can still get badges if
the authors make necessary improvements in time, and evaluators should provide
actionable feedback to enable this. Artifacts should only “miss” badges if there
was not enough time to reasonably address the evaluators’ concerns, or if the
authors were unresponsive or unreasonable. Note that authors will be able to
update their artifacts with no restrictions in response to your comments (e.g.,
to fix bugs). Authors can submit artifact/appendix updates through external
repositories rather than HotCRP. We’ll collect the final appendix (and stable
reference) via HotCRP again after finalizing decisions.

The papers under evaluation have already been accepted by the technical program
committee, so you do not need to evaluate their scientific soundness. However,
if you believe you have found a technical flaw in a paper anyway, contact the
artifact evaluation chairs.


## Timeline

The bidding deadline is the first important deadline, as it will allow the
chairs to distribute artifacts in a way that maximizes evaluator expertise and
interest. Bidding maximizes your chances to evaluate artifacts in domains you
know about and are interested in.

The “kick the tires” period is when evaluators go through the artifacts to
ensure they will be able to properly evaluate them later. It is important to do
this as soon as possible, so that authors have enough time to fix big issues if
needed.

The reviewing and author discussion period comes next, where evaluators evaluate
the artifacts and communicate with the authors to request
clarifications/improvements to the artifacts and the appendix. Reviews are due
at the end of the period, with individual proposals to award (or not to award)
each requested badge.

Afterwards, there is some time to agree on badges before the final deadline.
This to ensure that there is time for reviewers to discuss the artifacts that
need it as well as time for any extra or late evaluations. Keep in mind that the
final deadline for agreeing on badges is strict.


## Communicating with authors

Artifact evaluation is single-blind, meaning authors do not and must not know
who you are so that you can be frank in your assessment. To enable this, all
communication between authors and reviewers must be done through HotCRP, not by
other means such as email.

Please make sure that in your HotCRP profile, under “Preferences”, the “Send
mail” box for “Reviews and comments on authored or reviewed submissions” is
checked, so that you are notified of comments on your assigned artifacts from
authors and fellow reviewers.

To add a comment on HotCRP, at the bottom of the artifact page, click on the
“Add comment” button to show a form, type your comment, and select the right
visibility for your comment. Discussion with authors must be “Author
discussion”, while discussion with evaluators must be “Reviewer discussion”. For
chairs-only comments, you can use “Administrators only”. Leave the second option
to “about: submission”.

You can notify a fellow evaluator with an @-mention in a HotCRP comment, as on
many other platforms. Type @ and let HotCRP autocomplete the name you want. You
can also use the same @-mention mechanism to tag the AEC chairs and bring an issue to their attention.

Use “Reviewer discussion” comments to synchronize with your fellow evaluators
and ensure the same issue was not raised by another review before.

Authors submit their initial version of the artifact, artifact appendix and any
other information needed to evaluate the artifact. You should carefully read
these documents and make recommendations to the authors to improve the
documentation of the artifact. Any errors you find or missing information should
be documented and communicated as early as possible to the authors. They will
then update the artifact or appendix. The badge decision is made based on the
last submitted version of the artifact and appendix and should be independent of
how many problems you ran into or changes were needed.


## Evaluation setups

You can evaluate artifacts on various setups, in order of preference:

* Your own machine, if the artifact supports it
   * Even if the artifact requires a particular OS or multiple machines, you may
     be able to run it locally via Docker (e.g. see [this
     repo](https://github.com/SolalPirelli/docker-artifact-eval)) or using
     virtual machines such as with VirtualBox
* Any servers with beefy/special hardware you may have access to, for artifacts
  that could benefit from this
* The artifact authors’ machines, accessed via SSH or such, for artifacts that
  cannot run anywhere else due to hardware dependencies
* Commercial clouds such as AWS or Azure, but only if absolutely necessary and
  the authors are willing to pay for it; in that case, please agree with the
  authors on a protocol in which you agree to spawn and tear down machines to
  minimize unnecessary costs.

_Note on anonymization_: If you have to SSH to the authors’ machines, make sure
your public SSH key does not identify you (remove the user@host part at the
end). If you are concerned you could be identified through other means, such as
because of your IP address (e.g., because you do not have access to a VPN),
contact the chairs.

## Bidding phase

Once artifacts are submitted, you need to bid for the artifacts you want to
review. You can enter your preferences by the bidding deadline by logging into
HotCRP and clicking on “Review preferences”. You can use -20 to 20 as the range
to rank the artifacts by preference and -100 to declare a conflict of interest
(contact the AE chairs if unsure). When bidding, also pay attention to the
hardware/software requirements of the artifact.

Note: we will try to match artifacts to your preferences, but if you don’t bid
by the deadline, you may be assigned less-than-ideal artifact(s) for your
profile.


## Initial "kick the tires" phase

Once you have been assigned artifacts comes the initial “kick the tires” period.
The goal of this period is to quickly determine whether you have everything you
need for a full review: the artifact itself, any necessary hardware or other
dependencies, and a plan on how you will evaluate the artifact. If that is not
the case, you must discuss with your fellow evaluators and let the authors know
of any problems as soon as possible, so that they have enough time to fix
issues.

Double-check which badges the authors requested in their artifact submission;
you do not need to evaluate the artifact for badges that were not requested (if
you believe an artifact already meets the requirements for a badge the authors
did not request, ask the authors; they may have forgotten to request that
badge).

Carefully read the artifact documentation. In particular, check the software and
hardware dependencies to make sure you have all you need. You are allowed to use
your own judgment when making decisions, for instance to evaluate reasons why
some artifacts may not be able to reproduce everything their paper contains.
Before starting the evaluation, consider the following points and ideally share
the evaluation plan with the authors:


Before starting the evaluation, consider the following points and ideally share
the evaluation plan with the authors:
* Whether you have everything you need to do the evaluation, and if not, what is missing including:
   * Access to the necessary hardware owned by you, by the authors
   * For artifacts requesting the "functional" badge, documentation and full source code as mentioned
     in [the checklist](tips#artifact-functional), and whether the code compiles
   * For artifacts requesting the "reproduced" badge, additionally the scripts to run the experiments and generate figures as mentioned
     in [the checklist](tips#results-reproduced)
* A plan on how you will evaluate the artifact during the review period:
s   * Time frames of when experiments will be run in case hardware is shared

## Reviewing artifacts

For each artifact you are assigned to, you will produce one review explaining
which badges you believe should be awarded and why or why not. You will work
with the authors to produce your review, as this is a cooperative process.
Authors are a resource you can use, exclusively through HotCRP, if you have
trouble with an artifact or if you need more details about specific portions of
an artifact.

There is an example review at the end of this guide.

First, (re-)read the [page on badges](badges).The checklists are particularly
important: artifacts that meet these requirements should get the corresponding
badges, while artifacts that do not should either justify why or not get the
badges. If an artifact does not satisfy a checklist but the authors provide a
good reason as to why they should get the badge anyway, use your judgment based
on the definitions of the badges. Remember that the Artifacts Functional and
Results Reproduced badges require not only running the code but also auditing it
to ensure that (for Artifacts Functional) the code is documented and
understandable, and (for Results Reproduced) the code actually does what the
paper states it does and reproduces results to support all the main claims of
the paper (which must be documented in the submitted artifact appendix). Merely
reproducing similar output as the paper, such as performance metrics, is not
enough, the artifact must actually do what it claims to do. You are not expected
to understand every single line of code, but you should be confident that the
artifact overall matches the paper’s description.

**Most of your time should be spent auditing artifacts, not debugging them**. If
you run into issues such as missing dependencies, try to quickly work around
them, such as by finding the right package containing the dependency for your
operating system and letting the authors know they have to fix their
instructions. However, it is the authors’ responsibility to make their artifacts
work, not yours. You do not need to spend hours trying to debug and fix complex
issues; if you encounter a non-trivial error, first ask your fellow evaluators
if they encountered it too or if they know how to fix it, then ask the authors
to fix it.

**It is acceptable to deny badges if artifacts require unreasonable effort**,
especially if such effort could be avoided through automation. For instance, if
reproducing a claim requires 50 points of data, and the artifact requires you to
manually edit 5 config files then run 4 commands on 3 machines for each data
point, you do not need to actually perform hundreds of manual steps; instead,
ask the authors to automate this, or even write a script yourself if you have
the time that you can then share with the authors.

Concerning the artifact appendix, please verify it follows the provided
[template](https://secartifacts.github.io/usenixsec2023/instructions#artifact-appendix)
and its constraints (mandatory sections in particular). Do ask the authors for
updates during the review process if the appendix does not follow the template
or if important information is missing. Similarly, if authors apply for the
Artifacts Available badge, please verify they provided a stable reference (URL)
to the artifact at submission time (see
[badge](https://secartifacts.github.io/usenixsec2023/badges) requirements for
details). If not, do ask for updates during the review process.

Once you are finished evaluating an artifact, fill in the review form and submit
it at your earliest convenience. Your review must explain in detail why the
artifact should or should not get each of the badges that the authors requested.
You can also include additional suggestions for the authors to improve their
artifacts if you have any. Note that you can edit your review as many times as
you like, since reviews only become visible to the authors when final decisions
are announced.

Remember that the artifact evaluation process is cooperative, not adversarial.
Give authors a chance to fix issues by discussing through HotCRP comments before
deciding that their artifact should not get a badge. In other words, help the
authors improve their artifacts and reach badge status in the allocated time,
whenever possible. However, if authors are being unresponsive or unreasonable,
feel free to post a comment stating a badge cannot be awarded unless the authors
take the specified steps in time by the deadline.

HotCRP allows you to rate your fellow evaluators’ reviews. If you think a review
is well done, don’t hesitate to add a positive vote! If you think a review could
use improvement, you can leave a negative vote and a reviewer discussion comment
explaining your thoughts.

## Example review

We provide here an example review for a fictitious artifact/paper.
This review started by copy-pasting each point from the badge checklists, then modifying the text to suit the artifact and
starting each point with one of ✔ (= yes), ❌ (= no), or ⚠ (= yes, but has issues). For the "Results Reproduced" badges,
if results differ from the original in any way it's good to explain how, even if the badge should be awarded.
Remember that on HotCRP you can use Markdown for headings, lists, tables, and so on.

### Artifact Available

- ✔ The artifact is available on a public GitHub repository
- ✔ The artifact has a "read me" file with a reference to the paper
- ⚠ The artifact does not have a license that allows use for comparison purposes; this is not necessary but it would be good to have

I suggest awarding the badge.

### Artifact Functional

- ❌ The artifact 's "read me" file is missing some information:
  - ✔ It has a description
  - ✔ It has compilation and running instructions
  - ✔ It has usage instructions to run experiments
  - ❌ It does not have a list of supported environments
  - ❌ It does not have configuration instructions to select the client and server IPs
  - ❌ It does not have instructions for a "minimal working example", only for full experiments on 12 machines
- ✔ The code is well documented at both the module and class level, good job!
- ⚠ The artifact contains all major parts described in the paper;
     it would be good if it included the extra experiments mentioned in the paper's Limitations section as well, but this is not mandatory

I hope authors can fix the issues mentioned above so that the Artifact Functional badge can be awarded.

### Results Reproduced

I considered the 3 claims as per the artifact appendix, except for claim #3 in which I used a different configuration file after our discussion with the authors.
All experiments were carried out on CloudLab using the authors' profile.
I obtained all software from the artifact's GitHub repository, commit abc0def.

- ✔ The artifact has a "read me" file that documents:
  - ✔ The exact environment the authors used
  - ✔ The exact commands to run to reproduce each claim from the paper
  - ⚠ The time used per claim, but not the disk space which would be nice to indicate since it is multiple GBs
  - ✔ The scripts to reproduce claims are very well documented and correspond to what the paper states

For claim 2, I obtained 4400 ops/s for the artifact and 3500 ops/s for the baseline, which is a bit lower for the artifact than what the paper claims.
However, the key part of the claim is that the artifact is at least as fast as the baseline, not an absolute performance number, so I believe this is fine.
I suggest awarding the badge.
