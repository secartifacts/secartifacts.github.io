---
title: Non-evaluated artifacts
permalink: /artifinder/
---

Artifacts automatically discovered by [ArtiFinder](https://github.com/DistriNet/ArtiFinder) that were not submitted to formal artifact evaluation.
If you notice a mistake in the automatically extracted links or want to manually validate correct entries (marked with a <abbr title="This extracted link has been manually validated." class="af-validated">✓</abbr> in the dataset), please submit a [pull request](https://github.com/DistriNet/ArtiFinder-Data)!

In addition to these links, we also cross-checked the URLs submitted for artifact evaluation with those extracted from the papers.
When there is a mismatch, the URL reported in the paper is listed on the artifact evaluation outcome page under "Link in paper".
These can often point to project websites or actively maintained repositories instead of archived versions or expired temporary URLs.

<style>
.af-count { color: #888; font-size: 0.82em; }
.af-years { font-size: 0.9rem; margin: 0.25rem 0 1rem; padding: 0.5rem 1rem; background: #f8f8f8; border-radius: 6px; }
details > summary { font-size: 1.5em; font-weight: bold; cursor: pointer; margin: 1rem 0 0.25rem; }
.af-table { width: 100%; table-layout: fixed; }
.af-table td:nth-child(1) { width: 60%; }
.af-table td:nth-child(2) { width: 35%; }
.af-table td:nth-child(3) { width: 5%; text-align: center; }
</style>

{% for conf in site.data.artifinder_nonevaluated %}
{% assign conf_total = 0 %}
{% for year_data in conf[1] %}{% assign conf_total = conf_total | plus: year_data[1].size %}{% endfor %}
<details>
<summary><strong>{{ conf[0] | upcase }}</strong> <span class="af-count">({{ conf_total }})</span></summary>
<p class="af-years">{% for year_data in conf[1] %}{% unless forloop.first %} &middot; {% endunless %}<a href="#{{ conf[0] }}-{{ year_data[0] }}">{{ year_data[0] }}</a> <span class="af-count">({{ year_data[1].size }})</span>{% endfor %}</p>

{% for year_data in conf[1] %}
<h3 id="{{ conf[0] }}-{{ year_data[0] }}">{{ conf[0] | upcase }} {{ year_data[0] }} <span class="af-count">({{ year_data[1].size }})</span></h3>

<table class="af-table">
<thead><tr><th>Paper</th><th>Artifact</th><th></th></tr></thead>
<tbody>
{% for a in year_data[1] -%}
<tr>
<td><a href="{{ a.page_link }}">{{ a.title }}</a></td>
<td><a href="{{ a.artifact }}" target="_blank">{{ a.artifact }}</a></td>
<td>{% if a.validated %}<abbr title="This extracted link has been manually validated." class="af-validated">✓</abbr>{% else %}<abbr title="This link was automatically extracted and has not been manually validated." class="af-unvalidated">?</abbr>{% endif %}</td>
</tr>
{% endfor %}
</tbody>
</table>

{% endfor %}
</details>
{% endfor %}
