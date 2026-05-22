# Source References

This document lists the external reference sources that informed the design, structure, and threat simulation parameters of the Rakshak AI Research Dataset. All data in this repository is synthetic; these sources were consulted for realistic threat patterns, URL structures, and classification taxonomies only.

---

## PhishTank

- **URL:** https://www.phishtank.com
- **Description:** A free community-driven service operated by Cisco Talos that maintains a real-time database of verified phishing URLs. Users submit suspected phishing links, which are then verified by the community and made available via API and bulk download in JSON/CSV formats.
- **Relevance:** Informed the URL structure, domain impersonation patterns (typosquatting, subdomain abuse), and risk labelling conventions used in `phishing_urls/phishing_links.txt`, `phishing_urls/malicious_domains.csv`, and `phishing_urls/url_risk_labels.json`. The Malicious/Suspicious detection label threshold and the four domain categories (Banking_Phishing, Welfare_Portal_Spoofing, KYC_Fraud, APK_Distribution) were modelled on PhishTank's classification approach.

---

## OpenPhish

- **URL:** https://openphish.com
- **Description:** An automated phishing intelligence platform that provides continuously updated feeds of active phishing URLs. OpenPhish uses machine learning to detect and classify phishing sites without human verification, offering both free community feeds and commercial threat intelligence tiers.
- **Relevance:** Provided reference patterns for automated phishing URL detection and confidence scoring, which informed the `risk_score` range design and the `detection_label` derivation logic used across the phishing URL dataset files. The concept of source-tagged URL records in `url_risk_labels.json` (the `source` field) was inspired by OpenPhish feed attribution.

---

## Kaggle Phishing Datasets

- **URL:** https://www.kaggle.com/datasets/shashwatwork/web-page-phishing-detection-dataset
- **Description:** A collection of publicly available phishing and legitimate URL datasets hosted on Kaggle, contributed by the data science community. These datasets include feature-engineered URL attributes (length, special character counts, subdomain depth, HTTPS usage) alongside binary or multi-class phishing labels, widely used for training URL-based threat classifiers.
- **Relevance:** Guided the schema design for `url_risk_labels.json` and `malicious_domains.csv`, particularly the choice of fields (`url`, `risk_score`, `threat_category`, `detection_label`, `source`). The distribution of risk scores and the 85% detection accuracy target in `testing_exports/ai_detection_results.csv` were calibrated against typical model performance benchmarks reported in Kaggle phishing classification notebooks.

---

## CERT-In Advisories (Indian Computer Emergency Response Team)

- **URL:** https://www.cert-in.org.in
- **Description:** CERT-In is the national nodal agency under the Ministry of Electronics and Information Technology (MeitY), Government of India, responsible for collecting, analysing, and disseminating information on cyber incidents. It publishes security advisories, vulnerability notes, and guidelines covering phishing campaigns, malware alerts, and fraud targeting Indian citizens and organisations.
- **Relevance:** Served as the primary reference for Indian-context threat scenarios, including defence-sector phishing campaigns, OTP scams targeting veterans, fake KYC portals impersonating government services, and APK-based malware distributed via messaging platforms. The CERT escalation workflow (L1_Alert → L2_Investigation → L3_CERT_Escalation) modelled in `testing_exports/cert_escalation_logs.txt` and the complaint escalation logic in `fake_complaints/complaint_samples.json` are directly inspired by CERT-In's incident response and escalation procedures.

---

## SPARSH Portal — Defence Pension Disbursement System

- **URL:** https://sparsh.defencepensions.gov.in
- **Description:** The official SPARSH (System for Pension Administration Raksha) portal managed by the Department of Ex-Servicemen Welfare, Ministry of Defence, Government of India. It handles pension disbursement for defence pensioners and provides a digital interface for pension-related services.
- **Relevance:** Provided the authentic naming conventions, service descriptions, and user context for defence-sector social engineering scenarios. Fake phishing URLs, scam messages, and APK impersonation samples in this dataset reference SPARSH to simulate realistic threats targeting defence pensioners, consistent with known fraud patterns reported by CERT-In and defence welfare organisations.

---

## ECHS (Ex-Servicemen Contributory Health Scheme)

- **URL:** https://echs.gov.in
- **Description:** The official portal for the Ex-Servicemen Contributory Health Scheme, a healthcare programme for retired Indian Armed Forces personnel and their dependants. The scheme provides medical facilities through a network of polyclinics and empanelled hospitals.
- **Relevance:** Informed the design of welfare-scheme fraud scenarios in `scam_messages/sms_scams.txt`, `scam_messages/whatsapp_scams.txt`, and `apk_samples/fake_apk_alerts.json`. Fake APK names and phishing URLs impersonating ECHS services were modelled on the real portal's branding and service names to reflect realistic social engineering tactics targeting veterans.

---

## Android Malware Datasets — Drebin / AndroZoo

- **URL:** https://www.sec.cs.tu-bs.de/~danarp/drebin/
- **Description:** Drebin is a well-known academic Android malware dataset containing feature vectors and metadata for thousands of malicious APK samples across multiple malware families. AndroZoo is a complementary large-scale APK collection maintained by the University of Luxembourg, used extensively in mobile security research.
- **Relevance:** Informed the APK alert schema design in `apk_samples/fake_apk_alerts.json`, particularly the `malware_behavior` taxonomy (Data_Exfiltration, SMS_Interception, Remote_Access_Trojan, Credential_Harvesting), `package_name` conventions, and `installation_risk` classification. The distribution of malware behaviors across APK records was calibrated against malware family prevalence patterns documented in Drebin research papers.
