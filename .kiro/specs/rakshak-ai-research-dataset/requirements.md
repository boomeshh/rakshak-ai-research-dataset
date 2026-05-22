# Requirements Document

## Introduction

This feature defines the structured research dataset repository for **Rakshak AI** — a Defence Cyber Safety Portal designed for Indian defence personnel, veterans, and their families. The repository provides realistic, synthetic cyber threat datasets to support AI/ML model training, NLP-based threat classification, rule-based risk scoring, dashboard analytics, and CERT escalation workflow testing. All data is fake and generated for research and testing purposes only.

The dataset covers phishing URLs, scam messages (SMS/WhatsApp/Telegram), fake APK threat reports, complaint records, and AI detection exports — all modelled on Indian defence-related cyber threat scenarios.

---

## Glossary

- **Rakshak_AI**: The AI-powered Defence Cyber Safety Portal system
- **Dataset_Repository**: The structured folder-based collection of synthetic cyber threat data files
- **Complaint_Record**: A structured JSON entry representing a fake cyber complaint with metadata
- **Phishing_URL**: A fake or simulated malicious web link used for threat classification testing
- **Scam_Message**: A synthetic fraudulent text message (SMS, WhatsApp, or Telegram) used for NLP model testing
- **APK_Sample**: Metadata describing a suspicious or fake Android application package
- **CERT**: Computer Emergency Response Team — the escalation authority for high-severity threats
- **Risk_Score**: A numeric value (0–100) representing the assessed threat severity of a record
- **Threat_Category**: A classification label such as Phishing, APK_Malware, Impersonation, Banking_Fraud, or OTP_Scam
- **Detection_Label**: A binary or categorical AI output label (e.g., Malicious, Suspicious, Benign)
- **Dashboard_Metric**: An aggregated analytics value used for visualisation in the Rakshak AI portal
- **Escalation_Status**: The current CERT escalation state of a complaint (e.g., Pending, Escalated, Resolved)
- **Evidence_Type**: The category of supporting evidence attached to a complaint (e.g., Screenshot, URL, APK_Hash)
- **User_Role**: The role of the person filing a complaint (e.g., Defence_Personnel, Veteran, Family_Member)

---

## Requirements

### Requirement 1: Fake Complaint Records Dataset

**User Story:** As a researcher or AI engineer, I want structured fake complaint records, so that I can test complaint ingestion pipelines, threat classification models, and CERT escalation workflows.

#### Acceptance Criteria

1. THE Dataset_Repository SHALL contain a `fake_complaints/complaint_samples.json` file with a minimum of 15 complaint records in valid JSON array format.
2. WHEN a complaint record is parsed, THE Complaint_Record SHALL contain the fields: `complaint_id`, `threat_type`, `risk_level`, `risk_score`, `description`, `evidence_type`, `complaint_status`, `user_role`, `cert_escalation_status`, and `timestamp`.
3. THE Dataset_Repository SHALL contain a `fake_complaints/complaint_export.csv` file with the same complaint records exported in CSV format with matching column headers.
4. THE Dataset_Repository SHALL contain a `fake_complaints/complaint_summary.md` file summarising complaint distribution by threat type, risk level, and escalation status.
5. WHEN complaint records are generated, THE Complaint_Record SHALL use realistic Indian defence-related scenarios including army welfare fraud, KYC scams, impersonation of defence officials, and banking fraud targeting veterans.
6. THE Complaint_Record SHALL assign `risk_score` values as integers in the range 0–100, where values 75–100 indicate High risk, 40–74 indicate Medium risk, and 0–39 indicate Low risk.
7. WHEN `cert_escalation_status` is set to "Escalated", THE Complaint_Record SHALL have a `risk_score` of 70 or above.
8. THE Dataset_Repository SHALL include complaint records covering at least 5 distinct `threat_type` values: Phishing, APK_Malware, Impersonation, Banking_Fraud, and OTP_Scam.

---

### Requirement 2: Phishing URLs Dataset

**User Story:** As an AI/ML engineer, I want a curated list of fake phishing URLs with risk metadata, so that I can train and evaluate URL-based threat detection models.

#### Acceptance Criteria

1. THE Dataset_Repository SHALL contain a `phishing_urls/phishing_links.txt` file with a minimum of 15 fake phishing URLs, one per line.
2. THE Dataset_Repository SHALL contain a `phishing_urls/malicious_domains.csv` file with columns: `domain`, `category`, `risk_score`, `detection_label`, and `first_seen_date`.
3. THE Dataset_Repository SHALL contain a `phishing_urls/url_risk_labels.json` file with a minimum of 15 URL records, each containing: `url`, `risk_score`, `threat_category`, `detection_label`, and `source`.
4. WHEN phishing URLs are generated, THE Dataset_Repository SHALL include fake URLs impersonating Indian defence-related services including SBI defence salary accounts, Army welfare portals, KYC update pages, and SPARSH pension portals.
5. THE Dataset_Repository SHALL include URLs across at least 4 domain categories: Banking_Phishing, Welfare_Portal_Spoofing, KYC_Fraud, and APK_Distribution.
6. WHEN a URL record is parsed, THE Dataset_Repository SHALL assign a `detection_label` of either "Malicious" or "Suspicious" based on the `risk_score`, where scores above 70 are labelled "Malicious".
7. THE Dataset_Repository SHALL use realistic fake domain patterns such as typosquatting, subdomain abuse, and hyphenated impersonation domains.

---

### Requirement 3: Scam Messages Dataset

**User Story:** As an NLP engineer, I want realistic fake scam messages across multiple channels, so that I can train and test text-based threat classification and phishing detection models.

#### Acceptance Criteria

1. THE Dataset_Repository SHALL contain a `scam_messages/sms_scams.txt` file with a minimum of 10 fake SMS phishing messages targeting defence personnel.
2. THE Dataset_Repository SHALL contain a `scam_messages/whatsapp_scams.txt` file with a minimum of 10 fake WhatsApp scam messages including impersonation of defence officials and welfare scheme fraud.
3. THE Dataset_Repository SHALL contain a `scam_messages/telegram_scams.txt` file with a minimum of 10 fake Telegram scam messages including APK distribution links and fake defence group invitations.
4. THE Dataset_Repository SHALL contain a `scam_messages/social_engineering_samples.md` file documenting at least 5 annotated social engineering message patterns with threat category labels and analysis notes.
5. WHEN scam messages are generated, THE Dataset_Repository SHALL cover at least 6 scam categories: OTP_Scam, KYC_Fraud, Banking_Fraud, APK_Distribution, Impersonation, and Welfare_Scheme_Fraud.
6. THE Dataset_Repository SHALL include messages that reference realistic Indian defence context such as SPARSH pension, CSD canteen, Army welfare funds, Ex-Servicemen Contributory Health Scheme (ECHS), and Sainik welfare boards.
7. WHEN a scam message references a URL, THE Dataset_Repository SHALL use fake URLs consistent with the phishing URLs dataset.

---

### Requirement 4: APK Samples Metadata Dataset

**User Story:** As a mobile security researcher, I want structured metadata about suspicious APK files, so that I can test APK threat detection models and malware classification pipelines.

#### Acceptance Criteria

1. THE Dataset_Repository SHALL contain an `apk_samples/fake_apk_alerts.json` file with a minimum of 10 APK alert records in valid JSON array format.
2. WHEN an APK alert record is parsed, THE Dataset_Repository SHALL include the fields: `apk_id`, `apk_name`, `package_name`, `source`, `malware_behavior`, `installation_risk`, `threat_category`, `risk_score`, and `reported_date`.
3. THE Dataset_Repository SHALL contain an `apk_samples/suspicious_apk_names.txt` file listing a minimum of 15 suspicious APK file names, one per line.
4. THE Dataset_Repository SHALL contain an `apk_samples/apk_analysis_report.md` file summarising APK threat categories, common malware behaviours, and risk distribution.
5. WHEN APK records are generated, THE Dataset_Repository SHALL include APKs impersonating Indian defence applications such as SPARSH, ECHS, Army welfare apps, and CSD canteen apps.
6. THE Dataset_Repository SHALL include at least 4 distinct `malware_behavior` values: Data_Exfiltration, SMS_Interception, Remote_Access_Trojan, and Credential_Harvesting.
7. THE Dataset_Repository SHALL include at least 3 distinct `source` values representing APK distribution channels: Telegram_Group, WhatsApp_Link, and Third_Party_Store.

---

### Requirement 5: AI Testing Exports Dataset

**User Story:** As a QA engineer or data scientist, I want pre-generated AI detection results and dashboard metrics, so that I can validate the Rakshak AI portal's analytics, alert generation, and CERT escalation workflows without live data.

#### Acceptance Criteria

1. THE Dataset_Repository SHALL contain a `testing_exports/ai_detection_results.csv` file with a minimum of 15 records and columns: `record_id`, `input_type`, `threat_category`, `predicted_label`, `confidence_score`, `actual_label`, `is_correct`, and `timestamp`.
2. THE Dataset_Repository SHALL contain a `testing_exports/dashboard_metrics.json` file with aggregated analytics including: total threats detected, breakdown by threat category, average risk score, escalation rate, and detection accuracy percentage.
3. THE Dataset_Repository SHALL contain a `testing_exports/cert_escalation_logs.txt` file with a minimum of 10 log entries in a structured log format including timestamp, complaint ID, escalation level, and action taken.
4. WHEN AI detection results are generated, THE Dataset_Repository SHALL include records for all input types: URL, SMS, WhatsApp, Telegram, and APK.
5. THE Dataset_Repository SHALL include detection results with a simulated overall accuracy of 85% or above, with `is_correct` values reflecting this distribution.
6. WHEN dashboard metrics are parsed, THE Dataset_Repository SHALL include metrics for at least 5 threat categories matching those defined in the Complaint_Record and APK alert datasets.
7. THE Dataset_Repository SHALL include CERT escalation log entries covering at least 3 escalation levels: L1_Alert, L2_Investigation, and L3_CERT_Escalation.

---

### Requirement 6: Dataset References and Methodology

**User Story:** As a researcher, I want documented references and methodology, so that I can understand the data sources, generation approach, and appropriate usage of the dataset.

#### Acceptance Criteria

1. THE Dataset_Repository SHALL contain a `dataset_references/source_references.md` file citing at least 4 external reference sources including PhishTank, OpenPhish, Kaggle phishing datasets, and CERT-In advisories.
2. THE Dataset_Repository SHALL contain a `dataset_references/dataset_methodology.md` file describing the data generation approach including synthetic data generation, seeded threat simulation, and manual testing methodology.
3. WHEN the methodology document is read, THE Dataset_Repository SHALL clearly state that all data is synthetic and does not represent real individuals, organisations, or incidents.
4. THE Dataset_Repository SHALL document the threat simulation seed parameters used to generate consistent and reproducible dataset samples.
5. THE Dataset_Repository SHALL include a section on dataset limitations, known biases, and recommended usage guidelines for AI model training.

---

### Requirement 7: Screenshots Placeholder

**User Story:** As a contributor, I want a designated screenshots folder with guidance, so that I can add visual evidence or UI screenshots to support the dataset documentation.

#### Acceptance Criteria

1. THE Dataset_Repository SHALL contain a `screenshots/README.md` file explaining the purpose of the screenshots folder and the naming convention for screenshot files.
2. WHEN a contributor reads the screenshots README, THE Dataset_Repository SHALL provide guidance on acceptable screenshot formats (PNG, JPG) and recommended dimensions.

---

### Requirement 8: Root README Documentation

**User Story:** As a developer or researcher visiting the repository, I want a professional README, so that I can quickly understand the purpose, structure, and usage of the dataset.

#### Acceptance Criteria

1. THE Dataset_Repository SHALL contain a root `README.md` file with sections covering: Project Purpose, Dataset Structure, Folder Descriptions, Usage Instructions, AI Testing Support, Research Usage, Disclaimer, and Defence Cyber Awareness Context.
2. WHEN the README is read, THE Dataset_Repository SHALL clearly identify Rakshak AI as a Defence Cyber Safety Portal and explain the dataset's role in supporting AI/ML model development.
3. THE Dataset_Repository SHALL include a disclaimer stating that all data is fake, synthetic, and intended solely for research, testing, and educational purposes.
4. THE Dataset_Repository SHALL include a section describing how the dataset supports threat classification, risk scoring, dashboard analytics, CERT escalation testing, and real-time alert simulation.
5. WHEN the README references dataset folders, THE Dataset_Repository SHALL provide a visual folder tree and a brief description of each folder's contents and purpose.

---

### Requirement 9: Data Consistency and Cross-File Integrity

**User Story:** As a data engineer, I want consistent identifiers and threat categories across all dataset files, so that I can join and cross-reference records during testing and model evaluation.

#### Acceptance Criteria

1. THE Dataset_Repository SHALL use consistent `threat_type` and `threat_category` label values across all dataset files (complaint records, URL labels, APK alerts, and AI detection results).
2. WHEN complaint IDs are assigned, THE Dataset_Repository SHALL use a consistent format such as `RKS-YYYY-NNNN` across JSON and CSV exports.
3. THE Dataset_Repository SHALL use ISO 8601 format (`YYYY-MM-DDTHH:MM:SSZ`) for all timestamp fields across all files.
4. WHEN `risk_score` values are assigned, THE Dataset_Repository SHALL apply a consistent scoring scale of 0–100 across all dataset files.
5. THE Dataset_Repository SHALL ensure that records referenced across multiple files (e.g., a complaint ID appearing in both complaint_samples.json and cert_escalation_logs.txt) use matching identifiers and consistent field values.
