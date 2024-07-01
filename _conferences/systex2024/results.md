---
title: Results
order: 20

artifacts:

-   title: 'Delegating Verification for Remote Attestation using TEE'
    badges: 'Artifacts Available + Functional'
    artifact_url: https://github.com/hatena75/ProxyVerifier_QVS/tree/49fbc48af05806f9cea76bd0f56fc40ce729bad0

-   title: 'duet: Combining a Trustworthy Controller with a Confidential Computing Environment'
    badges: 'Artifacts Available + Functional + Reusable'
    artifact_url: https://github.com/Nokia-Bell-Labs/tee-duet/tree/9eb44fe5e1b60519656b93630b9f5cbf5a111861

-   title: 'NetReach: Guaranteed Network Availability and Reachability to enable Resilient Networks for  Embedded Systems'
    badges: 'Artifacts Available + Functional'
    artifact_url: https://gitlab.com/distrinet-netreach/documentation/-/tree/systex-2024

-   title: 'PraaS: Verifiable Proofs of Property as-a-Service with Intel SGX'
    badges: 'Artifacts Available + Functional + Reusable'
    artifact_url: https://github.com/Nokia-Bell-Labs/proof-as-a-service/tree/1e24dce47fd468e56ebc3ad2b55c093c412b866d

-   title: 'Revisiting Rollbacks on Smart Contracts in TEE-protected Private Blockchains'
    badges: 'Artifacts Available'
    artifact_url: https://github.com/chenchanglew/systex2024/tree/2bd229b4d4c4e6be9648c411aa8e4d744eff3524

-   title: 'Secure Intermittent Computing with ARM TrustZone on the Cortex-M'
    badges: 'Artifacts Available + Functional'
    artifact_url: https://github.com/ptrchv/STM32-IntermittentSecurity/tree/systex2024_submission

-   title: 'SNPGuard: Remote Attestation of SEV-SNP VMs Using Open Source Tools'
    badges: 'Artifacts Available + Functional + Reusable'
    artifact_url: https://github.com/SNPGuard/snp-guard/tree/v0.1.3


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
      <td width="250px">
        {% if artifact.badges contains "Available" %}
          <img src="{{ site.baseurl }}/images/systexbadges-available.svg" alt="Artifacts Evaluated: Available">
        {% endif %}
        {% if artifact.badges contains "Functional" %}
          <img src="{{ site.baseurl }}/images/systexbadges-functional.svg" alt="Artifacts Evaluated: Functional">
        {% endif %}
        {% if artifact.badges contains "Reusable" %}
          <img src="{{ site.baseurl }}/images/systexbadges-reusable.svg" alt="Artifacts Evaluated: Reusable">
        {% endif %}
      </td>
      <td>
        {% if artifact.artifact_url %}
          {% if artifact.artifact_url contains "github" %}
            <i class="fab fa-github"></i>
          {% else %}
            {% if artifact.artifact_url contains "gitlab" %}
              <i class="fab fa-gitlab"></i>
            {% endif %}
          {% endif %}
          <a href="{{artifact.artifact_url}}">Artifact</a>
        {% endif %}
      </td>
    </tr>
  {% endfor %}
  </tbody>
</table>
