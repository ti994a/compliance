# POLICY: CP-7.1: Separation from Primary Site

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CP-7.1 |
| NIST Control | CP-7.1: Separation from Primary Site |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | alternate processing site, separation, threat reduction, contingency planning, disaster recovery |

## 1. POLICY STATEMENT
The organization MUST identify and maintain alternate processing sites that are sufficiently separated from primary processing sites to reduce susceptibility to the same threats. Site separation requirements MUST be based on organizational threat assessments and risk analysis.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Primary Processing Sites | YES | All facilities housing critical systems |
| Alternate Processing Sites | YES | All designated backup facilities |
| Cloud Service Providers | YES | When providing alternate processing |
| Third-party Data Centers | YES | When contracted for contingency operations |
| Mobile/Temporary Sites | CONDITIONAL | Only if designated as alternate sites |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve site separation criteria<br>• Review threat assessments<br>• Validate alternate site selections |
| Business Continuity Manager | • Identify alternate processing sites<br>• Assess separation adequacy<br>• Maintain site agreements<br>• Coordinate threat assessments |
| Risk Management Team | • Conduct threat assessments<br>• Define separation requirements<br>• Evaluate geographic and operational risks |

## 4. RULES
[RULE-01] Organizations MUST identify alternate processing sites that are geographically separated from primary sites based on documented threat assessments.
[VALIDATION] IF alternate_site_identified = FALSE OR threat_assessment_documented = FALSE THEN violation

[RULE-02] Site separation distance MUST be sufficient to reduce susceptibility to identified threats, with minimum 50 miles for natural disasters and 10 miles for infrastructure failures.
[VALIDATION] IF threat_type = "natural_disaster" AND separation_distance < 50_miles THEN violation
[VALIDATION] IF threat_type = "infrastructure_failure" AND separation_distance < 10_miles THEN violation

[RULE-03] Threat assessments used for site separation decisions MUST be reviewed and updated annually or when significant environmental changes occur.
[VALIDATION] IF threat_assessment_age > 365_days OR environmental_change = TRUE AND assessment_updated = FALSE THEN violation

[RULE-04] Alternate site selections MUST be documented with justification for separation adequacy based on specific threat scenarios.
[VALIDATION] IF alternate_site_documented = FALSE OR separation_justification = FALSE THEN violation

[RULE-05] Organizations MUST evaluate both physical and logical separation requirements when selecting alternate processing sites.
[VALIDATION] IF physical_separation_assessed = FALSE OR logical_separation_assessed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Threat Assessment for Site Selection - Annual assessment of threats affecting site locations
- [PROC-02] Site Separation Analysis - Evaluation of geographic and operational separation adequacy
- [PROC-03] Alternate Site Identification - Process for identifying and validating alternate processing sites
- [PROC-04] Site Agreement Management - Maintenance of contracts and agreements for alternate sites

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major environmental changes, new threat intelligence, site relocations, significant business changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Inadequate Geographic Separation]
IF primary_site_location = "California"
AND alternate_site_location = "California"
AND threat_type = "earthquake"
AND separation_distance < 50_miles
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Shared Infrastructure Risk]
IF primary_site_power_grid = "Grid_A"
AND alternate_site_power_grid = "Grid_A"
AND threat_type = "infrastructure_failure"
AND logical_separation_assessed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Outdated Threat Assessment]
IF threat_assessment_date < (current_date - 365_days)
AND site_selection_basis = "outdated_assessment"
AND environmental_changes = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Undocumented Site Selection]
IF alternate_site_identified = TRUE
AND separation_justification_documented = FALSE
AND threat_scenario_analysis = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Adequate Separation Implementation]
IF separation_distance >= required_minimum
AND threat_assessment_current = TRUE
AND site_selection_documented = TRUE
AND separation_justification = "adequate"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Alternate processing site identified with sufficient separation | RULE-01, RULE-02 |
| Threat-based separation criteria | RULE-01, RULE-03 |
| Documentation of separation adequacy | RULE-04 |
| Physical and logical separation evaluation | RULE-05 |