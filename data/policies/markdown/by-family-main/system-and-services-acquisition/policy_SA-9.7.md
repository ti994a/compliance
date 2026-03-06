# POLICY: SA-9.7: Organization-controlled Integrity Checking

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-9.7 |
| NIST Control | SA-9.7: Organization-controlled Integrity Checking |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | integrity checking, external systems, data validation, third-party services, cloud storage |

## 1. POLICY STATEMENT
The organization MUST implement capabilities to verify the integrity of organizational information stored in external systems without requiring data transfer. All external service providers MUST provide integrity checking mechanisms that allow real-time validation of data authenticity and completeness.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Cloud storage services | YES | All organizational data stored externally |
| SaaS applications | YES | Applications processing organizational data |
| Third-party data centers | YES | Physical hosting of organizational systems |
| Backup service providers | YES | External backup and archival services |
| Internal systems | NO | Covered under separate integrity controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve integrity checking requirements for external services<br>• Review integrity validation reports<br>• Ensure compliance with regulatory requirements |
| IT Security Manager | • Implement integrity checking mechanisms<br>• Monitor integrity validation results<br>• Coordinate with external service providers |
| Vendor Management | • Include integrity checking requirements in contracts<br>• Validate provider integrity capabilities<br>• Manage service level agreements for integrity checking |

## 4. RULES
[RULE-01] External service providers MUST provide real-time integrity checking capabilities that can be controlled and monitored by the organization.
[VALIDATION] IF external_service = TRUE AND integrity_checking_capability = FALSE THEN critical_violation

[RULE-02] Integrity checking MUST be performed at least every 24 hours for critical data and every 7 days for standard data stored in external systems.
[VALIDATION] IF data_classification = "critical" AND last_integrity_check > 24_hours THEN violation
[VALIDATION] IF data_classification = "standard" AND last_integrity_check > 7_days THEN violation

[RULE-03] All integrity checking mechanisms MUST use cryptographic hash functions approved by NIST (SHA-256 or higher).
[VALIDATION] IF integrity_method NOT IN ["SHA-256", "SHA-384", "SHA-512", "SHA-3"] THEN violation

[RULE-04] Integrity validation failures MUST trigger automated alerts within 15 minutes of detection.
[VALIDATION] IF integrity_failure = TRUE AND alert_time > 15_minutes THEN violation

[RULE-05] External service contracts MUST include specific integrity checking requirements and performance metrics with penalties for non-compliance.
[VALIDATION] IF external_contract = TRUE AND integrity_requirements_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Service Integrity Assessment - Evaluate and validate integrity capabilities before service adoption
- [PROC-02] Continuous Integrity Monitoring - Implement automated monitoring of integrity checking results
- [PROC-03] Integrity Failure Response - Define response procedures for integrity validation failures
- [PROC-04] Vendor Integrity Compliance Review - Regular assessment of provider integrity capabilities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New external service adoption, integrity failure incidents, regulatory changes, contract renewals

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Storage Integrity Failure]
IF service_type = "cloud_storage"
AND integrity_check_result = "FAILED"
AND alert_generated = FALSE
AND time_elapsed > 15_minutes
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unapproved Hash Algorithm]
IF external_service = TRUE
AND integrity_method = "MD5"
AND data_classification = "sensitive"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Missing Contract Requirements]
IF new_external_service = TRUE
AND contract_signed = TRUE
AND integrity_requirements_specified = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Delayed Critical Data Validation]
IF data_classification = "critical"
AND storage_location = "external"
AND last_integrity_check > 48_hours
AND system_availability = "operational"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Compliant Integrity Checking]
IF external_service = TRUE
AND integrity_checking_enabled = TRUE
AND hash_algorithm IN ["SHA-256", "SHA-384", "SHA-512"]
AND last_check_time <= required_frequency
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Capability to check integrity while data resides in external system | [RULE-01] |
| Regular integrity validation frequency | [RULE-02] |
| Approved cryptographic methods | [RULE-03] |
| Timely failure detection and alerting | [RULE-04] |
| Contractual integrity requirements | [RULE-05] |