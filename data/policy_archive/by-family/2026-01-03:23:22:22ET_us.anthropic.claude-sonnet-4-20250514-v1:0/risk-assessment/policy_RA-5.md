# POLICY: RA-5: Vulnerability Monitoring and Scanning

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-5 |
| NIST Control | RA-5: Vulnerability Monitoring and Scanning |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | vulnerability, scanning, monitoring, remediation, CVSS, CVE, SCAP, assessment |

## 1. POLICY STATEMENT
The organization must continuously monitor and scan all systems and applications for security vulnerabilities using automated tools and standardized processes. Identified vulnerabilities must be analyzed, prioritized by risk, and remediated within defined timeframes based on severity levels.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All cloud and on-premises systems |
| Development Systems | YES | Systems containing production data |
| Network Infrastructure | YES | Routers, switches, firewalls, load balancers |
| Applications | YES | Web apps, APIs, databases, custom software |
| Third-party Services | CONDITIONAL | When organization has scanning access |
| Personal Devices | NO | Covered under separate BYOD policy |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Team | • Conduct vulnerability scans<br>• Analyze scan results<br>• Coordinate remediation activities<br>• Maintain scanning tools and signatures |
| System Owners | • Provide system access for scanning<br>• Execute approved remediation plans<br>• Report new vulnerabilities discovered<br>• Validate remediation effectiveness |
| Risk Management | • Define risk-based remediation timeframes<br>• Approve risk acceptance decisions<br>• Review vulnerability metrics and trends |

## 4. RULES
[RULE-01] Vulnerability scans MUST be performed on all in-scope systems at least weekly for external-facing systems and monthly for internal systems.
[VALIDATION] IF system_type = "external" AND last_scan_date > 7_days THEN violation
[VALIDATION] IF system_type = "internal" AND last_scan_date > 30_days THEN violation

[RULE-02] Vulnerability scanning tools MUST be SCAP-validated and capable of identifying CVE-numbered vulnerabilities with CVSS scoring.
[VALIDATION] IF scanning_tool_scap_validated = FALSE THEN violation

[RULE-03] Critical vulnerabilities (CVSS 9.0-10.0) MUST be remediated within 72 hours of confirmed discovery.
[VALIDATION] IF vulnerability_cvss >= 9.0 AND remediation_time > 72_hours THEN critical_violation

[RULE-04] High vulnerabilities (CVSS 7.0-8.9) MUST be remediated within 30 days of confirmed discovery.
[VALIDATION] IF vulnerability_cvss >= 7.0 AND vulnerability_cvss < 9.0 AND remediation_time > 30_days THEN violation

[RULE-05] Medium vulnerabilities (CVSS 4.0-6.9) MUST be remediated within 90 days of confirmed discovery.
[VALIDATION] IF vulnerability_cvss >= 4.0 AND vulnerability_cvss < 7.0 AND remediation_time > 90_days THEN violation

[RULE-06] Vulnerability scan results and remediation status MUST be shared with system owners within 24 hours of scan completion.
[VALIDATION] IF scan_completion_date + 24_hours < notification_date THEN violation

[RULE-07] Scanning tools MUST be updated with new vulnerability signatures within 24 hours of vendor release.
[VALIDATION] IF signature_release_date + 24_hours < update_applied_date THEN violation

[RULE-08] Emergency scans MUST be initiated within 4 hours when new critical vulnerabilities are publicly disclosed affecting organizational systems.
[VALIDATION] IF public_disclosure_critical = TRUE AND emergency_scan_start > 4_hours THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Vulnerability Scanning Schedule - Defines scanning frequency and maintenance windows
- [PROC-02] Vulnerability Analysis and Prioritization - Risk-based assessment and CVSS scoring methodology
- [PROC-03] Remediation Workflow - Tracking, assignment, and validation of vulnerability fixes
- [PROC-04] Exception Management - Risk acceptance process for vulnerabilities that cannot be remediated
- [PROC-05] Tool Management - Scanner deployment, configuration, and signature updates

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, new compliance requirements, significant infrastructure changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Overdue Critical Vulnerability]
IF vulnerability_cvss >= 9.0
AND days_since_discovery > 3
AND remediation_status != "completed"
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Missing Emergency Scan]
IF public_cve_disclosed = TRUE
AND vulnerability_affects_org_systems = TRUE
AND cvss_score >= 9.0
AND emergency_scan_initiated = FALSE
AND hours_since_disclosure > 4
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Outdated Scanner Signatures]
IF scanner_signature_age > 24_hours
AND vendor_updates_available = TRUE
AND maintenance_window_available = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Delayed Scan Results Sharing]
IF scan_completed = TRUE
AND hours_since_completion > 24
AND results_shared_with_owners = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Non-SCAP Scanner Usage]
IF vulnerability_scanner_deployed = TRUE
AND scap_validation = FALSE
AND scanner_type = "primary"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Monitor systems for vulnerabilities at defined frequency | [RULE-01] |
| Scan systems for vulnerabilities at defined frequency | [RULE-01] |
| Employ interoperable vulnerability monitoring tools | [RULE-02] |
| Analyze vulnerability scan reports and results | [RULE-03, RULE-04, RULE-05] |
| Remediate vulnerabilities per risk assessment | [RULE-03, RULE-04, RULE-05] |
| Share vulnerability information with appropriate personnel | [RULE-06] |
| Employ tools with update capability | [RULE-07] |
| Respond to newly identified vulnerabilities | [RULE-08] |