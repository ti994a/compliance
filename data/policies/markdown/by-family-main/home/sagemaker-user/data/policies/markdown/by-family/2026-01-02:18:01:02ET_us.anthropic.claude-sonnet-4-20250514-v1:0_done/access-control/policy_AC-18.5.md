```markdown
# POLICY: AC-18.5: Antennas and Transmission Power Levels

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-18.5 |
| NIST Control | AC-18.5: Antennas and Transmission Power Levels |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | wireless, antennas, transmission power, RF emissions, wireless surveys, boundary control |

## 1. POLICY STATEMENT
The organization SHALL select radio antennas and calibrate transmission power levels to prevent wireless signals from extending beyond organization-controlled boundaries. Regular wireless surveys MUST be conducted to validate signal containment and identify unauthorized wireless emissions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Wireless Access Points | YES | All corporate and guest networks |
| Bluetooth Devices | YES | Fixed infrastructure devices only |
| Mobile Hotspots | CONDITIONAL | Only organization-managed devices |
| IoT Wireless Devices | YES | All connected sensors and controllers |
| Temporary Wireless Equipment | YES | Events, testing, contractor equipment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Engineering Team | • Configure antenna selection and power calibration<br>• Conduct quarterly wireless surveys<br>• Document RF coverage maps |
| Information Security Team | • Define boundary requirements<br>• Review wireless survey results<br>• Approve exceptions and remediation plans |
| Facilities Management | • Coordinate physical boundary assessments<br>• Support antenna placement decisions<br>• Report unauthorized wireless devices |

## 4. RULES
[RULE-01] All wireless access points MUST use directional or beamforming antennas that limit signal propagation beyond organization-controlled boundaries.
[VALIDATION] IF antenna_type = "omnidirectional" AND boundary_containment = FALSE THEN violation

[RULE-02] Transmission power levels SHALL be calibrated to ensure wireless signals do not exceed -85 dBm at organization boundary perimeters.
[VALIDATION] IF signal_strength_at_boundary > -85_dBm THEN violation

[RULE-03] Wireless surveys MUST be conducted quarterly and whenever new wireless equipment is deployed to validate signal containment.
[VALIDATION] IF days_since_last_survey > 90 OR new_deployment = TRUE AND survey_completed = FALSE THEN violation

[RULE-04] Any wireless signals detected beyond organization boundaries MUST be remediated within 48 hours of discovery.
[VALIDATION] IF signal_beyond_boundary = TRUE AND remediation_time > 48_hours THEN critical_violation

[RULE-05] Wireless equipment configurations MUST be documented including antenna specifications, power settings, and coverage maps.
[VALIDATION] IF wireless_device_deployed = TRUE AND documentation_complete = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Wireless Survey Procedure - Quarterly RF assessment methodology and reporting
- [PROC-02] Antenna Selection and Placement - Technical standards for equipment selection
- [PROC-03] Power Calibration Process - Methods for measuring and adjusting transmission levels
- [PROC-04] Signal Containment Remediation - Response procedures for boundary violations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Bi-annually  
- Triggering events: New facility acquisition, major wireless infrastructure changes, boundary violations

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Access Point Deployment]
IF new_wireless_access_point = TRUE
AND antenna_type = "directional"
AND power_calibration_completed = TRUE
AND boundary_survey_passed = TRUE
THEN compliance = TRUE

[SCENARIO-02: Signal Leakage Detection]
IF wireless_survey_conducted = TRUE
AND signals_detected_beyond_boundary = TRUE
AND remediation_time <= 48_hours
THEN compliance = TRUE

[SCENARIO-03: Omnidirectional Antenna Usage]
IF antenna_type = "omnidirectional"
AND signal_strength_at_boundary <= -85_dBm
AND technical_exception_approved = TRUE
THEN compliance = TRUE

[SCENARIO-04: Overdue Wireless Survey]
IF days_since_last_survey > 90
AND no_new_deployments = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: High Power Transmission]
IF signal_strength_at_boundary > -85_dBm
AND remediation_not_completed = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Radio antennas are selected to reduce signal reception outside boundaries | [RULE-01] |
| Transmission power levels are calibrated to reduce external signal reception | [RULE-02], [RULE-04] |
| Periodic wireless surveys validate signal containment | [RULE-03] |
| Documentation supports antenna and power level decisions | [RULE-05] |
```