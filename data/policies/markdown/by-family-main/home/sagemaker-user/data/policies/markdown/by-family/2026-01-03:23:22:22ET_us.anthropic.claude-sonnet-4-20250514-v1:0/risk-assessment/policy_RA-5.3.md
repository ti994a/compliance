# POLICY: RA-5.3: Breadth and Depth of Coverage

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-5.3 |
| NIST Control | RA-5.3: Breadth and Depth of Coverage |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | vulnerability scanning, coverage, breadth, depth, risk assessment, security controls |

## 1. POLICY STATEMENT
The organization must define and document specific breadth and depth requirements for vulnerability scanning coverage across all information systems. Coverage definitions must specify measurable criteria for both the scope of systems scanned and the level of detail examined during vulnerability assessments.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing organizational data |
| Development Systems | YES | Systems containing production-like data |
| Test Systems | CONDITIONAL | Only if containing sensitive data |
| Network Infrastructure | YES | Routers, switches, firewalls, load balancers |
| Cloud Resources | YES | IaaS, PaaS, SaaS components under org control |
| Third-party Systems | CONDITIONAL | Only systems with direct network connectivity |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Manager | • Define breadth and depth coverage requirements<br>• Approve scanning tool configurations<br>• Review coverage metrics quarterly |
| Vulnerability Management Team | • Implement scanning coverage requirements<br>• Configure scanning tools per depth specifications<br>• Generate coverage reports |
| System Owners | • Provide system inventory for breadth calculations<br>• Coordinate scanning schedules<br>• Validate scanning results |

## 4. RULES
[RULE-01] Organizations MUST define breadth of vulnerability scanning coverage as a minimum percentage of components within each system category.
[VALIDATION] IF system_category_coverage < defined_minimum_percentage THEN violation

[RULE-02] Organizations MUST define depth of vulnerability scanning coverage specifying the system design levels to be monitored (component, module, subsystem, or element level).
[VALIDATION] IF scanning_depth_level NOT IN approved_depth_levels THEN violation

[RULE-03] Breadth coverage definitions MUST specify minimum coverage percentages for critical systems (≥95%), high-impact systems (≥90%), and moderate-impact systems (≥85%).
[VALIDATION] IF system_criticality = "critical" AND coverage_percentage < 95 THEN violation
[VALIDATION] IF system_criticality = "high" AND coverage_percentage < 90 THEN violation
[VALIDATION] IF system_criticality = "moderate" AND coverage_percentage < 85 THEN violation

[RULE-04] Depth coverage definitions MUST specify vulnerability check categories including network services, operating systems, applications, and databases.
[VALIDATION] IF vulnerability_categories_scanned NOT INCLUDES required_categories THEN violation

[RULE-05] Coverage definitions MUST be documented, approved by the CISO, and reviewed annually or when significant system changes occur.
[VALIDATION] IF coverage_definition_approval_date > 365_days_ago THEN violation
[VALIDATION] IF significant_system_change = TRUE AND coverage_review_completed = FALSE THEN violation

[RULE-06] Multiple scanning tools MAY be deployed to achieve required depth and coverage when a single tool cannot meet all requirements.
[VALIDATION] IF single_tool_sufficient = FALSE AND multiple_tools_deployed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Coverage Definition Process - Establish methodology for calculating and documenting breadth and depth requirements
- [PROC-02] Scanning Tool Configuration - Configure tools to meet defined coverage requirements
- [PROC-03] Coverage Measurement - Monitor and report actual vs. required coverage metrics
- [PROC-04] Coverage Gap Analysis - Identify and remediate coverage deficiencies

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system implementations, significant architecture changes, new regulatory requirements, coverage gaps exceeding thresholds

## 7. SCENARIO PATTERNS
[SCENARIO-01: Insufficient Critical System Coverage]
IF system_criticality = "critical"
AND actual_coverage_percentage < 95
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Undefined Depth Requirements]
IF vulnerability_scanning_active = TRUE
AND depth_requirements_documented = FALSE
AND system_go_live_date < current_date
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Outdated Coverage Definitions]
IF coverage_definition_last_updated > 365_days_ago
AND no_coverage_review_scheduled = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Tool Configuration Mismatch]
IF required_vulnerability_categories = ["network", "os", "application", "database"]
AND scanning_tool_categories = ["network", "os"]
AND additional_tools_deployed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Multi-Tool Setup]
IF coverage_percentage >= required_minimum
AND all_required_depth_levels_scanned = TRUE
AND coverage_definitions_current = TRUE
AND CISO_approval_valid = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Breadth of coverage defined | RULE-01, RULE-03 |
| Depth of coverage defined | RULE-02, RULE-04 |
| Coverage definitions documented and approved | RULE-05 |
| Appropriate tools configured for coverage | RULE-06 |