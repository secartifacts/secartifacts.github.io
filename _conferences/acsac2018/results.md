---
title: Results
order: 20
functional_img: acmartifactbadge_functional.png
functional_name: Artifacts Functional
artifacts:
-   title: A Measurement Study of Authentication Rate-Limiting Mechanisms of Modern Websites
    badges: functional
    artifact_url: https://docs.google.com/spreadsheets/d/1K2Y5PH1jIhhIbf_8FDb2YvqZTHFLNHjzlY75QiOYs90/edit?usp=sharing
    paper_url: https://www.acsac.org/2018/program-files/s125.html
-   title: An Extensive Evaluation of the Internet's Open Proxies
    badges: functional
    artifact_url: https://openproxies-acsac18.github.io/
    paper_url: https://www.acsac.org/2018/program-files/s113.html
-   title: An Historical Analysis of the SEAndroid Policy Evolution
    badges: functional
    artifact_url: http://imbumjin.github.io/gitmining_sepolicy.tar.gz
    paper_url: https://www.acsac.org/2018/program-files/s99.html
-   title: Analyzing Cache Side Channels Using Deep Neural Networks
    badges: functional
    artifact_url: https://github.com/tianweiz07/DeepLearningSideChannel
    paper_url: https://www.acsac.org/2018/program-files/s131.html
-   title: 'DeDoS: Defusing DoS with Dispersion Oriented Software'
    badges: functional
    artifact_url: https://github.com/dedos-project/DeDOS
    paper_url: https://www.acsac.org/2018/program-files/s200.html
-   title: Finding The Greedy, Prodigal, and Suicidal Contracts at Scale
    badges: functional
    artifact_url: https://github.com/MAIAN-tool/MAIAN
    paper_url: https://www.acsac.org/2018/program-files/s267.html
-   title: 'Hiding in the Shadows: Empowering ARM for Stealthy Virtual Machine Introspection'
    badges: functional
    artifact_url: https://github.com/drakvuf-on-arm/drakvuf-on-arm
    paper_url: https://www.acsac.org/2018/program-files/s17.html
-   title: Improving Accuracy of Android Malware Detection with Lightweight Contextual Awareness
    badges: functional
    artifact_url: https://github.com/jallen89/pikadroid.git
    paper_url: https://www.acsac.org/2018/program-files/s268.html
-   title: 'MicroWalk: A Framework for Finding Side Channels in Binaries'
    badges: functional
    artifact_url: https://github.com/UzL-ITS/Microwalk
    paper_url: https://www.acsac.org/2018/program-files/s264.html
-   title: 'Noise Matters: Using Sensor and Process Noise Fingerprint to Detect Stealthy Cyber Attacks and Authenticate sensors in CPS'
    badges: functional
    artifact_url: https://itrust.sutd.edu.sg/research/dataset/dataset_characteristics/#swat
    paper_url: https://www.acsac.org/2018/program-files/s280.html
-   title: 'Obscuro: A Bitcoin Mixer using Trusted Execution Environments'
    badges: functional
    artifact_url: https://github.com/BitObscuro/Obscuro
    paper_url: https://www.acsac.org/2018/program-files/s300.html
-   title: 'Osiris: Hunting for Integer Bugs in Ethereum Smart Contracts'
    badges: functional
    artifact_url: https://github.com/christoftorres/Osiris
    paper_url: https://www.acsac.org/2018/program-files/s245.html
-   title: Practical Integrity Protection with Oblivious Hashing
    badges: functional
    artifact_url: https://github.com/tum-i22/sip-oblivious-hashing/tree/acsac
    paper_url: https://www.acsac.org/2018/program-files/s224.html
-   title: SENSS Against Volumetric DDoS Attacks
    badges: functional
    artifact_url: https://steel.isi.edu/projects/SENSS/ACSAC2018/
    paper_url: https://www.acsac.org/2018/program-files/s142.html
-   title: 'Shredder: Breaking Exploits through API Specialization'
    badges: functional
    artifact_url: https://github.com/shach33/shredder
    paper_url: https://www.acsac.org/2018/program-files/s43.html
-   title: 'Side-Channel Analysis of SM2: A Late-Stage Featurization Case Study'
    badges: functional
    artifact_url: https://doi.org/10.5281/zenodo.1436828
    paper_url: https://www.acsac.org/2018/program-files/s186.html
-   title: 'SmarTor: Smarter Tor with Smart Contracts'
    badges: functional
    artifact_url: https://greubelhome.ddns.net/index.php/s/NY2BxWnd88LP8XN
    paper_url: https://www.acsac.org/2018/program-files/s170.html
-   title: 'StateDroid: Stateful Detection of Stealthy Attacks in Android Apps via Horn-Clause Verification'
    badges: functional
    artifact_url: https://github.com/mohsinjuni/statedroid
    paper_url: https://www.acsac.org/2018/program-files/s62.html
-   title: 'TIFF: Using Input Type Inference To Improve Fuzzing'
    badges: functional
    artifact_url: https://www.vusec.net/projects/#testing
    paper_url: https://www.acsac.org/2018/program-files/s271.html
-   title: Towards Automated Generation of Exploitation Primitives for Web Browsers
    badges: functional
    artifact_url: https://github.com/RUB-SysSec/PrimGen
    paper_url: https://www.acsac.org/2018/program-files/s177.html
-   title: 'Type-after-Type: Practical and Complete Type-Safe Memory Reuse'
    badges: functional
    artifact_url: https://github.com/vusec/type-after-type
    paper_url: https://www.acsac.org/2018/program-files/s50.html
-   title: 'Wi Not Calling: Practical Privacy and Availability Attacks in Wi-Fi Calling'
    badges: functional
    artifact_url: https://github.com/sefcom/Wi-Fi-Calling-scource-code
    paper_url: https://www.acsac.org/2018/program-files/s320.html
---

Results automatically obtained from <a href="https://www.acsac.org/2018/artifacts/">ACSAC website</a>.

**Evaluation Results**:

* 22 Artifacts Functional

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
