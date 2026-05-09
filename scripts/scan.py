import subprocess
import json
import os
from datetime import datetime

def run_bandit():
    print("🔍 Running SAST scan with Bandit...")
    result = subprocess.run(
        ["bandit", "-r", "src/", "-f", "json"],
        capture_output=True, text=True
    )
    return json.loads(result.stdout) if result.stdout else {}

def run_safety():
    print("🔍 Running dependency scan with Safety...")
    result = subprocess.run(
        ["safety", "check", "--json"],
        capture_output=True, text=True
    )
    return json.loads(result.stdout) if result.stdout else {}

def generate_report(bandit_results, safety_results):
    report = {
        "scan_time": datetime.utcnow().isoformat(),
        "sast_issues": len(bandit_results.get("results", [])),
        "dependency_issues": len(safety_results) if isinstance(safety_results, list) else 0,
        "bandit_findings": bandit_results.get("results", []),
        "safety_findings": safety_results,
        "status": "FAILED" if bandit_results.get("results") else "PASSED"
    }
    
    with open("reports/security-report.json", "w") as f:
        json.dump(report, f, indent=2)
    
    print(f"\n📊 Scan Complete!")
    print(f"SAST Issues Found:       {report['sast_issues']}")
    print(f"Dependency Issues Found: {report['dependency_issues']}")
    print(f"Overall Status:          {report['status']}")
    
    return report

if __name__ == "__main__":
    os.makedirs("reports", exist_ok=True)
    bandit = run_bandit()
    safety = run_safety()
    report = generate_report(bandit, safety)
    
    # Exit with error if critical issues found
    if report["status"] == "FAILED":
        exit(1)
