# SecureCloud Pipeline 🔐

A production-grade **automated DevSecOps security scanning pipeline** built on AWS and GitHub Actions. Automatically scans code, dependencies, infrastructure, and containers for vulnerabilities on every commit — blocking insecure code from reaching production.

---

## 🏗️ Architecture

```
Developer pushes code
        ↓
GitHub Actions triggers automatically
        ↓
┌─────────────────────────────┐
│   Security Gate 1 - SAST    │
│   Bandit scans Python code  │
│   Finds: SQLi, CMDi, weak   │
│   crypto, path traversal    │
└─────────────────────────────┘
        ↓
┌─────────────────────────────┐
│   Security Gate 2 - Deps    │
│   Safety scans packages     │
│   Finds: known CVEs in      │
│   Flask, Requests, etc.     │
└─────────────────────────────┘
        ↓
┌─────────────────────────────┐
│   Security Gate 3 - IaC     │
│   Checkov scans Terraform   │
│   Finds: S3 misconfigs,     │
│   open security groups      │
└─────────────────────────────┘
        ↓
┌─────────────────────────────┐
│   Security Gate 4 - Docker  │
│   Trivy scans containers    │
│   Finds: OS vulns, package  │
│   vulnerabilities in image  │
└─────────────────────────────┘
        ↓
   Security Summary Report
   Artifacts saved to GitHub
```

---

## 🛡️ Security Gates

| Gate | Tool | What It Scans | Vulnerabilities Found |
|------|------|---------------|----------------------|
| 1 | **Bandit** | Python source code (SAST) | SQL Injection, Command Injection, Weak MD5 Hash |
| 2 | **Safety** | Python dependencies | 6 CVEs in Flask & Requests |
| 3 | **Checkov** | Terraform IaC | S3 public access, open security groups |
| 4 | **Trivy** | Docker containers | OS & package vulnerabilities |

---

## 🚨 Real Vulnerabilities Detected

### SAST Findings (Bandit)
```
HIGH   - Command Injection (CWE-78)   → os.system(cmd)
HIGH   - Weak MD5 Hashing (CWE-327)  → hashlib.md5()
MEDIUM - SQL Injection (CWE-89)       → string query construction
LOW    - Subprocess Import (CWE-78)   → import subprocess
```

### Dependency CVEs (Safety)
```
CVE-2023-30861 → Flask 2.2.0 - Response data leak
CVE-2026-27205 → Flask 2.2.0 - Information disclosure
CVE-2023-32681 → Requests 2.28.0 - Proxy credential leak
CVE-2024-47081 → Requests 2.28.0 - .netrc credential leak
CVE-2024-35195 → Requests 2.28.0 - Certificate bypass
CVE-2026-25645 → Requests 2.28.0 - Insecure temp files
```

### Infrastructure Misconfigs (Checkov)
```
S3 bucket public access not blocked
Security group allows all inbound traffic (0.0.0.0/0)
Missing S3 bucket encryption
Missing S3 bucket versioning
```

---

## ⚙️ CI/CD Pipeline

The pipeline runs automatically on every git push:

```yaml
Jobs:
  sast-scan         → Bandit SAST scan
  dependency-scan   → Safety CVE check
  infra-scan        → Checkov Terraform scan
  container-scan    → Trivy Docker scan
  security-summary  → Final report
```

All jobs run in parallel for speed, then summarize results.

---

## 🛠️ Tools Used

| Tool | Purpose |
|------|---------|
| **Bandit** | Python SAST scanner |
| **Safety** | Dependency CVE scanner |
| **Checkov** | Terraform/IaC scanner |
| **Trivy** | Container vulnerability scanner |
| **GitHub Actions** | CI/CD automation |
| **AWS S3** | Report storage |
| **Terraform** | Infrastructure as Code |
| **Docker** | Container scanning target |

---

## 📁 Project Structure

```
securecloud-pipeline/
├── .github/
│   └── workflows/
│       └── security-pipeline.yml  # 5-stage pipeline
├── src/
│   └── app.py                     # Demo app with vulnerabilities
├── terraform/
│   └── main.tf                    # Intentionally misconfigured IaC
├── scripts/
│   └── scan.py                    # Local scanning script
├── reports/
│   └── bandit-report.json         # Scan results
├── Dockerfile
└── requirements.txt
```

---

## 🚀 Run Locally

```bash
# Clone the repo
git clone https://github.com/ali-zameer-dev/securecloud-pipeline.git
cd securecloud-pipeline

# Install scanners
pip install bandit safety

# Run SAST scan
python -m bandit -r src/

# Run dependency scan
python -m safety check -r requirements.txt
```

---

## 📊 Sample Scan Output

```
$ python -m bandit -r src/

>> Issue: [B605] Command Injection
   Severity: High   Confidence: High
   Location: src/app.py:12

>> Issue: [B324] Weak MD5 Hash
   Severity: High   Confidence: High
   Location: src/app.py:16

>> Issue: [B608] SQL Injection
   Severity: Medium   Confidence: Low
   Location: src/app.py:7

Total: 2 High, 1 Medium, 1 Low
```

---

## 💼 What This Demonstrates

- **DevSecOps** — Security integrated into every commit
- **Shift Left Security** — Catching vulnerabilities before production
- **CI/CD Automation** — Zero manual security reviews needed
- **Multi-layer scanning** — Code, deps, infra, containers all covered
- **Real CVE detection** — Finding actual known vulnerabilities
- **IaC Security** — Terraform misconfiguration detection

---

## 👨‍💻 Author

**Ali Zameer**
Cloud & DevSecOps Engineer
[GitHub](https://github.com/ali-zameer-dev)

---

## 📄 License

MIT
