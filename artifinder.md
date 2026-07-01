---
title: Non-evaluated artifacts
permalink: /artifinder/
---

Artifacts automatically discovered by [ArtiFinder](https://github.com/DistriNet/ArtiFinder) that were not submitted to formal artifact evaluation.
If you notice a mistake in the automatically extracted links or want to manually validate correct entries (marked with a <abbr title="This extracted link has been manually validated." class="af-validated">✓</abbr> in the dataset), please submit a [pull request](https://github.com/DistriNet/ArtiFinder-Data)!

In addition to these links, we also cross-checked the URLs submitted for artifact evaluation with those extracted from the papers.
When there is a mismatch, the URL reported in the paper is listed on the artifact evaluation outcome page under "Link in paper".
These can often point to project websites or actively maintained repositories instead of archived versions (or even expired temporary URLs).

<style>
.af-toc { margin: 1.5rem 0 2rem; padding: 0.75rem 1.25rem; background: #f8f8f8; border-radius: 6px; }
.af-toc-entry { margin: 0.6rem 0; }
.af-toc-entry:not(:last-child) { padding-bottom: 0.6rem; border-bottom: 1px solid #e0e0e0; }
.af-toc-heading { font-size: 0.95rem; margin: 0 0 0.2rem; }
.af-toc-years { font-size: 0.9rem; margin: 0; }
.af-count { color: #888; font-size: 0.82em; }
</style>

<div class="af-toc">
{% for conf in site.data.artifinder_nonevaluated %}
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

{% for conf in site.data.artifinder_nonevaluated %}
<h2 id="{{ conf[0] }}">{{ conf[0] | upcase }}</h2>

{% for year_data in conf[1] %}
<h3 id="{{ conf[0] }}-{{ year_data[0] }}">{{ year_data[0] }} <span class="af-count">({{ year_data[1].size }})</span></h3>

| Paper | Artifact |
|-------|----------|
{% for a in year_data[1] -%}
| [{{ a.title }}]({{ a.page_link }}) | <{{ a.artifact }}>{% if a.validated %} <abbr title="This extracted link has been manually validated." class="af-validated">✓</abbr>{% else %} <abbr title="This link was automatically extracted and has not been manually validated." class="af-unvalidated">?</abbr>{% endif %} |
{% endfor %}

{% endfor %}
{% endfor %}
