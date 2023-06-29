---
title: Results
order: 20
artifacts:
  - title: "Abusing Trust: Mobile Kernel Subversion via TrustZone Rootkits"
    artifact_url: "https://github.com/establishingsecurity/trustzone-rootkit"
    paper_url: "https://security.inso.tuwien.ac.at/pdfs/woot22-preprint.pdf"

  - title: "AirTag of the Clones: Shenanigans with Liberated Item Finders"
    artifact_url: "https://github.com/stacksmashing/airtag-glitcher,https://github.com/seemoo-lab/airtag"
    paper_url: "https://github.com/seemoo-lab/airtag/blob/main/woot22-paper.pdf"
    
  - title: "DABANGG: A Case for Noise Resilient Flush Based Cache Attacks "
    artifact_url: "https://github.com/DABANGG-Attack/Source-Code"
    paper_url: "https://eprint.iacr.org/2020/637.pdf"
      
  - title: "Exploring Widevine for Fun and Profit "
    artifact_url: "https://github.com/Avalonswanderer/wideXtractor,https://github.com/Avalonswanderer/widevine_key_ladder"
    paper_url: "https://arxiv.org/pdf/2204.09298"
  
  - title: "Hack the Heap: Heap Layout Manipulation made Easy"
    artifact_url: "https://github.com/Usibre/hacktheheap-puzzlegen,https://hacktheheap.io/"
    paper_url: "https://www.computer.org/csdl/proceedings-article/spw/2022/964300a289/1FiwVVvAR0Y"

  - title: "On the Security of Parsing Security-Relevant HTTP Headers in Modern Browsers"
    artifact_url: "https://github.com/hen95/HTTPHeaderBrowserTesting"
    paper_url: "https://www.computer.org/csdl/proceedings-article/spw/2022/964300a342/1FiwZHjFEHK"
---

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Artifact(s)</th>
    </tr>
  </thead>
  <tbody>
  {% for artifact in page.artifacts %}
    <tr>
      <td>
        <a href="{{artifact.paper_url}}">{{artifact.title}}</a>
      </td>
      <td>
        {% assign artifacts = artifact.artifact_url | split: "," %}    
        {% for url in artifacts %}        
          <a href="{{url}}">{{url}}</a>
        {% endfor %}
      </td>
    </tr>
  {% endfor %}
  </tbody>
</table>
