# POLICY: AT-2.6: Cyber Threat Environment

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AT-2.6 |
| NIST Control | AT-2.6: Cyber Threat Environment |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cyber threat, literacy training, threat intelligence, system operations, awareness |

## 1. POLICY STATEMENT
The organization SHALL provide literacy training on the current cyber threat environment to all personnel and ensure that system operations reflect current cyber threat information. Training content must be dynamic and updated to address evolving threats relevant to organizational mission and business functions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Including full-time, part-time, and temporary staff |
| Contractors | YES | With system access or security responsibilities |
| Third-party vendors | CONDITIONAL | Only those with privileged access |
| All information systems | YES | Operations must reflect current threat intelligence |
| Cloud services | YES | Including hybrid and multi-cloud environments |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve threat literacy curriculum<br>• Ensure threat intelligence integration<br>• Oversee program effectiveness |
| Security Training Manager | • Develop threat literacy training materials<br>• Coordinate with threat intelligence team<br>• Track training completion and effectiveness |
| Threat Intelligence Team | • Provide current threat information<br>• Update threat landscape assessments<br>• Support training content development |
| System Administrators | • Implement threat-informed operational procedures<br>• Apply current threat intelligence to system operations |

## 4. RULES

[RULE-01] All personnel MUST complete cyber threat environment literacy training within 30 days of hire and annually thereafter.
[VALIDATION] IF employee_start_date + 30_days < current_date AND initial_training_completed = FALSE THEN violation

[RULE-02] Threat literacy training content MUST be updated at least quarterly to reflect current cyber threat information.
[VALIDATION] IF training_content_last_updated + 90_days < current_date THEN violation

[RULE-03] System operations procedures MUST incorporate current cyber threat intelligence and be updated within 30 days of significant threat landscape changes.
[VALIDATION] IF threat_intelligence_update_date + 30_days < system_procedures_update_date THEN violation

[RULE-04] Training completion rates MUST achieve 95% compliance across all in-scope personnel within required timeframes.
[VALIDATION] IF training_completion_rate < 95% THEN violation

[RULE-05] Threat literacy training MUST include organization-specific threat scenarios relevant to business functions and technology stack.
[VALIDATION] IF training_content_includes_org_specific_threats = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Threat Intelligence Integration - Process for incorporating current threat data into training materials
- [PROC-02] Training Content Development - Methodology for creating and updating cyber threat literacy curriculum
- [PROC-03] System Operations Threat Integration - Procedures for applying threat intelligence to operational activities
- [PROC-04] Training Effectiveness Measurement - Methods for assessing learning outcomes and behavioral changes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major threat landscape changes, security incidents, regulatory updates, technology stack changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Employee Training Delay]
IF employee_type = "new_hire"
AND days_since_start_date > 30
AND threat_literacy_training_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Outdated Training Content]
IF current_date > training_content_last_updated + 90_days
AND no_threat_landscape_changes = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: System Operations Without Current Threat Intel]
IF system_operational_procedures_updated = FALSE
AND threat_intelligence_received = TRUE
AND days_since_threat_update > 30
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Low Training Completion Rate]
IF training_completion_percentage < 95%
AND reporting_period = "current_quarter"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Generic Training Content]
IF training_content_includes_org_specific_threats = FALSE
AND training_content_includes_industry_specific_threats = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Literacy training on cyber threat environment is provided | RULE-01, RULE-02, RULE-05 |
| System operations reflects current cyber threat information | RULE-03 |
| Training effectiveness and coverage | RULE-04 |
| Dynamic threat information integration | RULE-02, RULE-03 |