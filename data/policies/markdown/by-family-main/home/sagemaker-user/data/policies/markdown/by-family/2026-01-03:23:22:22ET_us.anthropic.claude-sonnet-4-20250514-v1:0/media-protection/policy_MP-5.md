```markdown
# POLICY: MP-5: Media Transport

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-5 |
| NIST Control | MP-5: Media Transport |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | media transport, controlled areas, cryptography, accountability, authorized personnel, documentation |

## 1. POLICY STATEMENT
All system media (digital and non-digital) MUST be protected and controlled during transport outside of controlled areas using approved security measures. The organization SHALL maintain accountability and restrict transport activities to authorized personnel only.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Digital Media | YES | Flash drives, external drives, tapes, CDs, DVDs |
| Non-Digital Media | YES | Microfilm, paper documents with sensitive data |
| Internal Transport | CONDITIONAL | Only when crossing controlled area boundaries |
| External Courier Services | YES | All third-party transport providers |
| Employee Personal Devices | YES | When containing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Custodians | • Classify media before transport<br>• Apply appropriate protection controls<br>• Document transport activities |
| Transport Coordinators | • Verify personnel authorization<br>• Maintain transport accountability records<br>• Coordinate with approved courier services |
| Security Operations | • Monitor transport compliance<br>• Investigate transport incidents<br>• Maintain authorized personnel lists |

## 4. RULES
[RULE-01] System media containing sensitive data MUST be encrypted using FIPS 140-2 Level 2 or higher approved cryptographic modules before transport outside controlled areas.
[VALIDATION] IF media_classification >= "Internal" AND transport_destination = "outside_controlled_area" AND encryption_status = FALSE THEN critical_violation

[RULE-02] Physical transport containers MUST be locked and tamper-evident when transporting unencrypted media or media classified as Confidential or above.
[VALIDATION] IF media_classification >= "Confidential" AND encryption_status = FALSE AND container_locked = FALSE THEN violation

[RULE-03] Media transport activities MUST be restricted to personnel specifically authorized in the current Media Transport Authorization List.
[VALIDATION] IF transport_personnel NOT IN authorized_transport_list THEN violation

[RULE-04] All media transport activities MUST be documented with chain of custody records including sender, recipient, transport method, and completion verification.
[VALIDATION] IF transport_occurred = TRUE AND documentation_complete = FALSE THEN violation

[RULE-05] Media accountability MUST be maintained through tracking mechanisms that provide real-time location status during transport.
[VALIDATION] IF transport_duration > 24_hours AND tracking_status = "unknown" THEN violation

[RULE-06] External courier services MUST be pre-approved and maintain appropriate security certifications for handling organizational data.
[VALIDATION] IF courier_service = "external" AND approval_status = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Classification and Marking - Classify and label media before transport
- [PROC-02] Encryption Key Management - Manage cryptographic keys for media protection
- [PROC-03] Chain of Custody Documentation - Document all transport activities and handoffs
- [PROC-04] Personnel Authorization Management - Maintain and update authorized transport personnel lists
- [PROC-05] Incident Response for Media Loss - Respond to lost or compromised media during transport

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving media transport, changes to data classification scheme, new transport methods or vendors

## 7. SCENARIO PATTERNS
[SCENARIO-01: Encrypted Laptop Transport]
IF device_type = "laptop"
AND data_classification = "Confidential"
AND encryption_enabled = TRUE
AND transport_personnel IN authorized_list
THEN compliance = TRUE

[SCENARIO-02: Unencrypted Backup Tape]
IF media_type = "backup_tape"
AND data_classification = "Internal"
AND encryption_status = FALSE
AND transport_destination = "offsite_storage"
AND locked_container = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Unauthorized Courier Service]
IF transport_method = "external_courier"
AND courier_approval_status = FALSE
AND media_classification >= "Internal"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Missing Documentation]
IF transport_completed = TRUE
AND chain_of_custody_complete = FALSE
AND transport_date > 7_days_ago
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Personal Device with Company Data]
IF device_ownership = "personal"
AND contains_company_data = TRUE
AND transport_authorization = FALSE
AND data_classification >= "Internal"
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Media types defined and protected during transport | RULE-01, RULE-02 |
| Controls used to protect media are defined | RULE-01, RULE-02 |
| Media controlled during transport outside controlled areas | RULE-03, RULE-06 |
| Accountability maintained during transport | RULE-05 |
| Transport activities documented | RULE-04 |
| Authorized personnel identified | RULE-03 |
| Activities restricted to authorized personnel | RULE-03 |
```