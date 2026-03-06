# POLICY: SI-18.4: Individual Requests

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-18.4 |
| NIST Control | SI-18.4: Individual Requests |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | personally identifiable information, PII correction, data subject rights, individual requests, privacy |

## 1. POLICY STATEMENT
The organization SHALL correct or delete personally identifiable information (PII) upon verified request by individuals or their designated representatives. All correction and deletion requests MUST be processed through established procedures with appropriate legal and privacy review.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All PII processing systems | YES | Including cloud and hybrid environments |
| Employee PII | YES | Subject to HR policy coordination |
| Customer/Client PII | YES | All business functions |
| Third-party PII | YES | When organization is data controller |
| Archived/Backup data | YES | Technical feasibility considerations apply |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Establish correction/deletion procedures<br>• Review complex requests<br>• Coordinate with legal counsel |
| Data Protection Officers | • Process individual requests<br>• Validate requestor identity<br>• Execute approved corrections/deletions |
| System Administrators | • Implement technical corrections/deletions<br>• Maintain audit logs of changes<br>• Coordinate cross-system updates |
| Legal Counsel | • Review requests with legal implications<br>• Advise on regulatory requirements<br>• Approve/deny complex cases |

## 4. RULES
[RULE-01] Organizations MUST establish documented procedures for receiving, validating, and processing PII correction and deletion requests from individuals or their designated representatives.
[VALIDATION] IF correction_deletion_procedure = "not_documented" OR correction_deletion_procedure = "not_established" THEN violation

[RULE-02] Individual identity and authorization MUST be verified before processing any PII correction or deletion request using multi-factor authentication or equivalent verification methods.
[VALIDATION] IF request_processed = TRUE AND identity_verified = FALSE THEN critical_violation

[RULE-03] PII correction or deletion requests MUST be acknowledged within 5 business days and completed within 30 business days unless legal or technical constraints require extension.
[VALIDATION] IF acknowledgment_time > 5_business_days THEN violation
[VALIDATION] IF completion_time > 30_business_days AND extension_documented = FALSE THEN violation

[RULE-04] All PII corrections and deletions MUST be logged with timestamp, requestor identity, data elements affected, and personnel responsible for the action.
[VALIDATION] IF pii_change_executed = TRUE AND audit_log_entry = FALSE THEN violation

[RULE-05] Complex correction or deletion requests that may impact legal, regulatory, or business requirements MUST be reviewed by the Chief Privacy Officer and legal counsel before execution.
[VALIDATION] IF request_complexity = "high" AND (cpo_review = FALSE OR legal_review = FALSE) THEN violation

[RULE-06] When PII correction or deletion is technically infeasible or legally prohibited, individuals MUST be notified in writing with specific reasons and alternative remedies within 15 business days.
[VALIDATION] IF request_denied = TRUE AND written_notification_time > 15_business_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Individual Request Intake Process - Standardized forms and channels for receiving correction/deletion requests
- [PROC-02] Identity Verification Protocol - Multi-step process to validate requestor identity and authorization
- [PROC-03] PII Impact Assessment - Evaluation of correction/deletion impact on business operations and legal compliance
- [PROC-04] Cross-System Data Synchronization - Coordinated updates across all systems containing the affected PII
- [PROC-05] Legal Review Escalation - Process for complex cases requiring legal counsel involvement

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Privacy regulation changes, significant data breaches, audit findings, technology changes affecting PII processing

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Individual Correction Request]
IF request_type = "correction"
AND identity_verified = TRUE
AND request_complexity = "standard"
AND processing_time <= 30_business_days
THEN compliance = TRUE

[SCENARIO-02: Unverified Deletion Request]
IF request_type = "deletion"
AND identity_verified = FALSE
AND pii_deleted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Complex Request Without Legal Review]
IF request_impact = "high_legal_risk"
AND legal_review_completed = FALSE
AND request_processed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Delayed Response Without Extension]
IF acknowledgment_sent = FALSE
AND request_age > 5_business_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Technically Infeasible Request]
IF deletion_technically_feasible = FALSE
AND written_explanation_provided = TRUE
AND alternative_remedies_offered = TRUE
AND notification_time <= 15_business_days
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| PII corrected or deleted upon individual request | RULE-01, RULE-03 |
| Proper verification of requestor identity | RULE-02 |
| Timely processing and response | RULE-03, RULE-06 |
| Audit trail maintenance | RULE-04 |
| Appropriate review for complex cases | RULE-05 |