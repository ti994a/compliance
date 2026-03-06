# POLICY: MA-7: Field Maintenance

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MA-7 |
| NIST Control | MA-7: Field Maintenance |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | field maintenance, trusted facilities, depot maintenance, critical systems, maintenance restrictions |

## 1. POLICY STATEMENT
The organization SHALL restrict or prohibit field maintenance on designated critical systems and components, requiring such maintenance to be performed only at trusted maintenance facilities. Field maintenance restrictions ensure maintenance activities meet organizational security and quality control standards.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical Information Systems | YES | As defined by system categorization |
| High-Impact System Components | YES | Security-sensitive components |
| Standard Business Systems | CONDITIONAL | Based on risk assessment |
| Development/Test Systems | NO | Unless containing production data |
| Third-Party Maintenance Providers | YES | When performing restricted maintenance |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Define field maintenance restrictions for owned systems<br>• Approve trusted maintenance facilities<br>• Ensure maintenance compliance |
| CISO | • Establish criteria for maintenance restrictions<br>• Approve trusted facility designations<br>• Monitor compliance with maintenance policies |
| Maintenance Personnel | • Comply with field maintenance restrictions<br>• Use only approved trusted facilities<br>• Document maintenance activities |

## 4. RULES

[RULE-01] Critical systems and high-impact system components MUST have field maintenance restrictions documented in their system security plans.
[VALIDATION] IF system_impact_level IN ["high", "critical"] AND field_maintenance_restrictions_documented = FALSE THEN violation

[RULE-02] Field maintenance on restricted systems MUST be performed only at organizationally-approved trusted maintenance facilities.
[VALIDATION] IF system_restricted = TRUE AND maintenance_location NOT IN approved_trusted_facilities THEN critical_violation

[RULE-03] Trusted maintenance facilities MUST be formally designated and approved by the CISO or designated authority.
[VALIDATION] IF facility_used_for_maintenance = TRUE AND facility_approval_status != "approved" THEN violation

[RULE-04] Field maintenance restrictions MUST be based on documented risk assessments and system criticality determinations.
[VALIDATION] IF maintenance_restrictions_applied = TRUE AND risk_assessment_documented = FALSE THEN violation

[RULE-05] All maintenance activities on restricted systems MUST be documented with facility location, personnel, and scope of work.
[VALIDATION] IF restricted_system_maintenance = TRUE AND (facility_location = NULL OR personnel_list = NULL OR scope_documented = FALSE) THEN violation

[RULE-06] Emergency field maintenance exceptions MUST be pre-approved by system owner and CISO, with compensating controls implemented.
[VALIDATION] IF emergency_field_maintenance = TRUE AND (system_owner_approval = FALSE OR ciso_approval = FALSE OR compensating_controls = FALSE) THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Criticality Assessment - Process for determining field maintenance restrictions
- [PROC-02] Trusted Facility Designation - Criteria and approval process for maintenance facilities  
- [PROC-03] Maintenance Authorization - Approval workflow for restricted system maintenance
- [PROC-04] Emergency Maintenance Exception - Process for urgent maintenance needs

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: System categorization changes, security incidents involving maintenance, new critical system deployments

## 7. SCENARIO PATTERNS

[SCENARIO-01: Critical System Field Maintenance]
IF system_impact_level = "high"
AND maintenance_location = "field_site"
AND trusted_facility_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Trusted Facility Usage]
IF system_restricted = TRUE
AND maintenance_facility IN approved_trusted_facilities
AND maintenance_documented = TRUE
THEN compliance = TRUE

[SCENARIO-03: Emergency Field Maintenance]
IF emergency_maintenance = TRUE
AND system_restricted = TRUE
AND system_owner_approval = TRUE
AND ciso_approval = TRUE
AND compensating_controls_implemented = TRUE
THEN compliance = TRUE

[SCENARIO-04: Undocumented Maintenance Restrictions]
IF system_impact_level = "high"
AND field_maintenance_restrictions_documented = FALSE
AND system_security_plan_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Unauthorized Maintenance Facility]
IF maintenance_performed = TRUE
AND facility_approval_status = "pending"
AND maintenance_completed = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Field maintenance restrictions defined for applicable systems | [RULE-01] |
| Trusted maintenance facilities designated and approved | [RULE-03] |
| Field maintenance restricted to trusted facilities | [RULE-02] |
| Maintenance restrictions based on risk assessment | [RULE-04] |
| Maintenance activities properly documented | [RULE-05] |
| Emergency exceptions properly authorized | [RULE-06] |