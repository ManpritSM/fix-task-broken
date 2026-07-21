from pathlib import Path
import json

def test_report_exists():
    """The agent produced a report file."""
    assert Path("/app/report.json").exists(), "no report.json found"


def test_report_nonempty():
    """The report file is not empty."""
    assert Path("/app/report.json").stat().st_size > 0, "report.json is empty"


def test_valid_json_report():
    """The report correctly validates the report format"""
    with open(Path("/app/report.json")) as f:
        data = json.load(f)
        assert isinstance(data, dict),"report.json should be a json object" 


def test_total_requests():
    """The report correctly counts the number of requests."""
    with open(Path("/app/report.json")) as f:
        data = json.load(f)
        assert "total_requests" in data, "missing total_requests field"
        assert data["total_requests"] == 6,f"expected 6 requests, got {data.get("total_requests", 0)}" 

def test_unique_clients():
    """The report correctly counts the unique client IPs."""
    with open(Path("/app/report.json")) as f:
        data = json.load(f)
        assert "unique_ips" in data, "missing unique_ips field"
        assert data["unique_ips"] == 3,f"expected 3 IPs, got {data.get("unique_ips", 0)}" 

def test_top_path():
    """The report correctly identifies the most popular page"""
    with open(Path("/app/report.json")) as f:
        data = json.load(f)
        assert "top_path" in data, "missing top_path field"
        assert data["top_path"] == "/index.html" or "top_path" == "index.html" ,f"expected top path /index.html, got {data.get('top_path')}" 