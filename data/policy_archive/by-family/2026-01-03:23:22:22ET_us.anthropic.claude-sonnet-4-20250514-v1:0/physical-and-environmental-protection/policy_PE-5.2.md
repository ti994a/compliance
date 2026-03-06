# POLICY: PE-5.2: Link to Individual Identity

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-5.2 |
| NIST Control | PE-5.2: Link to Individual Identity |
| Version | 1.0 |
| Owner | Physical Security Manager |
| Keywords | output devices, authentication, identity verification, printers, copiers, facsimile |

## 1. POLICY STATEMENT
All output devices SHALL require individual identity verification before releasing output to users. Organizations MUST implement authentication mechanisms that link specific individuals to the receipt of output from printers, copiers, facsimile machines, and other output devices.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Printers (network/standalone) | YES | All organizational printers |
| Copiers/Multifunction devices | YES | All devices capable of producing output |
| Facsimile machines | YES | All fax machines processing sensitive data |
| Plotters/Large format printers | YES | All specialized output devices |
| Personal printers | CONDITIONAL | Only if processing sensitive data |
| Guest/Visitor devices | NO | Separate visitor access controls apply |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Establish output device authentication requirements<br>• Monitor compliance with identity linking controls<br>• Review access logs and authentication failures |
| IT Operations Team | • Configure authentication mechanisms on output devices<br>• Maintain device security settings<br>• Troubleshoot authentication issues |
| Facility Security Officers | • Monitor physical access to output device areas<br>• Investigate unauthorized output retrieval incidents<br>• Maintain logs of device access |

## 4. RULES

[RULE-01] All network-connected output devices MUST implement user authentication before releasing output.
[VALIDATION] IF device_type = "output_device" AND network_connected = TRUE AND authentication_enabled = FALSE THEN violation

[RULE-02] Authentication mechanisms SHALL verify individual identity through badge readers, PIN codes, or biometric verification before output release.
[VALIDATION] IF output_request = TRUE AND (badge_scan = FALSE AND pin_entered = FALSE AND biometric_verified = FALSE) THEN violation

[RULE-03] Output devices processing sensitive data MUST log all authentication attempts and output retrieval events with timestamp and user identity.
[VALIDATION] IF sensitive_data = TRUE AND (authentication_logged = FALSE OR retrieval_logged = FALSE) THEN violation

[RULE-04] Failed authentication attempts on output devices SHALL be logged and reported after 3 consecutive failures within 15 minutes.
[VALIDATION] IF failed_attempts >= 3 AND time_window <= 15_minutes AND alert_generated = FALSE THEN violation

[RULE-05] Unclaimed output MUST be automatically purged from device queues after 24 hours for standard documents and 4 hours for sensitive documents.
[VALIDATION] IF document_age > 24_hours AND sensitivity = "standard" AND purged = FALSE THEN violation
[VALIDATION] IF document_age > 4_hours AND sensitivity = "sensitive" AND purged = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Output Device Authentication Configuration - Standard procedures for enabling and configuring identity verification
- [PROC-02] Authentication Failure Response - Process for investigating and responding to authentication failures
- [PROC-03] Unclaimed Output Management - Procedures for handling and disposing of unclaimed printed materials
- [PROC-04] Device Access Log Review - Regular review process for output device authentication logs

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving output devices, new device installations, authentication system changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Authenticated Print Release]
IF user_authenticated = TRUE
AND identity_verified = TRUE  
AND output_released = TRUE
THEN compliance = TRUE

[SCENARIO-02: Unauthenticated Output Access]
IF user_authenticated = FALSE
AND output_released = TRUE
AND device_type = "network_printer"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Excessive Authentication Failures]
IF failed_attempts >= 3
AND time_window <= 15_minutes
AND alert_generated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unclaimed Sensitive Document]
IF document_sensitivity = "sensitive"
AND queue_time > 4_hours
AND document_purged = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Guest Printer Access]
IF user_type = "guest"
AND device_authentication = "badge_required"
AND guest_badge_issued = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Individual identity is linked to receipt of output from output devices | [RULE-01], [RULE-02] |
| Authentication mechanisms implemented on output devices | [RULE-02] |
| Logging and monitoring of output device access | [RULE-03], [RULE-04] |
| Protection of unclaimed output materials | [RULE-05] |