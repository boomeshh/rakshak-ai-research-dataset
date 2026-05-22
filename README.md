# Rakshak AI Research Dataset

> **Disclaimer:** All data in this repository is entirely synthetic and fake. It is generated solely for research, testing, and educational purposes. No real individuals, organisations, incidents, or systems are represented.

---

## 1. Project Purpose

**Rakshak AI** is a Defence Cyber Safety Portal designed to protect Indian defence personnel, veterans, and their families from cyber threats including phishing, APK malware, social engineering scams, and banking fraud.

This repository provides a structured, synthetic research dataset to support the development and evaluation of the Rakshak AI platform. It is intended for:

- AI/ML engineers building threat classification and risk scoring models
- NLP researchers developing scam message detection pipelines
- QA engineers validating dashboard analytics and CERT escalation workflows
- Security researchers studying Indian defence-related cyber threat patterns

All dataset files are pre-generated, reproducible, and self-consistent. They model realistic Indian defence cyber threat scenarios without using any real data.

---

## 2. Dataset Structure

```
rakshak-ai-research-dataset/
├── fake_complaints/
│   ├── complaint_samples.json
│   ├── complaint_export.csv
│   └── complaint_summary.md
├── phishing_urls/
│   ├── phishing_links.txt
│   ├── malicious_domains.csv
│   └── url_risk_labels.json
├── scam_messages/
│   ├── sms_scams.txt
│   ├── whatsapp_scams.txt
│   ├── telegram_scams.txt
│   └── social_engineering_samples.md
├── apk_samples/
│   ├── fake_apk_alerts.json
│   ├── suspicious_apk_names.txt
│   └── apk_analysis_report.md
├── testing_exports/
│   ├── ai_detection_results.csv
│   ├── dashboard_metrics.json
│   └── cert_escalation_logs.txt
├── screenshots/
│   └── README.md
├── dataset_references/
│   ├── source_references.md
│   └── dataset_methodology.md
└── README.md
```

---

## 3. Folder Descriptions

| Folder | Description |
|--------|-------------|
| `fake_complaints/` | Structured fake complaint records in JSON and CSV format, covering 5 threat types across 3 user roles (Defence Personnel, Veteran, Family Member). Includes a summary markdown with distribution tables. |
| `phishing_urls/` | Fake phishing URLs and domain metadata for URL-based threat detection model training. Covers Banking Phishing, Welfare Portal Spoofing, KYC Fraud, and APK Distribution categories. |
| `scam_messages/` | Synthetic scam messages across SMS, WhatsApp, and Telegram channels. Includes annotated social engineering patterns for NLP model training. |
| `apk_samples/` | Metadata for fake malicious APK files impersonating Indian defence apps (SPARSH, ECHS, Army welfare, CSD canteen). Includes an analysis report with threat distribution tables. |
| `testing_exports/` | Pre-generated AI detection results, dashboard metrics, and CERT escalation logs for validating the Rakshak AI portal without live data. |
| `screenshots/` | Placeholder folder for visual evidence and UI screenshots. See `screenshots/README.md` for naming conventions and contribution guidelines. |
| `dataset_references/` | Documentation of external reference sources and the data generation methodology, including seed parameters and usage guidelines. |

---

## 4. Usage Instructions

### Prerequisites

- Python 3.8 or higher (for running tests and data validation scripts)
- `pip install hypothesis pytest` (for property-based and structural tests)

### Loading Dataset Files

**JSON files:**
```python
import json

with open("fake_complaints/complaint_samples.json", encoding="utf-8") as f:
    complaints = json.load(f)
```

**CSV files:**
```python
import csv

with open("fake_complaints/complaint_export.csv", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    records = list(reader)
```

**Plain text files (one entry per line):**
```python
with open("phishing_urls/phishing_links.txt", encoding="utf-8") as f:
    urls = [line.strip() for line in f if line.strip()]
```

### Running Tests

```bash
# Run all structural and property-based tests
pytest tests/ -v

# Run only structural unit tests
pytest tests/test_structure.py -v

# Run only property-based tests
pytest tests/test_properties.py -v

# Run cross-file consistency tests
pytest tests/test_cross_file.py -v
```

### File Encoding

All files use **UTF-8** encoding. When reading CSV files, handle BOM if present by using `encoding="utf-8-sig"` as a fallback.

---

## 5. AI Testing Support

This dataset is designed to support the following AI/ML testing scenarios within the Rakshak AI portal:

### Threat Classification
- **URL classification**: Use `phishing_urls/url_risk_labels.json` and `phishing_urls/malicious_domains.csv` to train and evaluate URL-based threat detection models across 4 domain categories.
- **Text classification**: Use `scam_messages/sms_scams.txt`, `whatsapp_scams.txt`, and `telegram_scams.txt` to train NLP models for scam message detection across 6 scam categories.
- **APK threat detection**: Use `apk_samples/fake_apk_alerts.json` to test malware classification pipelines covering 4 malware behaviour types.

### Risk Scoring
- All records include a `risk_score` (integer, 0–100) with consistent thresholds:
  - **High**: 75–100
  - **Medium**: 40–74
  - **Low**: 0–39
- Detection labels (`Malicious` / `Suspicious`) are derived from risk scores using a threshold of 70.

### Dashboard Analytics
- `testing_exports/dashboard_metrics.json` provides pre-aggregated metrics to seed the Rakshak AI portal analytics view, including total threats detected, breakdown by category, average risk score, escalation rate, and detection accuracy.

### CERT Escalation Testing
- `testing_exports/cert_escalation_logs.txt` contains structured log entries covering all 3 escalation levels: `L1_Alert`, `L2_Investigation`, and `L3_CERT_Escalation`.
- `fake_complaints/complaint_samples.json` includes complaint records with `cert_escalation_status` values (`Pending`, `Escalated`, `Resolved`) for end-to-end escalation workflow testing.

### Real-Time Alert Simulation
- `testing_exports/ai_detection_results.csv` provides pre-generated detection results with confidence scores, predicted labels, and actual labels to simulate real-time alert generation without live inference.
- The dataset maintains a simulated detection accuracy of **≥ 85%** (`is_correct = True` for at least 85% of records).

---

## 6. Research Usage

### Intended Use Cases

- **AI/ML model training**: Use JSON and CSV files as labelled training data for threat classification, risk scoring, and anomaly detection models.
- **NLP research**: Use scam message files for text classification, intent detection, and phishing language pattern analysis.
- **Dashboard prototyping**: Use `dashboard_metrics.json` to prototype and test analytics dashboards without requiring a live data pipeline.
- **CERT workflow simulation**: Use complaint records and escalation logs to simulate and validate CERT triage and escalation workflows.
- **Security awareness research**: Use social engineering samples and annotated patterns to study manipulation techniques targeting defence personnel.

### Data Consistency Guarantees

All cross-file references are consistent:
- `complaint_id` values in `cert_escalation_logs.txt` match records in `complaint_samples.json`
- URLs in scam message files match entries in `phishing_links.txt`
- Domains in `malicious_domains.csv` are extracted from `phishing_links.txt`
- Threat category labels are consistent across all files using the global enum: `Phishing`, `APK_Malware`, `Impersonation`, `Banking_Fraud`, `OTP_Scam`

### Reproducibility

The dataset is generated using a fixed seed (`DATASET_SEED = 42`) for reproducibility. See `dataset_references/dataset_methodology.md` for full seed parameters and generation methodology.

### Citation and References

If you use this dataset in research, please refer to `dataset_references/source_references.md` for the external sources that informed the dataset design, including PhishTank, OpenPhish, Kaggle phishing datasets, and CERT-In advisories.

---

## 7. Disclaimer

> **All data in this repository is entirely fake and synthetic.**
>
> - No real individuals, defence personnel, veterans, or family members are represented.
> - No real organisations, government bodies, banks, or defence establishments are represented.
> - No real cyber incidents, complaints, or threat events are described.
> - All URLs, domain names, APK names, package names, and phone numbers are fictitious.
> - All complaint IDs, detection results, and log entries are generated for testing purposes only.
>
> This dataset is intended **solely for research, testing, and educational use**. It must not be used to train models intended for deployment without additional validation on real-world data. It must not be used to generate, distribute, or promote actual phishing content, malware, or scam messages.
>
> The Rakshak AI Research Dataset is provided as-is, without warranty of any kind.

---

## 8. Defence Cyber Awareness Context

### The Threat Landscape

Indian defence personnel, veterans, and their families face a growing range of targeted cyber threats. Attackers exploit the trust associated with official defence services and welfare schemes to conduct fraud, steal credentials, and distribute malware.

Common threat vectors modelled in this dataset include:

- **SPARSH pension portal phishing**: Fake websites impersonating the SPARSH (System for Pension Administration Raksha) portal to harvest login credentials and OTPs from veterans.
- **ECHS impersonation**: Fraudulent messages and websites mimicking the Ex-Servicemen Contributory Health Scheme (ECHS) to conduct KYC fraud and banking scams.
- **CSD canteen fraud**: Scam messages targeting Canteen Stores Department (CSD) canteen card holders with fake discount offers and account update requests.
- **Army welfare fund scams**: Messages impersonating Army Welfare Education Society (AWES), Army Group Insurance Fund (AGIF), and Sainik welfare boards to solicit payments or personal information.
- **Malicious APK distribution**: Fake Android apps distributed via WhatsApp and Telegram groups, impersonating official defence apps to perform data exfiltration, SMS interception, and remote access.
- **Defence official impersonation**: Social engineering attacks where attackers pose as commanding officers, welfare officers, or CERT personnel to manipulate targets into sharing sensitive information.

### Why This Dataset Matters

The Rakshak AI portal aims to detect, classify, and escalate these threats in real time. Building effective AI models for this domain requires labelled training data that reflects the specific language patterns, domain names, and social engineering techniques used in Indian defence-targeted attacks.

This synthetic dataset provides a safe, reproducible, and ethically sound foundation for that model development — enabling researchers and engineers to build and test threat detection systems without exposing real victim data or operational security information.

### Key Indian Defence Cyber Safety Resources

- **CERT-In** (Indian Computer Emergency Response Team): [https://www.cert-in.org.in](https://www.cert-in.org.in)
- **SPARSH Portal** (official): [https://sparsh.defencepensions.gov.in](https://sparsh.defencepensions.gov.in)
- **ECHS** (official): [https://echs.gov.in](https://echs.gov.in)
- **Cyber Dost** (MHA cyber safety initiative): [https://cyberdost.mha.gov.in](https://cyberdost.mha.gov.in)

---

*Rakshak AI Research Dataset — maintained for the Rakshak AI Defence Cyber Safety Portal.*
