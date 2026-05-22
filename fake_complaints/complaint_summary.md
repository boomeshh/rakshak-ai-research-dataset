# Complaint Dataset Summary

## Overview

This dataset contains **15 synthetic complaint records** submitted to the Rakshak AI Defence Cyber Safety Portal. All records are fabricated for research, testing, and educational purposes — no real individuals or incidents are represented.

The complaints span five threat categories targeting Indian defence personnel, veterans, and their family members. Records cover a range of risk levels and escalation outcomes, making the dataset suitable for training and evaluating AI-based threat detection and triage models.

- **Total Records:** 15
- **Date Range:** 2024-03-15 to 2024-03-29
- **User Roles Covered:** Defence_Personnel, Veteran, Family_Member
- **ID Format:** `RKS-2024-NNNN`

---

## Distribution by Threat Type

| Threat Type    | Count | Percentage |
|----------------|-------|------------|
| Phishing       | 3     | 20.0%      |
| APK_Malware    | 3     | 20.0%      |
| Impersonation  | 3     | 20.0%      |
| Banking_Fraud  | 3     | 20.0%      |
| OTP_Scam       | 3     | 20.0%      |
| **Total**      | **15**| **100.0%** |

All five threat types are equally represented, ensuring balanced coverage for model training across all categories.

---

## Distribution by Risk Level

| Risk Level | Count | Avg Risk Score |
|------------|-------|----------------|
| High       | 6     | 83.5           |
| Medium     | 6     | 59.5           |
| Low        | 3     | 31.7           |
| **Total**  | **15**| —              |

High-risk records (risk_score ≥ 70) account for 40% of the dataset. Medium-risk records make up another 40%, and Low-risk records represent 20%.

---

## Distribution by Escalation Status

| cert_escalation_status | Count |
|------------------------|-------|
| Escalated              | 6     |
| Pending                | 4     |
| Resolved               | 5     |
| **Total**              | **15**|

All 6 escalated records have a `risk_score >= 70`, consistent with the escalation threshold rule. The 5 resolved records span all risk levels, reflecting real-world complaint lifecycle outcomes.

---

## Sample Records

### Record 1 — RKS-2024-0001

| Field                   | Value                                                                                                      |
|-------------------------|------------------------------------------------------------------------------------------------------------|
| complaint_id            | RKS-2024-0001                                                                                              |
| threat_type             | Phishing                                                                                                   |
| risk_level              | High                                                                                                       |
| risk_score              | 88                                                                                                         |
| description             | Received a fake SMS claiming to be from SBI defence salary account asking to click a link to verify KYC details immediately. |
| evidence_type           | Screenshot                                                                                                 |
| complaint_status        | Open                                                                                                       |
| user_role               | Defence_Personnel                                                                                          |
| cert_escalation_status  | Escalated                                                                                                  |
| timestamp               | 2024-03-15T10:30:00Z                                                                                       |

---

### Record 2 — RKS-2024-0007

| Field                   | Value                                                                                                      |
|-------------------------|------------------------------------------------------------------------------------------------------------|
| complaint_id            | RKS-2024-0007                                                                                              |
| threat_type             | APK_Malware                                                                                                |
| risk_level              | High                                                                                                       |
| risk_score              | 76                                                                                                         |
| description             | Suspicious APK named CSD_Canteen_App_v2.apk distributed via WhatsApp group was found harvesting credentials. |
| evidence_type           | APK_Hash                                                                                                   |
| complaint_status        | Under_Review                                                                                               |
| user_role               | Defence_Personnel                                                                                          |
| cert_escalation_status  | Escalated                                                                                                  |
| timestamp               | 2024-03-21T07:50:00Z                                                                                       |

---

### Record 3 — RKS-2024-0013

| Field                   | Value                                                                                                      |
|-------------------------|------------------------------------------------------------------------------------------------------------|
| complaint_id            | RKS-2024-0013                                                                                              |
| threat_type             | OTP_Scam                                                                                                   |
| risk_level              | Medium                                                                                                     |
| risk_score              | 47                                                                                                         |
| description             | Received fake ECHS hospital appointment confirmation SMS with a link asking for OTP to confirm the booking. |
| evidence_type           | SMS_Log                                                                                                    |
| complaint_status        | Under_Review                                                                                               |
| user_role               | Family_Member                                                                                              |
| cert_escalation_status  | Pending                                                                                                    |
| timestamp               | 2024-03-27T08:30:00Z                                                                                       |
