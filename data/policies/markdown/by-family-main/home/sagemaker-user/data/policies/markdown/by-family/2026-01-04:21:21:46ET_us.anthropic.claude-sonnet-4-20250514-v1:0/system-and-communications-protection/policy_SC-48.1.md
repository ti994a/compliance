# POLICY: SC-48.1: Dynamic Relocation of Sensors or Monitoring Capabilities

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-48.1 |
| NIST Control | SC-48.1: Dynamic Relocation of Sensors or Monitoring Capabilities |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | sensors, monitoring, dynamic relocation, threat response, security controls |

## 1. POLICY STATEMENT
The organization SHALL implement dynamic relocation capabilities for security sensors and monitoring systems to counter adversarial activities and maintain effective security posture. Sensors and monitoring capabilities MUST be relocated automatically or manually based on predefined conditions to ensure continuous security coverage and prevent evasion by threat actors.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Network Security Sensors | YES | IDS, IPS, network monitoring tools |
| Host-based Monitoring | YES | EDR, host sensors, log collectors |
| Cloud Infrastructure Monitoring | YES | Cloud-native and hybrid deployments |
| Physical Security Sensors | CONDITIONAL | If integrated with IT security systems |
| Third-party Monitoring Services | YES | Must support relocation capabilities |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) | • Monitor relocation triggers and conditions<br>• Execute manual relocations when required<br>• Validate sensor functionality post-relocation |
| Network Security Team | • Define sensor placement strategies<br>• Configure automated relocation rules<br>• Maintain sensor inventory and capabilities |
| Infrastructure Team | • Provide technical infrastructure for sensor mobility<br>• Ensure network connectivity for relocated sensors<br>• Support sensor deployment and decommissioning |

## 4. RULES
[RULE-01] All security sensors and monitoring capabilities deployed in production environments MUST support dynamic relocation functionality or have documented compensating controls.
[VALIDATION] IF sensor_type = "security_monitoring" AND relocation_capable = FALSE AND compensating_controls = NULL THEN violation

[RULE-02] Organizations MUST define and document specific conditions and circumstances that trigger dynamic relocation of sensors and monitoring capabilities.
[VALIDATION] IF relocation_triggers_defined = FALSE OR relocation_triggers_documented = FALSE THEN violation

[RULE-03] Dynamic relocation of sensors MUST be completed within 15 minutes of trigger activation for automated relocations and within 4 hours for manual relocations.
[VALIDATION] IF relocation_type = "automated" AND relocation_time > 15_minutes THEN violation
[VALIDATION] IF relocation_type = "manual" AND relocation_time > 4_hours THEN violation

[RULE-04] All sensor relocations MUST be logged with timestamp, source location, destination location, trigger condition, and responsible party.
[VALIDATION] IF sensor_relocated = TRUE AND (log_timestamp = NULL OR source_location = NULL OR destination_location = NULL OR trigger_condition = NULL) THEN violation

[RULE-05] Relocated sensors MUST maintain equivalent or enhanced monitoring coverage compared to their original placement.
[VALIDATION] IF post_relocation_coverage < original_coverage THEN violation

[RULE-06] Organizations MUST test dynamic relocation capabilities quarterly and after any significant infrastructure changes.
[VALIDATION] IF last_relocation_test > 90_days OR (infrastructure_change = TRUE AND post_change_test = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Sensor Relocation Planning - Define relocation strategies and target locations
- [PROC-02] Trigger Condition Management - Establish and maintain relocation triggers
- [PROC-03] Automated Relocation Configuration - Configure and test automated relocation systems
- [PROC-04] Manual Relocation Execution - Process for emergency manual relocations
- [PROC-05] Post-Relocation Validation - Verify sensor functionality and coverage

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving sensor evasion, infrastructure changes, new threat intelligence

## 7. SCENARIO PATTERNS
[SCENARIO-01: Automated Threat Response Relocation]
IF threat_detected = TRUE
AND threat_type = "sensor_evasion"
AND automated_relocation_enabled = TRUE
AND relocation_completed_within_15_minutes = TRUE
THEN compliance = TRUE

[SCENARIO-02: Manual Emergency Relocation]
IF emergency_condition = TRUE
AND automated_relocation_failed = TRUE
AND manual_relocation_initiated = TRUE
AND relocation_time > 4_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Untested Relocation Capability]
IF sensor_supports_relocation = TRUE
AND last_relocation_test > 90_days
AND quarterly_test_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Inadequate Post-Relocation Coverage]
IF sensor_relocated = TRUE
AND post_relocation_coverage < original_coverage
AND compensating_controls = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Missing Relocation Documentation]
IF sensor_relocation_occurred = TRUE
AND relocation_triggers_documented = FALSE
AND relocation_log_complete = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Sensors and monitoring capabilities dynamically relocated are defined | RULE-01, RULE-02 |
| Dynamic relocation to defined locations under specified conditions | RULE-03, RULE-05 |
| Conditions or circumstances for relocation are defined | RULE-02, RULE-06 |