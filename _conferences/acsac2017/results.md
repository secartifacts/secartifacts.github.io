---
title: Results
order: 20
functional_img: acmartifactbadge_functional.png
functional_name: Artifacts Functional
artifacts:
-   title: A Secure Mobile Authentication Alternative To Biometrics
    badges: functional
    artifact_url: https://github.com/casprlab/ai.lock
    paper_url: https://www.acsac.org/2017/program-files/s144.html
-   title: Automated Analysis Of Secure Internet Of Things Protocols
    badges: functional
    artifact_url: https://github.com/jun-kim/Automated-security-verification-of-IoT-protocols
    paper_url: https://www.acsac.org/2017/program-files/s189.html
-   title: 'Decanter: Detection Of Anomalous Outbound Http Traffic By Passive Application Fingerprinting'
    badges: functional
    artifact_url: http://scs.ewi.utwente.nl/downloads/show,Data%20Exfiltration%20Malware%20(DEM)/ https://github.com/rbortolameotti/decanter
    paper_url: https://www.acsac.org/2017/program-files/s72.html
-   title: 'Grid Shock: Coordinated Load-change Attacks On Power Grids'
    badges: functional
    artifact_url: http://seclab.tuwien.ac.at/people/atrox/gridshock-dabrowski.zip
    paper_url: https://www.acsac.org/2017/program-files/s259.html
-   title: 'Kakute: A Precise, Unified Information Flow Analysis System For Big-data Security'
    badges: functional
    artifact_url: https://github.com/hku-systems/kakute
    paper_url: https://www.acsac.org/2017/program-files/s78.html
-   title: Measuring Popularity Of Cryptographic Libraries In Internet-wide Scans
    badges: functional
    artifact_url: https://crocs.fi.muni.cz/public/papers/acsac2017 https://github.com/crocs-muni/classifyRSAkey
    paper_url: https://www.acsac.org/2017/program-files/s106.html
-   title: 'Picky Attackers: Quantifying The Role Of System Properties On Intruder Behavior'
    badges: functional
    artifact_url: https://drive.google.com/uc?id=1q5jZin2KozCnkX-PDVleEU7dqybbGX4S&export=download
    paper_url: https://www.acsac.org/2017/program-files/s115.html
-   title: 'Quasar: Quantitative Attack Space Analysis And Reasoning'
    badges: functional
    artifact_url: https://drive.google.com/open?id=1aLmAwEXR1g3hAJeQwThn6JDpOI6Ff_u_
    paper_url: https://www.acsac.org/2017/program-files/s225.html
-   title: Secure And Efficient Software-based Attestation For Industrial Control Devices With Arm Processors
    badges: functional
    artifact_url: http://www.illinois.adsc.com.sg/attestation/Attestation-ADSC-Release-2017.zip
    paper_url: https://www.acsac.org/2017/program-files/s175.html
-   title: 'Spinner: Semi-automatic Detection Of Pinning Without Hostname Verification (or Why 10m Bank Users Were Vulnerable)'
    badges: functional
    artifact_url: https://github.com/ChrisMcMStone/spinner
    paper_url: https://www.acsac.org/2017/program-files/s206.html
-   title: Supplementing Modern Software Defenses With Stack-pointer Sanity
    badges: functional
    artifact_url: https://github.com/bingseclab/spiglass
    paper_url: https://www.acsac.org/2017/program-files/s274.html
-   title: 'Vulcan: Efficient Component Authentication And Software Isolation For Automotive Control Networks'
    badges: functional
    artifact_url: https://distrinet.cs.kuleuven.be/software/vulcan/ https://github.com/sancus-pma/vulcan/
    paper_url: https://www.acsac.org/2017/program-files/s183.html
---

Results automatically obtained from <a href="https://www.acsac.org/2017/artifacts/">ACSAC website</a>.

**Evaluation Results**:

* 12 Artifacts Functional

<table>
  <thead>
    <tr>
      <th>
        Title
      </th>
      <th>
        Funct.
      </th>
      <th>
        Available At
      </th>
    </tr>
  </thead>
  <tbody>
    {% for artifact in page.artifacts %}
    <tr>
      <td>
        {% if artifact.paper_url %}
        <a href="{{artifact.paper_url}}" target="_blank">
          {{artifact.title}}
        </a>
        {% else %}
            {{ artifact.title }}
        {% endif %}
      </td>
      <td width="62px">
        {% if artifact.badges contains "functional" %}
        <img alt="{{ page.functional_name }}" src="{{ site.baseurl }}/images/{{ page.functional_img }}">
        {% endif %}
      </td>
      <td>
        {% if artifact.artifact_url %}
            {% assign artifacts = artifact.artifact_url | split: " " %}
            {% for url in artifacts %}
        <a href="{{url}}" target="_blank">
          Artifact
        </a>
        <br>
        {% endfor %}
        {% endif %}
        {% if artifact.appendix_url %}
        <a href="{{artifact.appendix_url}}" target="_blank">
          Appendix
        </a>
        <br>
        {% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
