---
title: Results
order: 40
issues:
  - issue_name: "2026.1"
    artifacts:
    - paper_url: ""
      title: "Gaze3P: Gaze-Based Prediction of Perceived Privacy"
      artifact_url: "https://doi.org/10.5281/zenodo.17104154"
      badges: "available"

    - paper_url: ""
      title: "Ad Personalization and Transparency in Mobile Ecosystems: A Comparative Analysis of Google’s and Apple’s EU App Stores"
      artifact_url: "https://github.com/seemoo-lab/appstore-ad-tools/tree/4bc9d4f70b13e52523382b81574c62983c3ca879"
      badges: "available, functional, reproduced"

    - paper_url: ""
      title: "dX-Privacy for Text and the Curse of Dimensionality"
      artifact_url: "https://github.com/r-carpentier/dx-privacy-curse/tree/acabdd7cc72046d32c354001cda6cf97ac7ebdf1"
      badges: "available, functional"

    - paper_url: ""
      title: "Location-Enhanced Information Flow for Home Automations"
      artifact_url: "https://doi.org/10.17605/OSF.IO/NPHRV"
      badges: "available, functional, reproduced"

    - paper_url: ""
      title: "PriVA-C: Defending Voice Assistants from Fingerprinting Attacks"
      artifact_url: "https://github.com/dilawer11/PriVA-C/tree/fc0e1fc8c1cb4656ff72d3b32a4d4e43367dc243"
      badges: "available"

    - paper_url: ""
      title: "Bot Among Us: Exploring User Awareness and Privacy Concerns About Chatbots in Group Chats"
      artifact_url: "https://github.com/csienslab/bot-among-us/tree/df1622ecaa2bf46f83d8153361a8b2abf7725a99"
      badges: "available, functional, reproduced"

    - paper_url: ""
      title: "SPRINT: Scalable Secure & Differentially Private Inference for Transformers"
      artifact_url: "https://github.com/SAP/sprint/tree/69179165f305075af9c765ee415bf1c77da4bd28"
      badges: "available, functional"

    - paper_url: ""
      title: "Ephemeral Network-Layer Fingerprinting Defenses"
      artifact_url: "https://github.com/maybenot-io/popets-2026.1-ephemeral-defs-paper-artifacts/tree/31ff58466742c69b738191bc66789064bac849c2"
      badges: "available, functional, reproduced"

    - paper_url: ""
      title: "Evaluating connection migration based QUIC censorship circumvention"
      artifact_url: "https://github.com/inspire-group/QUICstep-PETS/tree/0a3d0b577bcffc7e43c092920f94652a4e513b4a"
      badges: "available"

    - paper_url: ""
      title: "Privacy Attacks on Matrix Profiles based on Reconstruction Techniques"
      artifact_url: "https://gitlab.inria.fr/petscraft-public/attacks-by-reconstruction/-/tree/17dac8b10ca7998a3bf143ee30c88443899509d3"
      badges: "available, functional, reproduced"

    - paper_url: ""
      title: "Making Sense of Private Advertising: A Principled Approach to a Complex Ecosystem"
      artifact_url: "https://github.com/kylehogan/idealAdsFunctionalities/tree/5bddc412b536da75395ff822a853f126f9bdccfb"
      badges: "available, functional, reproduced"

    - paper_url: ""
      title: "Personal Data Flows and Privacy Policy Traceability in Third-party GPT Integrations"
      artifact_url: "https://doi.org/10.5281/zenodo.17094729"
      badges: "available, functional, reproduced"

    - paper_url: ""
      title: "Sanitization or Deception? Rethinking Privacy Protection in Large Language Models"
      artifact_url: "https://github.com/BipinPaudel/PrivacyOrDeception_PETS/tree/253ac69e826b13c0ab072d25e90b9f2739a69af5"
      badges: "available"

    - paper_url: ""
      title: "Word-level Annotation of GDPR Transparency Compliance in Privacy Policies using Large Language Models"
      artifact_url: "https://github.com/tomcory/privacy-policy-annotator/tree/28cc2b1ad104f78696793c33c548cab3ac07c070"
      badges: "available"

    - paper_url: ""
      title: "ReporTor: Facilitating User Reporting of Issues Encountered in Naturalistic Web Browsing via the Tor Browser"
      artifact_url: "https://doi.org/10.7278/S5d-f8b6-satb"
      badges: "available, functional"

    - paper_url: ""
      title: "Securing Private Federated Learning in a Malicious Setting: A Scalable TEE-Based Approach with Client Auditing"
      artifact_url: "https://arxiv.org/src/2509.08709v2/anc"
      badges: "available"

    - paper_url: ""
      title: "How Experts Personalize Privacy & Security Advice for At-Risk Users"
      artifact_url: "https://doi.org/10.17605/osf.io/pqh84"
      badges: "available"

  - issue_name: "2026.2"
    artifacts:
    - paper_url: ""
      title: "Breaking BAD? Better Call SAUL! -- Breaking and Fixing Bloom Filters with Added Diffusion"
      artifact_url: "https://github.com/SchaeferJ/BreakingBAD/tree/11ea61c1bdd0edf3082b77b60bacbc0991b3564f"
      badges: "available"

    - paper_url: ""
      title: "Frequency Estimation of Correlated Multi-attribute Data under Local Differential Privacy"
      artifact_url: "https://github.com/shafizurRseeam/Corr-RR/tree/cc6c059fcc073ab55feeb230ce66d78929e042c1"
      badges: "available, functional, reproduced"

    - paper_url: ""
      title: ""
      artifact_url: ""
      badges: "available, functional, reproduced"

    - paper_url: ""
      title: ""
      artifact_url: ""
      badges: "available, functional, reproduced"


---

<style>
a.pets-artifact-badge {
  font-weight: bold;
  font-size: smaller;
  color: #72bf02;
  background-color: #000000;
  padding: 2px;
  text-decoration: none;
}
</style>

The results can also be found on the <a href="https://petsymposium.org/popets/2026/">PETS 2026 proceedings</a>.

{% for issue in page.issues %}

## {{ issue.issue_name }}

<table>
  <thead>
    <tr>
      <th>Title</th>
      <th width="350px">Artifact URL</th>
    </tr>
  </thead>
  <tbody>
  {% for artifact in issue.artifacts %}
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
        {% if artifact.badges == "available" %}
          <a class="pets-artifact-badge" href="{{artifact.artifact_url}}">Artifact: Available</a>
        {% elsif artifact.badges == "available, functional" %}
          <a class="pets-artifact-badge" href="{{artifact.artifact_url}}">Artifact: Available, Functional</a>
        {% elsif artifact.badges == "available, functional, reproduced" %}
          <a class="pets-artifact-badge" href="{{artifact.artifact_url}}">Artifact: Available, Functional, Reproduced</a>
        {% endif %}
      {% endif %}
      </td>
    </tr>
  {% endfor %}
  </tbody>
</table>

{% endfor %}
