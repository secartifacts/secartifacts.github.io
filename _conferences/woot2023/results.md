---
title: Results
order: 20
artifacts:

  - title: "CustomProcessingUnit: Reverse Engineering and Customization of Intel Microcode"
    badges: "ORO"
    artifact_url: "https://doi.org/10.5281/zenodo.7728760"
    paper_url: "https://wootconference.org/papers/woot23-paper7.pdf"
  
  - title: "Hakuin: Optimizing Blind SQL Injection with Probabilistic Language Models"
    badges: "ORO, ROR"
    artifact_url: "https://zenodo.org/record/7804243"
    paper_url: "https://wootconference.org/papers/woot23-paper17.pdf"
  
  - title: "Emoji shellcoding in RISC-V"
    badges: "ORO, ROR"
    artifact_url: "https://zenodo.org/record/7733387"
    paper_url: "https://wootconference.org/papers/woot23-paper5.pdf"
  
  - title: "ROPfuscator: Robust Obfuscation with ROP"
    badges: "ORO"
    artifact_url: "https://zenodo.org/record/7749186"
    paper_url: "https://wootconference.org/papers/woot23-paper4.pdf"
  
  - title: "The ghost is the machine: weird machines in transient execution"
    badges: "ORO, ROR"
    artifact_url: "https://doi.org/10.5281/zenodo.7793427"
    paper_url: "https://wootconference.org/papers/woot23-paper10.pdf"
  
  - title: "Divergent Representations: When Compiler Optimizations Enable Exploitation"
    badges: "ORO, ROR"
    artifact_url: "https://github.com/wunused/divergent-representations-artifacts"
    paper_url: "https://wootconference.org/papers/woot23-paper6.pdf"
  
  - title: "Reflections on Trusting Docker: Invisible Malware in Continuous Integration Systems"
    badges: "ORO, ROR"
    artifact_url: "https://doi.org/10.5281/zenodo.7777331"
    paper_url: "https://wootconference.org/papers/woot23-paper15.pdf"
  
  - title: "ASanity: On Bug Shadowing by Early ASan Exits"
    badges: "ORO, ROR"
    artifact_url: "https://zenodo.org/record/7808197"
    paper_url: "https://wootconference.org/papers/woot23-paper34.pdf"
  
  - title: "ESPwn32: Hacking with ESP32 System-on-Chips"
    badges: "ORO, ROR"
    artifact_url: "https://doi.org/10.5281/zenodo.7786224"
    paper_url: "https://wootconference.org/papers/woot23-paper22.pdf"

---

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>ORO</th>
      <th>ROR</th>
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
        {% if artifact.badges contains "ORO" %}
          <img src="{{ site.baseurl }}/images/open_research-oro.png" alt="{{ page.badges }}" width="50px">
        {% endif %}
      </td><td>
        {% if artifact.badges contains "ROR" %}
          <img src="{{ site.baseurl }}/images/research-objects-reviewed-ror.png" alt="{{ page.badges }}" width="50px">
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
