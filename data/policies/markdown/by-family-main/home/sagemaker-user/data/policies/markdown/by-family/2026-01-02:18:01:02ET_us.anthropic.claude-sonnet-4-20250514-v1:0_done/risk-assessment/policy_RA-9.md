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
The organization SHALL identify critical system components and functions through systematic criticality analysis performed at defined decision points in the system development lifecycle. This analysis SHALL prioritize protection activities based on component and function criticality to organizational missions and operations.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing organizational data |
| System Components | YES | Hardware, software, firmware components |
| System Services | YES | Internal and outsourced IT services |
| Legacy Systems | YES | Must complete analysis within 12 months |
| Development Projects | YES | Required at all SDLC decision points |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Ensure criticality analysis completion<br>• Approve criticality determinations<br>• Coordinate with stakeholders |
| Security Architect | • Conduct technical criticality analysis<br>• Document component dependencies<br>• Assess security implications |
| Risk Manager | • Validate criticality assessments<br>• Ensure analysis methodology compliance<br>• Review and approve final determinations |

## 4. RULES

[RULE-01] Criticality analysis MUST be performed for all systems, system components, and system services at defined SDLC decision points including initial design, major modifications, and upgrades.
[VALIDATION] IF system_status IN ["new", "major_change", "upgrade"] AND criticality_analysis_completed = FALSE THEN violation

[RULE-02] Critical system components and functions MUST be identified through functional decomposition that traces organizational missions to specific hardware, software, and firmware components.
[VALIDATION] IF system_criticality = "high" AND functional_decomposition_documented = FALSE THEN violation

[RULE-03] Components providing unmediated access to critical system components MUST be classified as critical regardless of their individual function criticality.
[VALIDATION] IF component_access_type = "unmediated" AND target_component_criticality = "critical" AND component_criticality != "critical" THEN violation

[RULE-04] Criticality analysis MUST consider operational environment factors including cyber-physical system connections, system-of-systems dependencies, and outsourced IT service dependencies.
[VALIDATION] IF operational_dependencies_identified = FALSE AND criticality_analysis_status = "complete" THEN violation

[RULE-05] Criticality determinations MUST be documented with impact assessments describing effects of component or function failure on organizational missions.
[VALIDATION] IF criticality_level = "critical" AND impact_assessment_documented = FALSE THEN violation

[RULE-06] Criticality analysis MUST be updated within 30 days when system architecture, design, or operational environment changes occur.
[VALIDATION] IF system_change_date > criticality_analysis_date + 30_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Criticality Analysis Methodology - Standard approach for conducting systematic criticality assessments
- [PROC-02] Functional Decomposition Process - Method for tracing missions to technical components
- [PROC-03] Criticality Classification Scheme - Framework for assigning criticality levels and protection requirements
- [PROC-04] Dependency Mapping Process - Procedure for identifying and documenting system dependencies

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system changes, new regulatory requirements, significant security incidents

## 7. SCENARIO PATTERNS

[SCENARIO-01: New System Deployment]
IF system_status = "new_deployment"
AND sdlc_phase = "design_complete"
AND criticality_analysis_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Component Access Classification]
IF component_type = "network_device"
AND provides_access_to = "critical_database"
AND access_mediation = "none"
AND component_criticality != "critical"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Outsourced Service Analysis]
IF service_type = "outsourced"
AND service_criticality = "high"
AND dependency_analysis_completed = TRUE
AND impact_assessment_documented = TRUE
THEN compliance = TRUE

[SCENARIO-04: System Modification Update]
IF system_modification_date = "2024-01-15"
AND criticality_analysis_last_updated = "2023-12-01"
AND days_since_change > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Mission-Critical Function Mapping]
IF system_supports_mission = "financial_reporting"
AND functional_decomposition_completed = TRUE
AND component_traceability_documented = TRUE
AND criticality_levels_assigned = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Critical components identified through analysis | RULE-01, RULE-02 |
| Analysis performed at SDLC decision points | RULE-01, RULE-06 |
| Functional decomposition conducted | RULE-02 |
| Unmediated access components classified | RULE-03 |
| Operational environment considered | RULE-04 |
| Impact assessments documented | RULE-05 |