# POLICY: PT-8: Computer Matching Requirements

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-8 |
| NIST Control | PT-8: Computer Matching Requirements |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | computer matching, data integrity board, privacy act, federal register, adverse action |

## 1. POLICY STATEMENT
Organizations conducting computer matching programs MUST obtain proper approvals, establish formal agreements, provide public notice, and protect individual rights before taking adverse actions. All matching activities MUST comply with Privacy Act requirements and ensure due process protections for affected individuals.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal agencies | YES | Full Privacy Act compliance required |
| Contractors processing federal data | YES | When conducting matching on behalf of agency |
| State/local agencies | CONDITIONAL | Only when participating in federal matching programs |
| Commercial systems | CONDITIONAL | Only when processing federal benefit or personnel data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee matching program compliance<br>• Coordinate with Data Integrity Board<br>• Ensure proper agreements are established |
| Data Integrity Board | • Review and approve matching programs<br>• Monitor ongoing compliance<br>• Evaluate program effectiveness |
| System Administrators | • Implement technical matching controls<br>• Maintain audit logs<br>• Execute data verification procedures |
| Legal Counsel | • Draft matching agreements<br>• Review Federal Register notices<br>• Ensure regulatory compliance |

## 4. RULES
[RULE-01] Organizations MUST obtain Data Integrity Board approval before initiating any computer matching program involving Privacy Act systems of records.
[VALIDATION] IF matching_program_initiated = TRUE AND data_integrity_board_approval = FALSE THEN critical_violation

[RULE-02] A formal computer matching agreement MUST be developed and executed before any data matching activities commence.
[VALIDATION] IF matching_activities = TRUE AND signed_agreement = FALSE THEN critical_violation

[RULE-03] Organizations MUST publish a matching notice in the Federal Register at least 30 days before the matching program becomes effective.
[VALIDATION] IF federal_register_notice = FALSE OR notice_days < 30 THEN violation

[RULE-04] Information produced by matching programs MUST be independently verified before taking adverse action against individuals when verification is required by law.
[VALIDATION] IF adverse_action = TRUE AND verification_required = TRUE AND independent_verification = FALSE THEN critical_violation

[RULE-05] Individuals MUST receive notice and opportunity to contest findings before adverse action is taken against them.
[VALIDATION] IF adverse_action = TRUE AND (individual_notice = FALSE OR contest_opportunity = FALSE) THEN critical_violation

[RULE-06] Matching programs MUST NOT exceed the duration specified in the Data Integrity Board approval, with maximum 18-month initial terms.
[VALIDATION] IF program_duration > approved_duration OR initial_term > 18_months THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Integrity Board Review Process - Formal review and approval workflow for matching programs
- [PROC-02] Matching Agreement Development - Standard process for creating computer matching agreements
- [PROC-03] Federal Register Publication - Procedures for publishing required matching notices
- [PROC-04] Independent Verification - Process for verifying matching results before adverse actions
- [PROC-05] Individual Notice and Contest - Procedures for notifying individuals and handling contests

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 18 months
- Triggering events: New matching programs, Data Integrity Board guidance changes, Privacy Act amendments

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Benefit Matching Program]
IF program_type = "federal_benefit_matching"
AND data_integrity_board_approval = TRUE
AND matching_agreement = "signed"
AND federal_register_notice = "published_35_days_ago"
THEN compliance = TRUE

[SCENARIO-02: Adverse Action Without Notice]
IF matching_result = "eligibility_denial"
AND adverse_action_taken = TRUE
AND individual_notice_provided = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Unverified Match Results]
IF match_confidence = "probable"
AND verification_required = TRUE
AND independent_verification = FALSE
AND adverse_action = "benefit_termination"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Expired Matching Program]
IF program_start_date < current_date - 18_months
AND program_renewal_approved = FALSE
AND matching_activities = "ongoing"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Contest Process]
IF individual_contest_submitted = TRUE
AND contest_review_completed = TRUE
AND adverse_action_delayed = TRUE
AND final_determination_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Data Integrity Board approval obtained | RULE-01 |
| Computer matching agreement developed | RULE-02 |
| Computer matching agreement entered into | RULE-02 |
| Matching notice published in Federal Register | RULE-03 |
| Information independently verified before adverse action | RULE-04 |
| Individuals provided with notice | RULE-05 |
| Individuals provided opportunity to contest findings | RULE-05 |