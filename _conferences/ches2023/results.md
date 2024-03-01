---
title: Results
order: 20
issues:
  - name: Issue 1
    artifacts:
      - title: A Faster Third-Order Masking of Lookup Tables
        artifact_url: https://artifacts.iacr.org/tches/2023/a1/
      - title: "MCRank: Monte Carlo Key Rank Estimation for Side-Channel Security Evaluations"
        artifact_url: https://artifacts.iacr.org/tches/2023/a2/
      - title: "SoK: SCA-secure ECC in software – mission impossible?"
        artifact_url: https://artifacts.iacr.org/tches/2023/a4/
  - name: Issue 2
    artifacts:
      - title: On Protecting SPHINCS+ Against Fault Attacks
        artifact_url: https://artifacts.iacr.org/tches/2023/a5/
      - title: "RDS: FPGA Routing Delay Sensors for Effective Remote Power Analysis Attacks"
        artifact_url: https://artifacts.iacr.org/tches/2023/a6/
      - title: "A Closer Look at the Chaotic Ring Oscillators based TRNG Design"
        artifact_url: https://artifacts.iacr.org/tches/2023/a7/
      - title: "\"Whispering MLaaS\" – Exploiting Timing Channels to Compromise User Privacy in Deep Neural Networks"
        artifact_url: https://artifacts.iacr.org/tches/2023/a8/
---

{% for issue in page.issues %}
  <h2>{{ issue.name }}</h2>

  <table>
    <thead>
      <tr>
        <th>Title</th>
        <th>Artifact</th>
      </tr>
    </thead>
    <tbody>
    {% for artifact in issue.artifacts %}
      <tr>
        <td>
          {{ artifact.title }}
        </td>
        <td>
          {% if artifact.artifact_url %}
            <a href="{{artifact.artifact_url}}">Artifact</a>
          {% endif %}
        </td>
      </tr>
    {% endfor %}
    </tbody>
</table>
{% endfor %}
