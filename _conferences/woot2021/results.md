---
title: Results
order: 20
artifacts:

  - title: "An In-memory Embedding of CPython for Offensive Use"
    badges: "ORO, ROR-R"
    artifact_url: "https://zenodo.org/record/4638251"
    paper_url: "https://www.ieee-security.org/TC/SP2021/SPW2021/WOOT21/files/woot21-sharfuddin-slides.pdf"

  - title: "Your Censor is My Censor: Weaponizing Censorship Infrastructure for Availability Attacks"
    badges: "ORO, ROR-R"
    artifact_url: "https://zenodo.org/record/4774692"
    paper_url: "https://www.ieee-security.org/TC/SP2021/SPW2021/WOOT21/files/woot21-bock-slides.pdf"

  - title: "Evaluation of the Executional Power in Windows using Return Oriented Programming"
    badges: "ORO, ROR-R"
    artifact_url: "https://github.com/reverseame/rop3"
    paper_url: "https://www.ieee-security.org/TC/SP2021/SPW2021/WOOT21/files/woot21-rodriguez-slides.pdf"

  - title: "undeSErVed trust"
    badges: "ORO, ROR-R"
    artifact_url: "https://zenodo.org/record/4635706"
    paper_url: "https://www.ieee-security.org/TC/SP2021/SPW2021/WOOT21/files/woot21-wilke-slides.pdf"

---

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>ORO</th>
      <th>ROR-R</th>
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
        {% if artifact.badges contains "ROR-R" %}
          <img src="{{ site.baseurl }}/images/results_reproduced-ror-r.png" alt="{{ page.badges }}" width="50px">
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
