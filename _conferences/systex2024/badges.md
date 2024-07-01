---
title: Badges
order: 30
---

Submitted artifacts could select to be evaluated against the following badges (inspired by [ACM](https://www.acm.org/publications/policies/artifact-review-and-badging-current) and [USENIX](https://secartifacts.github.io/usenixsec2024/badges)):

<style>
table th:first-of-type {
    width: 30%;
}
table th:nth-of-type(2) {
    width: 70%;
}
</style>

| SysTEX Badges | Description |
|:-------------:|:------------|
| ![available badge]({{ site.baseurl }}/images/systexbadges-available.svg) | **Artifacts Available:** When the AEC could verify that the artifacts were made available permanently and publicly via a stable URL. Any public hosting website is allowed, but _not_ a personal webpage. When using a git repository (e.g., GitHub), a commit hash or tag is required for a stable URL. To earn this badge, no further requirements on documentation, completeness, or functionality are needed.  |
| ![functional badge]({{ site.baseurl }}/images/systexbadges-functional.svg) | **Artifacts Functional:** When the AEC deems the artifact to be (i) _complete_ (i.e., all key components described in the paper are included); (ii) reasonably well-documented; and (iii) _exercisable_ (e.g., building of the software could be verified).  |
| ![reproduced badge]({{ site.baseurl }}/images/systexbadges-reusable.svg) | **Artifacts Reusable:** When the quality of the artifact significantly exceeds minimal functionality, e.g., the code can be ran and at least some results could be reproduced.  |


**Note:** As this is a new initiative, and to keep the reviewing load manageable, verifying full reproducibility as per ACM's strict [definition](https://www.acm.org/publications/policies/artifact-review-and-badging-current) was put explicitly out of scope this year. The "Artifacts Reusable" badge is intended to recognize those artifacts that go beyond minimal expectations. 
