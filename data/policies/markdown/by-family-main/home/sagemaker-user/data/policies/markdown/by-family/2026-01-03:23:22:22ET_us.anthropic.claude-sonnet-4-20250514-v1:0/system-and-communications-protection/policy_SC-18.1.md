# POLICY: SC-18.1: Identify Unacceptable Code and Take Corrective Actions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-18.1 |
| NIST Control | SC-18.1: Identify Unacceptable Code and Take Corrective Actions |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | mobile code, malicious code, detection, quarantine, blocking, corrective actions |

## 1. POLICY STATEMENT
The organization SHALL identify unacceptable mobile code through automated detection mechanisms and take immediate corrective actions when such code is detected. All mobile code SHALL be monitored, inspected, and controlled to prevent execution of unauthorized or malicious code that could compromise system security or functionality.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid environments |
| Mobile applications | YES | Corporate and BYOD mobile applications |
| Web applications | YES | Internal and external-facing applications |
| Email systems | YES | Including attachments and embedded content |
| Development environments | YES | Code repositories and CI/CD pipelines |
| Third-party software | YES | Vendor applications and integrations |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center | • Monitor mobile code detection systems<br>• Execute immediate response procedures<br>• Escalate critical incidents |
| System Administrators | • Configure detection mechanisms<br>• Implement blocking and quarantine controls<br>• Maintain detection rule updates |
| Security Engineering | • Define unacceptable mobile code criteria<br>• Design corrective action procedures<br>• Validate detection effectiveness |

## 4. RULES

[RULE-01] The organization MUST maintain a documented list of unacceptable mobile code types including but not limited to malicious macros, unauthorized scripts, and suspicious executables.
[VALIDATION] IF unacceptable_code_list_exists = FALSE OR last_updated > 90_days THEN violation

[RULE-02] Automated detection mechanisms MUST be deployed on all systems that process mobile code and SHALL operate in real-time or near real-time.
[VALIDATION] IF system_processes_mobile_code = TRUE AND detection_mechanism_deployed = FALSE THEN critical_violation

[RULE-03] When unacceptable mobile code is identified, corrective actions MUST be initiated within 5 minutes for critical systems and 15 minutes for standard systems.
[VALIDATION] IF unacceptable_code_detected = TRUE AND response_time > threshold_minutes THEN violation

[RULE-04] Corrective actions SHALL include at minimum: blocking execution, quarantining the code, and alerting security personnel.
[VALIDATION] IF corrective_action IN ["block", "quarantine", "alert"] = FALSE THEN violation

[RULE-05] All mobile code detection events and corrective actions MUST be logged with sufficient detail for forensic analysis and compliance reporting.
[VALIDATION] IF detection_event_logged = FALSE OR log_detail_sufficient = FALSE THEN violation

[RULE-06] Detection mechanisms MUST be updated with new signatures and rules within 24 hours of availability from security vendors.
[VALIDATION] IF signature_age > 24_hours AND update_available = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Mobile Code Detection Configuration - Deployment and tuning of detection tools
- [PROC-02] Incident Response for Unacceptable Code - Step-by-step response procedures
- [PROC-03] Signature Update Management - Process for maintaining current detection rules
- [PROC-04] False Positive Analysis - Procedure for validating and adjusting detection accuracy

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New threat intelligence, detection bypass incidents, technology changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Malicious Macro Detection]
IF file_type = "office_document"
AND macro_detected = TRUE
AND macro_signature IN unacceptable_list
AND corrective_action_time <= 5_minutes
THEN compliance = TRUE

[SCENARIO-02: Delayed Response to Mobile Code]
IF unacceptable_code_detected = TRUE
AND system_criticality = "high"
AND response_time > 5_minutes
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Detection Coverage]
IF system_processes_mobile_code = TRUE
AND detection_mechanism_active = FALSE
AND business_justification_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Outdated Detection Signatures]
IF signature_last_updated > 24_hours
AND vendor_update_available = TRUE
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Incomplete Logging]
IF mobile_code_event_occurred = TRUE
AND (event_logged = FALSE OR log_missing_required_fields = TRUE)
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Unacceptable mobile code is defined | [RULE-01] |
| Unacceptable mobile code is identified | [RULE-02] |
| Corrective actions are defined | [RULE-04] |
| Corrective actions are taken when unacceptable mobile code is identified | [RULE-03] |