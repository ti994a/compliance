# POLICY: RA-5: Vulnerability Monitoring and Scanning

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-5 |
| NIST Control | RA-5: Vulnerability Monitoring and Scanning |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | vulnerability scanning, vulnerability monitoring, remediation, SCAP, CVE, CVSS, patch management |

## 1. POLICY STATEMENT
The organization must continuously monitor and scan all systems and applications for vulnerabilities using automated tools that support industry standards. All identified vulnerabilities must be analyzed, prioritized by risk, and remediated within defined timeframes based on severity levels.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid |
| Hosted applications | YES | Internal and third-party hosted |
| Network infrastructure | YES | Routers, switches, firewalls, sensors |
| IoT devices | YES | Printers, scanners, connected devices |
| Development systems | YES | Including CI/CD pipelines |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Team | • Conduct vulnerability scans<br>• Monitor vulnerability feeds<br>• Analyze scan results<br>• Coordinate remediation activities |
| System Administrators | • Apply patches and updates<br>• Implement configuration changes<br>• Validate remediation effectiveness |
| Risk Management Team | • Define risk-based remediation timeframes<br>• Assess vulnerability impact<br>• Approve risk acceptance decisions |

## 4. RULES
[RULE-01] Vulnerability scanning MUST be performed at least weekly for internet-facing systems and monthly for internal systems, with additional scans triggered when new vulnerabilities are announced.
[VALIDATION] IF system_type = "internet-facing" AND last_scan > 7_days THEN violation
[VALIDATION] IF system_type = "internal" AND last_scan > 30_days THEN violation

[RULE-02] Vulnerability monitoring tools MUST support SCAP standards, CVE naming convention, and CVSS scoring to ensure interoperability and standardized reporting.
[VALIDATION] IF scanning_tool_scap_compliant = FALSE OR cve_support = FALSE THEN violation

[RULE-03] Critical vulnerabilities (CVSS 9.0-10.0) MUST be remediated within 72 hours, High vulnerabilities (CVSS 7.0-8.9) within 30 days, Medium vulnerabilities (CVSS 4.0-6.9) within 90 days.
[VALIDATION] IF vuln_cvss >= 9.0 AND remediation_time > 72_hours THEN critical_violation
[VALIDATION] IF vuln_cvss >= 7.0 AND vuln_cvss < 9.0 AND remediation_time > 30_days THEN violation

[RULE-04] Vulnerability scan results and remediation status MUST be shared with system owners, security teams, and risk management within 24 hours of scan completion.
[VALIDATION] IF scan_completed = TRUE AND notification_sent = FALSE AND elapsed_time > 24_hours THEN violation

[RULE-05] Vulnerability scanning tools MUST be updated with the latest vulnerability signatures within 24 hours of vendor release.
[VALIDATION] IF signature_update_available = TRUE AND update_age > 24_hours THEN violation

[RULE-06] All vulnerability remediation activities MUST be documented with evidence of successful mitigation and verified through re-scanning.
[VALIDATION] IF vulnerability_status = "remediated" AND verification_scan = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Vulnerability Scanning Schedule - Define frequency and scope for different system types
- [PROC-02] Vulnerability Analysis and Prioritization - Risk-based assessment and remediation planning
- [PROC-03] Emergency Vulnerability Response - Expedited process for zero-day and critical vulnerabilities
- [PROC-04] Vulnerability Disclosure Program - Process for receiving and handling external vulnerability reports
- [PROC-05] Scan Tool Management - Configuration, updating, and maintenance of scanning infrastructure

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, new regulatory requirements, significant infrastructure changes, tool updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Vulnerability Response]
IF vulnerability_cvss >= 9.0
AND discovery_date < current_date - 3_days
AND remediation_status = "open"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Scanning Tool Standards Compliance]
IF scanning_tool_deployed = TRUE
AND scap_validated = FALSE
AND cve_support = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Scan Frequency Violation]
IF system_classification = "internet-facing"
AND last_vulnerability_scan > current_date - 7_days
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Remediation Documentation]
IF vulnerability_status = "closed"
AND remediation_evidence = NULL
AND verification_scan_passed = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Information Sharing Delay]
IF vulnerability_scan_completed = TRUE
AND stakeholder_notification_sent = FALSE
AND scan_completion_time < current_time - 24_hours
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Monitor systems for vulnerabilities at defined frequency | RULE-01 |
| Scan systems for vulnerabilities at defined frequency | RULE-01 |
| Employ interoperable vulnerability monitoring tools | RULE-02 |
| Use standards for vulnerability enumeration and measurement | RULE-02 |
| Analyze vulnerability scan reports and results | RULE-04 |
| Remediate vulnerabilities per risk assessment | RULE-03 |
| Share vulnerability information with designated personnel | RULE-04 |
| Update vulnerability monitoring tools capability | RULE-05 |
| Document remediation activities | RULE-06 |