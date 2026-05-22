"""
Cross-file consistency tests for the Rakshak AI Research Dataset.

These tests verify referential integrity and data consistency across
multiple dataset files.

Requirements: 9.1, 9.2, 9.5
"""

from urllib.parse import urlparse


# ---------------------------------------------------------------------------
# Test 1: complaint_id values in complaint_export.csv match complaint_samples.json
# Requirements: 9.2
# ---------------------------------------------------------------------------


def test_complaint_ids_csv_match_json(complaint_export_rows, complaint_samples):
    """
    All complaint_id values in complaint_export.csv must match exactly those
    in complaint_samples.json — same set, same count.
    """
    csv_ids = {row["complaint_id"] for row in complaint_export_rows}
    json_ids = {record["complaint_id"] for record in complaint_samples}

    assert csv_ids == json_ids, (
        f"Mismatch between complaint IDs in CSV and JSON.\n"
        f"  Only in CSV: {csv_ids - json_ids}\n"
        f"  Only in JSON: {json_ids - csv_ids}"
    )


# ---------------------------------------------------------------------------
# Test 2: complaint_export.csv row count equals complaint_samples.json array length
# Requirements: 9.2
# ---------------------------------------------------------------------------


def test_complaint_csv_row_count_equals_json_length(complaint_export_rows, complaint_samples):
    """
    The number of data rows in complaint_export.csv must equal the number of
    records in the complaint_samples.json array.
    """
    assert len(complaint_export_rows) == len(complaint_samples), (
        f"Row count mismatch: CSV has {len(complaint_export_rows)} rows, "
        f"JSON has {len(complaint_samples)} records."
    )


# ---------------------------------------------------------------------------
# Test 3: All domains in malicious_domains.csv appear in phishing_links.txt
# Requirements: 9.1
# ---------------------------------------------------------------------------


def test_malicious_domains_extracted_from_phishing_links(malicious_domains_rows, phishing_links):
    """
    Every domain in malicious_domains.csv must appear as a substring of at
    least one URL in phishing_links.txt, confirming the domains were extracted
    from the phishing URL list.
    """
    missing = []
    for row in malicious_domains_rows:
        domain = row["domain"].strip()
        if not any(domain in url for url in phishing_links):
            missing.append(domain)

    assert not missing, (
        f"The following domains in malicious_domains.csv were not found as a "
        f"substring of any URL in phishing_links.txt:\n  " + "\n  ".join(missing)
    )


# ---------------------------------------------------------------------------
# Test 4: All url values in url_risk_labels.json appear in phishing_links.txt
# Requirements: 9.1
# ---------------------------------------------------------------------------


def test_url_risk_labels_urls_in_phishing_links(url_risk_labels, phishing_links):
    """
    Every 'url' value in url_risk_labels.json must appear verbatim in
    phishing_links.txt.
    """
    missing = []
    for record in url_risk_labels:
        url = record["url"].strip()
        if url not in phishing_links:
            missing.append(url)

    assert not missing, (
        f"The following URLs in url_risk_labels.json were not found in "
        f"phishing_links.txt:\n  " + "\n  ".join(missing)
    )


# ---------------------------------------------------------------------------
# Test 5: dashboard_metrics.json category counts sum to total_threats_detected
# Requirements: 9.1
# ---------------------------------------------------------------------------


def test_dashboard_metrics_category_counts_sum_to_total(dashboard_metrics):
    """
    The sum of all category counts in 'breakdown_by_threat_category' must
    equal 'total_threats_detected' in dashboard_metrics.json.
    """
    total = dashboard_metrics["total_threats_detected"]
    breakdown = dashboard_metrics["breakdown_by_threat_category"]
    category_sum = sum(breakdown.values())

    assert category_sum == total, (
        f"Category counts sum ({category_sum}) does not equal "
        f"total_threats_detected ({total}). "
        f"Breakdown: {breakdown}"
    )
