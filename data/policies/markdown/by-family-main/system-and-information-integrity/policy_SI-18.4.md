# POLICY: SI-18.4: Individual Requests

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-18.4 |
| NIST Control | SI-18.4: Individual Requests |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII correction, deletion requests, individual rights, data subject requests, privacy compliance |

## 1. POLICY STATEMENT
The organization SHALL correct or delete personally identifiable information (PII) upon verified request by individuals or their designated representatives. All correction and deletion requests MUST be processed through established procedures with appropriate legal and privacy review.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Systems processing, storing, or transmitting PII |
| Third-Party Processors | YES | Must comply via contractual requirements |
| Archived/Backup Data | YES | Including offline storage and disaster recovery systems |
| Public Records | CONDITIONAL | Subject to legal retention requirements |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee PII correction/deletion program<br>• Approve complex requests<br>• Coordinate with legal counsel |
| Data Protection Team | • Process individual requests<br>• Verify requestor identity<br>• Execute approved corrections/deletions |
| System Administrators | • Implement technical corrections/deletions<br>• Verify completeness across all systems<br>• Maintain audit logs |
| Legal Counsel | • Review requests with legal implications<br>• Advise on retention requirements<br>• Assess regulatory compliance |

## 4. RULES
[RULE-01] Organizations MUST establish formal procedures for receiving, evaluating, and responding to individual requests for PII correction or deletion.
[VALIDATION] IF correction_deletion_procedure = "undefined" THEN violation

[RULE-02] Individual identity and authorization MUST be verified before processing any PII correction or deletion request.
[VALIDATION] IF identity_verified = FALSE AND request_processed = TRUE THEN critical_violation

[RULE-03] Correction or deletion requests MUST be acknowledged within 5 business days and completed within 30 business days unless legal review is required.
[VALIDATION] IF acknowledgment_time > 5_business_days THEN violation
[VALIDATION] IF completion_time > 30_business_days AND legal_review_required = FALSE THEN violation

[RULE-04] All PII corrections and deletions MUST be applied across all organizational systems and databases where the information is maintained.
[VALIDATION] IF correction_applied_all_systems = FALSE THEN critical_violation

[RULE-05] Organizations MUST consult with privacy officials and legal counsel for requests involving legal retention requirements or potential adverse impacts.
[VALIDATION] IF legal_retention_conflict = TRUE AND legal_consultation = FALSE THEN violation

[RULE-06] All correction and deletion actions MUST be logged with details including requestor, action taken, systems affected, and completion date.
[VALIDATION] IF correction_deletion_logged = FALSE THEN violation

[RULE-07] Individuals MUST be notified of the outcome of their correction or deletion request, including any limitations or denials with justification.
[VALIDATION] IF request_outcome_notification = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Individual Request Intake - Standardized process for receiving and documenting requests
- [PROC-02] Identity Verification - Methods for confirming requestor identity and authorization
- [PROC-03] System Discovery - Identifying all systems containing relevant PII
- [PROC-04] Legal Review Process - Escalation procedures for complex requests
- [PROC-05] Technical Implementation - Steps for executing corrections/deletions across systems

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Changes in privacy regulations, significant data breaches, audit findings, system architecture changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Correction Request]
IF request_type = "correction"
AND identity_verified = TRUE
AND no_legal_conflicts = TRUE
AND processing_time <= 30_days
THEN compliance = TRUE

[SCENARIO-02: Unverified Deletion Request]
IF request_type = "deletion"
AND identity_verified = FALSE
AND pii_deleted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Partial System Implementation]
IF correction_approved = TRUE
AND primary_system_updated = TRUE
AND backup_system_updated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Legal Retention Conflict]
IF deletion_requested = TRUE
AND legal_hold_active = TRUE
AND legal_counsel_consulted = FALSE
AND deletion_denied = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Delayed Response]
IF request_received = TRUE
AND acknowledgment_sent = FALSE
AND days_elapsed > 5
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| PII correction/deletion upon individual request | [RULE-01], [RULE-04] |
| Proper authorization and verification | [RULE-02] |
| Timely response to requests | [RULE-03] |
| Comprehensive system coverage | [RULE-04] |
| Legal and privacy consultation | [RULE-05] |
| Audit trail maintenance | [RULE-06] |
| Requestor notification | [RULE-07] |