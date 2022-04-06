---
title: Results
order: 20
artifacts:

  - title:: "RISC-V: #AlphanumericShellcoding"
  badges: "Artifact Evaluated"
  artifact_url: "https://github.com/RischardV/riscv-alphanumeric-shellcoding"
  paper_url: "https://www.usenix.org/system/files/woot19-paper_barral.pdf"

  - title: "A better zip bomb"
    badges: "Artifact Evaluated"
    paper_url: "https://www.usenix.org/system/files/woot19-paper_fifield_0.pdf"

  - title: "Automatic Wireless Protocol Reverse Engineering"
    badges: "Artifact Evaluated"
    artifact_url: "https://github.com/jopohl/urh/releases/tag/v2.7.3"
    paper_url: "https://www.usenix.org/system/files/woot19-paper_pohl.pdf"

  - title:: "D-TIME: Distributed Threadless Independent Malware Execution for Runtime Obfuscation"
    badges: "Artifact Evaluated"
    artifact_url: "https://github.com/JithinPavithran/d-time"
    paper_url: "https://www.usenix.org/system/files/woot19-paper_pavithran.pdf"

  - title:: "Unicorefuzz: On the Viability of Emulation for Kernelspace Fuzzing"
    badges: "Artifact Evaluated"
    artifact_url: "https://github.com/fgsect/unicorefuzz"
    paper_url: "https://www.usenix.org/system/files/woot19-paper_maier.pdf"

  - title: "Distributed Password Hash Computation on Commodity Heterogeneous Programmable Platforms"
    badges: "Artifact Evaluated"
    paper_url: "https://www.usenix.org/system/files/woot19-paper_pervan.pdf"

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
