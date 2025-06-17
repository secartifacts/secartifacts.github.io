---
title: Results
order: 30

artifacts:

-   title: 'An Early Experience with Confidential Computing Architecture for On-Device Model Protection'
    badges: 'Artifacts Available + Functional + Reusable'
    artifact_url: https://github.com/comet-cc/CCA-Evaluation/tree/SysTEX25

-   title: 'Enclave Application Cache for RISC-V Keystone'
    badges: 'Artifacts Available + Functional + Reusable'
    artifact_url: https://github.com/Nanamiiiii/keystone-ecache/tree/systex-2025

-   title: 'End-to-End Confidentiality with SEV-SNP Leveraging In-Memory Storage'
    badges: 'Artifacts Available + Functional + Reusable'
    artifact_url: https://github.com/lorenzobrescia/snp-guard-in-memory-storage/tree/v1.0.0

-   title: 'Principled Symbolic Validation of Enclaves on Low-End Microcontrollers'
    badges: 'Artifacts Available + Functional + Reusable'
    artifact_url: https://github.com/pandora-tee/pandora-examples/tree/systex25-artifact/sancus

-   title: 'Wait a Cycle: Eroding Cryptographic Trust in Low-End TEEs via Timing Side Channels'
    badges: 'Artifacts Available + Functional + Reusable'
    artifact_url: https://github.com/dnet-tee/wait-a-cycle/tree/systex25-artifacts

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
