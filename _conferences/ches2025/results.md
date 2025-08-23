---
title: Results
order: 20
issues:
  - name: Issue 1
    artifacts:
      - title: Multiplying Polynomials without Powerful Multiplication Instructions
        artifact_url: https://artifacts.iacr.org/tches/tches/2025/a1/
        badge:
        - functional
      - title: 'TraceCopilot: A framwork for integrating binary firmware and side-channel
          information of embedded cryptographic device'
        artifact_url: https://artifacts.iacr.org/tches/tches/2025/a2/
        badge:
        - available
      - title: 'Dash: Accelerating Distributed Private Convolutional Neural Network Inference
          with Arithmetic Garbled Circuits'
        artifact_url: https://artifacts.iacr.org/tches/tches/2025/a3/
        badge:
        - functional
      - title: Optimized Software Implementation of Keccak, Kyber, and Dilithium on RV{32,64}IM{B}{V}
        artifact_url: https://artifacts.iacr.org/tches/tches/2025/a4/
        badge:
        - functional
      - title: 'FANNG-MPC: Framework for Artificial Neural Networks and Generic MPC'
        artifact_url: https://artifacts.iacr.org/tches/tches/2025/a5/
        badge:
        - functional
      - title: Full Key-Recovery Cubic-Time Template Attack on Classic McEliece Decapsulation
        artifact_url: https://artifacts.iacr.org/tches/tches/2025/a6/
        badge:
        - functional
      - title: A Framework for Generating S-Box Circuits with Boyer-Peralta Algorithm-Based
          Heuristics, and Its Applications to AES, SNOW3G, and Saturnin
        artifact_url: https://artifacts.iacr.org/tches/tches/2025/a7/
        badge:
        - functional
      - title: 'Trojan Insertion versus Layout Defenses for Modern ICs: Red-versus-Blue
          Teaming in a Competitive Community Effort'
        artifact_url: https://artifacts.iacr.org/tches/tches/2025/a8/
        badge:
        - functional
      - title: 'PhaseSCA: Exploiting Phase-Modulated Emanations in Side Channels'
        artifact_url: https://artifacts.iacr.org/tches/tches/2025/a17/
        badge:
        - functional
  - name: Issue 2
    artifacts:
      - title: 'KyberSlash: Exploiting secret-dependent division timings in Kyber implementations'
        artifact_url: https://artifacts.iacr.org/tches/tches/2025/a9/
        badge:
        - functional
      - title: 'A TRAP for SAT: On the Imperviousness of a Transistor-Level Programmable
          Fabric to Satisfiability-Based Attacks'
        artifact_url: https://artifacts.iacr.org/tches/tches/2025/a10/
        badge:
        - functional
      - title: 'SimdMSM: SIMD-accelerated Multi-Scalar Multiplication Framework for zkSNARKs'
        artifact_url: https://artifacts.iacr.org/tches/tches/2025/a11/
        badge:
        - functional
      - title: Designing a General-Purpose 8-bit (T)FHE Processor Abstraction
        artifact_url: https://artifacts.iacr.org/tches/tches/2025/a12/
        badge:
        - functional
      - title: Constant time lattice reduction in dimension 4 with application to SQIsign
        artifact_url: https://artifacts.iacr.org/tches/tches/2025/a13/
        badge:
        - functional
      - title: 'CHERI-Crypt: Transparent Memory Encryption on Capability Architectures'
        artifact_url: https://artifacts.iacr.org/tches/tches/2025/a14/
        badge:
        - functional
      - title: Higher-Order Time Sharing Masking
        artifact_url: https://artifacts.iacr.org/tches/tches/2025/a15/
        badge:
        - functional
      - title: 'TFHE Gets Real: an Efficient and Flexible Homomorphic Floating-Point Arithmetic'
        artifact_url: https://artifacts.iacr.org/tches/tches/2025/a16/
        badge:
        - functional
  - name: Issue 3
    artifacts:
  - name: Issue 4
    artifacts:
---

{% for issue in page.issues %}
  <h2>{{ issue.name }}</h2>

  <table>
    <thead>
      <tr>
        <th>Title</th>
        <th>Artifact</th>
        <th>Badge</th>
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
        <td>
        {% for badge in artifact.badge %}
            {% if badge == "available" %}
                <span title="IACR CHES Artifacts Available">✅</span>
            {% elsif badge == "functional" %}
                <span title="IACR CHES Artifacts Functional">💡</span>
            {% elsif badge == "best" %}
                <span title="IACR CHES Best Artifact Award">🥇</span>
            {% endif %}
        {% endfor %}
        </td>
      </tr>
    {% endfor %}
    </tbody>
</table>
{% endfor %}
