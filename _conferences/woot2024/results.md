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

-   title: 'Exploiting Android’s Hardened Memory Allocator'
    badges: 'Badges: Available, Functional, Reproduced'
    artifact_url: https://github.com/HexHive/scudo-exploitation/tree/woot24
    appendix_url: appendix-files/woot24ae-final1.pdf
    paper_url: https://www.usenix.org/conference/woot24/presentation/mao

-   title: 'SoK: Where’s the “up”?! A Comprehensive (bottom-up) Study on the Security of Arm Cortex-M Systems'
    badges: 'Badges: Available'
    artifact_url: https://github.com/CactiLab/SoK-Cortex-M/releases/tag/v1.0
    paper_url: https://www.usenix.org/conference/woot24/presentation/tan

-   title: 'Introduction to Procedural Debugging through Binary Libification'
    badges: 'Badges: Available, Functional, Reproduced'
    artifact_url: https://zenodo.org/doi/10.5281/zenodo.11298208
    appendix_url: appendix-files/woot24ae-final3.pdf
    paper_url: https://www.usenix.org/conference/woot24/presentation/brossard

-   title: 'RIPencapsulation: Defeating IP Encapsulation on TI MSP Devices'
    badges: 'Badges: Available, Functional'
    artifact_url: https://github.com/FoRTE-Research/RIPencapsulation/tree/3dd345b79e541519bbfaec7c406f9745feec81e2
    appendix_url: appendix-files/woot24ae-final4.pdf
    paper_url: https://www.usenix.org/conference/woot24/presentation/sah

-   title: 'The Power of Words: Generating PowerShell Attacks from Natural Language'
    badges: 'Badges: Available, Functional'
    artifact_url: https://github.com/dessertlab/powershell-offensive-code-generation/releases/tag/artifact-release
    paper_url: https://www.usenix.org/conference/woot24/presentation/liguori

-   title: 'Attacking with Something That Does Not Exist: "Proof of Non-Existence" Can Exhaust DNS Resolver CPU'
    badges: 'Badges: Available, Functional'
    artifact_url: https://doi.org/10.5281/zenodo.11352869
    paper_url: https://www.usenix.org/conference/woot24/presentation/gruza

-   title: 'Basilisk: Remote Code Execution by Laser Excitation of P–N Junctions Without Insider Assistance'
    badges: 'Badges: Available, Functional'
    artifact_url: https://github.com/jloughry/basilisk_artifacts/releases/tag/v.1
    appendix_url: appendix-files/woot24ae-final7.pdf
    paper_url: https://www.usenix.org/conference/woot24/presentation/loughry

-   title: 'SOK: 3D Printer Firmware Attacks on Fused Filament Fabrication'
    badges: 'Badges: Functional'
    paper_url: https://www.usenix.org/conference/woot24/presentation/rais

-   title: 'Reverse Engineering the Eufy Ecosystem: A Deep Dive into Security Vulnerabilities and Proprietary Protocols'
    badges: 'Badges: Available, Functional'
    artifact_url: https://zenodo.org/doi/10.5281/zenodo.11085514
    paper_url: https://www.usenix.org/conference/woot24/presentation/goeman

-   title: 'SoK: On the Effectiveness of Control-Flow Integrity in Practice'
    badges: 'Badges: Available, Functional'
    artifact_url: https://github.com/seemoo-lab/woot24_cfi_coverage_tools/releases/tag/woot-submission
    paper_url: https://www.usenix.org/conference/woot24/presentation/becker

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