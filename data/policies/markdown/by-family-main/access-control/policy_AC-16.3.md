```markdown
# POLICY: AC-16.3: Maintenance of Attribute Associations by System

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-16.3 |
| NIST Control | AC-16.3: Maintenance of Attribute Associations by System |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | attribute integrity, security attributes, privacy attributes, automated policy, association maintenance |

## 1. POLICY STATEMENT
The organization SHALL maintain the association and integrity of security and privacy attributes to subjects and objects with sufficient assurance to support automated policy decisions. Attribute associations MUST be protected against unauthorized modification and monitored for integrity violations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information systems | YES | All systems processing regulated data |
| Cloud services | YES | Including IaaS, PaaS, SaaS platforms |
| Mobile devices | YES | Corporate and BYOD devices |
| IoT devices | CONDITIONAL | Only if processing sensitive data |
| Test environments | CONDITIONAL | If containing production data copies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Implement attribute integrity monitoring<br>• Configure automated policy enforcement<br>• Respond to integrity violations |
| Data Owners | • Define required security/privacy attributes<br>• Approve attribute association requirements<br>• Validate attribute accuracy |
| Security Operations | • Monitor attribute integrity alerts<br>• Investigate attribute tampering incidents<br>• Maintain integrity baselines |

## 4. RULES

[RULE-01] Systems MUST maintain cryptographic integrity protection for all security and privacy attribute associations to prevent unauthorized modification.
[VALIDATION] IF attribute_integrity_protection = FALSE THEN critical_violation

[RULE-02] Automated integrity monitoring MUST detect and alert on any changes to attribute associations within 15 minutes of occurrence.
[VALIDATION] IF detection_time > 15_minutes THEN violation

[RULE-03] Security attributes SHALL include at minimum: classification level, handling restrictions, retention period, and access control labels.
[VALIDATION] IF missing_required_attributes > 0 THEN violation

[RULE-04] Privacy attributes SHALL include at minimum: PII indicators, consent status, processing purpose, and retention requirements.
[VALIDATION] IF privacy_data = TRUE AND missing_privacy_attributes > 0 THEN violation

[RULE-05] Attribute associations MUST be restored from known-good baselines within 1 hour of detecting integrity violations.
[VALIDATION] IF integrity_violation = TRUE AND restoration_time > 1_hour THEN violation

[RULE-06] All attribute modifications MUST be logged with user identity, timestamp, old value, and new value for audit purposes.
[VALIDATION] IF attribute_change_logged = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Attribute Integrity Monitoring - Continuous monitoring and alerting on attribute changes
- [PROC-02] Baseline Management - Creation and maintenance of known-good attribute baselines
- [PROC-03] Incident Response - Response procedures for attribute integrity violations
- [PROC-04] Attribute Validation - Periodic verification of attribute accuracy and associations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving attributes, system architecture changes, new compliance requirements

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unauthorized Attribute Modification]
IF attribute_modified = TRUE
AND modification_authorized = FALSE
AND integrity_monitoring = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Missing Privacy Attributes on PII]
IF data_contains_pii = TRUE
AND privacy_attributes_present = FALSE
AND system_in_production = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Delayed Integrity Violation Detection]
IF attribute_tampering_detected = TRUE
AND detection_delay > 15_minutes
AND monitoring_system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Successful Automated Policy Enforcement]
IF security_attributes_intact = TRUE
AND privacy_attributes_intact = TRUE
AND automated_policy_applied = TRUE
AND no_integrity_violations = TRUE
THEN compliance = TRUE

[SCENARIO-05: Incomplete Attribute Restoration]
IF integrity_violation_detected = TRUE
AND restoration_attempted = TRUE
AND restoration_time > 1_hour
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Security attribute association maintenance | [RULE-01], [RULE-03] |
| Privacy attribute association maintenance | [RULE-01], [RULE-04] |
| Integrity monitoring implementation | [RULE-02], [RULE-05] |
| Automated policy support | [RULE-01], [RULE-06] |
| Attribute definition completeness | [RULE-03], [RULE-04] |
| Incident response capability | [RULE-05], [RULE-06] |
```