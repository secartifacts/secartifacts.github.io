---
title: Results
order: 20
artifacts:

  - title: "Compact Dilithium Implementations on Cortex-M3 and Cortex-M4"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a1/"

  - title: "Fill your Boots: Enhanced Embedded Bootloader Exploits via Fault Injection and Binary Analysis"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a2/"

  - title: "The design of scalar AES Instruction Set Extensions for RISC-V"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a3/"

  - title: "Polynomial Multiplication in NTRU Prime: Comparison of Optimization Strategies on Cortex-M4"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a4/"

  - title: "The Area-Latency Symbiosis: Towards Improved Serial Encryption Circuits"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a5/"

  - title: "Fixslicing AES-like ciphers: New bitsliced AES speed records on ARM-Cortex M and RISC-V"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a6/"

  - title: "NTT Multiplication for NTT-unfriendly Rings: New Speed Records for Saber and NTRU on Cortex-M4 and AVX2"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a7/"

  - title: "Masking in Fine-Grained Leakage Models: Construction, Implementation and Verification"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a8/"

  - title: "MFault Attacks on CCA-secure Lattice KEMs"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a9/"

  - title: "Time-Memory Analysis of Parallel Collision Search Algorithms"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a10/"

  - title: "Online Template Attacks: Revisited: PoC: emulated single-trace attack on wolfSSL scalar multiplication"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a11/"

  - title: "Optimizing BIKE for the Intel Haswell and ARM Cortex-M4"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a12/"

  - title: "Breaking Masked Implementations with Many Shares on 32-bit Software Platforms: or When the Security Order Does Not Matter"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a13/"

  - title: "Breaking CAS-Lock and Its Variants by Exploiting Structural Traces"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a14/"

  - title: "ROTed: Random Oblivious Transfer for embedded devices"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a15/"

  - title: "FIVER – Robust Veriﬁcation of Countermeasures against Fault Injections"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a16/"

  - title: "Side-Channel Protections for Picnic Signatures"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a17/"

  - title: "Rainbow on Cortex-M4"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a18/"

  - title: "Higher-Order Lookup Table Masking in Essentially Constant Memory"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a19/"

  - title: "CTIDH: faster constant-time CSIDH"
    artifact_url: "https://artifacts.iacr.org/tches/2021/a20/"

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
