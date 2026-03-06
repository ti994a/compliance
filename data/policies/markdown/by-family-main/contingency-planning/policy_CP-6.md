# POLICY: CP-6: Alternate Storage Site

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CP-6 |
| NIST Control | CP-6: Alternate Storage Site |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | alternate storage, backup, contingency planning, disaster recovery, geographically distributed, storage agreements |

## 1. POLICY STATEMENT
The organization SHALL establish and maintain alternate storage sites that are geographically distinct from primary storage sites to ensure continuity of operations during disruptions. Alternate storage sites MUST provide security controls equivalent to primary sites and operate under formal agreements that govern storage and retrieval of backup information.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud and hybrid environments |
| Backup storage facilities | YES | Primary and alternate locations |
| Third-party storage providers | YES | When used for backup storage |
| Development/test systems | CONDITIONAL | Only if containing production data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve alternate storage site strategy<br>• Ensure policy compliance<br>• Review storage site agreements |
| IT Operations Manager | • Establish alternate storage sites<br>• Negotiate storage agreements<br>• Coordinate backup/retrieval operations<br>• Monitor site security controls |
| Business Continuity Manager | • Align storage sites with contingency plans<br>• Test backup retrieval procedures<br>• Validate recovery time objectives |

## 4. RULES
[RULE-01] Organizations MUST establish alternate storage sites that are geographically separated from primary storage sites by a minimum distance that prevents both sites from being affected by the same localized disaster.
[VALIDATION] IF primary_site_location = alternate_site_location OR geographic_distance < minimum_separation_distance THEN violation

[RULE-02] Formal agreements MUST be established with alternate storage site providers that specify storage capacity, environmental conditions, access procedures, and retrieval timeframes.
[VALIDATION] IF alternate_storage_site_exists = TRUE AND formal_agreement_exists = FALSE THEN violation

[RULE-03] Alternate storage sites SHALL implement security controls equivalent to those at the primary storage site, including physical security, environmental controls, and access restrictions.
[VALIDATION] IF alternate_site_control_assessment < primary_site_control_baseline THEN violation

[RULE-04] System backup information MUST be stored at alternate sites within 24 hours of creation for critical systems and within 72 hours for non-critical systems.
[VALIDATION] IF system_criticality = "critical" AND backup_transfer_time > 24_hours THEN violation
[VALIDATION] IF system_criticality = "non-critical" AND backup_transfer_time > 72_hours THEN violation

[RULE-05] Backup retrieval procedures MUST be tested at least annually to verify accessibility and integrity of stored information.
[VALIDATION] IF last_retrieval_test_date > 365_days_ago THEN violation

[RULE-06] Environmental conditions at alternate storage sites MUST meet or exceed manufacturer specifications for stored media and equipment.
[VALIDATION] IF environmental_conditions < manufacturer_specifications THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Alternate Storage Site Selection - Geographic risk assessment and site evaluation process
- [PROC-02] Storage Agreement Management - Contract negotiation and maintenance procedures
- [PROC-03] Backup Transfer Operations - Automated and manual backup transportation procedures
- [PROC-04] Retrieval Testing - Regular testing of backup accessibility and integrity
- [PROC-05] Security Control Assessment - Periodic evaluation of alternate site security measures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or after significant changes
- Triggering events: Natural disasters, security incidents affecting storage sites, changes in business requirements, vendor changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Inadequate Geographic Separation]
IF primary_storage_site_location = "Building A"
AND alternate_storage_site_location = "Building B, same campus"
AND geographic_distance < 25_miles
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Storage Agreement]
IF alternate_storage_site_established = TRUE
AND formal_written_agreement = FALSE
AND storage_terms_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Delayed Backup Transfer]
IF system_classification = "critical"
AND backup_creation_time = "2024-01-01 09:00"
AND alternate_site_arrival_time = "2024-01-03 10:00"
AND transfer_duration > 24_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Equivalent Controls Validation]
IF primary_site_security_rating = "High"
AND alternate_site_security_rating = "Medium"
AND control_equivalency_assessment = "Not_Equivalent"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Successful Retrieval Test]
IF retrieval_test_conducted = TRUE
AND test_date = "within_365_days"
AND backup_integrity_verified = TRUE
AND retrieval_time_within_rto = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Alternate storage site is established | [RULE-01], [RULE-02] |
| Necessary agreements permit storage and retrieval | [RULE-02], [RULE-04] |
| Alternate site provides equivalent controls | [RULE-03], [RULE-06] |
| Backup information storage and retrieval capability | [RULE-04], [RULE-05] |