# POLICY: SC-28.3: Cryptographic Keys

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-28.3 |
| NIST Control | SC-28.3: Cryptographic Keys |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptographic keys, protected storage, hardware security modules, TPM, key management |

## 1. POLICY STATEMENT
All cryptographic keys used by organizational systems MUST be stored in hardware-protected storage mechanisms that provide tamper resistance and secure key isolation. Software-based key storage is prohibited for production systems handling sensitive data.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing regulated data |
| Development Systems | CONDITIONAL | Required if handling production keys |
| Test Systems | NO | Unless using production data copies |
| Cloud Services | YES | Must use cloud HSM or equivalent |
| Mobile Applications | YES | Must use device secure enclaves |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve hardware-protected storage solutions<br>• Define key protection requirements<br>• Oversee policy compliance |
| Security Architecture Team | • Design key storage architectures<br>• Validate hardware protection mechanisms<br>• Review system implementations |
| System Administrators | • Configure hardware security modules<br>• Implement key storage controls<br>• Monitor key access activities |

## 4. RULES

[RULE-01] All cryptographic keys MUST be stored exclusively in hardware-protected storage mechanisms such as Hardware Security Modules (HSMs), Trusted Platform Modules (TPMs), or cloud-native HSM services.
[VALIDATION] IF key_storage_type != "hardware_protected" THEN critical_violation

[RULE-02] Software-based key storage (including file systems, databases, or configuration files) MUST NOT be used for production cryptographic keys.
[VALIDATION] IF key_location IN ["filesystem", "database", "config_file"] AND environment = "production" THEN critical_violation

[RULE-03] Hardware-protected storage solutions MUST provide tamper resistance and secure key isolation capabilities verified through FIPS 140-2 Level 2 or higher certification.
[VALIDATION] IF hardware_certification_level < "FIPS_140-2_Level_2" THEN major_violation

[RULE-04] Cloud-based systems MUST utilize cloud provider HSM services or dedicated HSM instances rather than software-based key management.
[VALIDATION] IF deployment_type = "cloud" AND key_service_type != "HSM" THEN major_violation

[RULE-05] Key extraction from hardware-protected storage MUST be logged and monitored through security information and event management (SIEM) systems.
[VALIDATION] IF key_access_logged = FALSE OR siem_monitoring = FALSE THEN moderate_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Hardware Security Module Procurement - Evaluation and acquisition of FIPS-validated HSM solutions
- [PROC-02] Key Migration to Protected Storage - Secure transfer of existing keys to hardware-protected storage
- [PROC-03] HSM Configuration Management - Standardized setup and maintenance of hardware protection mechanisms
- [PROC-04] Key Access Monitoring - Continuous monitoring and alerting for key usage activities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New system deployments, security incidents involving keys, technology changes, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Production Key in Database]
IF key_storage_location = "database"
AND environment = "production"
AND data_classification = "sensitive"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Cloud HSM Implementation]
IF deployment_type = "cloud"
AND key_service = "AWS_CloudHSM"
AND fips_validated = TRUE
THEN compliance = TRUE

[SCENARIO-03: Development Environment Exception]
IF environment = "development"
AND production_data = FALSE
AND key_storage_type = "software"
THEN compliance = TRUE

[SCENARIO-04: Mobile App Secure Enclave]
IF application_type = "mobile"
AND key_storage = "secure_enclave"
AND hardware_backed = TRUE
THEN compliance = TRUE

[SCENARIO-05: Legacy System Migration]
IF system_age > 5_years
AND key_storage_type = "software"
AND migration_plan_approved = FALSE
AND current_date > compliance_deadline
THEN compliance = FALSE
violation_severity = "Major"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Protected storage for cryptographic keys is provided using hardware-protected mechanisms | RULE-01, RULE-03 |
| Software-based key storage is prohibited for production systems | RULE-02 |
| Cloud systems implement appropriate HSM solutions | RULE-04 |
| Key access activities are monitored and logged | RULE-05 |