# POLICY: SI-7.17: Runtime Application Self-protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-7.17 |
| NIST Control | SI-7.17: Runtime Application Self-protection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | runtime protection, application security, exploit prevention, vulnerability detection, software instrumentation |

## 1. POLICY STATEMENT
All applications deployed in production environments MUST implement runtime application self-protection (RASP) controls to detect and block exploitation of software vulnerabilities in real-time. RASP solutions SHALL be configured to provide contextual awareness and automated response capabilities beyond traditional perimeter defenses.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Web Applications | YES | All customer-facing and internal web apps |
| Mobile Applications | YES | Native and hybrid mobile applications |
| API Services | YES | REST, GraphQL, and SOAP services |
| Legacy Applications | CONDITIONAL | Where technically feasible |
| Third-party Applications | YES | When organization controls deployment |
| Development/Test Apps | NO | Unless handling production data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Application Security Team | • Define RASP control requirements<br>• Evaluate and approve RASP solutions<br>• Monitor RASP effectiveness metrics |
| Development Teams | • Integrate RASP agents into applications<br>• Configure application-specific protection rules<br>• Respond to RASP-generated alerts |
| Security Operations Center | • Monitor RASP alerts and incidents<br>• Investigate blocked exploitation attempts<br>• Coordinate incident response activities |

## 4. RULES

[RULE-01] All in-scope applications MUST implement approved RASP solutions before production deployment.
[VALIDATION] IF application_status = "production" AND rasp_implemented = FALSE THEN critical_violation

[RULE-02] RASP solutions MUST be configured to detect and block common vulnerability exploitations including SQL injection, cross-site scripting, and code injection attacks.
[VALIDATION] IF rasp_coverage < required_vulnerability_types THEN violation

[RULE-03] RASP solutions SHALL operate in protection mode, not monitor-only mode, unless explicitly approved by the Application Security Team.
[VALIDATION] IF rasp_mode = "monitor" AND protection_exception = FALSE THEN violation

[RULE-04] RASP alert responses MUST be configured with automated actions including session termination, user notification, and security team alerting within 30 seconds of threat detection.
[VALIDATION] IF threat_detected = TRUE AND response_time > 30_seconds THEN violation

[RULE-05] RASP configurations and protection rules MUST be reviewed and updated within 30 days of new vulnerability disclosures affecting the application technology stack.
[VALIDATION] IF vulnerability_disclosed = TRUE AND rasp_update_time > 30_days THEN violation

[RULE-06] Applications with RASP bypass mechanisms MUST maintain audit logs of all bypass events and require dual approval for activation.
[VALIDATION] IF rasp_bypass = TRUE AND (audit_logged = FALSE OR dual_approval = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] RASP Solution Evaluation - Assessment and approval process for RASP technologies
- [PROC-02] RASP Integration Standards - Technical requirements for embedding RASP in applications
- [PROC-03] RASP Alert Response - Incident handling procedures for runtime threat detection
- [PROC-04] RASP Configuration Management - Change control for protection rules and policies

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, new application deployments, RASP solution changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Production App Without RASP]
IF application_environment = "production"
AND customer_data_access = TRUE
AND rasp_solution = "none"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: RASP in Monitor Mode]
IF rasp_deployed = TRUE
AND rasp_mode = "monitor"
AND protection_exception_approved = FALSE
AND application_risk_level = "high"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Delayed RASP Update]
IF critical_vulnerability_disclosed = TRUE
AND vulnerability_affects_app = TRUE
AND rasp_rules_updated = FALSE
AND days_since_disclosure > 30
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: RASP Alert Response Delay]
IF rasp_threat_detected = TRUE
AND automated_response_time > 30_seconds
AND manual_intervention_required = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant RASP Implementation]
IF rasp_solution = "approved"
AND rasp_mode = "protection"
AND vulnerability_coverage >= 95_percent
AND response_time <= 30_seconds
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Controls for application self-protection at runtime are defined | RULE-01, RULE-02 |
| Controls are implemented for application self-protection at runtime | RULE-01, RULE-03, RULE-04 |
| Runtime instrumentation detects exploitation attempts | RULE-02, RULE-04 |
| Protection mechanisms block malicious inputs | RULE-03, RULE-04 |
| Automated response actions are configured | RULE-04, RULE-06 |