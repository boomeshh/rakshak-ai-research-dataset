# Screenshots

This folder is a designated space for visual evidence and UI screenshots that support the Rakshak AI Research Dataset documentation. Contributors can add screenshots of the Rakshak AI portal interface, threat detection dashboards, alert workflows, CERT escalation screens, or any other relevant UI captures that help illustrate how the dataset is used in practice.

---

## Purpose

Screenshots in this folder serve as supplementary documentation to:

- Illustrate the Rakshak AI portal's dashboard and analytics views
- Capture threat detection results and risk scoring outputs
- Document CERT escalation workflow states
- Provide visual context for AI model testing and evaluation results
- Support research papers, presentations, or technical reports referencing this dataset

---

## Naming Convention

All screenshot files must follow this naming pattern:

```
[category]_[description]_[YYYYMMDD].[ext]
```

| Component     | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `category`    | A short label for the area being captured (see categories below)            |
| `description` | A brief, lowercase, underscore-separated description of the screenshot      |
| `YYYYMMDD`    | The date the screenshot was taken, in `YYYYMMDD` format                     |
| `ext`         | File extension: `png` or `jpg`                                              |

### Examples

```
dashboard_threat_overview_20240815.png
escalation_l3_cert_alert_20240820.jpg
detection_apk_malware_result_20240901.png
complaints_high_risk_list_20240910.png
```

### Suggested Categories

| Category      | Description                                      |
|---------------|--------------------------------------------------|
| `dashboard`   | Portal dashboard and analytics views             |
| `detection`   | AI threat detection results and confidence scores|
| `escalation`  | CERT escalation workflow and alert screens       |
| `complaints`  | Complaint ingestion and management views         |
| `apk`         | APK analysis and malware alert screens           |
| `phishing`    | Phishing URL detection and risk label views      |
| `scam`        | Scam message classification results              |
| `misc`        | Any other relevant screenshots                   |

---

## Acceptable Formats and Dimensions

| Property            | Requirement                                      |
|---------------------|--------------------------------------------------|
| **File formats**    | PNG (preferred) or JPG                           |
| **Minimum dimensions** | 1280 × 720 pixels                            |
| **Recommended dimensions** | 1920 × 1080 pixels or higher            |
| **Colour mode**     | RGB (not CMYK)                                   |
| **File size**       | Keep under 5 MB per file where possible          |

PNG is preferred for UI screenshots because it is lossless and renders text and interface elements more clearly. JPG is acceptable for photographic content or when file size is a concern.

---

## How to Add Screenshots

1. **Capture the screenshot** at 1280 × 720 resolution or higher.
2. **Name the file** following the `[category]_[description]_[YYYYMMDD].[ext]` convention.
3. **Place the file** directly in this `screenshots/` folder.
4. **Do not commit** screenshots containing real personal data, real credentials, or any sensitive information. All screenshots must relate to synthetic/test data only.
5. **Update documentation** — if the screenshot illustrates a specific workflow or dataset feature, consider referencing it in the relevant section of the root `README.md` or the appropriate dataset file's documentation.

---

## Notes

- This folder does not contain any screenshots by default. It is a placeholder for contributor-added content.
- All screenshots added to this repository must relate exclusively to the Rakshak AI portal or the synthetic research dataset. Do not add unrelated images.
- Screenshots must not expose real user data, real threat intelligence, or any information outside the scope of this synthetic dataset.
