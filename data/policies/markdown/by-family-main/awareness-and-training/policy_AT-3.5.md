# POLICY: AT-3.5: Processing Personally Identifiable Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AT-3.5 |
| NIST Control | AT-3.5: Processing Personally Identifiable Information |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII training, privacy controls, transparency controls, role-based training, personally identifiable information |

## 1. POLICY STATEMENT
All personnel and roles involved in processing personally identifiable information (PII) must receive initial and refresher training on PII processing and transparency controls. Training must cover the organization's authority to process PII, processing purposes, and applicable privacy obligations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Employees | YES | All employees handling PII |
| Contractors | YES | Those with PII access |
| Third-party vendors | CONDITIONAL | If processing PII on behalf of organization |
| Systems administrators | YES | Managing systems containing PII |
| Privacy officers | YES | Primary responsibility for PII governance |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Develop PII training curriculum<br>• Define training frequency requirements<br>• Monitor training compliance |
| HR Department | • Track training completion<br>• Ensure new hire training<br>• Coordinate refresher training schedules |
| System Owners | • Identify personnel requiring PII training<br>• Ensure role-specific training completion |

## 4. RULES
[RULE-01] All personnel with PII processing responsibilities MUST complete initial PII training within 30 days of role assignment or system access.
[VALIDATION] IF personnel_has_PII_access = TRUE AND initial_training_completed = FALSE AND days_since_access > 30 THEN violation

[RULE-02] Refresher training on PII processing and transparency controls MUST be completed annually.
[VALIDATION] IF last_training_date > 365_days AND PII_access = TRUE THEN violation

[RULE-03] Training content MUST include organization's authority to process PII, processing purposes, and applicable privacy documentation.
[VALIDATION] IF training_curriculum_missing_required_elements = TRUE THEN violation

[RULE-04] Role-based training MUST address specific types of PII handled and associated risks for each role.
[VALIDATION] IF role_specific_training = FALSE AND PII_processing_role = TRUE THEN violation

[RULE-05] Training completion MUST be documented and tracked for all personnel with PII access.
[VALIDATION] IF training_documentation = NULL AND PII_access = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Training Curriculum Development - Define role-specific training content and materials
- [PROC-02] Training Delivery and Tracking - Manage training schedules and completion records
- [PROC-03] New Hire PII Training - Ensure timely training for new personnel
- [PROC-04] Training Effectiveness Assessment - Evaluate and improve training programs

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Privacy incident, regulatory changes, new PII processing activities, system changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Employee PII Access]
IF employee_status = "new_hire"
AND PII_access_required = TRUE
AND days_since_start_date > 30
AND initial_PII_training_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Expired Refresher Training]
IF last_PII_training_date > 365_days
AND current_PII_access = TRUE
AND role_requires_PII_processing = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Contractor PII Training]
IF user_type = "contractor"
AND PII_processing_authorized = TRUE
AND contractor_PII_training_completed = FALSE
AND contract_start_date < 30_days_ago
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Role Change Without Training]
IF role_change_date < 30_days_ago
AND new_role_PII_access = TRUE
AND role_specific_PII_training = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Training Documentation Missing]
IF PII_access = TRUE
AND training_completion_documented = FALSE
AND audit_request = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Initial training provided | RULE-01 |
| Refresher training frequency defined and implemented | RULE-02 |
| Training covers PII processing and transparency controls | RULE-03 |
| Role-based training implementation | RULE-04 |
| Training completion tracking | RULE-05 |