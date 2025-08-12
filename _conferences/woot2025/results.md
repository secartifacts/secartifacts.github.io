---
title: Results
order: 70
available_img: "usenixbadges-available.svg"
available_name: "Artifacts Available (v1.1)"
functional_img: "usenixbadges-functional.svg"
functional_name: "Artifacts Evaluated - Functional (v1.1)"
reproduced_img: "usenixbadges-reproduced.svg"
reproduced_name: "Results Reproduced (v1.1)"

artifacts:

-   title: 'FUZZVPN: Finding Vulnerabilities in OpenVPN'
    badges: 'Badges: Available, Functional, Reproduced'
    artifact_url: https://doi.org/10.5281/zenodo.15476514
    paper_url: https://www.usenix.org/conference/woot25/presentation/chen

-   title: 'Making Acoustic Side-Channel Attacks on Noisy Keyboards Viable with LLM-Assisted Spectrograms’ Typo Correction'
    badges: 'Badges: Available, Functional, Reproduced'
    artifact_url: https://github.com/Botacin-s-Lab/EchoCrypt
    appendix_url: appendix-files/woot25ae-final2.pdf
    paper_url: https://www.usenix.org/conference/woot25/presentation/ayati

-   title: 'Bluetooth Security Testing with BlueToolkit: a Large-Scale Automotive Case Study'
    badges: 'Badges: Available, Functional, Reproduced'
    artifact_url: https://github.com/sgxgsx/BlueToolkit
    appendix_url: appendix-files/woot25ae-final3.pdf
    paper_url: https://www.usenix.org/conference/woot25/presentation/zubkov

-   title: 'GlitchGlück: Enabling Software Vulnerabilities through Guided Hardware Fault Injection'
    badges: 'Badges: Available, Functional'
    artifact_url: https://github.com/Secure-Embedded-Systems/woot2025-GlitchGluck/archive/refs/tags/woot25-artifact.tar.gz
    appendix_url: appendix-files/woot25ae-final4.pdf
    paper_url: https://www.usenix.org/conference/woot25/presentation/liu

-   title: 'BOOTKITTY: A Stealthy Bootkit-Rootkit Against Modern Operating Systems'
    badges: 'Badges: Functional'
    appendix_url: appendix-files/woot25ae-final5.pdf
    paper_url: https://www.usenix.org/conference/woot25/presentation/lee

-   title: 'SecurePoC: A Helping Hand to Identify Malicious CVE Proof of Concept Exploits in GitHub'
    badges: 'Badges: Available, Functional'
    artifact_url: https://zenodo.org/records/15675577
    appendix_url: appendix-files/woot25ae-final6.pdf
    paper_url: https://www.usenix.org/conference/woot25/presentation/el-yadmani

-   title: 'Extract: A PHP Foot-Gun Case Study'
    badges: 'Badges: Available, Functional'
    artifact_url: https://doi.org/10.5281/zenodo.15526425
    appendix_url: appendix-files/woot25ae-final7.pdf
    paper_url: https://www.usenix.org/conference/woot25/presentation/hartung

-   title: 'Stealth BGP Hijacks with uRPF Filtering'
    badges: 'Badges: Available'
    artifact_url: https://github.com/zsjstart/Stealthy-uRPF-Attack/tree/v1.1.0
    appendix_url: appendix-files/woot25ae-final8.pdf
    paper_url: https://www.usenix.org/conference/woot25/presentation/schulmann

-   title: 'Comma Separated Vulnerabilities: Detecting Formula Injection in the Wild'
    badges: 'Badges: Available, Functional'
    artifact_url: https://github.com/ias-tubs/Comma_Separated_Vulnerabilities/releases/tag/Woot25
    paper_url: https://www.usenix.org/conference/woot25/presentation/karl

-   title: 'No Key, No Problem: Vulnerabilities in Master Lock Smart Locks'
    badges: 'Badges: Functional'
    paper_url: https://www.usenix.org/conference/woot25/presentation/diao

-   title: 'Extraction of Secrets from 40nm CMOS Gate Dielectric Breakdown Antifuses by FIB Passive Voltage Contrast'
    badges: 'Badges: Available, Functional'
    artifact_url: https://github.com/lainy/rp2350-scripts/tree/5a5b2f3fea02ee570a56e68b5d34f21e7dc12b49
    paper_url: https://www.usenix.org/conference/woot25/presentation/zonenberg

-   title: 'Be Write Back: An in-depth Study of Fault Injection Effects on FRAM Technology'
    badges: 'Badges: Functional'
    paper_url: https://www.usenix.org/conference/woot25/presentation/huber

-   title: 'Security through Transparency: Tales from the RP2350 Hacking Challenge'
    badges: 'Badges: Available'
    artifact_url: https://github.com/bhamsec/woot25-rp2350-challenge/releases/tag/v1.0
    appendix_url: appendix-files/woot25ae-final13.pdf
    paper_url: https://www.usenix.org/conference/woot25/presentation/muench

-   title: 'Prekey Pogo: Investigating Security and Privacy Issues in WhatsApp’s Handshake Mechanism'
    badges: 'Badges: Available, Functional'
    artifact_url: https://github.com/sbaresearch/prekey-pogo/tree/woot25ae
    appendix_url: appendix-files/woot25ae-final14.pdf
    paper_url: https://www.usenix.org/conference/woot25/presentation/gegenhuber

-   title: 'DeepRed: A Deep Learning–Powered Command and Control Framework for Multi-Stage Red Teaming Against ML-based Network Intrusion Detection Systems'
    badges: 'Badges: Available, Functional'
    artifact_url: https://doi.org/10.5281/zenodo.15668685
    appendix_url: appendix-files/woot25ae-final15.pdf
    paper_url: https://www.usenix.org/conference/woot25/presentation/hajizadeh

-   title: 'Reality Check on Side-Channels: Lessons learnt from breaking AES on ARM Cortex-A72 processor with Out-of-Order Execution'
    badges: 'Badges: Available'
    artifact_url: https://doi.org/10.5281/zenodo.15524301
    appendix_url: appendix-files/woot25ae-final16.pdf
    paper_url: https://www.usenix.org/conference/woot25/presentation/boyapally

-   title: 'Oops, It Halted Again: Exploiting PLC Memory for Fun and Profit in Industrial Control Systems'
    badges: 'Badges:'
    paper_url: https://www.usenix.org/conference/woot25/presentation/jo

---

<table>
  <thead>
    <tr>
      <th>Paper</th>
      <th width="75px">Avail.</th>
      <th width="75px">Funct.</th>
      <th width="75px">Repro.</th>
      <th>Available At</th>
    </tr>
  </thead>
  <tbody>
  {% assign sorted_artifacts = page.artifacts | sort: "title" %}
  {% for artifact in sorted_artifacts %}
    <tr>
      <td>
        {% if artifact.paper_url %}
          <a href="{{artifact.paper_url}}" target="_blank">{{artifact.title}}</a>
        {% else %}
          {{ artifact.title }}
        {% endif %}
      </td>
      <td width="75px">
        {% if artifact.badges contains "Available" %}
          <img src="{{ site.baseurl }}/images/{{ page.available_img }}" alt="{{ page.available_name }}">
        {% endif %}
      </td>
      <td width="75px">
        {% if artifact.badges contains "Functional" %}
          <img src="{{ site.baseurl }}/images/{{ page.functional_img }}" alt="{{ page.functional_name }}">
        {% endif %}
      </td>
      <td width="75px">
        {% if artifact.badges contains "Reproduced" %}
          <img src="{{ site.baseurl }}/images/{{ page.reproduced_img }}" alt="{{ page.reproduced_name }}">
        {% endif %}
      </td>
      <td width="120px">
        {% if artifact.award %}
          <b>{{ artifact.award }}</b><br>
        {% endif %} {% if artifact.artifact_url %}
          📦 <a href="{{artifact.artifact_url}}" target="_blank">Artifact</a><br>
        {% endif %} {% if artifact.repository_url %}
          🗂️ <a href="{{artifact.repository_url}}" target="_blank">Repository</a><br>
        {% endif %} {% if artifact.appendix_url %}
          📄 <a href="{{artifact.appendix_url}}" target="_blank">Appendix</a><br>
        {% endif %}
      </td>
    </tr>
  {% endfor %}
  </tbody>
</table>
