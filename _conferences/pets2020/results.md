---
title: Results
order: 30
artifacts:

  - paper_url: "https://petsymposium.org/2020/files/papers/issue4/popets-2020-0059.pdf"
    title: "PriFi: Low-Latency Anonymity for Organizational Networks"
    artifact_url: "https://github.com/dedis/prifi"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue3/popets-2020-0054.pdf"
    title: "dPHI: An improved high-speed network-layer anonymity protocol"
    artifact_url: "https://github.com/AlexB030/dPHI"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue2/popets-2020-0019.pdf"
    title: "Protecting against Website Fingerprinting with Multihoming"
    artifact_url: "https://github.com/sebhenri/HyWF"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue2/popets-2020-0023.pdf"
    title: "A Framework of Metrics for Differential Privacy from Local Sensitivity"
    artifact_url: "https://pleak.io/wiki/"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue4/popets-2020-0058.pdf"
    title: "Automatic Discovery of Privacy-Utility Pareto Fronts"
    artifact_url: "https://github.com/amzn/differential-privacy-bayesian-optimization"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue4/popets-2020-0075.pdf"
    title: "Secure Evaluation of Quantized Neural Networks"
    artifact_url: "https://github.com/anderspkd/SecureQ8"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue3/popets-2020-0043.pdf"
    title: "Tik-Tok: The Utility of Packet Timing in Website Fingerprinting Attacks"
    artifact_url: "https://github.com/msrocean/Tik_Tok"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue1/popets-2020-0013.pdf"
    title: "Website Fingerprinting with Website Oracles"
    artifact_url: "https://github.com/pylls/wfwo"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue4/popets-2020-0066.pdf"
    title: "Effective writing style transfer via combinatorial paraphrasing"
    artifact_url: "https://gitlab.com/ssg-research/mlsec/parchoice/"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue2/popets-2020-0025.pdf"
    title: "Differentially Private SQL with Bounded User Contribution"
    artifact_url: "https://github.com/google/differential-privacy"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue2/popets-2020-0033.pdf"
    title: "Mind the Gap: Ceremonies for Applied Secret Sharing"
    artifact_url: "https://git-crysp.uwaterloo.ca/ckomlo/VerifiableSecretSharing"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue3/popets-2020-0055.pdf"
    title: "Tandem: Securing Keys by Using a Central Server While Preserving Privacy"
    artifact_url: "https://github.com/spring-epfl/tandem"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue2/popets-2020-0017.pdf"
    title: "NoMoATS: Towards Automatic Detection of Mobile Tracking"
    artifact_url: "https://athinagroup.eng.uci.edu/projects/nomoads/"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue2/popets-2020-0021.pdf"
    title: "The TV is Smart and Full of Trackers: Measuring Smart TV Advertising and Tracking"
    artifact_url: "https://athinagroup.eng.uci.edu/projects/smarttv/"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue2/popets-2020-0024.pdf"
    title: "Secure and Scalable Document Similarity on Distributed Databases: Differential Privacy to the Rescue"
    artifact_url: "https://github.com/schoppmp/private-knn"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue3/popets-2020-0053.pdf"
    title: "Protecting Private Inputs: Bounded Distortion Guarantees With Randomised Approximations"
    artifact_url: "https://github.com/pahfat/PoPETs2020.git"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue4/popets-2020-0070.pdf"
    title: "When Speakers Are All Ears: Characterizing Misactivations of IoT Smart Speakers"
    artifact_url: "https://github.com/djdubois/smart-speakers-study"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue2/popets-2020-0039.pdf"
    title: "A Tale of Two Trees: One Writes, and Other Reads. Optimized Oblivious Accesses to Large-Scale Blockchains"
    artifact_url: "https://github.com/TEE-3/T3"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue2/popets-2020-0020.pdf"
    title: "Explaining the Technology Use Behavior of Privacy-Enhancing Technologies: The Case of Tor and JonDonym"
    artifact_url: "https://pape.science/paper/HPR20pets/"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue2/popets-2020-0016.pdf"
    title: "A Comparative Measurement Study of Web Tracking on Mobile and Desktop Environments"
    artifact_url: "https://github.com/jun521ju/PETS2020_Web_Tracking"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue1/popets-2020-0004.pdf"
    title: "The Privacy Policy Landscape After the GDPR"
    artifact_url: "https://github.com/wi-pi/GDPR"

  - paper_url: "https://petsymposium.org/2020/files/papers/issue3/popets-2020-0049.pdf"
    title: "Mitigator: Privacy policy compliance using trusted hardware"
    artifact_url: "https://git-crysp.uwaterloo.ca/miti/mitigator"

---

Results obtained from <a href="https://petsymposium.org/popets/2020/">PETS 2020 proceedings</a>.

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th>Artifact URL</th>
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
          <a href="{{artifact.artifact_url}}"><img src ="{{ site.baseurl }}/images/pets-badge-artifact-2020.png" alt="artifact"></a>
        {% endif %}
      </td>
    </tr>
  {% endfor %}
  </tbody>
</table>
