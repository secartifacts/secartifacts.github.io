---
title: Results
order: 40
custom_css: pets-badges
artifacts:

  - title: ""
    paper_url: ""
    artifact_url: ""
    badges: "available"

  - title: ""
    paper_url: ""
    artifact_url: ""
    badges: "available,functional"

  - title: ""
    paper_url: ""
    artifact_url: ""
    badges: "available,functional,reproduced"

---

Results automatically obtained from <a href="https://petsymposium.org/2025/paperlist.php">PETS 2025 website</a>.

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th width="350px">Artifact URL</th>
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
      {% if artifact.artifact_url %}
        {% if artifact.badges == "available" %}
          <a class="pets-artifact-badge" href="{{artifact.artifact_url}}">Artifact: Available</a>
        {% elsif artifact.badges == "available,functional" %}
          <a class="pets-artifact-badge" href="{{artifact.artifact_url}}">Artifact: Available, Functional</a>
        {% elsif artifact.badges == "available,functional,reproduced" %}
          <a class="pets-artifact-badge" href="{{artifact.artifact_url}}">Artifact: Available, Functional, Reproduced</a>
        {% endif %}
      {% endif %}
      </td>
    </tr>
  {% endfor %}
  </tbody>
</table>

