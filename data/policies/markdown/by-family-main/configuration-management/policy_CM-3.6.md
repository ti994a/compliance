# POLICY: CM-3.6: Cryptography Management

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-3.6 |
| NIST Control | CM-3.6: Cryptography Management |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cryptography, configuration management, certificates, encryption, key management |

## 1. POLICY STATEMENT
All cryptographic mechanisms used to implement security and privacy controls SHALL be subject to formal configuration management processes. The organization MUST maintain documented procedures for managing the lifecycle of cryptographic implementations including deployment, updates, and retirement.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Cryptographic software | YES | All encryption applications and libraries |
| Digital certificates | YES | Including SSL/TLS, code signing, authentication |
| Hardware security modules | YES | HSMs and crypto accelerators |
| Cryptographic keys | YES | All symmetric and asymmetric keys |
| Legacy crypto systems | YES | Must be tracked for deprecation |
| Development environments | CONDITIONAL | If using production crypto mechanisms |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Cryptography Officer | • Define cryptographic standards and approved mechanisms<br>• Oversee crypto configuration management processes<br>• Approve cryptographic mechanism changes |
| Configuration Manager | • Implement CM processes for crypto mechanisms<br>• Maintain crypto asset inventory<br>• Coordinate crypto mechanism updates |
| System Administrators | • Deploy approved cryptographic mechanisms<br>• Monitor crypto mechanism status<br>• Report crypto-related incidents |

## 4. RULES
[RULE-01] All cryptographic mechanisms implementing organizational security controls MUST be documented in the configuration management database with baseline configurations.
[VALIDATION] IF crypto_mechanism_deployed = TRUE AND cmdb_entry_exists = FALSE THEN violation

[RULE-02] Changes to cryptographic mechanisms MUST follow the formal change control process including impact assessment and approval.
[VALIDATION] IF crypto_change_implemented = TRUE AND change_control_approval = FALSE THEN critical_violation

[RULE-03] Digital certificates MUST be renewed at least 30 days before expiration with automated monitoring for certificates expiring within 60 days.
[VALIDATION] IF certificate_expiry_date <= (current_date + 30_days) AND renewal_initiated = FALSE THEN violation

[RULE-04] Cryptographic mechanism inventories MUST be reviewed and validated quarterly with discrepancies resolved within 15 business days.
[VALIDATION] IF last_crypto_inventory_date > (current_date - 90_days) THEN violation

[RULE-05] Deprecated cryptographic algorithms MUST be identified and replaced according to the approved migration timeline with no new implementations permitted.
[VALIDATION] IF crypto_algorithm IN deprecated_list AND implementation_date > deprecation_date THEN critical_violation

[RULE-06] All cryptographic mechanisms MUST have documented rollback procedures tested annually.
[VALIDATION] IF crypto_mechanism_active = TRUE AND (rollback_procedure_exists = FALSE OR last_test_date > (current_date - 365_days)) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Cryptographic Asset Discovery - Automated scanning and manual verification of crypto mechanisms
- [PROC-02] Certificate Lifecycle Management - Enrollment, renewal, revocation, and monitoring processes
- [PROC-03] Cryptographic Change Control - Assessment, testing, and deployment procedures for crypto changes
- [PROC-04] Emergency Crypto Response - Procedures for crypto vulnerabilities and compromise incidents

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Crypto vulnerabilities, algorithm deprecation, regulatory changes, security incidents

## 7. SCENARIO PATTERNS
[SCENARIO-01: Expired Certificate in Production]
IF certificate_status = "expired"
AND system_environment = "production"
AND business_impact = "service_disruption"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Unapproved Cryptographic Library]
IF crypto_library_deployed = TRUE
AND approval_status = "not_approved"
AND configuration_managed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Crypto Inventory Entry]
IF cryptographic_mechanism = "active"
AND cmdb_entry = "missing"
AND discovery_date > 30_days_ago
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Deprecated Algorithm in Use]
IF algorithm_type IN ["MD5", "SHA1", "DES", "3DES"]
AND implementation_date > algorithm_deprecation_date
AND migration_plan = "not_executed"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Crypto Change Without Approval]
IF cryptographic_change = "implemented"
AND change_control_board_approval = FALSE
AND emergency_justification = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Cryptographic mechanisms under configuration management | RULE-01, RULE-04 |
| Defined controls provided by cryptographic mechanisms | RULE-01, RULE-05 |
| Change control for cryptographic mechanisms | RULE-02, RULE-06 |
| Certificate management processes | RULE-03 |
| Inventory and tracking procedures | RULE-04 |