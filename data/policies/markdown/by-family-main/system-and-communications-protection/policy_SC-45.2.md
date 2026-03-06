# POLICY: SC-45.2: Secondary Authoritative Time Source

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-45.2 |
| NIST Control | SC-45.2: Secondary Authoritative Time Source |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | time synchronization, authoritative time source, geographic region, failover, system clocks |

## 1. POLICY STATEMENT
All information systems MUST maintain a secondary authoritative time source located in a different geographic region than the primary source. Systems MUST automatically synchronize to the secondary time source when the primary source becomes unavailable to ensure continuous accurate timekeeping for security functions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing organizational data |
| Development Systems | YES | Systems containing production-like data |
| Test Systems | CONDITIONAL | Only if connected to production networks |
| Personal Devices | NO | Covered under separate mobile device policy |
| Vendor Systems | CONDITIONAL | Only if processing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure secondary time sources<br>• Monitor time synchronization status<br>• Implement failover mechanisms |
| Network Operations | • Maintain network connectivity to time sources<br>• Monitor time source availability<br>• Document geographic locations |
| Security Team | • Validate time source configurations<br>• Review time synchronization logs<br>• Assess geographic separation requirements |

## 4. RULES
[RULE-01] Each system MUST have a secondary authoritative time source configured that is geographically separated from the primary source by a minimum of 100 miles.
[VALIDATION] IF secondary_time_source_distance < 100_miles THEN violation

[RULE-02] Systems MUST automatically failover to the secondary time source within 60 seconds when the primary source becomes unavailable.
[VALIDATION] IF primary_source_unavailable = TRUE AND failover_time > 60_seconds THEN violation

[RULE-03] Geographic location verification MUST be performed using geolocation services or documented physical addresses for both primary and secondary time sources.
[VALIDATION] IF geolocation_verified = FALSE AND physical_address_documented = FALSE THEN violation

[RULE-04] Time synchronization status MUST be monitored continuously with alerts generated when either time source becomes unavailable.
[VALIDATION] IF monitoring_enabled = FALSE OR alert_configuration = NULL THEN violation

[RULE-05] Secondary time source failover testing MUST be performed quarterly to validate automatic switching functionality.
[VALIDATION] IF last_failover_test > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Time Source Configuration - Standard process for identifying and configuring geographically separated time sources
- [PROC-02] Geographic Verification - Process for validating geographic separation using geolocation or address verification
- [PROC-03] Failover Testing - Quarterly testing procedure to validate automatic failover to secondary time sources
- [PROC-04] Monitoring Setup - Configuration of continuous monitoring and alerting for time source availability

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Time source failures, geographic relocations, new system deployments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Insufficient Geographic Separation]
IF primary_time_source_location = "New York, NY"
AND secondary_time_source_location = "Newark, NJ"
AND geographic_distance < 100_miles
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Missing Secondary Time Source]
IF primary_time_source_configured = TRUE
AND secondary_time_source_configured = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Failover Not Working]
IF primary_time_source_available = FALSE
AND system_synchronized_to_secondary = FALSE
AND time_since_primary_failure > 60_seconds
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Proper Geographic Separation]
IF primary_time_source_location = "Virginia"
AND secondary_time_source_location = "Colorado"
AND geographic_distance > 100_miles
AND failover_tested_within_90_days = TRUE
THEN compliance = TRUE

[SCENARIO-05: Untested Failover Configuration]
IF secondary_time_source_configured = TRUE
AND geographic_separation_verified = TRUE
AND last_failover_test > 90_days
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Secondary authoritative time source identified in different geographic region | [RULE-01], [RULE-03] |
| Internal system clocks synchronized to secondary source when primary unavailable | [RULE-02], [RULE-04] |
| Geographic separation verification | [RULE-03] |
| Continuous monitoring and testing | [RULE-04], [RULE-05] |