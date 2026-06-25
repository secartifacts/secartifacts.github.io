---
title: Non-evaluated Artifacts
permalink: /non-evaluated/
---

Artifacts automatically discovered by [ArtiFinder](https://github.com/DistriNet/ArtiFinder) that were not submitted to formal artifact evaluation.
Results are not manually verified — pull requests with corrections are welcome.

<style>
.af-toc { margin: 1.5rem 0 2rem; padding: 0.75rem 1.25rem; background: #f8f8f8; border-radius: 6px; }
.af-toc-entry { margin: 0.6rem 0; }
.af-toc-entry:not(:last-child) { padding-bottom: 0.6rem; border-bottom: 1px solid #e0e0e0; }
.af-toc-heading { font-size: 0.95rem; margin: 0 0 0.2rem; }
.af-toc-years { font-size: 0.9rem; margin: 0; }
.af-count { color: #888; font-size: 0.82em; }
</style>

<div class="af-toc">
{% for conf in site.data.artifinder_artifacts %}
  {% assign conf_total = 0 %}
  {% for year_data in conf[1] %}
    {% assign conf_total = conf_total | plus: year_data[1].size %}
  {% endfor %}
  <div class="af-toc-entry">
    <p class="af-toc-heading"><strong><a href="#{{ conf[0] }}">{{ conf[0] | upcase }}</a></strong> <span class="af-count">({{ conf_total }})</span></p>
    <p class="af-toc-years">{% for year_data in conf[1] %}{% unless forloop.first %} &middot; {% endunless %}<a href="#{{ conf[0] }}-{{ year_data[0] }}">{{ year_data[0] }}</a> <span class="af-count">({{ year_data[1].size }})</span>{% endfor %}</p>
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
