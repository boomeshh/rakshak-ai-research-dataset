"""
Structural unit tests for the Rakshak AI Research Dataset.

Validates file existence, schema completeness, minimum record counts,
required column sets, enumeration coverage, and content constraints
across all 20 required dataset files.

Requirements: 1.1, 1.3, 1.4, 1.8, 2.1, 2.2, 2.3, 2.5, 3.1, 3.2, 3.3, 3.4,
              4.1, 4.3, 4.6, 4.7, 5.1, 5.2, 5.6, 5.7, 6.1, 6.3, 7.1, 8.1
"""

import csv
import re
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent


def _path(*parts: str) -> Path:
    return REPO_ROOT.joinpath(*parts)


# ---------------------------------------------------------------------------
# 1. File existence — all 20 required files
# ---------------------------------------------------------------------------

REQUIRED_FILES = [
    "fake_complaints/complaint_samples.json",
    "fake_complaints/complaint_export.csv",
    "fake_complaints/complaint_summary.md",
    "phishing_urls/phishing_links.txt",
    "phishing_urls/malicious_domains.csv",
    "phishing_urls/url_risk_labels.json",
    "scam_messages/sms_scams.txt",
    "scam_messages/whatsapp_scams.txt",
    "scam_messages/telegram_scams.txt",
    "scam_messages/social_engineering_samples.md",
    "apk_samples/fake_apk_alerts.json",
    "apk_samples/suspicious_apk_names.txt",
    "apk_samples/apk_analysis_report.md",
    "testing_exports/ai_detection_results.csv",
    "testing_exports/dashboard_metrics.json",
    "testing_exports/cert_escalation_logs.txt",
    "screenshots/README.md",
    "dataset_references/source_references.md",
    "dataset_references/dataset_methodology.md",
    "README.md",
]


@pytest.mark.parametrize("relative_path", REQUIRED_FILES)
def test_required_file_exists(relative_path):
    """Assert every required file exists at its specified path (Req 1.1, 8.1)."""
    assert _path(relative_path).is_file(), (
        f"Required file not found: {relative_path}"
    )


# ---------------------------------------------------------------------------
# 2. complaint_samples.json — array length and threat type coverage
# ---------------------------------------------------------------------------


def test_complaint_samples_min_length(complaint_samples):
    """Assert complaint_samples.json has at least 15 records (Req 1.1)."""
    assert len(complaint_samples) >= 15, (
        f"Expected >= 15 complaint records, got {len(complaint_samples)}"
    )


def test_complaint_samples_all_threat_types(complaint_samples):
    """Assert all 5 threat types are present in complaint_samples.json (Req 1.8)."""
    required_types = {"Phishing", "APK_Malware", "Impersonation", "Banking_Fraud", "OTP_Scam"}
    found_types = {r["threat_type"] for r in complaint_samples}
    missing = required_types - found_types
    assert not missing, f"Missing threat types in complaint_samples.json: {missing}"


# ---------------------------------------------------------------------------
# 3. complaint_export.csv — columns in correct order
# ---------------------------------------------------------------------------

COMPLAINT_EXPORT_COLUMNS = [
    "complaint_id",
    "threat_type",
    "risk_level",
    "risk_score",
    "description",
    "evidence_type",
    "complaint_status",
    "user_role",
    "cert_escalation_status",
    "timestamp",
]


def test_complaint_export_columns(complaint_export_rows):
    """Assert complaint_export.csv has all 10 required columns in correct order (Req 1.3)."""
    if not complaint_export_rows:
        pytest.fail("complaint_export.csv has no rows")
    actual_columns = list(complaint_export_rows[0].keys())
    assert actual_columns == COMPLAINT_EXPORT_COLUMNS, (
        f"Column mismatch.\nExpected: {COMPLAINT_EXPORT_COLUMNS}\nActual:   {actual_columns}"
    )


# ---------------------------------------------------------------------------
# 4. phishing_links.txt — non-empty line count
# ---------------------------------------------------------------------------


def test_phishing_links_min_count(phishing_links):
    """Assert phishing_links.txt has at least 15 non-empty lines (Req 2.1)."""
    assert len(phishing_links) >= 15, (
        f"Expected >= 15 phishing links, got {len(phishing_links)}"
    )


# ---------------------------------------------------------------------------
# 5. malicious_domains.csv — required columns and category coverage
# ---------------------------------------------------------------------------

MALICIOUS_DOMAINS_COLUMNS = {"domain", "category", "risk_score", "detection_label", "first_seen_date"}
REQUIRED_DOMAIN_CATEGORIES = {"Banking_Phishing", "Welfare_Portal_Spoofing", "KYC_Fraud", "APK_Distribution"}


def test_malicious_domains_columns(malicious_domains_rows):
    """Assert malicious_domains.csv has all 5 required columns (Req 2.2)."""
    if not malicious_domains_rows:
        pytest.fail("malicious_domains.csv has no rows")
    actual_columns = set(malicious_domains_rows[0].keys())
    missing = MALICIOUS_DOMAINS_COLUMNS - actual_columns
    assert not missing, f"Missing columns in malicious_domains.csv: {missing}"


def test_malicious_domains_all_categories(malicious_domains_rows):
    """Assert all 4 domain categories are present in malicious_domains.csv (Req 2.5)."""
    found_categories = {r["category"] for r in malicious_domains_rows}
    missing = REQUIRED_DOMAIN_CATEGORIES - found_categories
    assert not missing, f"Missing domain categories in malicious_domains.csv: {missing}"


# ---------------------------------------------------------------------------
# 6. url_risk_labels.json — array length
# ---------------------------------------------------------------------------


def test_url_risk_labels_min_length(url_risk_labels):
    """Assert url_risk_labels.json has at least 15 records (Req 2.3)."""
    assert len(url_risk_labels) >= 15, (
        f"Expected >= 15 URL risk label records, got {len(url_risk_labels)}"
    )


# ---------------------------------------------------------------------------
# 7. Scam message files — >= 10 message blocks each
# ---------------------------------------------------------------------------


def _count_message_blocks(text: str) -> int:
    """Count non-empty paragraphs separated by blank lines."""
    blocks = re.split(r"\n\s*\n", text.strip())
    return sum(1 for b in blocks if b.strip())


def test_sms_scams_min_blocks(sms_scams_text):
    """Assert sms_scams.txt has at least 10 message blocks (Req 3.1)."""
    count = _count_message_blocks(sms_scams_text)
    assert count >= 10, f"Expected >= 10 SMS scam blocks, got {count}"


def test_whatsapp_scams_min_blocks(whatsapp_scams_text):
    """Assert whatsapp_scams.txt has at least 10 message blocks (Req 3.2)."""
    count = _count_message_blocks(whatsapp_scams_text)
    assert count >= 10, f"Expected >= 10 WhatsApp scam blocks, got {count}"


def test_telegram_scams_min_blocks(telegram_scams_text):
    """Assert telegram_scams.txt has at least 10 message blocks (Req 3.3)."""
    count = _count_message_blocks(telegram_scams_text)
    assert count >= 10, f"Expected >= 10 Telegram scam blocks, got {count}"


# ---------------------------------------------------------------------------
# 8. social_engineering_samples.md — at least 5 pattern headings
# ---------------------------------------------------------------------------


def test_social_engineering_min_patterns(social_engineering_text):
    """Assert social_engineering_samples.md has at least 5 '## Pattern' headings (Req 3.4)."""
    pattern_headings = re.findall(r"^## Pattern", social_engineering_text, re.MULTILINE)
    assert len(pattern_headings) >= 5, (
        f"Expected >= 5 '## Pattern' headings, got {len(pattern_headings)}"
    )


# ---------------------------------------------------------------------------
# 9. fake_apk_alerts.json — array length, malware behaviors, source values
# ---------------------------------------------------------------------------

REQUIRED_MALWARE_BEHAVIORS = {
    "Data_Exfiltration",
    "SMS_Interception",
    "Remote_Access_Trojan",
    "Credential_Harvesting",
}
REQUIRED_APK_SOURCES = {"Telegram_Group", "WhatsApp_Link", "Third_Party_Store"}


def test_fake_apk_alerts_min_length(fake_apk_alerts):
    """Assert fake_apk_alerts.json has at least 10 records (Req 4.1)."""
    assert len(fake_apk_alerts) >= 10, (
        f"Expected >= 10 APK alert records, got {len(fake_apk_alerts)}"
    )


def test_fake_apk_alerts_all_malware_behaviors(fake_apk_alerts):
    """Assert all 4 malware behaviors are present in fake_apk_alerts.json (Req 4.6)."""
    found_behaviors = {r["malware_behavior"] for r in fake_apk_alerts}
    missing = REQUIRED_MALWARE_BEHAVIORS - found_behaviors
    assert not missing, f"Missing malware behaviors in fake_apk_alerts.json: {missing}"


def test_fake_apk_alerts_all_sources(fake_apk_alerts):
    """Assert all 3 source values are present in fake_apk_alerts.json (Req 4.7)."""
    found_sources = {r["source"] for r in fake_apk_alerts}
    missing = REQUIRED_APK_SOURCES - found_sources
    assert not missing, f"Missing source values in fake_apk_alerts.json: {missing}"


# ---------------------------------------------------------------------------
# 10. suspicious_apk_names.txt — non-empty line count
# ---------------------------------------------------------------------------


def test_suspicious_apk_names_min_count(suspicious_apk_names):
    """Assert suspicious_apk_names.txt has at least 15 non-empty lines (Req 4.3)."""
    assert len(suspicious_apk_names) >= 15, (
        f"Expected >= 15 suspicious APK names, got {len(suspicious_apk_names)}"
    )


# ---------------------------------------------------------------------------
# 11. ai_detection_results.csv — row count and all 5 input types
# ---------------------------------------------------------------------------

REQUIRED_INPUT_TYPES = {"URL", "SMS", "WhatsApp", "Telegram", "APK"}


def test_ai_detection_results_min_rows(ai_detection_results_rows):
    """Assert ai_detection_results.csv has at least 15 rows (Req 5.1)."""
    assert len(ai_detection_results_rows) >= 15, (
        f"Expected >= 15 AI detection result rows, got {len(ai_detection_results_rows)}"
    )


def test_ai_detection_results_all_input_types(ai_detection_results_rows):
    """Assert all 5 input types are present in ai_detection_results.csv (Req 5.1)."""
    found_types = {r["input_type"] for r in ai_detection_results_rows}
    missing = REQUIRED_INPUT_TYPES - found_types
    assert not missing, f"Missing input types in ai_detection_results.csv: {missing}"


# ---------------------------------------------------------------------------
# 12. dashboard_metrics.json — required keys, accuracy, threat categories
# ---------------------------------------------------------------------------

REQUIRED_DASHBOARD_KEYS = {
    "generated_at",
    "total_threats_detected",
    "breakdown_by_threat_category",
    "average_risk_score",
    "escalation_rate_percent",
    "detection_accuracy_percent",
    "total_complaints",
    "escalated_complaints",
    "resolved_complaints",
    "pending_complaints",
}
REQUIRED_THREAT_CATEGORIES = {"Phishing", "APK_Malware", "Impersonation", "Banking_Fraud", "OTP_Scam"}


def test_dashboard_metrics_required_keys(dashboard_metrics):
    """Assert dashboard_metrics.json has all required top-level keys (Req 5.2)."""
    missing = REQUIRED_DASHBOARD_KEYS - set(dashboard_metrics.keys())
    assert not missing, f"Missing keys in dashboard_metrics.json: {missing}"


def test_dashboard_metrics_detection_accuracy(dashboard_metrics):
    """Assert detection_accuracy_percent >= 85.0 in dashboard_metrics.json (Req 5.6)."""
    accuracy = dashboard_metrics["detection_accuracy_percent"]
    assert accuracy >= 85.0, (
        f"detection_accuracy_percent must be >= 85.0, got {accuracy}"
    )


def test_dashboard_metrics_all_threat_categories(dashboard_metrics):
    """Assert all 5 threat categories are present in breakdown_by_threat_category (Req 5.2)."""
    breakdown = dashboard_metrics.get("breakdown_by_threat_category", {})
    found = set(breakdown.keys())
    missing = REQUIRED_THREAT_CATEGORIES - found
    assert not missing, (
        f"Missing threat categories in dashboard_metrics breakdown: {missing}"
    )


# ---------------------------------------------------------------------------
# 13. cert_escalation_logs.txt — >= 10 entries and all 3 escalation levels
# ---------------------------------------------------------------------------

REQUIRED_ESCALATION_LEVELS = {"L1_Alert", "L2_Investigation", "L3_CERT_Escalation"}


def _parse_escalation_log_entries(text: str) -> list:
    """Return a list of non-empty, non-comment lines from the escalation log."""
    return [line.strip() for line in text.splitlines() if line.strip()]


def test_cert_escalation_logs_min_entries(cert_escalation_logs_text):
    """Assert cert_escalation_logs.txt has at least 10 log entries (Req 5.7)."""
    entries = _parse_escalation_log_entries(cert_escalation_logs_text)
    assert len(entries) >= 10, (
        f"Expected >= 10 escalation log entries, got {len(entries)}"
    )


def test_cert_escalation_logs_all_levels(cert_escalation_logs_text):
    """Assert all 3 escalation levels are present in cert_escalation_logs.txt (Req 6.3)."""
    found_levels = set(re.findall(r"escalation_level=(\S+)", cert_escalation_logs_text))
    missing = REQUIRED_ESCALATION_LEVELS - found_levels
    assert not missing, (
        f"Missing escalation levels in cert_escalation_logs.txt: {missing}"
    )


# ---------------------------------------------------------------------------
# 14. source_references.md — at least 4 source references (## headings)
# ---------------------------------------------------------------------------


def test_source_references_min_count(source_references_text):
    """Assert source_references.md has at least 4 '##' section headings (Req 6.1)."""
    headings = re.findall(r"^## ", source_references_text, re.MULTILINE)
    assert len(headings) >= 4, (
        f"Expected >= 4 '##' headings in source_references.md, got {len(headings)}"
    )


# ---------------------------------------------------------------------------
# 15. dataset_methodology.md — disclaimer text and seed parameters section
# ---------------------------------------------------------------------------


def test_dataset_methodology_has_disclaimer(dataset_methodology_text):
    """Assert dataset_methodology.md contains disclaimer text (Req 6.3)."""
    # The disclaimer section should mention synthetic/fictitious data
    assert re.search(r"(?i)disclaimer", dataset_methodology_text), (
        "dataset_methodology.md must contain a 'Disclaimer' section"
    )
    assert re.search(r"(?i)synthetic", dataset_methodology_text), (
        "dataset_methodology.md disclaimer must state data is synthetic"
    )


def test_dataset_methodology_has_seed_parameters(dataset_methodology_text):
    """Assert dataset_methodology.md contains a Seed Parameters section (Req 6.3)."""
    assert re.search(r"(?i)seed\s+parameters", dataset_methodology_text), (
        "dataset_methodology.md must contain a 'Seed Parameters' section"
    )
    assert re.search(r"DATASET_SEED\s*=\s*42", dataset_methodology_text), (
        "dataset_methodology.md must document DATASET_SEED = 42"
    )


# ---------------------------------------------------------------------------
# 16. README.md — 8 required section headings and folder tree
# ---------------------------------------------------------------------------

REQUIRED_README_SECTIONS = [
    "Project Purpose",
    "Dataset Structure",
    "Folder Descriptions",
    "Usage Instructions",
    "AI Testing Support",
    "Research Usage",
    "Disclaimer",
    "Defence Cyber Awareness Context",
]


def test_root_readme_required_sections(root_readme_text):
    """Assert root README.md has all 8 required section headings (Req 8.1)."""
    for section in REQUIRED_README_SECTIONS:
        assert section in root_readme_text, (
            f"README.md is missing required section: '{section}'"
        )


def test_root_readme_has_folder_tree(root_readme_text):
    """Assert root README.md contains a folder tree (fenced code block) (Req 8.1)."""
    assert "```" in root_readme_text, (
        "README.md must contain a fenced code block (```) for the folder tree"
    )


# ---------------------------------------------------------------------------
# 17. screenshots/README.md — naming convention, PNG/JPG, dimensions
# ---------------------------------------------------------------------------


def test_screenshots_readme_naming_convention(screenshots_readme_text):
    """Assert screenshots/README.md mentions the naming convention (Req 7.1)."""
    # Should mention the [category]_[description]_[YYYYMMDD].[ext] pattern
    assert re.search(r"naming\s+convention", screenshots_readme_text, re.IGNORECASE), (
        "screenshots/README.md must mention 'naming convention'"
    )
    # The pattern itself should be documented
    assert "YYYYMMDD" in screenshots_readme_text, (
        "screenshots/README.md must document the YYYYMMDD date format in the naming convention"
    )


def test_screenshots_readme_formats(screenshots_readme_text):
    """Assert screenshots/README.md mentions PNG and JPG formats (Req 7.1)."""
    assert re.search(r"\bPNG\b", screenshots_readme_text, re.IGNORECASE), (
        "screenshots/README.md must mention PNG format"
    )
    assert re.search(r"\bJPG\b", screenshots_readme_text, re.IGNORECASE), (
        "screenshots/README.md must mention JPG format"
    )


def test_screenshots_readme_dimensions(screenshots_readme_text):
    """Assert screenshots/README.md mentions recommended dimensions (Req 7.1)."""
    # Should mention 1280x720 or similar dimension specification
    assert re.search(r"1280", screenshots_readme_text), (
        "screenshots/README.md must mention dimensions (e.g., 1280×720)"
    )
    assert re.search(r"720", screenshots_readme_text), (
        "screenshots/README.md must mention dimensions (e.g., 1280×720)"
    )
