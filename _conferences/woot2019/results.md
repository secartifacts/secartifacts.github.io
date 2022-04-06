---
title: Results
order: 20
artifacts:

  - title: "RISC-V: #AlphanumericShellcoding"
    paper_url: "https://www.usenix.org/conference/woot19/presentation/barral"
    artifact_url: "#"
    badges: "Artifact Evaluated"

  - title: "Unicorefuzz: On the Viability of Emulation for Kernelspace Fuzzing"
    paper_url: "https://www.usenix.org/conference/woot19/presentation/maier"
    artifact_url: "#"
    badges: "Artifact Evaluated"

---

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Artifact URL</th>
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
      <td>
        {% if artifact.badges contains "Artifact Evaluated" %}
          <img src="https://www.usenix.org/sites/default/files/usenix_artifact_evaluation_passed_125.png" alt="{{ page.badges }}" width="50px">
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
