# SecureCloud Pipeline 🔐

A production-grade automated DevSecOps security scanning pipeline built on AWS and GitHub Actions. Automatically scans code, dependencies, infrastructure, and containers for vulnerabilities on every commit.

## Security Gates

| Gate | Tool | What It Scans |
|------|------|---------------|
| 1 | Bandit | Python source code (SAST) |
| 2 | Safety | Python dependencies (CVEs) |
| 3 | Checkov | Terraform IaC misconfigs |
| 4 | Trivy | Docker container vulns |

## Real Vulnerabilities Detected

### SAST (Bandit)
- HIGH - Command Injection CWE-78
- HIGH - Weak MD5 Hashing CWE-327
- MEDIUM - SQL Injection CWE-89

### Dependency CVEs (Safety)
- CVE-2023-30861 Flask data leak
- CVE-2023-32681 Requests credential leak
- CVE-2024-47081 Requests netrc leak
- CVE-2024-35195 Requests cert bypass
- 6 total CVEs found

## Run Locally

pip install bandit safety
python -m bandit -r src/
python -m safety check -r requirements.txt

## Author
Ali Zameer - Cloud and DevSecOps Engineer
github.com/ali-zameer-dev
