```markdown
# POLICY: PM-2: Information Security Program Leadership Role

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-2 |
| NIST Control | PM-2: Information Security Program Leadership Role |
| Version | 1.0 |
| Owner | Chief Executive Officer |
| Keywords | CISO, senior information security officer, leadership, program management, coordination |

## 1. POLICY STATEMENT
The organization MUST appoint a qualified senior agency information security officer (SAISO/CISO) with sufficient authority, mission clarity, and resources to coordinate, develop, implement, and maintain an enterprise-wide information security program. This role SHALL have direct executive access and organizational authority to ensure effective security governance across all business units and technology domains.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational units | YES | Including subsidiaries and divisions |
| Cloud service providers | YES | Must coordinate with CISO program |
| Third-party contractors | YES | Subject to CISO oversight requirements |
| Temporary staff | YES | Must follow CISO-established procedures |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Executive Officer | • Appoint qualified CISO<br>• Provide adequate resources and authority<br>• Ensure executive-level access |
| Senior Information Security Officer (CISO) | • Coordinate organization-wide security program<br>• Develop security policies and procedures<br>• Implement security controls across enterprise<br>• Maintain ongoing security program effectiveness |
| Business Unit Leaders | • Support CISO initiatives within their domains<br>• Provide necessary resources for security implementation<br>• Ensure compliance with CISO-established requirements |

## 4. RULES
[RULE-01] The organization MUST appoint a senior agency information security officer within 30 days of policy effective date or executive vacancy.
[VALIDATION] IF ciso_appointment_date = NULL OR (executive_vacancy_date + 30_days < current_date AND new_ciso_appointed = FALSE) THEN violation

[RULE-02] The appointed CISO MUST possess minimum qualifications including advanced cybersecurity degree or equivalent experience, relevant professional certifications, and demonstrated leadership experience in enterprise security programs.
[VALIDATION] IF ciso_qualifications.meets_minimum_requirements = FALSE THEN violation

[RULE-03] The CISO SHALL have direct reporting relationship to C-suite executive or board level, with no more than one organizational layer between CISO and CEO.
[VALIDATION] IF ciso_reporting_layers > 1 THEN violation

[RULE-04] The organization MUST provide the CISO with adequate budget allocation representing at least 3% of total IT budget for security program activities.
[VALIDATION] IF (security_budget / total_it_budget) < 0.03 THEN violation

[RULE-05] The CISO MUST have documented authority to coordinate security activities across all organizational units including cloud infrastructure, development teams, and business operations.
[VALIDATION] IF ciso_authority_documentation = NULL OR cross_unit_coordination_authority = FALSE THEN violation

[RULE-06] The CISO SHALL maintain and annually update a comprehensive organization-wide information security program plan covering all assessment objectives.
[VALIDATION] IF security_program_plan.last_update > 365_days OR program_plan_comprehensive = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] CISO Appointment and Succession Planning - Formal process for selecting, appointing, and transitioning CISO role
- [PROC-02] Security Program Coordination - Cross-functional coordination mechanisms and reporting structures
- [PROC-03] Resource Allocation and Budget Management - Annual security budget planning and resource allocation
- [PROC-04] Program Plan Development and Maintenance - Systematic approach to security program planning and updates

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: CISO departure, major organizational restructuring, significant security incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: CISO Vacancy Extended Period]
IF ciso_position = "vacant"
AND vacancy_duration > 30_days
AND interim_appointment = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Insufficient CISO Authority]
IF ciso_appointed = TRUE
AND cross_unit_coordination_authority = FALSE
AND executive_support_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Inadequate Resource Allocation]
IF ciso_appointed = TRUE
AND security_budget_percentage < 3%
AND resource_adequacy_assessment = "insufficient"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Qualified CISO with Proper Authority]
IF ciso_appointed = TRUE
AND ciso_qualifications.meets_requirements = TRUE
AND reporting_relationship = "c_suite_direct"
AND program_coordination_authority = TRUE
THEN compliance = TRUE

[SCENARIO-05: Outdated Program Plan]
IF ciso_appointed = TRUE
AND security_program_plan.exists = TRUE
AND program_plan.last_update > 365_days
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Senior agency information security officer is appointed | [RULE-01], [RULE-02] |
| CISO provided with mission to coordinate organization-wide program | [RULE-05], [RULE-06] |
| CISO provided with mission to develop organization-wide program | [RULE-06] |
| CISO provided with mission to implement organization-wide program | [RULE-05], [RULE-06] |
| CISO provided with mission to maintain organization-wide program | [RULE-06] |
| CISO provided with adequate resources | [RULE-04] |
```