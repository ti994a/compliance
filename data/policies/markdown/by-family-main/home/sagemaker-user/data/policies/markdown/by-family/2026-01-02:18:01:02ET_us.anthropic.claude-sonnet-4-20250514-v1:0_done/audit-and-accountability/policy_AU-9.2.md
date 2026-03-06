# POLICY: AU-9.2: Store on Separate Physical Systems or Components

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AU-9.2 |
| NIST Control | AU-9.2: Store on Separate Physical Systems or Components |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | audit records, physical separation, repository, backup storage, audit integrity |

## 1. POLICY STATEMENT
All audit records MUST be stored in repositories that are physically separate from the systems or components being audited. This separation applies to both initial generation and long-term storage of audit records to preserve confidentiality and integrity.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems generating audit logs |
| Development Systems | YES | Systems processing regulated data |
| Test Environments | CONDITIONAL | Only if processing production data |
| Network Infrastructure | YES | Routers, switches, firewalls |
| Cloud Services | YES | Must comply with physical separation requirements |
| Third-Party Systems | CONDITIONAL | If organization controls audit storage |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve audit storage architecture<br>• Ensure policy compliance across organization<br>• Define physical separation requirements |
| System Administrators | • Configure audit forwarding to separate repositories<br>• Maintain physical separation of storage systems<br>• Monitor audit storage capacity and health |
| Security Operations | • Verify audit record integrity<br>• Monitor for audit storage failures<br>• Manage access to audit repositories |

## 4. RULES
[RULE-01] Audit records MUST be stored on physically separate systems or components from the systems being audited within 15 minutes of generation.
[VALIDATION] IF audit_source_system = audit_storage_system THEN violation
[VALIDATION] IF storage_delay > 15_minutes THEN violation

[RULE-02] Audit storage repositories MUST NOT share physical infrastructure (servers, storage arrays, network segments) with audited systems.
[VALIDATION] IF shared_physical_infrastructure = TRUE THEN critical_violation

[RULE-03] Backup audit records MUST be stored on systems physically separate from both the audited system and the primary audit repository.
[VALIDATION] IF backup_location = primary_audit_location OR backup_location = audited_system_location THEN violation

[RULE-04] Cloud-based audit storage MUST utilize different availability zones or regions from the audited cloud resources.
[VALIDATION] IF cloud_audit_zone = cloud_system_zone AND geographic_separation < 50_miles THEN violation

[RULE-05] Physical separation requirements MUST be documented and validated quarterly through infrastructure reviews.
[VALIDATION] IF last_validation_date > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Audit Repository Architecture Review - Quarterly validation of physical separation requirements
- [PROC-02] Audit Forwarding Configuration - Standard process for configuring systems to forward logs to separate repositories
- [PROC-03] Emergency Audit Recovery - Procedures for recovering audit records from separate storage during incidents

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Infrastructure changes, cloud migrations, security incidents affecting audit systems, regulatory requirement updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Shared Storage Infrastructure]
IF audited_system_storage = "SAN_Array_1"
AND audit_repository_storage = "SAN_Array_1"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Cloud Same-Zone Storage]
IF audited_system_location = "AWS_US-East-1a"
AND audit_storage_location = "AWS_US-East-1a"
AND service_type = "cloud"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Proper Physical Separation]
IF audited_system_building = "DataCenter_A"
AND audit_repository_building = "DataCenter_B"
AND shared_infrastructure = FALSE
THEN compliance = TRUE

[SCENARIO-04: Backup Co-location Violation]
IF primary_audit_location = "Site_1"
AND backup_audit_location = "Site_1"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Delayed Audit Forwarding]
IF audit_generation_time = "10:00:00"
AND audit_storage_time = "10:20:00"
AND time_difference > 15_minutes
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Store audit records in physically separate repository | [RULE-01], [RULE-02] |
| Maintain separation for backup storage | [RULE-03] |
| Ensure cloud service separation | [RULE-04] |
| Document and validate separation requirements | [RULE-05] |