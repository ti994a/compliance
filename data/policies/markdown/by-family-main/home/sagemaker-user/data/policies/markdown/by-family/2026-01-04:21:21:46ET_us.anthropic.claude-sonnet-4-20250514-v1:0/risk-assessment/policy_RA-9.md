```markdown
# POLICY: RA-9: Criticality Analysis

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-9 |
| NIST Control | RA-9: Criticality Analysis |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | criticality analysis, critical components, system functions, risk assessment, SDLC, mission critical |

## 1. POLICY STATEMENT
The organization must identify critical system components and functions through formal criticality analysis at defined decision points in the system development lifecycle. This analysis prioritizes protection activities and informs supply chain risk management decisions based on mission impact assessment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing organizational data |
| System Components | YES | Hardware, software, firmware components |
| System Services | YES | Internal and outsourced IT services |
| Cyber-Physical Systems | YES | Including IoT and operational technology |
| Development Projects | YES | All SDLC phases requiring analysis |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Architects | • Conduct functional decomposition analysis<br>• Identify component dependencies<br>• Document critical system interfaces |
| Risk Managers | • Define criticality analysis methodology<br>• Review and approve criticality assessments<br>• Maintain criticality analysis procedures |
| System Owners | • Ensure criticality analysis completion<br>• Validate mission impact assessments<br>• Approve protection measure requirements |

## 4. RULES

[RULE-01] Criticality analysis MUST be performed at predefined decision points including system design, architecture modification, and major upgrades.
[VALIDATION] IF sdlc_phase IN ["design", "modification", "upgrade"] AND criticality_analysis_completed = FALSE THEN violation

[RULE-02] Critical system components SHALL be identified through functional decomposition that traces organizational missions to specific hardware, software, and firmware components.
[VALIDATION] IF functional_decomposition_documented = FALSE OR mission_traceability = FALSE THEN violation

[RULE-03] Components providing unmediated access to critical functions MUST be classified as critical regardless of their inherent functionality.
[VALIDATION] IF component_provides_unmediated_access = TRUE AND component_criticality != "critical" THEN violation

[RULE-04] Criticality analysis MUST consider system dependencies including cyber-physical connections, system-of-systems relationships, and outsourced services.
[VALIDATION] IF dependency_analysis_complete = FALSE OR external_dependencies_documented = FALSE THEN violation

[RULE-05] Component criticality assessment SHALL evaluate impact of component failure on supported organizational missions.
[VALIDATION] IF mission_impact_assessment = NULL OR failure_impact_documented = FALSE THEN violation

[RULE-06] Criticality analysis results MUST be documented and maintained with system security plans and updated when system changes occur.
[VALIDATION] IF criticality_documentation = NULL OR last_update > system_change_date THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Criticality Analysis Methodology - Standardized approach for conducting functional decomposition and impact assessment
- [PROC-02] SDLC Integration Process - Procedures for triggering criticality analysis at decision points
- [PROC-03] Dependency Mapping - Process for identifying and documenting system dependencies and interfaces
- [PROC-04] Protection Prioritization - Method for translating criticality levels into protection requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or when methodology changes
- Triggering events: Major system changes, new regulatory requirements, significant security incidents

## 7. SCENARIO PATTERNS

[SCENARIO-01: New System Development]
IF system_development_phase = "design"
AND criticality_analysis_completed = TRUE
AND functional_decomposition_documented = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Dependency Analysis]
IF system_has_external_dependencies = TRUE
AND dependency_analysis_documented = FALSE
AND criticality_analysis_claimed_complete = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Unmediated Access Component]
IF component_provides_direct_access_to_critical_function = TRUE
AND component_criticality_level = "low"
AND access_mediation_controls = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Outdated Criticality Assessment]
IF system_major_change_date > criticality_analysis_date
AND days_since_change > 30
AND updated_analysis_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Supply Chain Integration]
IF third_party_service_integrated = TRUE
AND service_criticality_assessed = TRUE
AND protection_requirements_defined = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Assessment Objective | Rule Reference |
|---------------------|----------------|
| Critical system components and functions are identified | RULE-02, RULE-03 |
| Criticality analysis performed for defined systems/components | RULE-01, RULE-04 |
| Analysis conducted at SDLC decision points | RULE-01, RULE-06 |
| Mission impact assessment completed | RULE-05 |
| Dependencies and interfaces considered | RULE-04 |
```