# POLICY: SI-7.7: Integration of Detection and Response

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-7.7 |
| NIST Control | SI-7.7: Integration of Detection and Response |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | incident response, detection, unauthorized changes, security-relevant changes, configuration settings, privilege escalation |

## 1. POLICY STATEMENT
The organization MUST incorporate detection of unauthorized security-relevant system changes into the incident response capability. All detected unauthorized changes SHALL be tracked, monitored, corrected, and maintained for historical analysis and potential legal proceedings.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing organizational data |
| Development Systems | YES | Systems containing production data or code |
| Test/Staging Systems | YES | Systems connected to production networks |
| Contractor Systems | CONDITIONAL | If processing organizational data |
| Personal Devices | CONDITIONAL | If accessing organizational resources |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define security-relevant changes<br>• Approve detection integration procedures<br>• Oversee incident response integration |
| SOC Manager | • Implement detection mechanisms<br>• Monitor for unauthorized changes<br>• Escalate incidents per procedures |
| Incident Response Team | • Respond to detected changes<br>• Document and track incidents<br>• Maintain historical records |
| System Administrators | • Configure change detection tools<br>• Report detected changes<br>• Implement corrective actions |

## 4. RULES
[RULE-01] Security-relevant changes MUST be formally defined and documented, including configuration changes, privilege escalations, and critical file modifications.
[VALIDATION] IF security_relevant_changes_defined = FALSE THEN violation

[RULE-02] Detection mechanisms MUST be integrated with the organizational incident response system within 30 days of implementation.
[VALIDATION] IF detection_integrated = FALSE AND days_since_implementation > 30 THEN violation

[RULE-03] All detected unauthorized changes MUST trigger an incident response workflow within 15 minutes of detection.
[VALIDATION] IF unauthorized_change_detected = TRUE AND incident_response_time > 15_minutes THEN violation

[RULE-04] Historical records of detected changes MUST be maintained for minimum 7 years for audit and legal purposes.
[VALIDATION] IF record_retention_period < 7_years THEN violation

[RULE-05] Detection tools MUST monitor configuration settings, system privileges, and critical system files continuously.
[VALIDATION] IF monitoring_coverage < 100% OR monitoring_frequency != "continuous" THEN violation

[RULE-06] Incident response personnel MUST be trained on security-relevant change detection procedures within 90 days of assignment.
[VALIDATION] IF training_completed = FALSE AND days_since_assignment > 90 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security-Relevant Change Definition - Document and maintain list of changes requiring detection
- [PROC-02] Detection Tool Integration - Configure and integrate detection mechanisms with incident response
- [PROC-03] Incident Response Workflow - Define response procedures for detected changes
- [PROC-04] Historical Record Maintenance - Establish retention and archival procedures
- [PROC-05] Personnel Training - Train incident response staff on detection procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving undetected changes, tool implementations, organizational changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unintegrated Detection Tool]
IF detection_tool_deployed = TRUE
AND incident_response_integration = FALSE
AND deployment_date > 30_days_ago
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Delayed Incident Response]
IF unauthorized_change_detected = TRUE
AND incident_ticket_created = TRUE
AND response_time = 25_minutes
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing Historical Records]
IF security_incident_occurred = TRUE
AND incident_date > 5_years_ago
AND historical_records_available = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Incomplete Change Definition]
IF privilege_escalation_detected = FALSE
AND unauthorized_privilege_change = TRUE
AND security_relevant_changes_list_updated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Proper Integration]
IF detection_tool_integrated = TRUE
AND incident_response_automated = TRUE
AND historical_records_maintained = TRUE
AND response_time < 15_minutes
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Detection of security-relevant changes defined | [RULE-01] |
| Detection incorporated into incident response capability | [RULE-02], [RULE-03] |
| Historical records maintained | [RULE-04] |
| Continuous monitoring implemented | [RULE-05] |
| Personnel trained on procedures | [RULE-06] |