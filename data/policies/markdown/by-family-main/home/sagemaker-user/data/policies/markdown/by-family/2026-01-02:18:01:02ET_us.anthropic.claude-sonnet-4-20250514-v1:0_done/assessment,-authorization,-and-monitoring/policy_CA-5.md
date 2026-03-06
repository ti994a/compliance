# POLICY: CA-5: Plan of Action and Milestones

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CA-5 |
| NIST Control | CA-5: Plan of Action and Milestones |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | remediation, vulnerabilities, milestones, assessment, tracking, deficiencies |

## 1. POLICY STATEMENT
The organization must develop and maintain a Plan of Action and Milestones (POA&M) to document planned remediation actions for correcting control weaknesses, deficiencies, and vulnerabilities identified during assessments. POA&M documents must be updated based on findings from control assessments, audits, reviews, and continuous monitoring activities at defined frequencies.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud and hybrid environments |
| Third-party Systems | YES | When processing company data |
| Development Systems | YES | If containing production data |
| Test Environments | CONDITIONAL | Only if containing sensitive data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Ensure POA&M development and maintenance<br>• Approve remediation timelines<br>• Coordinate with security teams |
| CISO/Security Team | • Review and validate POA&M entries<br>• Track remediation progress<br>• Report to executive leadership |
| System Administrator | • Implement remediation actions<br>• Update POA&M status<br>• Provide technical input on timelines |

## 4. RULES

[RULE-01] A POA&M MUST be developed for each system within 30 days of initial control assessment completion or vulnerability identification.
[VALIDATION] IF assessment_completed = TRUE AND poam_created_date > (assessment_date + 30_days) THEN violation

[RULE-02] POA&M entries MUST include weakness description, remediation plan, responsible party, estimated completion date, and current status.
[VALIDATION] IF poam_entry_missing_required_fields = TRUE THEN violation

[RULE-03] Critical vulnerabilities MUST have remediation completion dates within 30 days of identification.
[VALIDATION] IF vulnerability_severity = "critical" AND remediation_date > (identification_date + 30_days) THEN critical_violation

[RULE-04] High vulnerabilities MUST have remediation completion dates within 90 days of identification.
[VALIDATION] IF vulnerability_severity = "high" AND remediation_date > (identification_date + 90_days) THEN violation

[RULE-05] POA&M MUST be updated within 15 days following control assessments, audits, or continuous monitoring findings.
[VALIDATION] IF new_findings_date + 15_days < current_date AND poam_updated = FALSE THEN violation

[RULE-06] POA&M status updates MUST be provided monthly for all open items.
[VALIDATION] IF last_status_update > 30_days AND item_status = "open" THEN violation

[RULE-07] Completed remediation actions MUST be verified before closing POA&M items.
[VALIDATION] IF item_status = "closed" AND verification_completed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] POA&M Development - Standard template and entry creation process
- [PROC-02] Vulnerability Prioritization - Risk-based ranking methodology
- [PROC-03] Remediation Tracking - Progress monitoring and reporting procedures
- [PROC-04] POA&M Review - Monthly review and validation process

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, regulatory changes, significant system changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Missing Critical Vulnerability POA&M]
IF vulnerability_severity = "critical"
AND identification_date < (current_date - 5_days)
AND poam_entry_exists = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Overdue Remediation Timeline]
IF poam_item_status = "open"
AND planned_completion_date < current_date
AND extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Outdated POA&M After Assessment]
IF control_assessment_completed = TRUE
AND assessment_date < (current_date - 20_days)
AND poam_last_updated < assessment_date
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Incomplete POA&M Entry]
IF poam_entry_exists = TRUE
AND (responsible_party = NULL OR remediation_plan = NULL OR completion_date = NULL)
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Unverified Closed Item]
IF poam_item_status = "closed"
AND closure_date < (current_date - 30_days)
AND independent_verification = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| POA&M development for documented weaknesses | RULE-01, RULE-02 |
| Planned remediation actions documentation | RULE-02, RULE-03, RULE-04 |
| Regular POA&M updates based on findings | RULE-05, RULE-06 |
| Vulnerability remediation tracking | RULE-03, RULE-04, RULE-07 |