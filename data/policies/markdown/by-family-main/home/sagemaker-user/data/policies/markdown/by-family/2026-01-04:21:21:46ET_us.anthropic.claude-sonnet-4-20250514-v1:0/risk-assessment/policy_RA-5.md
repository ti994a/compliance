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
The organization SHALL continuously monitor and scan systems and applications for security vulnerabilities using automated tools and standardized processes. All identified legitimate vulnerabilities MUST be remediated within timeframes based on organizational risk assessment and vulnerability severity.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All production, development, and test systems |
| Applications | YES | Both hosted and internally developed applications |
| Infrastructure Components | YES | Network devices, printers, IoT devices |
| Cloud Resources | YES | IaaS, PaaS, and SaaS components under organizational control |
| Third-party Systems | CONDITIONAL | Only if organization has scanning rights |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Team | • Conduct vulnerability scans<br>• Analyze scan results<br>• Coordinate remediation activities<br>• Maintain scanning tools |
| System Administrators | • Implement remediation measures<br>• Provide system access for scanning<br>• Report scanning conflicts |
| Risk Management Office | • Define remediation timeframes<br>• Assess vulnerability risk ratings<br>• Approve risk acceptance decisions |

## 4. RULES
[RULE-01] Vulnerability scanning MUST be performed at least monthly for all in-scope systems and applications.
[VALIDATION] IF last_scan_date > 30_days AND system_status = "active" THEN violation

[RULE-02] Critical vulnerabilities (CVSS 9.0-10.0) MUST be remediated within 72 hours of confirmed discovery.
[VALIDATION] IF vulnerability_cvss >= 9.0 AND remediation_time > 72_hours AND risk_accepted = FALSE THEN critical_violation

[RULE-03] High vulnerabilities (CVSS 7.0-8.9) MUST be remediated within 30 days of confirmed discovery.
[VALIDATION] IF vulnerability_cvss >= 7.0 AND vulnerability_cvss < 9.0 AND remediation_time > 30_days AND risk_accepted = FALSE THEN violation

[RULE-04] Vulnerability scanning tools MUST support SCAP standards including CVE, OVAL, and CVSS scoring.
[VALIDATION] IF scanning_tool_scap_compliant = FALSE THEN violation

[RULE-05] Vulnerability scan results MUST be analyzed within 5 business days of scan completion.
[VALIDATION] IF scan_analysis_time > 5_business_days THEN violation

[RULE-06] Vulnerability information MUST be shared with relevant system owners within 24 hours of analysis completion.
[VALIDATION] IF vulnerability_notification_time > 24_hours THEN violation

[RULE-07] Scanning tool vulnerability signatures MUST be updated at least weekly.
[VALIDATION] IF signature_update_age > 7_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Vulnerability Scanning Schedule - Defines scanning frequency and methodology
- [PROC-02] Vulnerability Analysis and Triage - Process for evaluating and prioritizing findings
- [PROC-03] Vulnerability Remediation Workflow - Steps for coordinating and tracking fixes
- [PROC-04] Risk Acceptance Process - Procedure for formally accepting vulnerability risks
- [PROC-05] Tool Configuration Management - Maintaining and updating scanning tools

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major infrastructure changes, new compliance requirements, significant security incidents

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Vulnerability Overdue]
IF vulnerability_cvss >= 9.0
AND days_since_discovery > 3
AND remediation_status != "complete"
AND risk_accepted = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Scanning Gap Detection]
IF system_type = "production"
AND last_vulnerability_scan > 30_days
AND system_status = "active"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Non-SCAP Compliant Tool Usage]
IF scanning_tool_scap_validated = FALSE
AND tool_usage = "primary"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Delayed Analysis Response]
IF vulnerability_scan_completed = TRUE
AND analysis_completion_time > 5_business_days
AND business_justification = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Accepted Risk Documentation]
IF vulnerability_cvss >= 7.0
AND remediation_status = "risk_accepted"
AND risk_acceptance_documented = TRUE
AND acceptance_authority_approved = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Monitor systems for vulnerabilities at defined frequency | RULE-01 |
| Scan systems for vulnerabilities at defined frequency | RULE-01 |
| Employ interoperable vulnerability monitoring tools | RULE-04 |
| Automate vulnerability management using standards | RULE-04 |
| Analyze vulnerability scan reports and results | RULE-05 |
| Remediate legitimate vulnerabilities per risk assessment | RULE-02, RULE-03 |
| Share vulnerability information with designated personnel | RULE-06 |
| Update vulnerability scanning capabilities | RULE-07 |