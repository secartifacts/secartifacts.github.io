---
title: Awards
order: 80

reviewer_awards:
- Mir Masood Ali, University of Illinois Chicago
- Linard Arquint, ETH Zurich
- Fabian Bäumer Ruhr, University Bochum
- Yohan Beugin, University of Wisconsin-Madison
- Hongyan Chang, National University of Singapore
- Xiaoyu Cheng, Southeast University
- Michael Clark, Brigham Young University
- Jean-Charles Noirot Ferrand, University of Wisconsin-Madison
- Kyle Fredrickson, UCSC
- Alexander Hart, CISPA Helmholtz Center for Information Security
- Xuanbo Huang, University of Science and Technology of China
- Patrick Jattke, ETH Zurich
- Torsten Krauß, University of Würzburg
- Lukas Lamster, Graz University of Technology
- Ying Li, UCLA
- Kaixuan Luo, The Chinese University of Hong Kong
- Seyed Mohammad Mehdi Mirnajafizadeh, Wayne State University
- Junpeng Wan, Purdue University

noteworthy_reviewer_awards:
- Eric Ackermann, CISPA
- Shubham Agarwal, CISPA Helmholtz Center for Information Security
- Muhammad Abu Bakar Aziz, Northeastern University
- Evangelos Bitsikas, Northeastern University
- Marton Bognar, DistriNet, KU Leuven
- Yifeng Cai, Peking University
- Xiang Chen, The Hong Kong University of Science and Technology
- Guillaume DIDIER, Saarland University
- Kha Dinh, Sungkyunkwan University
- Andrea Di Dio, Vrije Universiteit Amsterdam
- Chuanpu Fu, Tsinghua University
- Xin Fan Guo, King's College London
- Chakshu Gupta, University of Twente
- Keno Hassler, CISPA Helmholtz Center for Information Security
- Yi He, Wuhan University
- Adrian Herrera, Interrupt Labs
- Yibo Huang, University of Michigan
- Abdullah Al Ishtiaq, The Pennsylvania State University
- Md. Ishtiaq Ashiq Khan, Virginia Tech
- Kelly Kaoudis, Trail of Bits
- Hugo Kermabon-Bobinnec, Concordia University
- Joseph Khoury, Louisiana State University
- Tomer Laor, Ben-Gurion University of the Negev
- Zichuan Li, Indiana University Bloomington
- Junming Liu, Zhejiang University
- Zhengyu Liu, Johns Hopkins University
- Zhengyao Lin, Carnegie Mellon University
- Maxime Puys, University Clermont Auvergne
- Grigoris Ntousakis, Brown University
- Vaishnavi Raghavajosyula, Max Planck Institute for Informatics
- Johnny So, Stony Brook University
- Tyler Tucker, University of Florida
- Xianbo Wang, The Chinese University of Hong Kong
- Felix Weissberg, TU Berlin
- Minghui Xu, Shandong University
- Zheng Yang, Georgia Institute of Technology
- Huanqi Yang, City University of Hong Kong
- Tianchang Yang, The Pennsylvania State University
- Yupeng Yang, Georgia Institute of Technology
- Kyle Zeng, Arizona State University
- Yiwei Zhang, Purdue University
- Junqi Zhang, University of Science and Technology of China
- Guangsheng Zhang, University of Technology Sydney
- Zidong Zhang, Simon Fraser University, QI-ANXIN Research Institute

ninjas_reviewer_awards:
- Eric Ackermann, CISPA
- Linard Arquint, ETH Zurich
- Fabian Bäumer Ruhr, University Bochum
- Abdulrahman Diaa, University of Waterloo
- Xuanbo Huang, University of Science and Technology of China
- Rahul Kande, Texas A&M University
- Hugo Kermabon-Bobinnec, Concordia University
- Joseph Khoury, Louisiana State University
- Kiho Lee, ETRI
- Ahmed Lekssays, Qatar Computing Research Institute
- Atefeh Mohseni, University of California
- Jean-Charles Noirot Ferrand, University of Wisconsin-Madison
- Grigoris Ntousakis, Brown University
- Maxime Puys, University Clermont Auvergne
- Christoph Sendner, University of Würzburg
- Ryan Vrecenar, Sandia National Laboratories
- Feng Wei, University at Buffalo

---

## 🏆 Distinguished Artifact Awards

- [Encarsia: Evaluating CPU Fuzzers via Automatic Bug Injection](https://www.usenix.org/conference/usenixsecurity25/presentation/bolcskei) - Matej Bölcskei, Flavien Solt, Katharina Ceesay-Seitz, and Kaveh Razavi, ETH Zurich
- [SoK: So, You Think You Know All About Secure Randomized Caches?](https://www.usenix.org/conference/usenixsecurity25/presentation/bhatla) - Anubhav Bhatla, Hari Rohit Bhavsar, Sayandeep Saha, and Biswabandan Panda, Indian Institute of Technology Bombay
- [Tracking You from a Thousand Miles Away! Turning a Bluetooth Device into an Apple AirTag Without Root Privileges](https://www.usenix.org/conference/usenixsecurity25/presentation/chen-junming) - Junming Chen, Xiaoyue Ma, Lannan Luo, and Qiang Zeng, George Mason University
- [Exposing the Guardrails: Reverse-Engineering and Jailbreaking Safety Filters in DALL·E Text-to-Image Pipelines](https://www.usenix.org/conference/usenixsecurity25/presentation/villa) - Corban Villa, New York University Abu Dhabi; Shujaat Mirza, New York University; Christina Pöpper, New York University Abu Dhabi
- [Nothing is Unreachable: Automated Synthesis of Robust Code-Reuse Gadget Chains for Arbitrary Exploitation Primitives](https://www.usenix.org/conference/usenixsecurity25/presentation/bailluet) - Nicolas Bailluet, Univ Rennes, Inria, CNRS, IRISA; Emmanuel Fleury, Univ Bordeaux, CNRS, LaBRI; Isabelle Puaut and Erven Rohou, Univ Rennes, Inria, CNRS, IRISA
- [owlc: Compiling Security Protocols to Verified, Secure, High-Performance Libraries](https://www.usenix.org/conference/usenixsecurity25/presentation/singh) - Pratap Singh, Carnegie Mellon University; Joshua Gancher, Northeastern University; Bryan Parno, Carnegie Mellon University

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

