```markdown
# POLICY: IA-12.2: Identity Evidence

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-12.2 |
| NIST Control | IA-12.2: Identity Evidence |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | identity proofing, registration authority, documentary evidence, biometrics, identification |

## 1. POLICY STATEMENT
All individuals requesting system access MUST present acceptable evidence of identification to the registration authority before account provisioning. The forms and combination of identity evidence required SHALL be commensurate with the risk level of the systems, roles, and privileges being requested.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Full-time, part-time, temporary |
| Contractors | YES | All external personnel requiring system access |
| Vendors | YES | Third-party personnel requiring system access |
| Partners | YES | Business partners requiring system access |
| Guests | CONDITIONAL | Only if requiring authenticated system access |
| Service accounts | NO | Technical accounts without human identity |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Registration Authority | • Verify identity evidence authenticity<br>• Maintain evidence validation procedures<br>• Document evidence acceptance decisions<br>• Escalate suspicious documentation |
| Identity Management Team | • Define acceptable evidence types<br>• Train registration authority personnel<br>• Audit evidence collection processes<br>• Maintain evidence retention policies |
| HR Department | • Provide employee verification support<br>• Validate employment status<br>• Coordinate with registration authority |

## 4. RULES
[RULE-01] Registration authority MUST require presentation of identity evidence before provisioning any system account or access privileges.
[VALIDATION] IF account_provisioned = TRUE AND identity_evidence_presented = FALSE THEN critical_violation

[RULE-02] Identity evidence requirements MUST align with system risk classification: Low risk systems require one form of documentary evidence, Moderate risk systems require two forms including one government-issued photo ID, High risk systems require two forms plus biometric verification.
[VALIDATION] IF system_risk = "high" AND (documentary_evidence_count < 2 OR biometric_verification = FALSE) THEN violation

[RULE-03] Registration authority MUST verify authenticity of presented identity documents using established verification procedures within 5 business days of presentation.
[VALIDATION] IF verification_time > 5_business_days THEN violation

[RULE-04] All identity evidence presentations and verification decisions MUST be documented and retained for audit purposes for minimum 7 years.
[VALIDATION] IF evidence_documented = FALSE OR retention_period < 7_years THEN violation

[RULE-05] Suspicious or potentially fraudulent identity evidence MUST be escalated to security team within 24 hours of detection.
[VALIDATION] IF suspicious_evidence_detected = TRUE AND escalation_time > 24_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Identity Evidence Verification - Standardized process for validating documentary evidence authenticity
- [PROC-02] Biometric Enrollment - Procedures for collecting and storing biometric identifiers for high-risk access
- [PROC-03] Evidence Documentation - Requirements for recording evidence types, verification results, and retention
- [PROC-04] Fraud Detection - Process for identifying and responding to suspicious identity documentation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving identity fraud, changes to risk classification, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Employee Onboarding]
IF user_type = "employee"
AND system_risk = "moderate"
AND documentary_evidence_count >= 2
AND government_photo_id_present = TRUE
THEN compliance = TRUE

[SCENARIO-02: High-Risk Contractor Access]
IF user_type = "contractor"
AND system_risk = "high"
AND documentary_evidence_count >= 2
AND biometric_verification = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Unverified Identity Evidence]
IF identity_evidence_presented = TRUE
AND verification_completed = FALSE
AND days_since_presentation > 5
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Documentation]
IF account_provisioned = TRUE
AND identity_evidence_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Fraudulent Document Response]
IF suspicious_evidence_detected = TRUE
AND escalation_completed = TRUE
AND escalation_time <= 24_hours
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Evidence of individual identification is presented to registration authority | RULE-01, RULE-02 |
| Identity evidence verification and documentation | RULE-03, RULE-04 |
| Fraud detection and response | RULE-05 |
```