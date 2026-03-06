# POLICY: PE-3.8: Access Control Vestibules

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-3.8 |
| NIST Control | PE-3.8: Access Control Vestibules |
| Version | 1.0 |
| Owner | Chief Physical Security Officer |
| Keywords | access control, vestibules, piggybacking, tailgating, interlocking doors, physical security |

## 1. POLICY STATEMENT
The organization SHALL employ access control vestibules at designated high-security facility locations to prevent unauthorized individuals from following authorized personnel into controlled access areas. Vestibules MUST utilize interlocking door systems that prevent piggybacking and tailgating incidents.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data centers | YES | All primary and backup facilities |
| Executive floors | YES | C-suite and board meeting areas |
| R&D laboratories | YES | Intellectual property protection zones |
| Financial processing areas | YES | SOX compliance requirement |
| Server rooms | YES | Critical infrastructure protection |
| General office space | NO | Standard badge access sufficient |
| Public areas | NO | Vestibules not applicable |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Physical Security Officer | • Define vestibule deployment locations<br>• Approve vestibule system specifications<br>• Oversee compliance monitoring |
| Facilities Manager | • Implement vestibule systems<br>• Maintain interlocking door mechanisms<br>• Coordinate with security operations |
| Security Operations Center | • Monitor vestibule access events<br>• Respond to containment alerts<br>• Document security incidents |

## 4. RULES
[RULE-01] Access control vestibules MUST be deployed at all facilities classified as Security Level 3 or higher per the Physical Security Classification Standard.
[VALIDATION] IF facility_security_level >= 3 AND vestibule_present = FALSE THEN violation

[RULE-02] Vestibule interlocking systems MUST prevent more than one door from being open simultaneously during normal operations.
[VALIDATION] IF door1_open = TRUE AND door2_open = TRUE AND emergency_mode = FALSE THEN violation

[RULE-03] Vestibule capacity SHALL NOT exceed two authorized individuals per access cycle unless specifically approved for group access scenarios.
[VALIDATION] IF individuals_in_vestibule > 2 AND group_access_approved = FALSE THEN violation

[RULE-04] Failed vestibule access attempts MUST trigger immediate security alert and containment procedures within 30 seconds.
[VALIDATION] IF access_attempt_failed = TRUE AND alert_time > 30_seconds THEN violation

[RULE-05] Vestibule systems MUST maintain operational logs for all access events for minimum 90 days for compliance review.
[VALIDATION] IF log_retention_days < 90 THEN violation

[RULE-06] Emergency override capabilities MUST be available to security personnel and fire safety systems while maintaining audit trail.
[VALIDATION] IF emergency_override_used = TRUE AND audit_record = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Vestibule Access Authorization - Define personnel authorized for vestibule-protected areas
- [PROC-02] Interlocking Door Maintenance - Regular testing and calibration of door mechanisms
- [PROC-03] Containment Response - Security response to failed access attempts or system alerts
- [PROC-04] Emergency Override - Procedures for emergency access during system failures or evacuations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, facility modifications, technology upgrades, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Piggybacking Prevention]
IF authorized_person_enters = TRUE
AND unauthorized_person_follows = TRUE
AND vestibule_prevents_entry = TRUE
THEN compliance = TRUE

[SCENARIO-02: Interlocking Door Failure]
IF door1_open = TRUE
AND door2_opens = TRUE
AND emergency_mode = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Excessive Occupancy]
IF individuals_in_vestibule = 4
AND group_access_approved = FALSE
AND system_allows_entry = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Failed Access Response]
IF tailgating_detected = TRUE
AND security_alert_time = 45_seconds
AND containment_activated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Emergency Override Usage]
IF fire_alarm_active = TRUE
AND vestibule_override_engaged = TRUE
AND audit_log_created = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Vestibules employed at defined locations | [RULE-01] |
| Interlocking door functionality | [RULE-02] |
| Occupancy control | [RULE-03] |
| Security incident response | [RULE-04] |
| Access logging and retention | [RULE-05] |
| Emergency procedures | [RULE-06] |