---
title: Results
order: 20
artifacts:

  - title: "Practical Multiple Persistent Faults Analysis"
    artifact_url: "https://artifacts.iacr.org/tches/2022/a1/"

  - title: "Neon NTT: Faster Dilithium, Kyber, and Saber on Cortex-A72 and Apple M1"
    artifact_url: "https://artifacts.iacr.org/tches/2022/a2/"

  - title: "Multi-moduli NTTs for Saber on Cortex-M3 and Cortex-M4"
    artifact_url: "https://artifacts.iacr.org/tches/2022/a3/"

  - title: "Racing BIKE: Improved Polynomial Multiplication and Inversion in Hardware"
    artifact_url: "https://artifacts.iacr.org/tches/2022/a4/"

  - title: "VITI: A Tiny Self-Calibrating Sensor for Power-Variation Measurement in FPGAs"
    artifact_url: "https://artifacts.iacr.org/tches/2022/a5/"

  - title: "Quantum Period Finding against Symmetric Primitives in Practice"
    artifact_url: "https://artifacts.iacr.org/tches/2022/a6/"

  - title: "Curse of Re-encryption: A Generic Power/EM Analysis on Post-Quantum KEMs"
    artifact_url: "https://artifacts.iacr.org/tches/2022/a7/"

  - title: "Semi-Automatic Locating of Cryptographic Operations in Side-Channel Traces"
    artifact_url: "https://artifacts.iacr.org/tches/2022/a8/"

  - title: "Will You Cross the Threshold for Me? - Generic Side-Channel Assisted Chosen-Ciphertext Attacks on NTRU-based KEMs"
    artifact_url: "https://artifacts.iacr.org/tches/2022/a9/"

  - title: "Side Channel Attack On Stream Ciphers: A Three-Step Approach To State/Key Recovery"
    artifact_url: "https://artifacts.iacr.org/tches/2022/a10/"

---

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Artifact</th>
    </tr>
  </thead>
  <tbody>
  {% for artifact in page.artifacts %}
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
