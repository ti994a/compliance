# POLICY: SC-45.2: Secondary Authoritative Time Source

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-45.2 |
| NIST Control | SC-45.2: Secondary Authoritative Time Source |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | time synchronization, authoritative time source, geographic redundancy, failover, system clocks |

## 1. POLICY STATEMENT
All systems must maintain accurate time synchronization through a secondary authoritative time source located in a different geographic region than the primary source. System clocks must automatically failover to the secondary time source when the primary source becomes unavailable.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid systems |
| Network infrastructure devices | YES | Routers, switches, firewalls requiring time sync |
| Security monitoring systems | YES | Critical for log correlation and forensics |
| Development/test systems | CONDITIONAL | If processing sensitive data or integrated with production |
| IoT devices | CONDITIONAL | If capable of time synchronization |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure primary and secondary time sources<br>• Monitor time synchronization status<br>• Implement failover mechanisms |
| Network Operations Center | • Monitor time source availability<br>• Respond to time synchronization alerts<br>• Coordinate with vendors for time source issues |
| Information Security Team | • Validate geographic separation requirements<br>• Review time synchronization logs<br>• Assess security implications of time drift |

## 4. RULES
[RULE-01] Systems MUST identify and configure a secondary authoritative time source that is geographically separated from the primary time source by a minimum of 100 miles.
[VALIDATION] IF secondary_time_source_distance < 100_miles THEN violation

[RULE-02] Systems MUST automatically synchronize internal clocks to the secondary authoritative time source within 5 minutes when the primary source becomes unavailable.
[VALIDATION] IF primary_time_source_unavailable = TRUE AND failover_time > 5_minutes THEN violation

[RULE-03] Geographic separation between primary and secondary time sources MUST be verified using geolocation data and documented in the system security plan.
[VALIDATION] IF geolocation_verification = FALSE OR documentation_current = FALSE THEN violation

[RULE-04] Time synchronization status and failover events MUST be logged and monitored continuously with alerts generated for synchronization failures.
[VALIDATION] IF logging_enabled = FALSE OR monitoring_active = FALSE THEN violation

[RULE-05] Maximum acceptable time drift between system clocks and authoritative time sources SHALL NOT exceed 1 second for security-critical systems and 30 seconds for standard systems.
[VALIDATION] IF system_criticality = "high" AND time_drift > 1_second THEN critical_violation
[VALIDATION] IF system_criticality = "standard" AND time_drift > 30_seconds THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Time Source Configuration - Establish and validate primary/secondary time sources with geographic separation
- [PROC-02] Failover Testing - Quarterly testing of automatic failover to secondary time source
- [PROC-03] Time Drift Monitoring - Continuous monitoring and alerting for time synchronization issues
- [PROC-04] Geographic Verification - Annual verification of time source geographic separation using updated geolocation data

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Time synchronization incidents, infrastructure changes, vendor changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Primary Time Source Failure]
IF primary_time_source_status = "unavailable"
AND secondary_time_source_configured = TRUE
AND failover_time <= 5_minutes
THEN compliance = TRUE

[SCENARIO-02: Insufficient Geographic Separation]
IF primary_time_source_location = "New York"
AND secondary_time_source_location = "New Jersey"
AND geographic_distance < 100_miles
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Time Drift Exceeding Limits]
IF system_type = "security_critical"
AND time_drift > 1_second
AND drift_duration > 5_minutes
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Missing Secondary Time Source]
IF primary_time_source_configured = TRUE
AND secondary_time_source_configured = FALSE
AND system_criticality >= "moderate"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Undocumented Geographic Verification]
IF secondary_time_source_exists = TRUE
AND geolocation_verification_date = NULL
AND system_deployment_date < 90_days_ago
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Secondary time source in different geographic region identified | [RULE-01], [RULE-03] |
| Internal system clocks synchronized to secondary source when primary unavailable | [RULE-02], [RULE-04] |
| Geographic separation verification | [RULE-03] |
| Time synchronization monitoring | [RULE-04], [RULE-05] |