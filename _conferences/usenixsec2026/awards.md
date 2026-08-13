---
title: Awards
order: 80

reviewer_awards:
- Abdullah Al Ishtiaq, The Pennsylvania State University
- Ahmed Lekssays, Qatar Computing Research Institute
- Corban Villa, UC Berkeley
- Jinhao Zhu, UC Berkeley
- Junming Chen, George Mason University
- Keno Hassler, CISPA Helmholtz Center for Information Security
- Mathé Hertogh, VU Amsterdam
- Pratik M. Kamble, Binghamton University
- Vishnu Dasu, Pennsylvania State University
- Yi Zhou, Amazon Web Serivce
- Zachary Espiritu, MongoDB Research

noteworthy_reviewer_awards:
- Alessandro Baccarini, Input Output
- Dominic Troppmann, CISPA Helmholtz Center for Information Security
- Elizabeth Lin, North Carolina State University
- Eric Ackermann, CISPA
- Eric García Arribas, TU Graz
- Giuseppe Parrella, University of Salerno
- Huiyun Peng, Purdue University
- Iman Alipour, Max Planck Institute for Informatics
- Ismat Jarin, University of California, Irvine
- Jiangrui Yu, Peking University
- Jie Fu, Stevens Institute of Technology
- Jiwon Kim, Purdue University
- Joseph Khoury, Louisiana State University
- Kaixuan Luo, The Chinese University of Hong Kong
- Kyungchan Lim, University of Maryland
- Lipeng He, University of Waterloo
- Longxiang Wang, City University of Hong Kong
- Luca Wilke, Microsoft Research
- Marcel Maehren, Ruhr University Bochum
- Maynard Koch, TU Dresden
- Nima Naderloui, University of Connecticut
- Patrick Jattke, ETH Zurich
- Side Liu, Tulane University
- Sofiane Azogagh, Université du Québec à Montréal
- Sungwoo Kim, Purdue University
- Vaishnavi Raghavajosyula, Max Planck Institute for Informatics
- Xiaohan Zhang, Fudan University
- Ying Li, University of California, Los Angeles
- Yu-Jye Tung, The Pennsylvania State University
- Yunpeng Tian, The Hong Kong Polytechnic University
- Zeyang Zhuang, The Chinese University of Hong Kong
- Zhikang Xie, The University of Hong Kong
- Zizhuang Deng, Shandong University

ninjas_reviewer_awards:
- Ahmed Lekssays, Qatar Computing Research Institute
- Antonio Muñoz, University of Malaga
- Eric Ackermann, CISPA
- Felix Graf Lange, Paderborn University
- Guillaume Didier, Universität des Saarlandes
- Hassan El Alami, Howard University
- Hocheol Nam, KAIST
- Jinseo Vik Lee, KAIST
- Junqi Zhang, University of Science and Technology of China
- Ryan Vrecenar, Sandia National Laboratories
- Shubham Agarwal, Max Planck Institute for Security and Privacy
- Yao Zhao, Victoria University
- Zachary Espiritu, MongoDB Research

---

## 🏆 Distinguished Artifact Awards

- [CompLeak: Deep Learning Model Compression Exacerbates Privacy Leakage](https://www.usenix.org/conference/usenixsecurity26/presentation/li-na) - Na Li, Yansong Gao, Hongsheng Hu, Boyu Kuang, Anmin Fu
- [Leveraging Cryptographic Simulator Synthesis for Formally Verifying the FOO E-Voting Protocol -- Artifacts](https://www.usenix.org/conference/usenixsecurity26/presentation/baelde) - David Baelde, Adrien Koutsos, Justine Sauvage
- [Do You Need a Receipt? Anonymous Credential Revocation at Continental Scale via Private Record Certification](https://www.usenix.org/conference/usenixsecurity26/presentation/edalatnejad) - Kasra EdalatNejad, Sebastian Faust, Jonas Hofmann, Philipp-Florens Lehwalder, Thomas Schneider 
- [Meerkat: Pushing the Practical Limits of Dynamic Bisection with PoC Mutation](https://www.usenix.org/conference/usenixsecurity26/presentation/bursey) - Joseph Bursey, Christoph Sendner, Ardalan Amiri Sani, Zhiyun Qian
- [Principled Design of Indexing Functions for Memory Coloring](https://www.usenix.org/conference/usenixsecurity26/presentation/duebler) - Stephan Dübler, Jana Hofmann, Boris Köpf, Stavros Volos

## 🏆 Distinguished Reviewer Awards

<ul>
  {% assign sorted_reviewer_awards = page.reviewer_awards | sort %}
  {% for reviewer_award in sorted_reviewer_awards %}
    <li>{{ reviewer_award }}</li>
  {% endfor %}
</ul>

## ⭐ Noteworthy Reviewer Recognition

<ul>
  {% assign sorted_noteworthy_reviewer_awards = page.noteworthy_reviewer_awards | sort %}
  {% for noteworthy_reviewer_award in sorted_noteworthy_reviewer_awards %}
    <li>{{ noteworthy_reviewer_award }}</li>
  {% endfor %}
</ul>

## 🥷 Ninja Reviewer Recognition

<ul>
  {% assign sorted_ninjas_reviewer_awards = page.ninjas_reviewer_awards | sort %}
  {% for ninjas_reviewer_award2 in sorted_ninjas_reviewer_awards %}
    <li>{{ ninjas_reviewer_award2 }}</li>
  {% endfor %}
</ul>

