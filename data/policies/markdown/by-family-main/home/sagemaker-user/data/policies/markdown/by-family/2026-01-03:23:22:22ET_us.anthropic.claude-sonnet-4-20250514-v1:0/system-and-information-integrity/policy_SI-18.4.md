# POLICY: SI-18.4: Individual Requests

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-18.4 |
| NIST Control | SI-18.4: Individual Requests |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII, correction, deletion, individual requests, privacy rights, data accuracy |

## 1. POLICY STATEMENT
The organization SHALL correct or delete personally identifiable information (PII) upon valid request by individuals or their designated representatives. All correction and deletion requests MUST be evaluated based on organizational discretion, legal requirements, and impact assessment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All PII processing systems | YES | Including cloud and hybrid environments |
| Customer PII | YES | All customer-facing applications |
| Employee PII | YES | HR and internal systems |
| Third-party PII | YES | Partner and vendor data |
| Public information | CONDITIONAL | Subject to legal review |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee PII correction/deletion program<br>• Final approval for complex cases<br>• Policy compliance monitoring |
| Privacy Team | • Process individual requests<br>• Coordinate with legal counsel<br>• Maintain request documentation |
| System Administrators | • Execute technical corrections/deletions<br>• Verify data removal completeness<br>• Document system changes |
| Legal Counsel | • Review legally complex requests<br>• Advise on regulatory compliance<br>• Approve/deny borderline cases |

## 4. RULES
[RULE-01] All individual requests for PII correction or deletion MUST be acknowledged within 5 business days of receipt.
[VALIDATION] IF request_received_date + 5_business_days < acknowledgment_date THEN violation

[RULE-02] PII correction or deletion actions MUST be completed within 30 calendar days unless legal review is required.
[VALIDATION] IF request_type = "standard" AND completion_date > request_date + 30_days THEN violation

[RULE-03] Requests requiring legal consultation MUST be completed within 60 calendar days with documented legal review.
[VALIDATION] IF legal_review_required = TRUE AND completion_date > request_date + 60_days THEN violation

[RULE-04] All correction and deletion actions MUST be logged with requester identity verification, action taken, and system affected.
[VALIDATION] IF action_completed = TRUE AND (log_entry = NULL OR verification_status = NULL) THEN violation

[RULE-05] Designated representatives MUST provide valid authorization documentation before PII correction or deletion.
[VALIDATION] IF requester_type = "designated_representative" AND authorization_verified = FALSE THEN violation

[RULE-06] PII corrections or deletions SHALL be coordinated across all systems containing the affected data.
[VALIDATION] IF pii_systems_count > affected_systems_count AND justification_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Individual Request Intake Process - Standardized process for receiving and categorizing correction/deletion requests
- [PROC-02] Identity and Authorization Verification - Process to verify requester identity and representative authorization
- [PROC-03] Legal Review Process - Escalation process for legally complex or sensitive requests
- [PROC-04] Cross-System Data Location - Process to identify all systems containing requested PII
- [PROC-05] Correction/Deletion Execution - Technical procedures for safely modifying or removing PII

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Privacy law changes, significant compliance violations, system architecture changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Customer Correction Request]
IF requester_type = "individual"
AND request_type = "correction"
AND identity_verified = TRUE
AND completion_time <= 30_days
THEN compliance = TRUE

[SCENARIO-02: Designated Representative Without Authorization]
IF requester_type = "designated_representative"
AND authorization_documentation = FALSE
AND action_taken = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Delayed Legal Review Case]
IF legal_review_required = TRUE
AND completion_time > 60_days
AND extension_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Incomplete Cross-System Deletion]
IF request_type = "deletion"
AND pii_systems_identified = 5
AND systems_processed = 3
AND justification_provided = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Unacknowledged Request]
IF request_received = TRUE
AND acknowledgment_sent = FALSE
AND days_elapsed > 5
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| PII corrected or deleted upon individual request | RULE-02, RULE-03, RULE-06 |
| Designated representative authorization verified | RULE-05 |
| Request processing documented and logged | RULE-04 |
| Timely response to individual requests | RULE-01, RULE-02, RULE-03 |