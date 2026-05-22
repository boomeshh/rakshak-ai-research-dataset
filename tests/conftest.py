"""
Shared pytest fixtures for Rakshak AI Research Dataset tests.

Fixtures load all dataset files once per test session and expose parsed
data (JSON, CSV, TXT) to all test modules.
"""

import csv
import json
import os
import re
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Root path helpers
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent


def _path(*parts: str) -> Path:
    """Return an absolute path relative to the repository root."""
    return REPO_ROOT.joinpath(*parts)


# ---------------------------------------------------------------------------
# JSON fixtures
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def complaint_samples():
    """Load fake_complaints/complaint_samples.json as a list of dicts."""
    with open(_path("fake_complaints", "complaint_samples.json"), encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def url_risk_labels():
    """Load phishing_urls/url_risk_labels.json as a list of dicts."""
    with open(_path("phishing_urls", "url_risk_labels.json"), encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def fake_apk_alerts():
    """Load apk_samples/fake_apk_alerts.json as a list of dicts."""
    with open(_path("apk_samples", "fake_apk_alerts.json"), encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture(scope="session")
def dashboard_metrics():
    """Load testing_exports/dashboard_metrics.json as a dict."""
    with open(_path("testing_exports", "dashboard_metrics.json"), encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# CSV fixtures
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def complaint_export_rows():
    """Load fake_complaints/complaint_export.csv as a list of dicts (DictReader)."""
    with open(_path("fake_complaints", "complaint_export.csv"), encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


@pytest.fixture(scope="session")
def malicious_domains_rows():
    """Load phishing_urls/malicious_domains.csv as a list of dicts."""
    with open(_path("phishing_urls", "malicious_domains.csv"), encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


@pytest.fixture(scope="session")
def ai_detection_results_rows():
    """Load testing_exports/ai_detection_results.csv as a list of dicts."""
    with open(_path("testing_exports", "ai_detection_results.csv"), encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)


# ---------------------------------------------------------------------------
# TXT fixtures
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def phishing_links():
    """
    Load phishing_urls/phishing_links.txt.

    Returns a set of non-empty, non-comment lines (stripped).
    """
    with open(_path("phishing_urls", "phishing_links.txt"), encoding="utf-8") as f:
        lines = f.readlines()
    return {line.strip() for line in lines if line.strip() and not line.strip().startswith("#")}


@pytest.fixture(scope="session")
def sms_scams_text():
    """Load scam_messages/sms_scams.txt as a raw string."""
    with open(_path("scam_messages", "sms_scams.txt"), encoding="utf-8") as f:
        return f.read()


@pytest.fixture(scope="session")
def whatsapp_scams_text():
    """Load scam_messages/whatsapp_scams.txt as a raw string."""
    with open(_path("scam_messages", "whatsapp_scams.txt"), encoding="utf-8") as f:
        return f.read()


@pytest.fixture(scope="session")
def telegram_scams_text():
    """Load scam_messages/telegram_scams.txt as a raw string."""
    with open(_path("scam_messages", "telegram_scams.txt"), encoding="utf-8") as f:
        return f.read()


@pytest.fixture(scope="session")
def cert_escalation_logs_text():
    """Load testing_exports/cert_escalation_logs.txt as a raw string."""
    with open(_path("testing_exports", "cert_escalation_logs.txt"), encoding="utf-8") as f:
        return f.read()


@pytest.fixture(scope="session")
def suspicious_apk_names():
    """
    Load apk_samples/suspicious_apk_names.txt.

    Returns a list of non-empty, non-comment lines (stripped).
    """
    with open(_path("apk_samples", "suspicious_apk_names.txt"), encoding="utf-8") as f:
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip() and not line.strip().startswith("#")]


# ---------------------------------------------------------------------------
# Markdown fixtures
# ---------------------------------------------------------------------------


@pytest.fixture(scope="session")
def social_engineering_text():
    """Load scam_messages/social_engineering_samples.md as a raw string."""
    with open(_path("scam_messages", "social_engineering_samples.md"), encoding="utf-8") as f:
        return f.read()


@pytest.fixture(scope="session")
def source_references_text():
    """Load dataset_references/source_references.md as a raw string."""
    with open(_path("dataset_references", "source_references.md"), encoding="utf-8") as f:
        return f.read()


@pytest.fixture(scope="session")
def dataset_methodology_text():
    """Load dataset_references/dataset_methodology.md as a raw string."""
    with open(_path("dataset_references", "dataset_methodology.md"), encoding="utf-8") as f:
        return f.read()


@pytest.fixture(scope="session")
def root_readme_text():
    """Load root README.md as a raw string."""
    with open(_path("README.md"), encoding="utf-8") as f:
        return f.read()


@pytest.fixture(scope="session")
def screenshots_readme_text():
    """Load screenshots/README.md as a raw string."""
    with open(_path("screenshots", "README.md"), encoding="utf-8") as f:
        return f.read()


@pytest.fixture(scope="session")
def apk_analysis_report_text():
    """Load apk_samples/apk_analysis_report.md as a raw string."""
    with open(_path("apk_samples", "apk_analysis_report.md"), encoding="utf-8") as f:
        return f.read()


@pytest.fixture(scope="session")
def complaint_summary_text():
    """Load fake_complaints/complaint_summary.md as a raw string."""
    with open(_path("fake_complaints", "complaint_summary.md"), encoding="utf-8") as f:
        return f.read()
