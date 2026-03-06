```markdown
# POLICY: PM-2: Information Security Program Leadership Role

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-2 |
| NIST Control | PM-2: Information Security Program Leadership Role |
| Version | 1.0 |
| Owner | Chief Executive Officer |
| Keywords | CISO, senior information security officer, information security program, leadership, governance, coordination |

## 1. POLICY STATEMENT
The organization SHALL appoint a senior agency information security officer (CISO) with appropriate authority, mission, and resources to coordinate, develop, implement, and maintain an enterprise-wide information security program. This role ensures centralized governance and accountability for information security across all organizational units.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational units | YES | Including subsidiaries and business units |
| Third-party service providers | YES | Where contractually managing security programs |
| Temporary/project teams | YES | Must coordinate with CISO office |
| Board of Directors | CONDITIONAL | Oversight and governance responsibilities only |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Executive Officer | • Appoint qualified CISO<br>• Provide adequate resources and authority<br>• Ensure CISO has direct reporting relationship |
| Senior Information Security Officer (CISO) | • Coordinate organization-wide security program<br>• Develop security policies and procedures<br>• Implement security controls and measures<br>• Maintain ongoing security program effectiveness |
| Business Unit Leaders | • Support CISO initiatives within their domains<br>• Provide resources for security implementation<br>• Ensure compliance with security program requirements |

## 4. RULES
[RULE-01] The organization MUST appoint a senior information security officer at the executive level with direct reporting to the CEO or equivalent C-suite executive.
[VALIDATION] IF ciso_appointed = FALSE OR ciso_reporting_level != "executive" THEN critical_violation

[RULE-02] The CISO MUST be provided with sufficient authority to coordinate security activities across all organizational units without requiring approval from subordinate management.
[VALIDATION] IF ciso_authority_scope != "organization_wide" OR approval_required_from_subordinates = TRUE THEN violation

[RULE-03] The organization MUST provide the CISO with adequate budget, staff, and resources to develop enterprise security policies, standards, and procedures.
[VALIDATION] IF ciso_budget_allocated = FALSE OR ciso_staff_count < minimum_required THEN violation

[RULE-04] The CISO MUST have documented responsibility and authority to implement security controls and measures across all information systems and business processes.
[VALIDATION] IF ciso_implementation_authority_documented = FALSE OR scope != "all_systems" THEN violation

[RULE-05] The organization MUST ensure the CISO has ongoing resources and support to maintain the security program through regular assessments, updates, and improvements.
[VALIDATION] IF maintenance_resources_allocated = FALSE OR assessment_frequency < "annual" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] CISO Appointment Process - Formal process for selecting, appointing, and onboarding the senior information security officer
- [PROC-02] Authority Documentation - Process for documenting and communicating CISO authority and responsibilities
- [PROC-03] Resource Allocation - Annual process for determining and allocating budget and staff resources to security program
- [PROC-04] Program Coordination - Procedures for coordinating security activities across business units and functions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annual
- Procedure review frequency: Annual
- Triggering events: CISO role change, organizational restructure, significant security incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: CISO Reports to Non-Executive]
IF ciso_appointed = TRUE
AND ciso_reporting_level = "middle_management"
AND direct_ceo_access = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Limited Cross-Unit Authority]
IF ciso_appointed = TRUE
AND business_unit_compliance_required = TRUE
AND ciso_override_authority = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Insufficient Resources]
IF ciso_appointed = TRUE
AND (budget_adequate = FALSE OR staff_adequate = FALSE)
AND program_scope = "enterprise_wide"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Proper CISO Implementation]
IF ciso_appointed = TRUE
AND ciso_reporting_level = "executive"
AND resources_adequate = TRUE
AND authority_documented = TRUE
AND scope = "organization_wide"
THEN compliance = TRUE

[SCENARIO-05: Acting CISO Without Authority]
IF ciso_status = "acting"
AND appointment_duration > 180_days
AND formal_authority_granted = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Senior agency information security officer is appointed | RULE-01 |
| CISO provided with mission and resources to coordinate organization-wide program | RULE-02, RULE-03 |
| CISO provided with mission and resources to develop organization-wide program | RULE-03, RULE-04 |
| CISO provided with mission and resources to implement organization-wide program | RULE-04, RULE-02 |
| CISO provided with mission and resources to maintain organization-wide program | RULE-05, RULE-03 |
```