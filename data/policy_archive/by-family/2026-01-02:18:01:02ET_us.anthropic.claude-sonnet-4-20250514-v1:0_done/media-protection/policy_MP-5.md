# POLICY: MP-5: Media Transport

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-5 |
| NIST Control | MP-5: Media Transport |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | media transport, controlled areas, accountability, documentation, authorized personnel, cryptography, physical protection |

## 1. POLICY STATEMENT
All system media must be protected and controlled during transport outside controlled areas using approved security measures. The organization shall maintain accountability and documentation for all media transport activities, restricting such activities to authorized personnel only.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Digital Media | YES | Flash drives, external drives, tapes, CDs, DVDs |
| Non-Digital Media | YES | Paper documents, microfilm containing system data |
| Internal Transfers | CONDITIONAL | Only when crossing controlled area boundaries |
| Third-Party Couriers | YES | Must be pre-authorized and tracked |
| Personal Devices | YES | When containing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Media Custodian | • Approve media transport requests<br>• Maintain transport documentation<br>• Verify encryption and container requirements |
| Authorized Transport Personnel | • Follow transport procedures<br>• Maintain chain of custody<br>• Report incidents immediately |
| Security Officer | • Define controlled areas<br>• Authorize transport personnel<br>• Review transport logs |

## 4. RULES
[RULE-01] All system media containing sensitive data MUST be encrypted using FIPS 140-2 Level 2 approved encryption before transport outside controlled areas.
[VALIDATION] IF media_location = "outside_controlled_area" AND encryption_status = "unencrypted" AND data_classification >= "sensitive" THEN critical_violation

[RULE-02] Physical media transport MUST use locked, tamper-evident containers when encryption alone is insufficient for data classification level.
[VALIDATION] IF data_classification = "confidential" OR data_classification = "secret" AND container_type != "locked_tamper_evident" THEN violation

[RULE-03] Media transport activities MUST be restricted to personnel specifically authorized in the current transport authorization list.
[VALIDATION] IF transport_personnel NOT IN authorized_transport_list THEN critical_violation

[RULE-04] All media transport outside controlled areas MUST be documented with chain of custody records including departure time, destination, courier identity, and expected delivery time.
[VALIDATION] IF transport_location = "outside_controlled_area" AND (departure_time = NULL OR destination = NULL OR courier_id = NULL) THEN violation

[RULE-05] Media accountability MUST be maintained through continuous tracking or periodic verification at intervals not exceeding 24 hours during transport.
[VALIDATION] IF last_verification_time > 24_hours AND transport_status = "in_transit" THEN violation

[RULE-06] Transport incidents including delays exceeding 4 hours, route deviations, or custody transfers MUST be reported to the Security Operations Center within 2 hours of discovery.
[VALIDATION] IF (delay > 4_hours OR route_deviation = TRUE OR custody_transfer = TRUE) AND incident_report_time > 2_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Transport Authorization - Pre-approval process for all media leaving controlled areas
- [PROC-02] Chain of Custody Documentation - Standardized forms and tracking requirements
- [PROC-03] Authorized Personnel Management - Vetting, training, and authorization maintenance
- [PROC-04] Incident Response for Transport - Procedures for handling transport security events
- [PROC-05] Controlled Area Definition - Criteria and boundaries for controlled vs uncontrolled areas

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, regulatory changes, technology updates, organizational restructuring

## 7. SCENARIO PATTERNS
[SCENARIO-01: Encrypted Backup Tape Transport]
IF media_type = "backup_tape"
AND encryption_status = "FIPS_140-2_compliant"
AND transport_personnel IN authorized_list
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-02: Unencrypted Laptop Transport]
IF media_type = "laptop"
AND encryption_status = "unencrypted"
AND data_classification = "confidential"
AND location = "outside_controlled_area"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Unauthorized Courier Usage]
IF courier_id NOT IN authorized_transport_list
AND media_classification >= "sensitive"
AND transport_status = "active"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Missing Chain of Custody]
IF transport_distance > controlled_area_boundary
AND departure_time = documented
AND courier_verification = NULL
AND tracking_interval > 24_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Delayed Incident Reporting]
IF transport_delay = 6_hours
AND incident_discovery_time = "10:00"
AND incident_report_time = "13:30"
AND required_report_time = "12:00"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Media types and protection controls defined | RULE-01, RULE-02 |
| Media protected during transport | RULE-01, RULE-02 |
| Media controlled during transport | RULE-03, RULE-05 |
| Accountability maintained during transport | RULE-04, RULE-05 |
| Transport activities documented | RULE-04, RULE-06 |
| Transport restricted to authorized personnel | RULE-03 |