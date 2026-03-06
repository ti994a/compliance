# POLICY: CP-6.1: Separation from Primary Site

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CP-6.1 |
| NIST Control | CP-6.1: Separation from Primary Site |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | alternate storage, site separation, threat reduction, disaster recovery, contingency planning |

## 1. POLICY STATEMENT
The organization MUST identify and maintain alternate storage sites that are geographically and logically separated from primary storage sites to reduce susceptibility to common threats. Site separation requirements SHALL be based on organizational risk assessments and threat analysis.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Primary data storage sites | YES | All production storage facilities |
| Alternate storage sites | YES | All backup and recovery storage locations |
| Cloud storage services | YES | Both primary and alternate cloud regions |
| Mobile storage devices | CONDITIONAL | Only if part of formal contingency plan |
| Development environments | NO | Unless storing production data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve site separation requirements<br>• Review threat assessments<br>• Validate compliance with separation standards |
| IT Operations Manager | • Implement site separation requirements<br>• Monitor site availability and accessibility<br>• Coordinate with site vendors and providers |
| Risk Management Team | • Conduct threat assessments for site selection<br>• Define minimum separation requirements<br>• Evaluate site vulnerability to common threats |

## 4. RULES
[RULE-01] Alternate storage sites MUST be located at least 50 miles from the primary storage site for natural disaster protection.
[VALIDATION] IF distance_between_sites < 50_miles AND threat_type = "natural_disaster" THEN violation

[RULE-02] Alternate storage sites SHALL NOT share common infrastructure dependencies (power grid, telecommunications, transportation) with primary sites.
[VALIDATION] IF shared_infrastructure = TRUE AND dependency_type IN ["power", "telecom", "transport"] THEN violation

[RULE-03] Site separation requirements MUST be documented in the contingency plan and reviewed annually.
[VALIDATION] IF separation_requirements NOT documented OR last_review > 365_days THEN violation

[RULE-04] Cloud-based alternate storage MUST utilize different availability zones or regions from primary cloud storage.
[VALIDATION] IF cloud_primary_region = cloud_alternate_region THEN violation

[RULE-05] Threat-based separation analysis MUST be performed before selecting alternate storage sites.
[VALIDATION] IF threat_analysis_date IS NULL OR site_selection_date > threat_analysis_date THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Site Selection Assessment - Evaluate potential alternate sites against threat and separation criteria
- [PROC-02] Threat Analysis - Identify and assess threats common to geographic regions
- [PROC-03] Infrastructure Dependency Mapping - Document shared dependencies between primary and alternate sites
- [PROC-04] Site Separation Validation - Verify and test accessibility of alternate sites during various threat scenarios

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major natural disasters, infrastructure changes, new threat intelligence, site relocations

## 7. SCENARIO PATTERNS
[SCENARIO-01: Inadequate Geographic Separation]
IF primary_site_location = "New York, NY"
AND alternate_site_location = "Newark, NJ"
AND distance_between_sites = 10_miles
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Shared Infrastructure Dependencies]
IF primary_site_power_grid = "Eastern_Grid_Zone_1"
AND alternate_site_power_grid = "Eastern_Grid_Zone_1"
AND threat_type = "power_grid_failure"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Cloud Region Separation]
IF primary_storage = "AWS_us-east-1"
AND alternate_storage = "AWS_us-east-2"
AND separation_analysis_completed = TRUE
THEN compliance = TRUE

[SCENARIO-04: Missing Threat Analysis]
IF alternate_site_selected = TRUE
AND threat_analysis_performed = FALSE
AND site_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Earthquake Zone Vulnerability]
IF primary_site_seismic_zone = "Zone_4_High_Risk"
AND alternate_site_seismic_zone = "Zone_4_High_Risk"
AND distance_between_sites < 100_miles
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Alternate storage site identification with sufficient separation | [RULE-01], [RULE-02] |
| Threat-based separation analysis | [RULE-05] |
| Documentation of separation requirements | [RULE-03] |
| Cloud storage separation requirements | [RULE-04] |