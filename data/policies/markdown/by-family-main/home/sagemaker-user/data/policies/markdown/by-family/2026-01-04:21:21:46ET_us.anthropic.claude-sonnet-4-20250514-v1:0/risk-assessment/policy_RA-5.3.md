# POLICY: RA-5.3: Breadth and Depth of Coverage

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-5.3 |
| NIST Control | RA-5.3: Breadth and Depth of Coverage |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | vulnerability scanning, coverage, assessment, risk tolerance, scanning tools |

## 1. POLICY STATEMENT
The organization must define and document specific breadth and depth parameters for vulnerability scanning coverage across all information systems. Coverage requirements must align with organizational risk tolerance and system criticality levels to ensure comprehensive vulnerability identification.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing organizational data |
| Development Systems | YES | Systems containing production-like data |
| Test Systems | CONDITIONAL | Only if containing sensitive data |
| Network Infrastructure | YES | Routers, switches, firewalls, load balancers |
| Cloud Resources | YES | IaaS, PaaS, SaaS components under org control |
| Third-party Systems | CONDITIONAL | Only if organization has scanning rights |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Team | • Define scanning coverage parameters<br>• Execute vulnerability scans<br>• Analyze scan results and coverage gaps |
| System Owners | • Provide system inventory and criticality ratings<br>• Coordinate scanning schedules<br>• Remediate identified vulnerabilities |
| Risk Management Office | • Approve coverage definitions based on risk tolerance<br>• Review coverage adequacy quarterly<br>• Update requirements based on threat landscape |

## 4. RULES
[RULE-01] Organizations MUST define breadth of vulnerability scanning coverage as a minimum percentage of components within each system criticality level.
[VALIDATION] IF system_criticality = "high" AND coverage_percentage < 95% THEN violation
[VALIDATION] IF system_criticality = "moderate" AND coverage_percentage < 85% THEN violation
[VALIDATION] IF system_criticality = "low" AND coverage_percentage < 75% THEN violation

[RULE-02] Organizations MUST define depth of vulnerability scanning coverage by specifying the system design levels to be monitored for each system type.
[VALIDATION] IF scanning_depth NOT IN ["component", "module", "subsystem", "element"] THEN violation
[VALIDATION] IF high_criticality_system AND scanning_depth NOT IN ["component", "module"] THEN violation

[RULE-03] Vulnerability scanning coverage definitions MUST be documented and approved by the Risk Management Office within 30 days of system deployment.
[VALIDATION] IF system_deployed = TRUE AND coverage_definition_approved = FALSE AND days_since_deployment > 30 THEN violation

[RULE-04] Organizations MUST utilize multiple scanning tools when a single tool cannot achieve the defined breadth and depth requirements.
[VALIDATION] IF coverage_gap_identified = TRUE AND additional_tools_deployed = FALSE AND gap_duration > 14_days THEN violation

[RULE-05] Coverage definitions MUST specify the types of vulnerabilities to be checked based on system function and data classification.
[VALIDATION] IF vulnerability_types_defined = FALSE OR vulnerability_types_count < minimum_required_types THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Coverage Definition Process - Systematic approach for defining breadth and depth parameters
- [PROC-02] Scanning Tool Selection - Evaluation and selection of appropriate vulnerability scanning tools
- [PROC-03] Coverage Gap Analysis - Process for identifying and addressing scanning coverage deficiencies
- [PROC-04] Coverage Validation - Regular verification that actual scanning meets defined coverage requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New system deployments, significant architecture changes, major security incidents, changes in risk tolerance

## 7. SCENARIO PATTERNS
[SCENARIO-01: Insufficient High-Criticality Coverage]
IF system_criticality = "high"
AND actual_coverage_percentage = 88%
AND required_coverage_percentage = 95%
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Undefined Scanning Depth]
IF system_deployed = TRUE
AND scanning_depth_defined = FALSE
AND days_since_deployment > 15
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Single Tool Limitation]
IF coverage_gap_percentage > 10%
AND available_additional_tools = TRUE
AND additional_tools_deployed = FALSE
AND gap_duration > 14_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Compliant Multi-Tool Coverage]
IF required_coverage_percentage = 90%
AND tool1_coverage = 70%
AND tool2_coverage = 25%
AND combined_coverage = 95%
AND coverage_documented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Vulnerability Type Coverage Gap]
IF system_function = "web_application"
AND required_vulnerability_types = ["OWASP_Top_10", "infrastructure", "configuration"]
AND actual_vulnerability_types = ["infrastructure"]
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Breadth of vulnerability scanning coverage is defined | RULE-01, RULE-05 |
| Depth of vulnerability scanning coverage is defined | RULE-02 |
| Coverage definitions are documented and approved | RULE-03 |
| Multiple tools used when necessary for coverage | RULE-04 |