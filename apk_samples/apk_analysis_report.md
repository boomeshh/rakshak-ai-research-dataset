# APK Threat Analysis Report

## Overview

This report summarises the threat intelligence derived from the `fake_apk_alerts.json` dataset, which contains **12 synthetic APK alert records** representing suspicious Android applications targeting Indian defence personnel, veterans, and their families.

All APKs in this dataset impersonate legitimate Indian defence applications — including SPARSH pension portal, ECHS health scheme, Army Welfare apps, and CSD Canteen services — and were distributed through unofficial channels. The dataset is entirely synthetic and intended for AI/ML model training, mobile threat detection research, and CERT escalation workflow testing within the **Rakshak AI Defence Cyber Safety Portal**.

**Dataset Summary:**
- Total APK alert records: 12
- Date range: March 2024 – May 2024
- All records classified under threat category: `APK_Malware`
- Risk score range: 65 – 96
- All records carry `installation_risk` of High or Medium

---

## Threat Category Distribution

All APK samples in this dataset are classified under a single threat category, reflecting the focused scope of this dataset on mobile malware targeting defence applications.

| Threat Category | Count | Percentage |
|-----------------|-------|------------|
| APK_Malware     | 12    | 100%       |
| **Total**       | **12**| **100%**   |

> **Note for AI Training:** This dataset is intentionally homogeneous in threat category. When combined with complaint records and URL labels (which cover Phishing, Impersonation, Banking_Fraud, and OTP_Scam), the full multi-class threat taxonomy is represented across the repository.

---

## Malware Behavior Analysis

The dataset covers all four defined malware behavior categories with equal distribution, providing balanced training data for multi-class malware behavior classification models.

| Malware Behavior       | Count | Description                                                                                                   |
|------------------------|-------|---------------------------------------------------------------------------------------------------------------|
| Data_Exfiltration      | 3     | APK silently transmits device data (contacts, files, location) to a remote command-and-control server          |
| SMS_Interception       | 3     | APK intercepts incoming SMS messages, including OTPs and bank alerts, forwarding them to the attacker          |
| Remote_Access_Trojan   | 3     | APK installs a backdoor granting the attacker persistent remote control over the victim's device               |
| Credential_Harvesting  | 3     | APK presents fake login screens to capture usernames, passwords, and banking credentials                       |
| **Total**              | **12**|                                                                                                               |

**Affected APKs by Behavior:**

- **Data_Exfiltration:** `SPARSH_Official_Update.apk`, `SPARSH_Pension_Tracker.apk`, `ECHS_OPD_Booking_v3.apk`
- **SMS_Interception:** `ECHS_Card_Renewal_v2.apk`, `ECHS_Hospital_Locator_Official.apk`, `ArmyWelfare_Fund_Apply.apk`
- **Remote_Access_Trojan:** `ArmyWelfare_Portal_Verified.apk`, `ArmyWelfare_Scheme_Register.apk`, `CSD_Canteen_Order_Tracker.apk`
- **Credential_Harvesting:** `CSD_Canteen_App_Update.apk`, `CSD_Price_List_2024.apk`, `SPARSH_KYC_Verify.apk`

---

## Risk Score Distribution

Risk levels are derived from the `risk_score` field using the standard Rakshak AI scoring scale: High (75–100), Medium (40–74), Low (0–39).

| Risk Level | Count | Score Range | Percentage | APK IDs                                                                 |
|------------|-------|-------------|------------|-------------------------------------------------------------------------|
| High       | 9     | 75–100      | 75%        | APK-2024-001, 002, 003, 004, 005, 006, 007, 009, 012                   |
| Medium     | 3     | 40–74       | 25%        | APK-2024-008 (72), APK-2024-010 (68), APK-2024-011 (65)                |
| Low        | 0     | 0–39        | 0%         | —                                                                       |
| **Total**  | **12**|             | **100%**   |                                                                         |

**Score Statistics:**
- Minimum risk score: 65 (ArmyWelfare_Fund_Apply.apk)
- Maximum risk score: 96 (ArmyWelfare_Scheme_Register.apk)
- Average risk score: **84.7**
- Median risk score: **88.5**

The high concentration of High-risk records (75%) reflects the severe threat posed by APKs that impersonate trusted defence applications — users are more likely to grant elevated permissions to apps they believe are official.

---

## Source Channel Analysis

APKs were distributed through three unofficial channels. The dataset provides equal representation across all three channels to support balanced channel-attribution model training.

| Source Channel    | Count | Percentage | Description                                                                 |
|-------------------|-------|------------|-----------------------------------------------------------------------------|
| Telegram_Group    | 4     | 33.3%      | Distributed via fake defence-themed Telegram groups and channels            |
| WhatsApp_Link     | 4     | 33.3%      | Shared as download links in WhatsApp messages impersonating welfare offices |
| Third_Party_Store | 4     | 33.3%      | Hosted on unofficial APK mirror sites and third-party app stores            |
| **Total**         | **12**| **100%**   |                                                                             |

**APKs by Source Channel:**

- **Telegram_Group:** `SPARSH_Official_Update.apk`, `CSD_Canteen_App_Update.apk`, `ArmyWelfare_Scheme_Register.apk`, `ECHS_OPD_Booking_v3.apk`
- **WhatsApp_Link:** `ECHS_Card_Renewal_v2.apk`, `SPARSH_Pension_Tracker.apk`, `CSD_Price_List_2024.apk`, `ArmyWelfare_Fund_Apply.apk`
- **Third_Party_Store:** `ArmyWelfare_Portal_Verified.apk`, `ECHS_Hospital_Locator_Official.apk`, `SPARSH_KYC_Verify.apk`, `CSD_Canteen_Order_Tracker.apk`

---

## Common Indicators of Compromise

The following Indicators of Compromise (IOCs) are observed across the APK samples in this dataset. These can be used to build detection signatures, train classification models, and configure alert rules in the Rakshak AI portal.

### Package Name Patterns
- Package names mimicking official apps with added suffixes: `.fake`, `.update`, `.official`, `.verified`
- Examples: `com.sparsh.defence.update`, `com.echs.card.renewal.official`, `com.army.welfare.portal.verified`
- Pattern: `com\.(sparsh|echs|army|csd)\.[a-z.]+\.(fake|update|official|verified|register|tracker)`

### APK Filename Patterns
- Filenames containing trust-inducing keywords: `Official`, `Verified`, `Update`, `v2`, `v3`
- Impersonation of known defence brands: `SPARSH`, `ECHS`, `ArmyWelfare`, `CSD`
- Examples: `SPARSH_Official_Update.apk`, `ECHS_Card_Renewal_v2.apk`, `ArmyWelfare_Portal_Verified.apk`

### Behavioural IOCs
- **Excessive permission requests** at install time (SMS read, contacts, camera, microphone)
- **Background network activity** to non-official domains immediately after installation
- **Overlay attacks** — fake login screens rendered over legitimate banking apps
- **SMS forwarding** to attacker-controlled numbers (observed in SMS_Interception samples)
- **Persistence mechanisms** — APK registers as device administrator to prevent uninstallation

### Distribution IOCs
- APK download links shared via Telegram groups with names like "Army Welfare Official", "SPARSH Updates", "Defence Personnel Group"
- WhatsApp messages from unknown numbers claiming to be from welfare offices, containing direct APK download links
- Third-party store listings with inflated fake review counts and copied official app descriptions

### Risk Score Thresholds
- All 12 samples score ≥ 65, with 9 of 12 scoring ≥ 75 (High risk)
- Remote_Access_Trojan samples carry the highest average risk score (~93.3), reflecting their persistent and severe impact
- No Low-risk APKs present in this dataset — all samples represent active threats

---

## Recommendations

### For AI/ML Model Training

1. **Multi-label classification:** Use the `malware_behavior` field as the primary classification target. The balanced 3-record-per-class distribution (Data_Exfiltration, SMS_Interception, Remote_Access_Trojan, Credential_Harvesting) provides equal class representation for training.

2. **Risk score regression:** The `risk_score` field (range 65–96 in this dataset) can serve as a continuous regression target for APK threat severity prediction models.

3. **Source attribution:** The equal distribution across `Telegram_Group`, `WhatsApp_Link`, and `Third_Party_Store` supports training channel-attribution classifiers without class imbalance correction.

4. **Feature engineering:** Extract features from `apk_name` and `package_name` fields — keyword presence (`Official`, `Verified`, `Update`), brand impersonation tokens (`sparsh`, `echs`, `army`, `csd`), and package suffix patterns are strong discriminative features.

5. **Augmentation guidance:** This dataset contains 12 records. For production model training, augment with additional synthetic samples maintaining the same schema and distribution targets. Use `DATASET_SEED = 42` for reproducible augmentation.

### For CERT Escalation Workflow Testing

6. **High-risk alert routing:** All 9 High-risk APKs (risk_score ≥ 75) should trigger L2_Investigation or L3_CERT_Escalation in workflow tests. Use these records to validate escalation threshold logic.

7. **Medium-risk triage:** The 3 Medium-risk APKs (APK-2024-008, 010, 011) are suitable for testing L1_Alert handling and analyst triage queues.

### For Dashboard Analytics

8. **Metric seeding:** The average risk score of 84.7 and 75% High-risk rate can be used to seed the `dashboard_metrics.json` APK-specific analytics fields.

9. **Trend simulation:** The `reported_date` range (March–May 2024) supports time-series visualisation of APK threat trends in the Rakshak AI portal dashboard.

### Dataset Limitations

- All 12 records are classified as `APK_Malware` — this dataset does not cover benign APK samples. Combine with benign app metadata for binary classification tasks.
- Risk scores are synthetically assigned and do not reflect real dynamic analysis results (sandbox detonation, static code analysis).
- Package names and APK filenames are fictional and do not correspond to real applications on any app store.
- All data is synthetic and must not be used for real threat intelligence, law enforcement, or production security operations.
