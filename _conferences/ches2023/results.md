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
        artifact_url: https://artifacts.iacr.org/tches/2023/a8/
      - title: "\"Whispering MLaaS\" – Exploiting Timing Channels to Compromise User Privacy in Deep Neural Networks"
        artifact_url: https://artifacts.iacr.org/tches/2023/a9/
  - name: Issue 3
    artifacts:
      - title: "Kavach: Lightweight masking techniques for polynomial arithmetic in lattice-based cryptography"
        artifact_url: https://artifacts.iacr.org/tches/2023/a10/
      - title: "Oil and Vinegar: Modern Parameters and Implementations"
        artifact_url: https://artifacts.iacr.org/tches/2023/a11/
      - title: "Formally verifying Kyber – Episode IV: Implementation correctness"
        artifact_url: https://artifacts.iacr.org/tches/2023/a12/
      - title: "Pasta: A Case for Hybrid Homomorphic Encryption"
        artifact_url: https://artifacts.iacr.org/tches/2023/a13/
      - title: Carry-based Differential Power Analysis (CDPA) and its Application to Attacking HMAC-SHA-2
        artifact_url: https://artifacts.iacr.org/tches/2023/a14/
      - title: Separating Oil and Vinegar with a Single Trace – Side-Channel Assisted Kipnis-Shamir Attack on UOV
        artifact_url: https://artifacts.iacr.org/tches/2023/a15/
      - title: Faster Montgomery multiplication and Multi-Scalar-Multiplication for SNARKs
        artifact_url: https://artifacts.iacr.org/tches/2023/a16/
      - title: PROLEAD_SW – Probing-Based Software Leakage Detection for ARM Binaries
        artifact_url: https://artifacts.iacr.org/tches/2023/a17/
      - title: Efficient Regression-Based Linear Discriminant Analysis for Side-Channel Security Evaluations – Towards Analytical Attacks against 32-bit Implementations
        artifact_url: https://artifacts.iacr.org/tches/2023/a18/
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
