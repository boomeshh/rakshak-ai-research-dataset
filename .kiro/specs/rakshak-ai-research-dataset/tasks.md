# Implementation Plan: Rakshak AI Research Dataset Repository

## Overview

Build the complete structured synthetic dataset repository for the Rakshak AI Defence Cyber Safety Portal. Tasks proceed folder-by-folder, creating all data files first, then wiring cross-file consistency, and finally adding property-based and structural tests.

## Tasks

- [x] 1. Set up repository structure and test scaffolding
  - Create all 8 top-level folders: `fake_complaints/`, `phishing_urls/`, `scam_messages/`, `apk_samples/`, `testing_exports/`, `screenshots/`, `dataset_references/`, and `tests/`
  - Create empty placeholder files at all 20 required paths so the structure is visible
  - Create `tests/conftest.py` with shared fixtures that load all dataset files once (JSON, CSV, TXT parsers)
  - Install test dependencies: `pip install hypothesis pytest`
  - _Requirements: 1.1, 2.1, 3.1, 4.1, 5.1, 6.1, 7.1, 8.1_

- [x] 2. Create fake_complaints/ dataset files
  - [x] 2.1 Create `fake_complaints/complaint_samples.json`
    - Write a JSON array of exactly 15 complaint records following the schema in the design
    - Cover all 5 threat types, all 3 user roles, mix of High/Medium/Low risk levels
    - Ensure at least 3 records have `cert_escalation_status = "Escalated"` with `risk_score >= 70`
    - Use `RKS-2024-NNNN` ID format and ISO 8601 timestamps
    - _Requirements: 1.1, 1.2, 1.5, 1.6, 1.7, 1.8_

  - [x] 2.2 Create `fake_complaints/complaint_export.csv`
    - Write CSV with header row and the same 15 records from `complaint_samples.json`
    - Columns in order: `complaint_id`, `threat_type`, `risk_level`, `risk_score`, `description`, `evidence_type`, `complaint_status`, `user_role`, `cert_escalation_status`, `timestamp`
    - Quote fields containing commas; UTF-8 encoding
    - _Requirements: 1.3, 9.2_

  - [x] 2.3 Create `fake_complaints/complaint_summary.md`
    - Write summary with sections: Overview, Distribution by Threat Type (table), Distribution by Risk Level (table), Distribution by Escalation Status (table), Sample Records
    - Tables must reflect the actual distribution in `complaint_samples.json`
    - _Requirements: 1.4_

- [x] 3. Create phishing_urls/ dataset files
  - [x] 3.1 Create `phishing_urls/phishing_links.txt`
    - Write 15+ fake phishing URLs, one per line, no headers
    - Cover all 4 domain categories: Banking_Phishing, Welfare_Portal_Spoofing, KYC_Fraud, APK_Distribution
    - Use typosquatting, subdomain abuse, and hyphenated impersonation patterns
    - All domains must be fake/non-existent
    - _Requirements: 2.1, 2.4, 2.5, 2.7_

  - [x] 3.2 Create `phishing_urls/malicious_domains.csv`
    - Write CSV with columns: `domain`, `category`, `risk_score`, `detection_label`, `first_seen_date`
    - 15+ records using bare domains extracted from `phishing_links.txt`
    - `detection_label` must be `Malicious` if `risk_score > 70`, else `Suspicious`
    - _Requirements: 2.2, 2.6_

  - [x] 3.3 Create `phishing_urls/url_risk_labels.json`
    - Write JSON array of 15+ URL risk objects with fields: `url`, `risk_score`, `threat_category`, `detection_label`, `source`
    - URLs must match entries in `phishing_links.txt`
    - `detection_label` derived from `risk_score` per the threshold rule
    - _Requirements: 2.3, 2.6_

- [x] 4. Create scam_messages/ dataset files
  - [x] 4.1 Create `scam_messages/sms_scams.txt`
    - Write 10+ fake SMS phishing messages, each separated by a blank line
    - Reference SPARSH pension, CSD canteen, Army welfare funds, ECHS, Sainik welfare boards
    - Cover at least 3 of the 6 scam categories; any inline URLs must match `phishing_links.txt`
    - _Requirements: 3.1, 3.5, 3.6, 3.7_

  - [x] 4.2 Create `scam_messages/whatsapp_scams.txt`
    - Write 10+ fake WhatsApp scam messages, each separated by a blank line
    - Include impersonation of defence officials and welfare scheme fraud
    - Cover at least 3 scam categories; inline URLs must match `phishing_links.txt`
    - _Requirements: 3.2, 3.5, 3.6, 3.7_

  - [x] 4.3 Create `scam_messages/telegram_scams.txt`
    - Write 10+ fake Telegram scam messages, each separated by a blank line
    - Include APK distribution links and fake defence group invitations
    - Cover at least 3 scam categories; inline URLs must match `phishing_links.txt`
    - _Requirements: 3.3, 3.5, 3.6, 3.7_

  - [x] 4.4 Create `scam_messages/social_engineering_samples.md`
    - Document 5+ annotated social engineering patterns with: Threat Category, Channel, Sample Message, Analysis, Indicators of Compromise
    - Each pattern must cover a distinct scam category
    - _Requirements: 3.4, 3.5_

- [x] 5. Create apk_samples/ dataset files
  - [x] 5.1 Create `apk_samples/fake_apk_alerts.json`
    - Write JSON array of 10+ APK alert records following the schema in the design
    - Cover all 4 malware behaviors and all 3 source channels
    - Impersonate SPARSH, ECHS, Army welfare, CSD canteen apps
    - Use `APK-2024-NNN` ID format and ISO 8601 timestamps
    - _Requirements: 4.1, 4.2, 4.5, 4.6, 4.7_

  - [x] 5.2 Create `apk_samples/suspicious_apk_names.txt`
    - Write 15+ suspicious APK filenames, one per line, all ending in `.apk`
    - Include version numbers, "official", "update", "verified" suffixes
    - _Requirements: 4.3, 4.5_

  - [x] 5.3 Create `apk_samples/apk_analysis_report.md`
    - Write report with sections: Overview, Threat Category Distribution (table), Malware Behavior Analysis (table), Risk Score Distribution (table), Source Channel Analysis (table), Common Indicators of Compromise, Recommendations
    - Tables must reflect actual distribution in `fake_apk_alerts.json`
    - _Requirements: 4.4_

- [x] 6. Create testing_exports/ dataset files
  - [x] 6.1 Create `testing_exports/ai_detection_results.csv`
    - Write CSV with 15+ records and columns: `record_id`, `input_type`, `threat_category`, `predicted_label`, `confidence_score`, `actual_label`, `is_correct`, `timestamp`
    - Cover all 5 input types (at least 2 records each) and all 5 threat categories
    - At least 85% of records must have `is_correct = True`
    - Use `DET-2024-NNNN` ID format
    - _Requirements: 5.1, 5.4, 5.5_

  - [x] 6.2 Create `testing_exports/dashboard_metrics.json`
    - Write JSON object with all required keys: `generated_at`, `total_threats_detected`, `breakdown_by_threat_category`, `average_risk_score`, `escalation_rate_percent`, `detection_accuracy_percent`, `total_complaints`, `escalated_complaints`, `resolved_complaints`, `pending_complaints`
    - `detection_accuracy_percent` must be >= 85.0; all 5 threat categories in breakdown; category counts must sum to `total_threats_detected`
    - _Requirements: 5.2, 5.6_

  - [x] 6.3 Create `testing_exports/cert_escalation_logs.txt`
    - Write 10+ structured log entries in the format: `[ISO8601] [LEVEL] complaint_id=RKS-YYYY-NNNN escalation_level=... action="..." analyst="..."`
    - All 3 escalation levels (L1_Alert, L2_Investigation, L3_CERT_Escalation) must be represented
    - All `complaint_id` values must match IDs in `complaint_samples.json`
    - _Requirements: 5.3, 5.7, 9.5_

- [x] 7. Create documentation files
  - [x] 7.1 Create `screenshots/README.md`
    - Explain the purpose of the screenshots folder
    - Document naming convention: `[category]_[description]_[YYYYMMDD].[ext]`
    - State acceptable formats (PNG, JPG) and recommended dimensions (1280×720 or higher)
    - _Requirements: 7.1, 7.2_

  - [x] 7.2 Create `dataset_references/source_references.md`
    - Cite at least 4 external sources: PhishTank, OpenPhish, Kaggle phishing datasets, CERT-In advisories
    - Each entry includes: Source Name, URL, Description, Relevance
    - _Requirements: 6.1_

  - [x] 7.3 Create `dataset_references/dataset_methodology.md`
    - Write all 7 required sections: Synthetic Data Generation, Seeded Threat Simulation, Manual Testing Methodology, Disclaimer, Dataset Limitations, Recommended Usage Guidelines, Seed Parameters
    - Disclaimer must explicitly state all data is synthetic
    - Document seed parameters: `DATASET_SEED = 42`, year range, ID starts, distribution targets
    - _Requirements: 6.2, 6.3, 6.4, 6.5_

  - [x] 7.4 Create root `README.md`
    - Write all 8 required sections: Project Purpose, Dataset Structure (with visual folder tree), Folder Descriptions, Usage Instructions, AI Testing Support, Research Usage, Disclaimer, Defence Cyber Awareness Context
    - Identify Rakshak AI as a Defence Cyber Safety Portal
    - Include disclaimer that all data is fake and for research/testing/educational use only
    - _Requirements: 8.1, 8.2, 8.3, 8.4, 8.5_

- [x] 8. Checkpoint — verify all files exist and are non-empty
  - Ensure all 20 required files are present and contain content
  - Ensure all JSON files parse without errors
  - Ensure all CSV files have correct headers
  - Ask the user if any content adjustments are needed before proceeding to tests.

- [x] 9. Write structural unit tests
  - [x] 9.1 Create `tests/test_structure.py` with file existence and structure tests
    - Assert all 20 required files exist at their specified paths
    - Assert `complaint_samples.json` array length >= 15
    - Assert `complaint_export.csv` has all 10 required columns in correct order
    - Assert `phishing_links.txt` non-empty line count >= 15
    - Assert `malicious_domains.csv` has all 5 required columns
    - Assert `url_risk_labels.json` array length >= 15
    - Assert `sms_scams.txt`, `whatsapp_scams.txt`, `telegram_scams.txt` each have >= 10 message blocks
    - Assert `social_engineering_samples.md` has at least 5 pattern headings
    - Assert `fake_apk_alerts.json` array length >= 10
    - Assert `suspicious_apk_names.txt` non-empty line count >= 15
    - Assert `ai_detection_results.csv` row count >= 15 and all 5 input types present
    - Assert `dashboard_metrics.json` has all required top-level keys, `detection_accuracy_percent >= 85.0`, all 5 threat categories in breakdown
    - Assert `cert_escalation_logs.txt` has >= 10 entries and all 3 escalation levels present
    - Assert `fake_apk_alerts.json` has all 4 malware behaviors and all 3 source values
    - Assert `complaint_samples.json` has all 5 threat types
    - Assert `malicious_domains.csv` has all 4 domain categories
    - Assert `source_references.md` has at least 4 source references
    - Assert `dataset_methodology.md` contains disclaimer text and seed parameters section
    - Assert root `README.md` has all 8 required section headings and a folder tree
    - Assert `screenshots/README.md` mentions naming convention, PNG/JPG, and dimensions
    - _Requirements: 1.1, 1.3, 1.4, 1.8, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.3, 3.4, 4.1, 4.3, 4.6, 4.7, 5.1, 5.2, 5.6, 5.7, 6.1, 6.3, 7.1, 8.1_

- [x] 10. Write property-based tests
  - [x] 10.1 Create `tests/test_properties.py` with Hypothesis property tests
    - Import shared fixtures from `conftest.py`
    - Each test must include the tag comment: `# Feature: rakshak-ai-research-dataset, Property N: ...`

  - [ ]* 10.2 Write property test for Property 1: Complaint Record Schema Completeness
    - **Property 1: Complaint Record Schema Completeness**
    - For each record in `complaint_samples.json`, assert all 10 required fields are present, non-null, and correctly typed
    - **Validates: Requirements 1.2**

  - [ ]* 10.3 Write property test for Property 2: Escalation Requires High Risk Score
    - **Property 2: Escalation Requires High Risk Score**
    - For each complaint record where `cert_escalation_status == "Escalated"`, assert `risk_score >= 70`
    - **Validates: Requirements 1.7**

  - [ ]* 10.4 Write property test for Property 3: URL Risk Label Schema Completeness
    - **Property 3: URL Risk Label Schema Completeness**
    - For each record in `url_risk_labels.json`, assert all 5 required fields are present, non-null, and correctly typed
    - **Validates: Requirements 2.3**

  - [ ]* 10.5 Write property test for Property 4: Detection Label Derived from Risk Score
    - **Property 4: Detection Label Derived from Risk Score**
    - For each record in `url_risk_labels.json` and `malicious_domains.csv`, assert `detection_label == "Malicious"` if `risk_score > 70`, else `"Suspicious"`
    - **Validates: Requirements 2.6**

  - [ ]* 10.6 Write property test for Property 5: Scam Message URLs Are Consistent with Phishing Dataset
    - **Property 5: Scam Message URLs Are Consistent with Phishing Dataset**
    - Extract all URLs from `sms_scams.txt`, `whatsapp_scams.txt`, `telegram_scams.txt`; assert each URL exists in `phishing_links.txt`
    - **Validates: Requirements 3.7**

  - [ ]* 10.7 Write property test for Property 6: APK Alert Record Schema Completeness
    - **Property 6: APK Alert Record Schema Completeness**
    - For each record in `fake_apk_alerts.json`, assert all 9 required fields are present, non-null, and correctly typed
    - **Validates: Requirements 4.2**

  - [ ]* 10.8 Write property test for Property 7: AI Detection Accuracy Is At Least 85%
    - **Property 7: AI Detection Accuracy Is At Least 85%**
    - Over all records in `ai_detection_results.csv`, assert proportion where `is_correct == "True"` is >= 0.85
    - **Validates: Requirements 5.5**

  - [ ]* 10.9 Write property test for Property 8: Threat Labels Are Consistent Across All Files
    - **Property 8: Threat Labels Are Consistent Across All Files**
    - Collect all `threat_type`/`threat_category` values from all dataset files; assert each is in the global enum: `{Phishing, APK_Malware, Impersonation, Banking_Fraud, OTP_Scam}`
    - **Validates: Requirements 9.1**

  - [ ]* 10.10 Write property test for Property 9: Complaint IDs Follow Consistent Format
    - **Property 9: Complaint IDs Follow Consistent Format**
    - For each `complaint_id` in `complaint_samples.json`, `complaint_export.csv`, and `cert_escalation_logs.txt`, assert it matches regex `RKS-\d{4}-\d{4}`
    - **Validates: Requirements 9.2**

  - [ ]* 10.11 Write property test for Property 10: All Timestamps Use ISO 8601 Format
    - **Property 10: All Timestamps Use ISO 8601 Format**
    - For each timestamp field across all dataset files, assert it conforms to `YYYY-MM-DDTHH:MM:SSZ`
    - **Validates: Requirements 9.3**

  - [ ]* 10.12 Write property test for Property 11: Risk Scores Are Integers in Range 0–100
    - **Property 11: Risk Scores Are Integers in Range 0–100**
    - For each `risk_score` value in complaint records, URL labels, domain records, APK alerts, and AI detection results, assert it is an integer in [0, 100]
    - **Validates: Requirements 1.6, 9.4**

  - [ ]* 10.13 Write property test for Property 12: Cross-File Complaint ID Referential Integrity
    - **Property 12: Cross-File Complaint ID Referential Integrity**
    - For each `complaint_id` in `cert_escalation_logs.txt`, assert it exists in `complaint_samples.json`
    - **Validates: Requirements 9.5**

- [x] 11. Write cross-file consistency tests
  - [x] 11.1 Create `tests/test_cross_file.py`
    - Assert all `complaint_id` values in `complaint_export.csv` match exactly those in `complaint_samples.json`
    - Assert all domains in `malicious_domains.csv` are extracted from URLs in `phishing_links.txt`
    - Assert all `url` values in `url_risk_labels.json` appear in `phishing_links.txt`
    - Assert `dashboard_metrics.json` category counts sum to `total_threats_detected`
    - Assert `complaint_export.csv` row count equals `complaint_samples.json` array length
    - _Requirements: 9.1, 9.2, 9.5_

- [x] 12. Final checkpoint — run all tests
  - Run `pytest tests/ -v` and ensure all tests pass
  - Fix any data inconsistencies surfaced by failing tests
  - Ask the user if questions arise before considering the implementation complete.

## Notes

- Tasks marked with `*` are optional and can be skipped for a faster MVP
- All data files must use UTF-8 encoding
- All IDs, timestamps, and enum values must be consistent across files before writing tests
- Property tests iterate over all records in each file (not sampled), satisfying the 100-iteration minimum
- Cross-file consistency tests in `test_cross_file.py` complement the property tests in `test_properties.py`
