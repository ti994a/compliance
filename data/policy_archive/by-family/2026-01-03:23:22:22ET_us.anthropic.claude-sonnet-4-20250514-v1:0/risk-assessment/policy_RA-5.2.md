# POLICY: RA-5.2: Update Vulnerabilities to Be Scanned

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-5.2 |
| NIST Control | RA-5.2: Update Vulnerabilities to Be Scanned |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | vulnerability scanning, vulnerability management, security assessments, patch management, threat intelligence |

## 1. POLICY STATEMENT
The organization MUST maintain current vulnerability scan configurations by regularly updating the list of system vulnerabilities to be scanned. This ensures newly discovered vulnerabilities are identified and mitigated in a timely manner across all information systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including production, development, and test environments |
| Cloud Infrastructure | YES | Both organization-managed and third-party cloud services |
| Network Infrastructure | YES | Routers, switches, firewalls, and network appliances |
| Mobile Devices | YES | Company-owned and BYOD devices with system access |
| Third-party Systems | CONDITIONAL | When organization has scanning responsibilities per contract |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Vulnerability Management Team | • Update vulnerability scan configurations<br>• Monitor threat intelligence feeds<br>• Maintain vulnerability scanning tools |
| Security Operations Center | • Execute vulnerability scans<br>• Analyze scan results<br>• Coordinate with system owners on remediation |
| System Owners | • Provide system access for scanning<br>• Implement approved vulnerability remediation<br>• Report system changes affecting scan scope |

## 4. RULES
[RULE-01] Vulnerability scan configurations MUST be updated within 72 hours of new Critical or High severity vulnerabilities being published in authoritative sources.
[VALIDATION] IF vulnerability_severity IN ["Critical", "High"] AND config_update_time > 72_hours THEN violation

[RULE-02] Vulnerability databases used for scanning MUST be updated at least weekly for Medium and Low severity vulnerabilities.
[VALIDATION] IF database_last_update > 7_days AND vulnerability_severity IN ["Medium", "Low"] THEN violation

[RULE-03] Threat intelligence feeds MUST be monitored daily to identify new vulnerabilities affecting organizational systems.
[VALIDATION] IF threat_intel_check_date < current_date THEN violation

[RULE-04] Vulnerability scan tool signatures MUST be updated within 24 hours of vendor release for emergency security updates.
[VALIDATION] IF signature_type = "emergency" AND update_delay > 24_hours THEN critical_violation

[RULE-05] All vulnerability scan configuration changes MUST be documented with justification and approved by the Vulnerability Management Team.
[VALIDATION] IF config_change = TRUE AND (documentation = FALSE OR approval = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Vulnerability Database Update Process - Weekly update and validation of vulnerability databases
- [PROC-02] Threat Intelligence Monitoring - Daily monitoring and analysis of security advisories and threat feeds
- [PROC-03] Emergency Vulnerability Response - Rapid configuration updates for critical vulnerabilities
- [PROC-04] Scan Configuration Management - Change control for vulnerability scanning parameters and scope

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, significant infrastructure changes, regulatory updates, vendor tool changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Zero-Day Response]
IF vulnerability_severity = "Critical"
AND cvss_score >= 9.0
AND vendor_patch_available = FALSE
AND config_updated = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Weekly Database Update Missed]
IF current_date - last_database_update > 7_days
AND vulnerability_scanning_active = TRUE
AND approved_exception = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Threat Intelligence Not Monitored]
IF threat_intel_last_check > 1_day
AND business_day = TRUE
AND system_outage = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Emergency Signature Update Delayed]
IF signature_release_type = "emergency"
AND vendor_release_time + 24_hours < current_time
AND signature_deployed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Undocumented Configuration Change]
IF scan_config_modified = TRUE
AND change_documentation = FALSE
AND modification_date > current_date - 30_days
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System vulnerabilities to be scanned are updated regularly | [RULE-01], [RULE-02] |
| Vulnerability databases are current | [RULE-02], [RULE-04] |
| Threat intelligence integration | [RULE-03] |
| Change management for scan configurations | [RULE-05] |
| Timely response to critical vulnerabilities | [RULE-01], [RULE-04] |