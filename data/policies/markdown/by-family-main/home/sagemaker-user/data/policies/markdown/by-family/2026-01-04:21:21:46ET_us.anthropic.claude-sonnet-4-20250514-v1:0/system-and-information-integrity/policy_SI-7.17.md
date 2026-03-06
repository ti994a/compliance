# POLICY: SI-7.17: Runtime Application Self-Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-7.17 |
| NIST Control | SI-7.17: Runtime Application Self-Protection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | runtime protection, application security, exploit prevention, vulnerability detection, software instrumentation |

## 1. POLICY STATEMENT
All applications processing sensitive data or supporting critical business functions MUST implement runtime application self-protection (RASP) controls to detect and block exploitation attempts in real-time. RASP solutions SHALL be configured to monitor application inputs, detect malicious activities, and take automated protective actions when threats are identified.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Web Applications | YES | All internet-facing and internal web apps |
| API Services | YES | REST, SOAP, GraphQL APIs |
| Mobile Applications | YES | iOS and Android applications |
| Desktop Applications | CONDITIONAL | Only those processing PII or financial data |
| Legacy Applications | CONDITIONAL | Risk assessment required |
| Development/Test Systems | NO | Unless processing production data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Application Security Team | • Define RASP implementation requirements<br>• Configure protection policies<br>• Monitor security events and alerts |
| Development Teams | • Integrate RASP agents into applications<br>• Test RASP functionality during deployment<br>• Remediate identified vulnerabilities |
| Security Operations Center | • Monitor RASP alerts and incidents<br>• Investigate security events<br>• Coordinate incident response activities |

## 4. RULES
[RULE-01] Applications classified as HIGH or MODERATE impact MUST implement RASP controls before production deployment.
[VALIDATION] IF impact_level IN ["HIGH", "MODERATE"] AND rasp_implemented = FALSE THEN violation

[RULE-02] RASP solutions MUST be configured to detect and block SQL injection, XSS, command injection, and path traversal attacks.
[VALIDATION] IF rasp_configured = TRUE AND attack_types_covered < ["SQLi", "XSS", "CMDi", "PathTraversal"] THEN violation

[RULE-03] RASP protection mode MUST be enabled for production applications within 30 days of initial monitor mode deployment.
[VALIDATION] IF environment = "production" AND rasp_mode = "monitor" AND deployment_days > 30 THEN violation

[RULE-04] RASP security events MUST be logged and forwarded to the SIEM within 5 minutes of detection.
[VALIDATION] IF rasp_event_detected = TRUE AND siem_forward_time > 5_minutes THEN violation

[RULE-05] Applications SHALL terminate user sessions when RASP detects active exploitation attempts.
[VALIDATION] IF exploitation_detected = TRUE AND session_terminated = FALSE THEN violation

[RULE-06] RASP configurations MUST be reviewed and updated within 48 hours of new vulnerability disclosures affecting protected applications.
[VALIDATION] IF new_vulnerability_disclosed = TRUE AND rasp_config_updated = FALSE AND hours_elapsed > 48 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] RASP Implementation - Standard process for integrating RASP into application deployment pipeline
- [PROC-02] Threat Response - Automated and manual response procedures for RASP-detected threats
- [PROC-03] Configuration Management - Process for maintaining and updating RASP policies and rules
- [PROC-04] Performance Monitoring - Procedures to monitor RASP impact on application performance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New vulnerability classes, major application updates, security incidents involving RASP-protected applications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Production Deployment Without RASP]
IF application_classification = "HIGH"
AND environment = "production"
AND rasp_implemented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Monitor Mode Extended Beyond Policy]
IF rasp_mode = "monitor"
AND environment = "production"
AND deployment_date < (current_date - 30_days)
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Attack Detection Without Session Termination]
IF rasp_attack_detected = TRUE
AND attack_type = "SQL_injection"
AND user_session_active = TRUE
AND session_terminated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Delayed SIEM Integration]
IF rasp_event_generated = TRUE
AND siem_received_time > (event_time + 5_minutes)
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant RASP Implementation]
IF application_classification = "HIGH"
AND rasp_implemented = TRUE
AND rasp_mode = "protection"
AND siem_integration = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Runtime protection controls are defined | [RULE-01], [RULE-02] |
| Runtime protection controls are implemented | [RULE-03], [RULE-04] |
| Threat detection and blocking capability | [RULE-02], [RULE-05] |
| Security event logging and monitoring | [RULE-04], [RULE-06] |