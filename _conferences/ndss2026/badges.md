---
title: Badges
order: 10
---

Authors can request their artifact to be evaluated towards one, two, or all of the following badges:

* **Available.** To earn this badge, the AEC must judge that the artifact associated with the paper has been made available for retrieval *permanently and publicly*. As an artifact undergoing AE often evolves as a consequence of AEC feedback, authors can use mutable storage for the initial submission, but must commit to uploading their materials to public services (e.g., Zenodo, FigShare, Dryad) for permanent storage backed by a Digital Object Identifier (DOI) if the badge is awarded. The artifact appendix prepared for publication will have to mention the artifact DOI. Authors are welcome to report additional sources, like GitHub and GitLab, that may ease the dissemination of the artifact and possible future updates. Furthermore, for this badge, authors must provide a `README` file referencing the paper and a `LICENSE` file for the materials.

* **Functional.** To earn this badge, the AEC must judge that the artifact conforms to the expectations set by the paper for functionality, usability, and relevance. Also, an artifact must be usable on *other machines* than the authors’, including when specialized hardware is required (for example, paths, addresses, and identifiers must not be hardcoded.) The AEC will particularly consider three aspects:
	* *Documentation*: is the artifact sufficiently documented to be exercised by readers of the paper?
	* *Completeness*: does the submitted artifact include all of the key components described in the paper?
	* *Exercisability*: does the submitted artifact include the scripts and data needed to run the experiments described in the paper, and can the software be successfully executed?

* **Reproduced.** To earn this badge, the AEC must judge that they can use the submitted artifact to obtain the main results presented in the paper. In short, is it possible for the AEC to independently repeat the experiments and obtain results that support the main claims made by the paper? The goal of this effort is not to reproduce the results exactly, but instead to generate results independently within an allowed tolerance such that the main claims of the paper are validated. For example, in the case of lengthy experiments, scaled-down versions can be proposed if clearly and convincingly explained for their significance. As another example, if results are about performance, response times, or other non-deterministic aspects, then the results should be reproducible within an acceptable margin of error.

Note that the badges are not hierarchical, for instance, you can request the Functional and Reproduced badges without requesting the Available badge, e.g., if you are unable to publicly share code due to license restrictions.

