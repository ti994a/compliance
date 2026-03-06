# POLICY: SC-45.2: Secondary Authoritative Time Source

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-45.2 |
| NIST Control | SC-45.2: Secondary Authoritative Time Source |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | time synchronization, authoritative time source, geographic regions, failover, system clocks |

## 1. POLICY STATEMENT
All information systems MUST maintain time synchronization through a secondary authoritative time source located in a different geographic region than the primary source. Systems SHALL automatically failover to the secondary time source when the primary source becomes unavailable to ensure continuous accurate timekeeping for security logging and audit functions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing regulated data |
| Development Systems | YES | Systems with audit requirements |
| Test Systems | CONDITIONAL | If connected to production networks |
| IoT Devices | YES | If capable of time synchronization |
| Cloud Services | YES | Customer-managed instances only |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure primary and secondary time sources<br>• Monitor time synchronization status<br>• Validate geographic separation requirements |
| Security Operations | • Monitor time source availability<br>• Investigate time synchronization failures<br>• Validate audit log timestamp accuracy |
| Infrastructure Teams | • Maintain network connectivity to time sources<br>• Implement failover mechanisms<br>• Document geographic locations of time sources |

## 4. RULES

[RULE-01] Systems MUST identify and configure a secondary authoritative time source located in a different geographic region than the primary time source, with geographic separation of at least 500 miles.
[VALIDATION] IF secondary_time_source_configured = FALSE OR geographic_distance < 500_miles THEN violation

[RULE-02] Systems SHALL automatically synchronize internal clocks to the secondary authoritative time source within 30 seconds when the primary source becomes unavailable.
[VALIDATION] IF primary_source_unavailable = TRUE AND failover_time > 30_seconds THEN violation

[RULE-03] Geographic location verification MUST be performed using geolocation services or documented coordinates for both primary and secondary time sources.
[VALIDATION] IF geolocation_verified = FALSE OR coordinates_documented = FALSE THEN violation

[RULE-04] Time synchronization status MUST be monitored continuously with alerts generated within 5 minutes of primary source failure.
[VALIDATION] IF monitoring_enabled = FALSE OR alert_delay > 5_minutes THEN violation

[RULE-05] Systems MUST maintain time accuracy within 1 second of the authoritative source during normal operations and within 10 seconds during failover scenarios.
[VALIDATION] IF time_drift > 1_second AND source_status = "primary" THEN violation
[VALIDATION] IF time_drift > 10_seconds AND source_status = "secondary" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Time Source Configuration - Establish and validate primary and secondary time sources with geographic verification
- [PROC-02] Failover Testing - Monthly testing of automatic failover to secondary time source
- [PROC-03] Geographic Validation - Annual verification of time source locations using geolocation services
- [PROC-04] Time Drift Monitoring - Continuous monitoring and alerting for time synchronization accuracy

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Time source failures, infrastructure changes, regulatory updates, security incidents involving timestamp integrity

## 7. SCENARIO PATTERNS

[SCENARIO-01: Primary Time Source Failure]
IF primary_time_source_status = "unavailable"
AND secondary_time_source_configured = TRUE
AND failover_completed = TRUE
AND failover_time <= 30_seconds
THEN compliance = TRUE

[SCENARIO-02: Insufficient Geographic Separation]
IF primary_time_source_location = "US-East"
AND secondary_time_source_location = "US-East"
AND geographic_distance < 500_miles
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Secondary Time Source]
IF system_type = "production"
AND primary_time_source_configured = TRUE
AND secondary_time_source_configured = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Excessive Time Drift During Failover]
IF active_time_source = "secondary"
AND time_drift > 10_seconds
AND failover_duration > 1_hour
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Unverified Geographic Locations]
IF secondary_time_source_configured = TRUE
AND geolocation_verified = FALSE
AND last_verification_date > 365_days
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Secondary time source identification in different geographic region | [RULE-01], [RULE-03] |
| Internal system clock synchronization to secondary source when primary unavailable | [RULE-02], [RULE-05] |
| Geographic region verification | [RULE-03] |
| Continuous time synchronization monitoring | [RULE-04] |