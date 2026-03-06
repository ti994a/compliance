# POLICY: IR-2.3: Breach

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IR-2.3 |
| NIST Control | IR-2.3: Breach |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | breach, incident response, training, PII, reporting, identification |

## 1. POLICY STATEMENT
All personnel MUST receive incident response training specifically focused on identifying and responding to breaches involving personally identifiable information (PII). Training MUST include the organization's mandatory breach reporting processes and procedures for both confirmed and suspected incidents.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Including contractors and temporary staff |
| Third-party vendors | YES | When handling organizational PII |
| System administrators | YES | Enhanced training requirements |
| Executive leadership | YES | Reporting and decision-making focus |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve breach training curriculum<br>• Ensure compliance with federal breach notification requirements<br>• Oversee incident response program |
| Security Training Manager | • Develop breach-specific training materials<br>• Conduct tabletop exercises<br>• Track training completion rates |
| Privacy Officer | • Define PII breach scenarios<br>• Ensure privacy law compliance<br>• Coordinate breach notification processes |

## 4. RULES
[RULE-01] All personnel MUST complete breach identification and response training within 30 days of hire or role change involving PII access.
[VALIDATION] IF employee_start_date + 30_days < current_date AND breach_training_completed = FALSE AND pii_access = TRUE THEN violation

[RULE-02] Breach response training MUST be refreshed annually for all personnel with PII access.
[VALIDATION] IF last_breach_training_date + 365_days < current_date AND pii_access = TRUE THEN violation

[RULE-03] Training MUST include tabletop exercises simulating breach scenarios at least once per year.
[VALIDATION] IF last_tabletop_exercise + 365_days < current_date THEN violation

[RULE-04] Personnel MUST report suspected or confirmed breaches within 1 hour of discovery through designated channels.
[VALIDATION] IF breach_discovered = TRUE AND report_time > discovery_time + 1_hour THEN critical_violation

[RULE-05] Training MUST cover breach identification for all media types including paper, oral, and electronic information.
[VALIDATION] IF training_curriculum_includes = ["paper", "oral", "electronic"] THEN compliant ELSE violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Breach Training Curriculum Development - Annual review and update of training materials
- [PROC-02] Tabletop Exercise Execution - Quarterly breach simulation exercises
- [PROC-03] Training Completion Tracking - Monthly reporting of training status
- [PROC-04] Breach Reporting Process - Step-by-step incident escalation procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major breach incidents, regulatory changes, organizational restructuring

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Employee PII Access]
IF employee_status = "new"
AND pii_access_required = TRUE
AND breach_training_completed = FALSE
AND days_since_hire > 30
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Tabletop Training]
IF department_type = "PII_handling"
AND last_tabletop_exercise > 12_months_ago
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Delayed Breach Reporting]
IF breach_suspected = TRUE
AND discovery_timestamp = "known"
AND report_timestamp > discovery_timestamp + 1_hour
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Incomplete Training Coverage]
IF training_media_types != ["paper", "oral", "electronic"]
AND training_completed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Contractor Training Gap]
IF user_type = "contractor"
AND pii_access = TRUE
AND breach_training_current = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Incident response training on breach identification provided | RULE-01, RULE-05 |
| Incident response training on breach reporting process provided | RULE-01, RULE-04 |
| Training includes tabletop exercises | RULE-03 |
| Training covers all media types | RULE-05 |
| Regular training updates maintained | RULE-02 |