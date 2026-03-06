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
All computer matching programs that compare records from automated Privacy Act systems must obtain Data Integrity Board approval, establish formal agreements, and provide due process protections before taking adverse actions against individuals. Organizations must independently verify matching results and provide individuals notice and opportunity to contest findings.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal Agencies | YES | All matching programs under Privacy Act |
| Contractors Processing Federal Data | YES | When conducting matching on behalf of agency |
| Non-Federal Agencies | CONDITIONAL | Only when participating in federal matching programs |
| Cloud Service Providers | CONDITIONAL | When processing data for matching programs |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee matching program compliance<br>• Coordinate with Data Integrity Board<br>• Ensure proper agreements and notices |
| Data Integrity Board | • Review and approve matching programs<br>• Monitor program compliance<br>• Evaluate cost-benefit analysis |
| Program Managers | • Develop matching agreements<br>• Implement verification procedures<br>• Manage individual notification processes |
| Legal Counsel | • Review matching agreements<br>• Ensure regulatory compliance<br>• Support due process procedures |

## 4. RULES
[RULE-01] Organizations MUST obtain Data Integrity Board approval before initiating any computer matching program involving Privacy Act systems of records.
[VALIDATION] IF matching_program = TRUE AND data_integrity_board_approval = FALSE THEN critical_violation

[RULE-02] Organizations MUST develop and execute a computer matching agreement before conducting matching operations.
[VALIDATION] IF matching_program = TRUE AND matching_agreement_executed = FALSE THEN critical_violation

[RULE-03] Organizations MUST publish a matching notice in the Federal Register at least 30 days before program implementation.
[VALIDATION] IF matching_program = TRUE AND federal_register_notice = FALSE THEN critical_violation

[RULE-04] Organizations MUST independently verify matching results before taking adverse action against individuals when verification is required by the matching agreement.
[VALIDATION] IF adverse_action_planned = TRUE AND verification_required = TRUE AND independent_verification = FALSE THEN critical_violation

[RULE-05] Organizations MUST provide individuals with written notice and at least 30 days opportunity to contest findings before taking adverse action.
[VALIDATION] IF adverse_action_taken = TRUE AND (individual_notice = FALSE OR contest_period < 30_days) THEN critical_violation

[RULE-06] Computer matching agreements MUST specify the purpose, legal authority, records to be matched, and procedures for verification and individual rights.
[VALIDATION] IF matching_agreement_executed = TRUE AND (purpose_specified = FALSE OR legal_authority_cited = FALSE OR verification_procedures = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Integrity Board Review Process - Formal review and approval workflow for matching programs
- [PROC-02] Matching Agreement Development - Standard template and negotiation process for agreements
- [PROC-03] Federal Register Publication - Process for drafting and publishing matching notices
- [PROC-04] Independent Verification - Procedures for verifying matching results before adverse action
- [PROC-05] Individual Notification and Due Process - Process for notifying individuals and handling contests

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: New matching programs, Data Integrity Board guidance changes, Privacy Act amendments

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Benefits Matching Program]
IF program_type = "federal_benefits_matching"
AND data_integrity_board_approval = FALSE
AND matching_agreement = "draft"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Adverse Action Without Verification]
IF matching_results = "potential_fraud"
AND verification_required = TRUE
AND independent_verification = FALSE
AND adverse_action_initiated = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Individual Contest Period]
IF individual_notice_sent = TRUE
AND contest_period_provided = 15_days
AND adverse_action_date = "scheduled"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Missing Federal Register Notice]
IF matching_program = "active"
AND federal_register_notice = FALSE
AND program_start_date < current_date
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Expired Matching Agreement]
IF matching_agreement_expiration < current_date
AND matching_operations = "ongoing"
AND renewal_status = "pending"
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Data Integrity Board approval obtained | [RULE-01] |
| Computer matching agreement developed | [RULE-02] |
| Computer matching agreement entered into | [RULE-02] |
| Matching notice published in Federal Register | [RULE-03] |
| Information independently verified before adverse action | [RULE-04] |
| Individuals provided notice | [RULE-05] |
| Individuals given opportunity to contest findings | [RULE-05] |