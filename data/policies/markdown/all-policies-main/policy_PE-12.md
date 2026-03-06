# POLICY: PE-12: Emergency Lighting

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-12 |
| NIST Control | PE-12: Emergency Lighting |
| Version | 1.0 |
| Owner | Facilities Security Manager |
| Keywords | emergency lighting, power outage, evacuation routes, emergency exits, data center, automatic activation |

## 1. POLICY STATEMENT
The organization MUST employ and maintain automatic emergency lighting systems that activate during power outages or disruptions to ensure safe evacuation from facilities containing information systems. Emergency lighting MUST cover all emergency exits and evacuation routes within facilities housing critical system resources.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | Primary scope - critical system concentrations |
| Server Rooms | YES | Contains system resources requiring protection |
| Mainframe Computer Rooms | YES | High-value system assets |
| Network Operations Centers | YES | Critical operational facilities |
| Office Areas | CONDITIONAL | Only if containing critical system resources |
| Storage Areas | CONDITIONAL | Only if containing system components |
| Vendor Facilities | CONDITIONAL | If processing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Security Manager | • Implement emergency lighting systems<br>• Maintain lighting equipment and batteries<br>• Coordinate with contingency planning team |
| System Administrator | • Document system-specific lighting requirements<br>• Report lighting failures affecting system operations |
| Contingency Planning Team | • Include emergency lighting in contingency plans<br>• Identify alternate processing sites for lighting failures |

## 4. RULES
[RULE-01] All facilities containing system resources MUST have automatic emergency lighting that activates within 10 seconds of power outage or disruption.
[VALIDATION] IF facility_has_systems = TRUE AND emergency_lighting_installed = FALSE THEN critical_violation
[VALIDATION] IF activation_time > 10_seconds THEN violation

[RULE-02] Emergency lighting MUST provide illumination for a minimum of 90 minutes during power outages.
[VALIDATION] IF battery_duration < 90_minutes THEN violation

[RULE-03] Emergency lighting MUST cover 100% of emergency exits and evacuation routes within in-scope facilities.
[VALIDATION] IF exit_coverage < 100% OR evacuation_route_coverage < 100% THEN critical_violation

[RULE-04] Emergency lighting systems MUST be tested monthly and maintained according to manufacturer specifications.
[VALIDATION] IF last_test_date > 30_days_ago THEN violation
[VALIDATION] IF maintenance_overdue = TRUE THEN violation

[RULE-05] Emergency lighting failures MUST be documented in the contingency plan and alternate processing sites MUST be identified.
[VALIDATION] IF lighting_failure_documented = FALSE AND alternate_site_identified = FALSE THEN violation

[RULE-06] Emergency lighting systems MUST be included in facility risk assessments and system security plans.
[VALIDATION] IF risk_assessment_includes_lighting = FALSE OR ssp_includes_lighting = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Emergency Lighting Installation - Standards for selecting and installing automatic emergency lighting systems
- [PROC-02] Monthly Testing Protocol - Procedures for testing emergency lighting activation and duration
- [PROC-03] Maintenance Schedule - Preventive maintenance procedures for batteries and lighting equipment
- [PROC-04] Failure Response - Actions to take when emergency lighting systems fail or are compromised

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Facility modifications, lighting system failures, power outage incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Data Center]
IF facility_type = "data_center"
AND emergency_lighting_installed = FALSE
AND facility_operational = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Monthly Testing Overdue]
IF last_emergency_lighting_test > 35_days_ago
AND facility_contains_systems = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Partial Exit Coverage]
IF emergency_exit_coverage = 80%
AND evacuation_route_coverage = 100%
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Battery Duration Insufficient]
IF emergency_lighting_duration = 60_minutes
AND power_outage_duration = 90_minutes
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Office Area Exception]
IF facility_type = "office"
AND critical_systems_present = FALSE
AND emergency_lighting_installed = FALSE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Automatic emergency lighting employed for system | [RULE-01] |
| Automatic emergency lighting maintained for system | [RULE-04] |
| Emergency lighting covers emergency exits | [RULE-03] |
| Emergency lighting covers evacuation routes | [RULE-03] |