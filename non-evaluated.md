---
title: Non-evaluated Artifacts
permalink: /non-evaluated/
---

Artifacts automatically discovered by [ArtiFinder](https://github.com/DistriNet/ArtiFinder) that were not submitted to formal artifact evaluation.
Results are not manually verified — pull requests with corrections are welcome.

<style>
.af-toc { display: flex; flex-wrap: wrap; gap: 1.5rem 2.5rem; margin: 1.5rem 0 2rem; padding: 1rem 1.25rem; background: #f8f8f8; border-radius: 6px; }
.af-toc-col { min-width: 7rem; }
.af-toc-col strong a { font-size: 1rem; }
.af-toc-col ul { list-style: none; margin: 0.3rem 0 0; padding: 0; }
.af-toc-col li { line-height: 1.7; font-size: 0.9rem; }
.af-count { color: #888; font-size: 0.82em; margin-left: 0.25rem; }
</style>

<div class="af-toc">
{% for conf in site.data.artifinder_artifacts %}
  {% assign conf_total = 0 %}
  {% for year_data in conf[1] %}
    {% assign conf_total = conf_total | plus: year_data[1].size %}
  {% endfor %}
  <div class="af-toc-col">
    <strong><a href="#{{ conf[0] }}">{{ conf[0] | upcase }}</a></strong><span class="af-count">({{ conf_total }})</span>
    <ul>
    {% for year_data in conf[1] %}
      <li><a href="#{{ conf[0] }}-{{ year_data[0] }}">{{ year_data[0] }}</a><span class="af-count">{{ year_data[1].size }}</span></li>
    {% endfor %}
    </ul>
  </div>
{% endfor %}
</div>

{% for conf in site.data.artifinder_artifacts %}
<h2 id="{{ conf[0] }}">{{ conf[0] | upcase }}</h2>

{% for year_data in conf[1] %}
<h3 id="{{ conf[0] }}-{{ year_data[0] }}">{{ year_data[0] }} <span class="af-count">({{ year_data[1].size }})</span></h3>

| Paper | Artifact |
|-------|----------|
{% for a in year_data[1] -%}
| [{{ a.title }}]({{ a.page_link }}) | <{{ a.artifact }}> |
{% endfor %}

{% endfor %}
{% endfor %}
