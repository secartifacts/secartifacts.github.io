---
title: Results
order: 20
functional_img: acmartifactbadge_functional.png
functional_name: Artifacts Functional
reusable_img: acmartifactbadge_reusable.png
reusable_name: Artifacts Reusable
artifacts:
-   title: 'A Game of "Cut and Mouse": Bypassing Antivirus by Simulating User Inputs'
    badges: functional
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359844
-   title: Co-Evaluation of Pattern Matching Algorithms on IoT Devices with Embedded GPUs
    badges: functional
    artifact_url: https://bitbucket.org/mpastyl/acsac_pattern_matching_benchmark_opencl/src/master/
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359811
-   title: Detecting organized eCommerce fraud using scalable categorical clustering
    badges: functional
    artifact_url: https://github.com/SSGAalto/recagglo
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359810
-   title: Function Boundary Detection in Stripped Binaries
    badges: functional
    artifact_url: https://github.com/CenterforSecureAndDependableSystems/FunctionBoundary
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359825
-   title: 'FuzzBuilder: Automated building greybox fuzzing environment for C/C++ library'
    badges: reusable
    artifact_url: https://github.com/hksecurity/FuzzBuilder
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359846
-   title: 'JStap: A Static Pre-Filter for Malicious JavaScript Detection'
    badges: reusable
    artifact_url: https://github.com/Aurore54F/JStap
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359813
-   title: 'Koinonia: Verifiable E-Voting with Long-term Privacy'
    badges: functional
    artifact_url: https://github.com/gehuangyi20/Koinonia
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359804
-   title: Model Inversion Attacks Against Collaborative Inference
    badges: functional
    artifact_url: https://github.com/zechenghe/Inverse_Collaborative_Inference
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359824
-   title: 'Opening Pandora''s Box through ATFuzzer: Dynamic Analysis of AT Interface for Android Smartphones'
    badges: functional
    artifact_url: https://github.com/Imtiazkarimik23/ATFuzzer
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359833
-   title: 'Out of Control: Stealthy Attacks Against Robotic Vehicles Protected by Control-based Techniques'
    badges: reusable
    artifact_url: https://github.com/DependableSystemsLab/stealthy-attacks
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359847
-   title: 'PDoT: Private DNS-over-TLS with TEE Support'
    badges: functional
    artifact_url: https://github.com/sprout-uci/PDoT
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359793
-   title: Privacy Preserving Substring Search Protocol with Polylogarithmic Communication Cost
    badges: reusable
    artifact_url: https://dx.doi.org/10.5281/zenodo.3384814
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359842
-   title: Proof of Aliveness
    badges: functional
    artifact_url: https://github.com/ChengluJin/Proof_of_Aliveness
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359827
-   title: Revisiting Utility Metrics for Location Privacy-Preserving Mechanisms
    badges: functional
    artifact_url: https://github.com/vrt1shjwlkr/Ride-Hailing-Service-Emulator
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359829
-   title: 'SIP Shaker: Software Integrity Protection Composition'
    badges: reusable
    artifact_url: https://github.com/mr-ma/sip-shaker-artifact/
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359848
-   title: 'STRIP: A Defence Against Trojan Attacks on Deep Neural Networks'
    badges: reusable
    artifact_url: https://github.com/garrisongys/STRIP
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359790
-   title: 'SecDATAVIEW: A Secure Big Data Workflow Management System for Heterogeneous Computing Environments'
    badges: functional
    artifact_url: https://github.com/shiyonglu/SecDATAVIEW
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359827
-   title: 'Speculator: A Tool to Analyze Speculative Execution Attacks and Mitigations'
    badges: reusable
    artifact_url: https://github.com/ibm-research/speculator
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359837
-   title: Will You Trust This TLS Certificate? Perceptions of People Working in IT
    badges: functional
    artifact_url: https://crocs.fi.muni.cz/public/papers/acsac2019
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359800
-   title: 'WooKey: Designing a Trusted and Efficient USB Device'
    badges: reusable
    artifact_url: https://wookey-project.github.io/
    paper_url: https://dl.acm.org/doi/pdf/10.1145/3359789.3359802
---

Results automatically obtained from <a href="https://www.acsac.org/2019/program/artifacts/">ACSAC website</a>.

**Evaluation Results**:

* 12 Artifacts Functional
* 8 Artifacts Reusable

<table>
  <thead>
    <tr>
      <th>
        Title
      </th>
      <th>
        Funct.
      </th>
      <th>
        Reusa.
      </th>
      <th>
        Available At
      </th>
    </tr>
  </thead>
  <tbody>
    {% for artifact in page.artifacts %}
    <tr>
      <td>
        {% if artifact.paper_url %}
        <a href="{{artifact.paper_url}}" target="_blank">
          {{artifact.title}}
        </a>
        {% else %}
            {{ artifact.title }}
        {% endif %}
      </td>
      <td width="62px">
        {% if artifact.badges contains "functional" %}
        <img alt="{{ page.functional_name }}" src="{{ site.baseurl }}/images/{{ page.functional_img }}">
        {% endif %}
      </td>
      <td width="62px">
        {% if artifact.badges contains "reusable" %}
        <img alt="{{ page.reusable_name }}" src="{{ site.baseurl }}/images/{{ page.reusable_img }}">
        {% endif %}
      </td>
      <td>
        {% if artifact.artifact_url %}
            {% assign artifacts = artifact.artifact_url | split: " " %}
            {% for url in artifacts %}
        <a href="{{url}}" target="_blank">
          Artifact
        </a>
        <br>
        {% endfor %}
        {% endif %}
        {% if artifact.appendix_url %}
        <a href="{{artifact.appendix_url}}" target="_blank">
          Appendix
        </a>
        <br>
        {% endif %}
      </td>
    </tr>
    {% endfor %}
  </tbody>
</table>
