# POLICY: CP-9.3: Separate Storage for Critical Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CP-9.3 |
| NIST Control | CP-9.3: Separate Storage for Critical Information |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | backup, separate storage, critical information, fire rated container, geographically distributed |

## 1. POLICY STATEMENT
Critical system software and security-related information backups MUST be stored in facilities that are separate from operational systems or in fire-rated containers that are not collocated with primary systems. This ensures availability of critical information during disasters or incidents affecting primary facilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical system software | YES | Operating systems, middleware, cryptographic key management systems |
| Security-related information | YES | Hardware/software inventories, firmware components |
| All backup storage media | YES | Regardless of media type |
| Operational systems | YES | Primary production systems requiring backup separation |
| Third-party hosted systems | CONDITIONAL | When organization controls backup strategy |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define critical information categories<br>• Approve separate storage locations<br>• Ensure policy compliance |
| IT Operations Manager | • Implement backup separation procedures<br>• Maintain backup storage documentation<br>• Monitor backup storage compliance |
| Facility Security Manager | • Validate fire-rated container specifications<br>• Assess physical separation adequacy<br>• Coordinate alternate site arrangements |

## 4. RULES
[RULE-01] Critical system software backups MUST be stored in facilities physically separated from operational systems by at least 10 miles or in GSA-approved fire-rated containers.
[VALIDATION] IF backup_type = "critical_system_software" AND (distance_from_primary < 10_miles AND fire_rated_container = FALSE) THEN violation

[RULE-02] Security-related information backups MUST NOT be collocated with their corresponding operational systems.
[VALIDATION] IF backup_contains_security_info = TRUE AND same_facility_as_primary = TRUE THEN violation

[RULE-03] Fire-rated containers used for backup storage MUST meet GSA standards and specifications for security and fire protection.
[VALIDATION] IF storage_method = "fire_rated_container" AND gsa_certified = FALSE THEN violation

[RULE-04] Automated backup processes to geographically distributed sites MUST maintain minimum 50-mile separation from primary data centers.
[VALIDATION] IF automated_backup = TRUE AND geographic_distance < 50_miles THEN violation

[RULE-05] Organizations MUST maintain documentation of all separate storage locations and their contents.
[VALIDATION] IF separate_storage_location EXISTS AND documentation_current = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Critical Information Classification - Process to identify and classify critical system software and security-related information
- [PROC-02] Separate Storage Site Selection - Criteria and process for selecting alternate storage facilities
- [PROC-03] Fire-Rated Container Certification - Validation process for GSA-compliant storage containers
- [PROC-04] Backup Separation Verification - Regular auditing of backup storage separation compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New critical systems deployment, facility changes, disaster recovery incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Collocated Critical Backups]
IF backup_type = "critical_system_software"
AND storage_location = primary_facility
AND fire_rated_container = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Compliant Fire-Rated Storage]
IF backup_type = "security_related_information"
AND fire_rated_container = TRUE
AND gsa_certified = TRUE
AND collocated_with_primary = TRUE
THEN compliance = TRUE

[SCENARIO-03: Insufficient Geographic Separation]
IF automated_backup = TRUE
AND alternate_site_distance = 25_miles
AND fire_rated_container = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Undocumented Separate Storage]
IF separate_storage_facility EXISTS
AND backup_inventory_documented = FALSE
AND storage_location_documented = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Third-Party Backup Compliance]
IF backup_provider = "third_party"
AND separation_verified = TRUE
AND contract_specifies_separation = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Backup copies stored in separate facility | [RULE-01], [RULE-02] |
| Fire-rated container specifications | [RULE-03] |
| Geographic distribution requirements | [RULE-04] |
| Documentation of storage locations | [RULE-05] |