# POLICY: RA-5.3: Breadth and Depth of Coverage

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-5.3 |
| NIST Control | RA-5.3: Breadth and Depth of Coverage |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | vulnerability scanning, coverage, breadth, depth, risk assessment, scanning tools |

## 1. POLICY STATEMENT
The organization must define and maintain comprehensive vulnerability scanning coverage parameters that specify both the breadth (scope of systems and components) and depth (level of system design layers) of vulnerability assessments. Coverage definitions must align with organizational risk tolerance and regulatory requirements to ensure adequate security posture evaluation.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing business data |
| Development Systems | YES | Systems with access to production data |
| Test/Staging Systems | YES | Systems mirroring production configurations |
| Contractor Systems | CONDITIONAL | If accessing organizational data |
| Air-gapped Systems | CONDITIONAL | Based on criticality assessment |
| Personal Devices | CONDITIONAL | If approved for business use |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve vulnerability scanning coverage definitions<br>• Review coverage adequacy quarterly<br>• Ensure regulatory compliance alignment |
| Security Operations Manager | • Define specific coverage parameters<br>• Maintain scanning tool configurations<br>• Monitor coverage metrics and reporting |
| System Owners | • Identify system components for scanning<br>• Validate coverage definitions for owned systems<br>• Coordinate scanning schedules |

## 4. RULES
[RULE-01] Organizations MUST define vulnerability scanning breadth coverage as a minimum percentage of components within each system criticality tier.
[VALIDATION] IF system_criticality = "high" AND coverage_percentage < 95% THEN violation
[VALIDATION] IF system_criticality = "medium" AND coverage_percentage < 85% THEN violation
[VALIDATION] IF system_criticality = "low" AND coverage_percentage < 75% THEN violation

[RULE-02] Organizations MUST define vulnerability scanning depth coverage to include at minimum the component, module, and subsystem levels for high-criticality systems.
[VALIDATION] IF system_criticality = "high" AND (component_scanning = FALSE OR module_scanning = FALSE OR subsystem_scanning = FALSE) THEN violation

[RULE-03] Coverage definitions MUST be documented and reviewed at least annually or when significant system changes occur.
[VALIDATION] IF coverage_definition_age > 365_days AND no_system_changes = TRUE THEN violation
[VALIDATION] IF significant_system_change = TRUE AND coverage_review_completed = FALSE THEN violation

[RULE-04] Multiple scanning tools MUST be employed when a single tool cannot achieve the defined breadth and depth requirements.
[VALIDATION] IF required_coverage > single_tool_capability AND additional_tools_deployed = FALSE THEN violation

[RULE-05] Coverage adequacy MUST be validated against organizational risk tolerance and documented risk acceptance criteria.
[VALIDATION] IF coverage_assessment_completed = FALSE OR risk_tolerance_alignment = "not_validated" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Coverage Definition Process - Establish methodology for determining scanning breadth and depth parameters
- [PROC-02] Tool Configuration Management - Maintain scanning tool settings to achieve defined coverage
- [PROC-03] Coverage Validation Process - Verify actual scanning coverage meets defined requirements
- [PROC-04] Coverage Gap Analysis - Identify and remediate scanning coverage deficiencies

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system changes, new regulatory requirements, significant security incidents, tool changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Insufficient High-Criticality Coverage]
IF system_criticality = "high"
AND actual_coverage_percentage < 95%
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Depth Coverage Documentation]
IF coverage_depth_definition = "undefined"
AND system_contains_sensitive_data = TRUE
AND last_coverage_review > 365_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Single Tool Limitation]
IF required_coverage_breadth = 90%
AND single_tool_max_coverage = 70%
AND additional_tools_deployed = FALSE
AND coverage_gap_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Adequate Multi-Tool Coverage]
IF defined_breadth_coverage >= 85%
AND defined_depth_coverage >= "component_level"
AND actual_coverage_meets_definition = TRUE
AND coverage_validated_within_90_days = TRUE
THEN compliance = TRUE

[SCENARIO-05: Risk-Aligned Coverage Exception]
IF coverage_percentage < defined_minimum
AND risk_assessment_completed = TRUE
AND coverage_exception_approved_by_ciso = TRUE
AND compensating_controls_implemented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Breadth coverage definition | [RULE-01] |
| Depth coverage definition | [RULE-02] |
| Coverage documentation and review | [RULE-03] |
| Multi-tool implementation | [RULE-04] |
| Risk tolerance alignment | [RULE-05] |