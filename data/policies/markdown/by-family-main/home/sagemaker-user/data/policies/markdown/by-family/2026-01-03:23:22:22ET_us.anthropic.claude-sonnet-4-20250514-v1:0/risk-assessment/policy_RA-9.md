# POLICY: RA-9: Criticality Analysis

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-9 |
| NIST Control | RA-9: Criticality Analysis |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | criticality analysis, critical components, system functions, risk assessment, SDLC, mission-critical |

## 1. POLICY STATEMENT
The organization must identify critical system components and functions through formal criticality analysis to prioritize protection activities and inform risk management decisions. Criticality analysis shall be performed at defined decision points in the system development life cycle to enable design modifications that reduce critical dependencies.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing organizational data |
| System Components | YES | Hardware, software, firmware components |
| System Services | YES | Internal and outsourced IT services |
| Cyber-Physical Systems | YES | Including IoT and operational technology |
| Development Projects | YES | All SDLC phases requiring criticality analysis |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Architects | • Conduct functional decomposition analysis<br>• Identify mission-critical functions<br>• Document component dependencies and interfaces |
| Risk Managers | • Define criticality analysis methodology<br>• Review and validate criticality assessments<br>• Maintain criticality analysis documentation |
| Development Teams | • Perform criticality analysis at SDLC decision points<br>• Implement design modifications based on analysis<br>• Document critical component protections |

## 4. RULES
[RULE-01] Organizations MUST perform criticality analysis for all systems, system components, and system services that process, store, or transmit organizational data.
[VALIDATION] IF system_in_inventory = TRUE AND criticality_analysis_completed = FALSE THEN violation

[RULE-02] Criticality analysis SHALL be performed at pre-defined decision points in the system development life cycle including design, development, modification, and upgrade phases.
[VALIDATION] IF sdlc_decision_point = TRUE AND criticality_analysis_current = FALSE THEN violation

[RULE-03] Critical system components and functions MUST be identified through functional decomposition that traces organizational missions to specific hardware, software, and firmware components.
[VALIDATION] IF functional_decomposition_complete = FALSE AND system_classification != "low_impact" THEN violation

[RULE-04] Components that allow unmediated access to critical system components or functions MUST be classified as critical regardless of their inherent functionality.
[VALIDATION] IF unmediated_access_to_critical = TRUE AND component_criticality != "critical" THEN violation

[RULE-05] Criticality analysis MUST consider the operational environment including connections to cyber-physical systems, system-of-systems, and outsourced services.
[VALIDATION] IF external_dependencies_exist = TRUE AND environmental_analysis_complete = FALSE THEN violation

[RULE-06] Organizations MUST maintain current criticality analysis documentation that is reviewed and updated at least annually or when significant system changes occur.
[VALIDATION] IF criticality_doc_age > 365_days OR significant_change = TRUE AND updated_analysis = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Criticality Analysis Methodology - Standardized approach for conducting functional decomposition and criticality assessment
- [PROC-02] SDLC Integration Process - Integration of criticality analysis into development life cycle decision points  
- [PROC-03] Critical Component Protection - Enhanced security measures for components identified as critical
- [PROC-04] Dependency Mapping Process - Documentation of system component dependencies and interfaces

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Major system changes, new regulatory requirements, significant security incidents affecting critical components

## 7. SCENARIO PATTERNS
[SCENARIO-01: New System Deployment]
IF system_deployment = "new"
AND criticality_analysis_completed = FALSE
AND go_live_date <= 30_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: System Modification Without Analysis]
IF system_modification = "major"
AND criticality_analysis_updated = FALSE
AND modification_affects_critical_functions = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Outdated Criticality Documentation]
IF criticality_analysis_age > 365_days
AND system_changes_occurred = TRUE
AND analysis_review_scheduled = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unclassified Critical Access Path]
IF component_provides_unmediated_access = TRUE
AND target_component_criticality = "critical"
AND access_component_criticality != "critical"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Missing Environmental Considerations]
IF external_system_connections > 0
AND cyber_physical_integration = TRUE
AND environmental_analysis_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Critical system components and functions are identified | RULE-01, RULE-03 |
| Criticality analysis performed for defined systems/components/services | RULE-01, RULE-05 |
| Analysis conducted at SDLC decision points | RULE-02 |
| Functional decomposition methodology implemented | RULE-03 |
| Current criticality documentation maintained | RULE-06 |