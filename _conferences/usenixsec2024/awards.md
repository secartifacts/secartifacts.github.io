---
title: Awards
order: 80

reviewer_awards:
- Fan Sang (Georgia Tech)
- Chuanpu Fu (Tsinghua University)
- Penghui Li (Zhongguancun Laboratory)
- Seongmin Lee (MPI-SP)
- Till Schlüter (CISPA)
- Vidya Lakshmi Rajagopalan (Stevens Institute of Technology)
- Ningyu He (Peking University)
- Jonas Juffinger (Graz University of Technology)
- Keno Hassler (CISPA)
- Mohammad Hammas Saeed (Boston University)
- Salvatore Signorello (Telefonica Research)
- Yi Zhou (Carnegie Mellon University)
- Yohan Beugin (University of Wisconsin, Madison)
- Yuzhou Fang (University of Southern California)
- Alfusainey Jallow (CISPA)
- Haojie He (Shanghai Jiao Tong University)
- Chen Chen (Texas A&M University)
- Shubham Agarwal (CISPA)
- Hossam Elatali (University of Waterloo)
- Ruiyi Zhang (CISPA)
- Pascal Cotret (ENSTA Bretagne)
- Lukas Gerlach (CISPA)
- Alexander J. Gaidis (Brown University)
- Xia Zhou (Zhejiang University)
- Jing Liu (University of California, Irvine)
- Bowen Zhang (The Hong Kong University of Science and Technology)
- David Balash (University of Richmond)
- Luca Baldesi (University of California, Irvine)
- Yi He (Tsinghua University)
- Ryan Vrecenar (Sandia National Laboratories)
---

## 🏆 Distinguished Artifact Awards

- [ChainReactor: Automated Privilege Escalation Chain Discovery via AI Planning](https://www.usenix.org/conference/usenixsecurity24/presentation/de-pasquale) - Giulio De Pasquale, King's College London and University College London; Ilya Grishchenko, University of California, Santa Barbara; Riccardo Iesari, Vrije Universiteit Amsterdam; Gabriel Pizarro, University of California, Santa Barbara; Lorenzo Cavallaro, University College London; Christopher Kruegel and Giovanni Vigna, University of California, Santa Barbara
- [PentestGPT: Evaluating and Harnessing Large Language Models for Automated Penetration Testing](https://www.usenix.org/conference/usenixsecurity24/presentation/deng) - Gelei Deng and Yi Liu, Nanyang Technological University; Víctor Mayoral-Vilches, Alias Robotics and Alpen-Adria-Universität Klagenfurt; Peng Liu, Institute for Infocomm Research (I2R), A*STAR, Singapore; Yuekang Li, University of New South Wales; Yuan Xu, Tianwei Zhang, and Yang Liu, Nanyang Technological University; Martin Pinzger, Alpen-Adria-Universität Klagenfurt; Stefan Rass, Johannes Kepler University Linz
- [SafeFetch: Practical Double-Fetch Protection with Kernel-Fetch Caching](https://www.usenix.org/conference/usenixsecurity24/presentation/duta) - Victor Duta, Mitchel Josephus Aloserij, and Cristiano Giuffrida, Vrije Universiteit Amsterdam
- [Terrapin Attack: Breaking SSH Channel Integrity By Sequence Number Manipulation](https://www.usenix.org/conference/usenixsecurity24/presentation/b%C3%A4umer) - Fabian Bäumer, Marcus Brinkmann, and Jörg Schwenk, Ruhr University Bochum
- [You Cannot Escape Me: Detecting Evasions of SIEM Rules in Enterprise Networks](https://www.usenix.org/conference/usenixsecurity24/presentation/uetz) - Rafael Uetz, Marco Herzog, and Louis Hackländer, Fraunhofer FKIE; Simon Schwarz, University of Göttingen; Martin Henze, RWTH Aachen University & Fraunhofer FKIE

## 🏆 Distinguished Reviewer Awards

<ul>
  {% assign sorted_reviewer_awards = page.reviewer_awards | sort %}
  {% for reviewer_award in sorted_reviewer_awards %}
    <li>{{ reviewer_award }}</li>
  {% endfor %}
</ul>