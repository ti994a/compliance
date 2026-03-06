# POLICY: SA-3.2: Use of Live or Operational Data

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-3.2 |
| NIST Control | SA-3.2: Use of Live or Operational Data |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | live data, operational data, preproduction, development, testing, PII, data protection |

## 1. POLICY STATEMENT
The organization must approve, document, and control the use of live or operational data in preproduction environments. Preproduction environments containing live data must be protected at the same impact or classification level as the live data itself.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Development environments | YES | All dev, test, staging environments |
| Testing environments | YES | Including integration and QA environments |
| Training environments | YES | When using live data for training purposes |
| Production environments | NO | Covered under separate production controls |
| Sandbox environments | CONDITIONAL | Only if processing live data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owner | • Approve live data usage requests<br>• Define data classification requirements<br>• Validate business justification |
| Development Manager | • Ensure team compliance with live data procedures<br>• Implement technical controls for data protection<br>• Document live data usage and access |
| Security Team | • Review and approve live data usage requests<br>• Conduct risk assessments for live data usage<br>• Monitor preproduction environment security |

## 4. RULES
[RULE-01] Live data usage in preproduction environments MUST be formally approved by the Data Owner and Security Team before implementation.
[VALIDATION] IF live_data_used = TRUE AND approval_documented = FALSE THEN violation

[RULE-02] All live data usage in preproduction environments MUST be documented including data types, justification, access controls, and retention period.
[VALIDATION] IF live_data_used = TRUE AND documentation_complete = FALSE THEN violation

[RULE-03] Access to live data in preproduction environments MUST be controlled through role-based access controls and logged for audit purposes.
[VALIDATION] IF live_data_access = TRUE AND (rbac_enabled = FALSE OR logging_enabled = FALSE) THEN violation

[RULE-04] Preproduction environments containing live data MUST implement security controls equivalent to the data's classification level.
[VALIDATION] IF live_data_classification > environment_security_level THEN critical_violation

[RULE-05] Live data in preproduction environments MUST be purged within 90 days unless extended approval is obtained and documented.
[VALIDATION] IF live_data_age > 90_days AND extended_approval = FALSE THEN violation

[RULE-06] Personally Identifiable Information (PII) MUST NOT be used in preproduction environments unless no alternative exists and explicit approval is obtained.
[VALIDATION] IF pii_present = TRUE AND (alternative_available = TRUE OR explicit_approval = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Live Data Usage Request Process - Formal approval workflow for requesting live data in preproduction
- [PROC-02] Risk Assessment for Live Data Usage - Security and privacy risk evaluation procedures
- [PROC-03] Data Sanitization and Masking - Technical procedures for protecting sensitive data elements
- [PROC-04] Preproduction Environment Hardening - Security configuration standards for environments with live data
- [PROC-05] Live Data Purging and Retention - Automated and manual data removal procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Data breach involving preproduction data, new regulatory requirements, significant system changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unapproved Live Data Usage]
IF live_data_used = TRUE
AND formal_approval = FALSE
AND environment_type = "development"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: PII in Test Environment]
IF data_contains_pii = TRUE
AND environment_type = "testing"
AND data_masking_applied = FALSE
AND explicit_pii_approval = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Inadequate Environment Protection]
IF live_data_classification = "Confidential"
AND environment_security_level = "Internal"
AND live_data_present = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Expired Live Data Retention]
IF live_data_age > 90_days
AND extended_approval_documented = TRUE
AND extended_approval_valid = TRUE
THEN compliance = TRUE

[SCENARIO-05: Proper Live Data Controls]
IF live_data_used = TRUE
AND formal_approval = TRUE
AND documentation_complete = TRUE
AND security_controls_adequate = TRUE
AND access_logging_enabled = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Live data usage approval | RULE-01 |
| Live data usage documentation | RULE-02 |
| Live data access control | RULE-03 |
| Environment protection level | RULE-04 |
| Data retention and purging | RULE-05 |
| PII protection requirements | RULE-06 |