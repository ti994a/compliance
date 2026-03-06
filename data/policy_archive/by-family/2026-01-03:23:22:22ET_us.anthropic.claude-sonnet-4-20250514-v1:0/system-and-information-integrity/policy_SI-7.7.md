# POLICY: SI-7.7: Integration of Detection and Response

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-7.7 |
| NIST Control | SI-7.7: Integration of Detection and Response |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | incident response, detection, unauthorized changes, security-relevant changes, configuration, privilege escalation |

## 1. POLICY STATEMENT
The organization MUST integrate the detection of unauthorized security-relevant changes into the organizational incident response capability. All detected unauthorized changes to system configurations and privilege escalations SHALL be tracked, monitored, corrected, and maintained for historical analysis and potential legal proceedings.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, hybrid, and on-premises |
| Security monitoring tools | YES | Detection systems must integrate with IR |
| Incident response team | YES | Must handle security-relevant changes |
| Configuration management | YES | Changes must be monitored and reported |
| Privileged accounts | YES | Elevation events require IR integration |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Ensure integration between detection and IR capabilities<br>• Define security-relevant changes requiring IR integration<br>• Approve detection and response procedures |
| Security Operations Center | • Monitor for unauthorized security-relevant changes<br>• Escalate detected changes to incident response team<br>• Maintain detection tools and integration points |
| Incident Response Team | • Respond to unauthorized security-relevant changes<br>• Document and track security-relevant incidents<br>• Maintain historical records for analysis |
| System Administrators | • Configure systems to detect security-relevant changes<br>• Report detected changes through proper channels<br>• Implement corrective actions as directed |

## 4. RULES

[RULE-01] The organization MUST define security-relevant changes that require integration with incident response capability, including but not limited to configuration changes and privilege escalations.
[VALIDATION] IF security_relevant_changes_defined = FALSE THEN violation

[RULE-02] Detection systems MUST automatically forward security-relevant change alerts to the incident response capability within 15 minutes of detection.
[VALIDATION] IF detection_to_ir_time > 15_minutes THEN violation

[RULE-03] All detected unauthorized security-relevant changes MUST be tracked through the incident response process with unique incident identifiers.
[VALIDATION] IF unauthorized_change_detected = TRUE AND incident_id = NULL THEN violation

[RULE-04] Historical records of security-relevant changes and responses MUST be maintained for a minimum of 7 years for analysis and legal purposes.
[VALIDATION] IF record_retention_period < 7_years THEN violation

[RULE-05] The incident response capability MUST include procedures for correcting unauthorized security-relevant changes within 4 hours of confirmation.
[VALIDATION] IF unauthorized_change_confirmed = TRUE AND correction_time > 4_hours AND exception_approved = FALSE THEN violation

[RULE-06] Integration between detection and response systems MUST be tested quarterly to ensure proper functionality.
[VALIDATION] IF integration_test_frequency > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security-Relevant Change Definition - Document and maintain list of changes requiring IR integration
- [PROC-02] Detection-to-Response Integration - Establish automated workflows between detection and IR systems
- [PROC-03] Unauthorized Change Response - Define steps for investigating and correcting unauthorized changes
- [PROC-04] Historical Record Management - Maintain and protect long-term records of security-relevant incidents
- [PROC-05] Integration Testing - Regular validation of detection and response system integration

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving undetected changes, integration failures, regulatory changes, system architecture changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unauthorized Configuration Change]
IF unauthorized_config_change_detected = TRUE
AND incident_response_notified = FALSE
AND detection_time > 15_minutes_ago
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Privilege Escalation Without IR Integration]
IF privilege_escalation_detected = TRUE
AND incident_created = FALSE
AND escalation_unauthorized = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Proper Change Detection and Response]
IF security_relevant_change_detected = TRUE
AND incident_response_engaged = TRUE
AND response_time < 4_hours
AND incident_documented = TRUE
THEN compliance = TRUE

[SCENARIO-04: Missing Historical Records]
IF security_incident_occurred = TRUE
AND incident_age > 6_months
AND historical_record_available = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Integration Testing Overdue]
IF last_integration_test_date > 90_days_ago
AND integration_active = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Detection of security-relevant changes defined | RULE-01 |
| Detection incorporated into incident response capability | RULE-02, RULE-03 |
| Historical records maintained | RULE-04 |
| Corrective actions implemented | RULE-05 |
| Integration functionality verified | RULE-06 |