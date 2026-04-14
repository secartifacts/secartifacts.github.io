---
title: Results
order: 30
artifacts:
  - title: "Epsilon: A Bring-Your-Own-Data Research Platform with Trusted Verification"
    artifact_url: https://github.com/Epsilon-Data/epsilon
    badges: "Available, Reusable"
  - title: "StepOverflow: PMC Overflows on AMD SEV"
    artifact_url: https://github.com/UzL-ITS/StepOverflow
    badges: "Available, Reusable"
  - title: "CACTEE: Confidential Asset Certification using Trusted Execution Environments"
    artifact_url: https://github.com/Nokia-Bell-Labs/confidential-asset-certification-using-tees
    badges: "Available, Reusable"
  - title: "AI Agents Need Both Hardware-Backed Security and Application-Level Guardrails"
    artifact_url: https://codeberg.org/BarryShichenHu/Secure_AI_Agent/src/tag/artifact-evaluation
    badges: "Available, Reusable"
  - title: "Control-Flow Balancing for Texas Instruments IPE"
    artifact_url: https://github.com/martonbognar/ipe-balancing
    badges: "Available, Reusable"
  - title: "Breaking Isolation: Last-level Cache Side-Channel Attacks on AWS Nitro Enclaves"
    artifact_url: https://codeberg.org/monder/LLCEnclave.git
    badges: "Available, Reusable"
  - title: "Optimizing Launch Latency for Confidential VMs with Device Passthrough in the Linux KVM Hypervisor"
    artifact_url: https://github.com/ntu-ssl/start-up-optimization
    badges: "Available, Functional"
  - title: "Keystone with Linux PREEMPT_RT: Real-Time Enclaves on RISC-V?"
    artifact_url: https://github.com/ReSP-Lab/2026-systex-keystone-rt-linux/tree/artifact-submission-version
    badges: "Available, Reusable"

---

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Badges</th>
      <th>Repository</th>
    </tr>
  </thead>
  <tbody>
  {% for artifact in page.artifacts %}
    <tr>
      <td>
        {% if artifact.paper_url %}
          <a href="{{artifact.paper_url}}">{{artifact.title}}</a>
        {% else %}
          {{ artifact.title }}
        {% endif %}
      </td>
      <td width="120px" style="display: flex; gap: 8px;">
        {% if artifact.badges contains "Available" %}
          <a href="https://www.acm.org/publications/policies/artifact-review-and-badging-current"><img src="{{ site.baseurl }}/images/acmartifactbadge_available.png" style="width: 50px;" alt="Artifacts Evaluated: Available"></a>
        {% endif %}
        {% if artifact.badges contains "Functional" %}
          <a href="https://www.acm.org/publications/policies/artifact-review-and-badging-current"><img src="{{ site.baseurl }}/images/acmartifactbadge_functional.png" style="width: 50px;" alt="Artifacts Evaluated: Functional"></a>
        {% endif %}
        {% if artifact.badges contains "Reusable" %}
          <a href="https://www.acm.org/publications/policies/artifact-review-and-badging-current"><img src="{{ site.baseurl }}/images/acmartifactbadge_reusable.png" style="width: 50px;" alt="Artifacts Evaluated: Reusable"></a>
        {% endif %}
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
