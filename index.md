---
title: Security Research Artifacts
---

The goal of artifact evaluation (AE) is to recognize the authors who have put in the effort to release
usable hardware and software systems as well as to validate the results of the accepted papers.

This website collects resources and results around artifact evaluation for security conferences and workshops, as well as published [artifacts](#artifacts-without-evaluation) that did not go through a formal evaluation process.

## Conference Artifact Evaluations

{% for p in site.conferences %}
  {% assign depth = p.path | split:"/" | size %}
  {% if depth == 2 %}

  {% assign conf_base_path = p.path | remove:p.ext %}
  {% assign years = site.conferences | where_exp:"conf","conf.path contains p.slug" | where_exp:"conf","conf != p" | group_by_exp:"conf","conf.path | remove:conf.slug | remove:conf.ext" | sort:"name" | reverse %}

**{{ p.title }}**:
{% for year in years %}
  {%- assign year_depth = year.name | split:"/" | size -%}
  {%- if year_depth == 2 -%}
  {%- assign year_number = year.name | remove:conf_base_path | remove:"/" -%}
    [{{ year_number }}]({{ conf_base_path | remove:"_conferences" | append:year_number | relative_url }})&nbsp;
  {%- endif -%}
{% endfor %}

  {% endif %}
{% endfor %}

## Artifacts without evaluation

While artifact evaluation is becoming more and more widespread, there are many papers that release artifacts without going through a formal evaluation process.
To increase the discoverability of these artifacts, the [ArtiFinder](https://github.com/DistriNet/ArtiFinder) tool was developed to automatically collect artifact URLs from papers.
A [dedicated page](artifinder) list these automatically extracted artifacts.
As these results were not manually verified, mistakes are possible, for which pull requests to the [dataset repository](https://github.com/DistriNet/ArtiFinder-Data) are very welcome.
Currently, ArtiFinder was used to collect artifacts from A* conferences from the years 2000--2025 and ACSAC between 2017--2025.
