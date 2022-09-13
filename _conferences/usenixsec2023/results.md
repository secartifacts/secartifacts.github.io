---
title: Results
order: 70
available_img: "acm_available_1.1.png"
available_name: "Artifacts Available (v1.1)"
functional_img: "acm_functional_1.1.png"
functional_name: "Artifacts Evaluated - Functional (v1.1)"
reproduced_img: "acm_reproduced_1.1.png"
reproduced_name: "Results Reproduced (v1.1)"

artifacts:

# - title: "OS Scheduling with Nest: Keeping Tasks Close Together on Warm Cores"
#    badges: "available,functional,reproduced"
#    paper_url: "10.1145/3492321.3519585"
#    artifact_url: "10.5281/zenodo.6344960"
#    repository_url: "https://gitlab.inria.fr/nest-public/nest-artifact"
#    summary: "nest"


# Example text for section below
#**Submissions**: 33 out of 45 (73% of accepted papers)

#**Evaluation Results**:

#* 33 Artifact Available
#* 27 Artifact Functional
#* 20 Results Reproduced


---

Results are published after each artifact submission cycle.


<table>
  <thead>
    <tr>
      <th>Paper title</th>
      <th>Avail.</th>
      <th>Funct.</th>
      <th>Repro.</th>
      <th>Available At</th>
      <!--<th>Review Summary</th>-->
    </tr>
  </thead>
  <tbody>
  {% for artifact in page.artifacts %}
    <tr>
      <td>
        {% if artifact.paper_url %}
          <a href="https://doi.org/{{artifact.paper_url}}" target="_blank">{{artifact.title}}</a>
        {% else %}
          {{ artifact.title }}
        {% endif %}
      </td>
      <td width="62px">
        {% if artifact.badges contains "available" %}
          <img src="{{ site.baseurl }}/images/{{ page.available_img }}" alt="{{ page.available_name }}" width="50px">
        {% endif %}
      </td>
      <td width="62px">
        {% if artifact.badges contains "functional" %}
          <img src="{{ site.baseurl }}/images/{{ page.functional_img }}" alt="{{ page.functional_name }}" width="50px">
        {% endif %}
      </td>
      <td width="62px">
        {% if artifact.badges contains "reproduced" %}
          <img src="{{ site.baseurl }}/images/{{ page.reproduced_img }}" alt="{{ page.reproduced_name }}" width="50px">
        {% endif %}
      </td>
      <td>
        {% if artifact.award %}
          <b>{{ artifact.award }}</b><br>
        {% endif %} {% if artifact.artifact_url %}
          <a href="https://doi.org/{{artifact.artifact_url}}" target="_blank">Artifact</a><br>
        {% endif %} {% if artifact.repository_url %}
          <a href="{{artifact.repository_url}}" target="_blank">Repository</a><br>
        {% endif %}
      </td>
      <td>
        {% if artifact.summary %}
          <a href="summaries/{{ artifact.summary }}.html">Summary</a>
        {% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
