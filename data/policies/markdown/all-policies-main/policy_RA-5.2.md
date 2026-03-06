# POLICY: RA-5.2: Update Vulnerabilities to Be Scanned

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-5.2 |
| NIST Control | RA-5.2: Update Vulnerabilities to Be Scanned |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | vulnerability scanning, vulnerability management, security updates, threat intelligence, risk assessment |

## 1. POLICY STATEMENT
The organization SHALL maintain current vulnerability scanning capabilities by regularly updating the list of system vulnerabilities to be scanned. This ensures newly discovered vulnerabilities are identified and mitigated in a timely manner across all organizational systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, hybrid, and on-premises |
| Third-party Systems | YES | Where organization has scanning responsibility |
| Development/Test Systems | YES | Must align with production scanning requirements |
| Network Infrastructure | YES | Routers, switches, firewalls, and security devices |
| Mobile Devices | CONDITIONAL | If managed by organization |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Vulnerability Management Team | • Update vulnerability databases and scanning tools<br>• Monitor threat intelligence feeds<br>• Coordinate with vendors for signature updates |
| System Administrators | • Implement updated vulnerability scans<br>• Validate scan coverage<br>• Report scanning issues or gaps |
| Security Operations Center | • Monitor vulnerability scanning activities<br>• Escalate critical vulnerabilities<br>• Maintain scanning schedules |

## 4. RULES
[RULE-01] Vulnerability scanning tools and databases MUST be updated at least weekly or within 24 hours of critical vulnerability disclosure.
[VALIDATION] IF last_update_date > 7_days OR (critical_vuln_published = TRUE AND update_delay > 24_hours) THEN violation

[RULE-02] Newly discovered vulnerabilities with CVSS score ≥ 7.0 MUST be added to scanning profiles within 48 hours of publication.
[VALIDATION] IF vuln_cvss_score >= 7.0 AND time_since_publication > 48_hours AND scan_profile_updated = FALSE THEN violation

[RULE-03] Vulnerability scan coverage MUST include all organizational asset types and SHALL be verified monthly.
[VALIDATION] IF asset_in_inventory = TRUE AND asset_in_scan_scope = FALSE THEN violation

[RULE-04] Organizations MUST subscribe to at least two independent threat intelligence feeds for vulnerability information.
[VALIDATION] IF active_threat_feeds < 2 THEN violation

[RULE-05] Vulnerability scanning signature updates MUST be tested in non-production environment before deployment to production systems.
[VALIDATION] IF production_deployment = TRUE AND non_prod_testing = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Vulnerability Database Update - Weekly update of scanning tools and vulnerability databases
- [PROC-02] Emergency Vulnerability Addition - Rapid inclusion of critical vulnerabilities in scanning profiles  
- [PROC-03] Scan Coverage Verification - Monthly validation of asset coverage in vulnerability scans
- [PROC-04] Threat Intelligence Integration - Process for incorporating external vulnerability intelligence

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major vulnerability disclosures, tool changes, regulatory updates, security incidents

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Zero-Day Vulnerability]
IF vulnerability_cvss_score >= 9.0
AND vulnerability_age <= 24_hours
AND scan_profile_updated = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Weekly Update Missed]
IF current_date - last_vulnerability_update > 7_days
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Asset Not in Scan Scope]
IF asset_in_cmdb = TRUE
AND asset_scannable = TRUE
AND asset_in_scan_scope = FALSE
AND coverage_review_date > 30_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Insufficient Threat Intelligence]
IF active_threat_intelligence_feeds < 2
AND no_compensating_controls = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Production Update Without Testing]
IF vulnerability_signature_update = TRUE
AND deployed_to_production = TRUE
AND non_production_testing = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System vulnerabilities to be scanned are updated regularly | [RULE-01], [RULE-02] |
| Vulnerability scanning covers all organizational assets | [RULE-03] |
| Organization maintains current threat intelligence | [RULE-04] |
| Updates are properly tested before production deployment | [RULE-05] |