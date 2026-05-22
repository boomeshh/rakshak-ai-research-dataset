"""
Property-based tests for the Rakshak AI Research Dataset.

These tests verify universal correctness properties across all records in all
dataset files. Each test iterates over every record in the relevant file(s) and
asserts that the property holds for every single record.

Hypothesis is imported as required by the design document, but since the data
comes from static files the tests use direct iteration rather than @given
decorators -- the "property-based" aspect is that the property is verified
universally across ALL records.
"""

import re

import pytest
from hypothesis import given, settings  # noqa: F401 -- imported as required by design

# ---------------------------------------------------------------------------
# Shared constants
# ---------------------------------------------------------------------------

ISO8601_RE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
COMPLAINT_ID_RE = re.compile(r"^RKS-\d{4}-\d{4}$")

VALID_THREAT_LABELS = {
    "Phishing",
    "APK_Malware",
    "Impersonation",
    "Banking_Fraud",
    "OTP_Scam",
}


# ===========================================================================
# Property 1: Complaint Record Schema Completeness
# ===========================================================================

def test_property_1_complaint_record_schema_completeness(complaint_samples):
    # Feature: rakshak-ai-research-dataset, Property 1: Complaint Record Schema Completeness
    # Validates: Requirements 1.2

    required_fields = {
        "complaint_id": str,
        "threat_type": str,
        "risk_level": str,
        "risk_score": int,
        "description": str,
        "evidence_type": str,
        "complaint_status": str,
        "user_role": str,
        "cert_escalation_status": str,
        "timestamp": str,
    }

    for record in complaint_samples:
        for field, expected_type in required_fields.items():
            assert field in record, (
                "Missing field '{}' in complaint record {}".format(
                    field, record.get("complaint_id", "<unknown>")
                )
            )
            assert record[field] is not None, (
                "Field '{}' is null in complaint record {}".format(
                    field, record.get("complaint_id", "<unknown>")
                )
            )
            assert isinstance(record[field], expected_type), (
                "Field '{}' has wrong type in record {}: expected {}, got {}".format(
                    field,
                    record.get("complaint_id", "<unknown>"),
                    expected_type.__name__,
                    type(record[field]).__name__,
                )
            )


# ===========================================================================
# Property 2: Escalation Requires High Risk Score
# ===========================================================================

def test_property_2_escalation_requires_high_risk_score(complaint_samples):
    # Feature: rakshak-ai-research-dataset, Property 2: Escalation Requires High Risk Score
    # Validates: Requirements 1.7

    for record in complaint_samples:
        if record.get("cert_escalation_status") == "Escalated":
            assert record["risk_score"] >= 70, (
                "Escalated complaint {} has risk_score {} which is below the required minimum of 70".format(
                    record["complaint_id"], record["risk_score"]
                )
            )


# ===========================================================================
# Property 3: URL Risk Label Schema Completeness
# ===========================================================================

def test_property_3_url_risk_label_schema_completeness(url_risk_labels):
    # Feature: rakshak-ai-research-dataset, Property 3: URL Risk Label Schema Completeness
    # Validates: Requirements 2.3

    required_fields = {
        "url": str,
        "risk_score": int,
        "threat_category": str,
        "detection_label": str,
        "source": str,
    }

    for record in url_risk_labels:
        for field, expected_type in required_fields.items():
            assert field in record, (
                "Missing field '{}' in URL risk label record {}".format(
                    field, record.get("url", "<unknown>")
                )
            )
            assert record[field] is not None, (
                "Field '{}' is null in URL risk label record {}".format(
                    field, record.get("url", "<unknown>")
                )
            )
            assert isinstance(record[field], expected_type), (
                "Field '{}' has wrong type in URL risk label record {}: expected {}, got {}".format(
                    field,
                    record.get("url", "<unknown>"),
                    expected_type.__name__,
                    type(record[field]).__name__,
                )
            )


# ===========================================================================
# Property 4: Detection Label Derived from Risk Score
# ===========================================================================

def test_property_4_detection_label_derived_from_risk_score(url_risk_labels, malicious_domains_rows):
    # Feature: rakshak-ai-research-dataset, Property 4: Detection Label Derived from Risk Score
    # Validates: Requirements 2.6

    for record in url_risk_labels:
        risk_score = record["risk_score"]
        detection_label = record["detection_label"]
        expected_label = "Malicious" if risk_score > 70 else "Suspicious"
        assert detection_label == expected_label, (
            "URL '{}' has risk_score={} but detection_label='{}'; expected '{}'".format(
                record["url"], risk_score, detection_label, expected_label
            )
        )

    for row in malicious_domains_rows:
        risk_score = int(row["risk_score"])
        detection_label = row["detection_label"]
        expected_label = "Malicious" if risk_score > 70 else "Suspicious"
        assert detection_label == expected_label, (
            "Domain '{}' has risk_score={} but detection_label='{}'; expected '{}'".format(
                row["domain"], risk_score, detection_label, expected_label
            )
        )


# ===========================================================================
# Property 5: Scam Message URLs Are Consistent with Phishing Dataset
# ===========================================================================

def test_property_5_scam_message_urls_consistent_with_phishing_dataset(
    sms_scams_text, whatsapp_scams_text, telegram_scams_text, phishing_links
):
    # Feature: rakshak-ai-research-dataset, Property 5: Scam Message URLs Are Consistent with Phishing Dataset
    # Validates: Requirements 3.7

    url_pattern = re.compile(r"https?://\S+")

    for source_name, text in [
        ("sms_scams.txt", sms_scams_text),
        ("whatsapp_scams.txt", whatsapp_scams_text),
        ("telegram_scams.txt", telegram_scams_text),
    ]:
        urls_in_text = url_pattern.findall(text)
        for url in urls_in_text:
            url = url.rstrip(".,;:!?)")
            assert url in phishing_links, (
                "URL '{}' found in {} is not present in phishing_links.txt".format(url, source_name)
            )


# ===========================================================================
# Property 6: APK Alert Record Schema Completeness
# ===========================================================================

def test_property_6_apk_alert_record_schema_completeness(fake_apk_alerts):
    # Feature: rakshak-ai-research-dataset, Property 6: APK Alert Record Schema Completeness
    # Validates: Requirements 4.2

    required_fields = {
        "apk_id": str,
        "apk_name": str,
        "package_name": str,
        "source": str,
        "malware_behavior": str,
        "installation_risk": str,
        "threat_category": str,
        "risk_score": int,
        "reported_date": str,
    }

    for record in fake_apk_alerts:
        for field, expected_type in required_fields.items():
            assert field in record, (
                "Missing field '{}' in APK alert record {}".format(
                    field, record.get("apk_id", "<unknown>")
                )
            )
            assert record[field] is not None, (
                "Field '{}' is null in APK alert record {}".format(
                    field, record.get("apk_id", "<unknown>")
                )
            )
            assert isinstance(record[field], expected_type), (
                "Field '{}' has wrong type in APK alert record {}: expected {}, got {}".format(
                    field,
                    record.get("apk_id", "<unknown>"),
                    expected_type.__name__,
                    type(record[field]).__name__,
                )
            )


# ===========================================================================
# Property 7: AI Detection Accuracy Is At Least 85%
# ===========================================================================

def test_property_7_ai_detection_accuracy_at_least_85_percent(ai_detection_results_rows):
    # Feature: rakshak-ai-research-dataset, Property 7: AI Detection Accuracy Is At Least 85%
    # Validates: Requirements 5.5

    total = len(ai_detection_results_rows)
    assert total > 0, "ai_detection_results.csv must contain at least one record"

    correct_count = sum(
        1 for row in ai_detection_results_rows if row["is_correct"] == "True"
    )
    accuracy = correct_count / total

    assert accuracy >= 0.85, (
        "AI detection accuracy is {:.2%} ({}/{}), which is below the required minimum of 85%".format(
            accuracy, correct_count, total
        )
    )


# ===========================================================================
# Property 8: Threat Labels Are Consistent Across All Files
# ===========================================================================

def test_property_8_threat_labels_consistent_across_all_files(
    complaint_samples,
    fake_apk_alerts,
    ai_detection_results_rows,
    dashboard_metrics,
):
    # Feature: rakshak-ai-research-dataset, Property 8: Threat Labels Are Consistent Across All Files
    # Validates: Requirements 9.1

    for record in complaint_samples:
        value = record["threat_type"]
        assert value in VALID_THREAT_LABELS, (
            "Invalid threat_type '{}' in complaint record {}".format(
                value, record.get("complaint_id", "<unknown>")
            )
        )

    for record in fake_apk_alerts:
        value = record["threat_category"]
        assert value in VALID_THREAT_LABELS, (
            "Invalid threat_category '{}' in APK alert record {}".format(
                value, record.get("apk_id", "<unknown>")
            )
        )

    for row in ai_detection_results_rows:
        value = row["threat_category"]
        assert value in VALID_THREAT_LABELS, (
            "Invalid threat_category '{}' in AI detection record {}".format(
                value, row.get("record_id", "<unknown>")
            )
        )

    breakdown = dashboard_metrics.get("breakdown_by_threat_category", {})
    for key in breakdown:
        assert key in VALID_THREAT_LABELS, (
            "Invalid threat category key '{}' in dashboard_metrics.json breakdown".format(key)
        )


# ===========================================================================
# Property 9: Complaint IDs Follow Consistent Format
# ===========================================================================

def test_property_9_complaint_ids_follow_consistent_format(
    complaint_samples, complaint_export_rows, cert_escalation_logs_text
):
    # Feature: rakshak-ai-research-dataset, Property 9: Complaint IDs Follow Consistent Format
    # Validates: Requirements 9.2

    for record in complaint_samples:
        cid = record["complaint_id"]
        assert COMPLAINT_ID_RE.match(cid), (
            "complaint_id '{}' in complaint_samples.json does not match pattern RKS-YYYY-NNNN".format(cid)
        )

    for row in complaint_export_rows:
        cid = row["complaint_id"]
        assert COMPLAINT_ID_RE.match(cid), (
            "complaint_id '{}' in complaint_export.csv does not match pattern RKS-YYYY-NNNN".format(cid)
        )

    log_ids = re.findall(r"complaint_id=(RKS-\d{4}-\d{4})", cert_escalation_logs_text)
    assert len(log_ids) > 0, "No complaint_ids found in cert_escalation_logs.txt"
    for cid in log_ids:
        assert COMPLAINT_ID_RE.match(cid), (
            "complaint_id '{}' in cert_escalation_logs.txt does not match pattern RKS-YYYY-NNNN".format(cid)
        )


# ===========================================================================
# Property 10: All Timestamps Use ISO 8601 Format
# ===========================================================================

def test_property_10_all_timestamps_use_iso8601_format(
    complaint_samples,
    fake_apk_alerts,
    ai_detection_results_rows,
    dashboard_metrics,
    cert_escalation_logs_text,
):
    # Feature: rakshak-ai-research-dataset, Property 10: All Timestamps Use ISO 8601 Format
    # Validates: Requirements 9.3

    for record in complaint_samples:
        ts = record["timestamp"]
        assert ISO8601_RE.match(ts), (
            "timestamp '{}' in complaint record {} does not conform to YYYY-MM-DDTHH:MM:SSZ".format(
                ts, record.get("complaint_id", "<unknown>")
            )
        )

    for record in fake_apk_alerts:
        ts = record["reported_date"]
        assert ISO8601_RE.match(ts), (
            "reported_date '{}' in APK alert record {} does not conform to YYYY-MM-DDTHH:MM:SSZ".format(
                ts, record.get("apk_id", "<unknown>")
            )
        )

    for row in ai_detection_results_rows:
        ts = row["timestamp"]
        assert ISO8601_RE.match(ts), (
            "timestamp '{}' in AI detection record {} does not conform to YYYY-MM-DDTHH:MM:SSZ".format(
                ts, row.get("record_id", "<unknown>")
            )
        )

    generated_at = dashboard_metrics.get("generated_at", "")
    assert ISO8601_RE.match(generated_at), (
        "generated_at '{}' in dashboard_metrics.json does not conform to YYYY-MM-DDTHH:MM:SSZ".format(
            generated_at
        )
    )

    log_timestamps = re.findall(
        r"\[(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z)\]", cert_escalation_logs_text
    )
    assert len(log_timestamps) > 0, "No timestamps found in cert_escalation_logs.txt"
    for ts in log_timestamps:
        assert ISO8601_RE.match(ts), (
            "Timestamp '{}' in cert_escalation_logs.txt does not conform to YYYY-MM-DDTHH:MM:SSZ".format(ts)
        )


# ===========================================================================
# Property 11: Risk Scores Are Integers in Range 0-100
# ===========================================================================

def test_property_11_risk_scores_are_integers_in_range_0_to_100(
    complaint_samples,
    url_risk_labels,
    malicious_domains_rows,
    fake_apk_alerts,
):
    # Feature: rakshak-ai-research-dataset, Property 11: Risk Scores Are Integers in Range 0-100
    # Validates: Requirements 1.6, 9.4

    for record in complaint_samples:
        score = record["risk_score"]
        assert isinstance(score, int), (
            "risk_score in complaint {} is not an int: {!r}".format(
                record.get("complaint_id", "<unknown>"), score
            )
        )
        assert 0 <= score <= 100, (
            "risk_score {} in complaint {} is out of range [0, 100]".format(
                score, record.get("complaint_id", "<unknown>")
            )
        )

    for record in url_risk_labels:
        score = record["risk_score"]
        assert isinstance(score, int), (
            "risk_score in URL record '{}' is not an int: {!r}".format(
                record.get("url", "<unknown>"), score
            )
        )
        assert 0 <= score <= 100, (
            "risk_score {} in URL record '{}' is out of range [0, 100]".format(
                score, record.get("url", "<unknown>")
            )
        )

    for row in malicious_domains_rows:
        score = int(row["risk_score"])
        assert 0 <= score <= 100, (
            "risk_score {} in domain record '{}' is out of range [0, 100]".format(
                score, row.get("domain", "<unknown>")
            )
        )

    for record in fake_apk_alerts:
        score = record["risk_score"]
        assert isinstance(score, int), (
            "risk_score in APK alert {} is not an int: {!r}".format(
                record.get("apk_id", "<unknown>"), score
            )
        )
        assert 0 <= score <= 100, (
            "risk_score {} in APK alert {} is out of range [0, 100]".format(
                score, record.get("apk_id", "<unknown>")
            )
        )


# ===========================================================================
# Property 12: Cross-File Complaint ID Referential Integrity
# ===========================================================================

def test_property_12_cross_file_complaint_id_referential_integrity(
    complaint_samples, cert_escalation_logs_text
):
    # Feature: rakshak-ai-research-dataset, Property 12: Cross-File Complaint ID Referential Integrity
    # Validates: Requirements 9.5

    valid_ids = {record["complaint_id"] for record in complaint_samples}

    log_ids = re.findall(r"complaint_id=(RKS-\d{4}-\d{4})", cert_escalation_logs_text)
    assert len(log_ids) > 0, "No complaint_ids found in cert_escalation_logs.txt"

    for cid in log_ids:
        assert cid in valid_ids, (
            "complaint_id '{}' in cert_escalation_logs.txt does not exist in complaint_samples.json".format(cid)
        )
