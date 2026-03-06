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
The organization MUST maintain the capability to verify and validate the integrity of organizational information while it resides in external systems without requiring data transfer. This capability ensures continuous visibility into data security status across all external service arrangements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Cloud storage services | YES | All organizational data stored externally |
| SaaS applications | YES | Business-critical applications only |
| Third-party data centers | YES | Colocation and managed services |
| Partner systems | CONDITIONAL | When storing organizational data |
| Backup services | YES | All external backup arrangements |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Establish integrity checking requirements<br>• Approve external system arrangements<br>• Review integrity validation reports |
| IT Security Team | • Implement integrity checking mechanisms<br>• Monitor integrity validation processes<br>• Investigate integrity anomalies |
| Procurement Team | • Include integrity checking requirements in contracts<br>• Validate vendor capabilities during acquisition<br>• Ensure SLA compliance |

## 4. RULES
[RULE-01] All external systems storing organizational data MUST provide real-time integrity checking capabilities that can be controlled and monitored by the organization.
[VALIDATION] IF external_system_stores_org_data = TRUE AND integrity_checking_capability = FALSE THEN critical_violation

[RULE-02] Integrity checking mechanisms MUST be implemented before organizational data is stored in any external system.
[VALIDATION] IF data_stored_externally = TRUE AND integrity_mechanism_implemented = FALSE THEN critical_violation

[RULE-03] External service providers MUST allow organizational access to integrity validation tools and reports without requiring data extraction or transfer.
[VALIDATION] IF provider_blocks_integrity_access = TRUE OR requires_data_transfer_for_validation = TRUE THEN violation

[RULE-04] Integrity checking capabilities MUST be validated during the acquisition process and documented in service agreements.
[VALIDATION] IF external_service_contract = TRUE AND integrity_capability_validated = FALSE THEN violation

[RULE-05] Integrity validation MUST be performed at least daily for business-critical data and weekly for standard organizational data.
[VALIDATION] IF data_criticality = "business_critical" AND validation_frequency > 24_hours THEN violation
[VALIDATION] IF data_criticality = "standard" AND validation_frequency > 168_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External System Integrity Assessment - Evaluate and document integrity checking capabilities before data placement
- [PROC-02] Continuous Integrity Monitoring - Establish automated monitoring of data integrity in external systems
- [PROC-03] Integrity Anomaly Response - Define response procedures for detected integrity violations
- [PROC-04] Vendor Capability Validation - Verify external provider integrity checking capabilities during procurement

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New external service adoption, integrity violation incidents, contract renewals

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Storage Without Integrity Checking]
IF system_type = "external_cloud_storage"
AND organizational_data_present = TRUE
AND integrity_checking_enabled = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: SaaS Application with Limited Validation Access]
IF service_type = "SaaS_application"
AND business_critical_data = TRUE
AND provider_allows_integrity_access = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Compliant External Backup Service]
IF service_type = "external_backup"
AND real_time_integrity_checking = TRUE
AND organization_controlled_validation = TRUE
AND validation_frequency <= 24_hours
THEN compliance = TRUE

[SCENARIO-04: New External Service Without Assessment]
IF external_service_deployment = "new"
AND integrity_capability_assessment = "not_performed"
AND organizational_data_migration = "planned"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Partner System Data Sharing]
IF system_type = "partner_system"
AND data_sharing_agreement = TRUE
AND integrity_checking_capability = FALSE
AND data_sensitivity = "confidential"
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Capability to check integrity of information in external systems | [RULE-01], [RULE-02] |
| Organization-controlled validation without data transfer | [RULE-03] |
| Continuous monitoring of external data integrity | [RULE-05] |
| Pre-deployment integrity capability validation | [RULE-04] |