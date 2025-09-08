---
title: Results
order: 20
artifacts:
 - title: Practical Multiple Persistent Faults Analysis
   artifact_url: https://artifacts.iacr.org/tches/2022/a1/
   issue: 1
 - title: "Neon NTT: Faster Dilithium, Kyber, and Saber on Cortex-A72 and Apple M1"
   artifact_url: https://artifacts.iacr.org/tches/2022/a2/
   issue: 1
 - title: Multi-moduli NTTs for Saber on Cortex-M3 and Cortex-M4
   artifact_url: https://artifacts.iacr.org/tches/2022/a3/
   issue: 1
 - title: "Racing BIKE: Improved Polynomial Multiplication and Inversion in
     Hardware"
   artifact_url: https://artifacts.iacr.org/tches/2022/a4/
   issue: 1
 - title: "VITI: A Tiny Self-Calibrating Sensor for Power-Variation Measurement in
     FPGAs"
   artifact_url: https://artifacts.iacr.org/tches/2022/a5/
   issue: 1
 - title: Quantum Period Finding against Symmetric Primitives in Practice
   artifact_url: https://artifacts.iacr.org/tches/2022/a6/
   issue: 1
 - title: "Curse of Re-encryption: A Generic Power/EM Analysis on Post-Quantum
     KEMs"
   artifact_url: https://artifacts.iacr.org/tches/2022/a7/
   issue: 1
 - title: Semi-Automatic Locating of Cryptographic Operations in Side-Channel
     Traces
   artifact_url: https://artifacts.iacr.org/tches/2022/a8/
   issue: 1
 - title: "Will You Cross the Threshold for Me? - Generic Side-Channel Assisted
     Chosen-Ciphertext Attacks on NTRU-based KEMs"
   artifact_url: https://artifacts.iacr.org/tches/2022/a9/
   issue: 1
 - title: "Side Channel Attack On Stream Ciphers: A Three-Step Approach To
     State/Key Recovery"
   artifact_url: https://artifacts.iacr.org/tches/2022/a10/
   issue: 2
 - title: "BreakMi: Reversing, Exploiting, and Fixing Xiaomi Fitness Tracking
     Ecosystem"
   artifact_url: https://artifacts.iacr.org/tches/2022/a11/
   issue: 3
 - title: "Don’t Reject This: Key-Recovery Timing Attacks Due to Rejection-Sampling
     in HQC and BIKE"
   artifact_url: https://artifacts.iacr.org/tches/2022/a12/
   issue: 3
 - title: A Security Model for Randomization-based Protected Caches
   artifact_url: https://artifacts.iacr.org/tches/2022/a13/
   issue: 3
 - title: "On Efficient and Secure Code-based Masking: A Pragmatic Evaluation"
   artifact_url: https://artifacts.iacr.org/tches/2022/a14/
   issue: 3
 - title: VERICA - Verification of Combined Attacks
   artifact_url: https://artifacts.iacr.org/tches/2022/a15/
   issue: 4
 - title: Improved Plantard Arithmetic for Lattice-based Cryptography
   artifact_url: https://artifacts.iacr.org/tches/2022/a16/
   issue: 4
 - title: A Power to Pulse Width Modulation Sensor for Remote Power Analysis
     Attacks
   artifact_url: https://artifacts.iacr.org/tches/2022/a17/
   issue: 4
 - title: Breaking Masked Implementations of the Clyde-Cipher by Means of
     Side-Channel Analysis
   artifact_url: https://artifacts.iacr.org/tches/2022/a18/
   issue: 4
 - title: PROLEAD - A Probing-Based Hardware Leakage Detection Tool
   artifact_url: https://artifacts.iacr.org/tches/2022/a19/
   issue: 4
 - title: "Verified NTT Multiplications for NISTPQC KEM Lattice Finalists: Kyber,
     Saber, and NTRU"
   artifact_url: https://artifacts.iacr.org/tches/2022/a20/
   issue: 4
 - title: Multi-Parameter Support with NTTs for NTRU and NTRU Prime on Cortex-M4
   artifact_url: https://artifacts.iacr.org/tches/2022/a21/
   issue: 4
 - title: Faster constant-time decoder for MDPC codes and applications to BIKE KEM
   artifact_url: https://artifacts.iacr.org/tches/2022/a22/
   issue: 4
 - title: "Roulette: A Diverse Family of Feasible Fault Attacks on Masked Kyber"
   artifact_url: https://artifacts.iacr.org/tches/2022/a23/
   issue: 4
 - title: "A Fast Large-Integer Extended GCD Algorithm and Hardware Design for
     Verifiable Delay Functions and Modular Inversion"
   artifact_url: https://artifacts.iacr.org/tches/2022/a24/
   issue: 4
 - title: SoC Root Canal!
   artifact_url: https://artifacts.iacr.org/tches/2022/a25/
   issue: 4
---

{% assign issue = 0 %}
{% for artifact in page.artifacts %}
  {% if issue != artifact.issue %}
  	{% if issue != 0 %}
  </tbody>
</table>
  	{% endif %}
  	{% assign issue = artifact.issue %}
<h2>Issue {{ issue }}</h2>
<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Artifact</th>
    </tr>
  </thead>
  <tbody>
  {% endif %}
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
  {% if forloop.last %}
  </tbody>
</table>
  {% endif %}
{% endfor %}
