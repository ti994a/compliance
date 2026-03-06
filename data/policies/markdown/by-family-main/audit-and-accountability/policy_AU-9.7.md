# POLICY: AU-9.7: Store on Component with Different Operating System

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AU-9.7 |
| NIST Control | AU-9.7: Store on Component with Different Operating System |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | audit storage, operating system diversity, audit protection, log segregation, cross-platform |

## 1. POLICY STATEMENT
Audit information MUST be stored on components running different operating systems than the systems or components being audited. This requirement ensures audit record integrity by reducing the risk of operating system-specific vulnerabilities compromising audit data.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems generating audit logs |
| Development Systems | YES | When processing sensitive data |
| Test Systems | CONDITIONAL | Only when containing production data |
| Audit Storage Systems | YES | All components storing audit information |
| Cloud Infrastructure | YES | Includes managed services and containers |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure audit forwarding to heterogeneous storage<br>• Maintain OS diversity mapping<br>• Monitor audit storage connectivity |
| Security Operations | • Validate OS diversity compliance<br>• Monitor audit storage integrity<br>• Investigate audit storage failures |
| Cloud Engineers | • Design multi-OS audit architectures<br>• Implement cross-platform log forwarding<br>• Maintain audit storage redundancy |

## 4. RULES
[RULE-01] Audit information MUST be stored on components running different operating systems than the source systems being audited.
[VALIDATION] IF source_os = audit_storage_os THEN violation

[RULE-02] Operating system diversity verification MUST be documented and maintained for all audit storage configurations.
[VALIDATION] IF os_diversity_documented = FALSE OR documentation_age > 90_days THEN violation

[RULE-03] Audit forwarding to heterogeneous storage MUST be configured within 24 hours of system deployment.
[VALIDATION] IF system_deployed = TRUE AND audit_forwarding_configured = FALSE AND hours_since_deployment > 24 THEN violation

[RULE-04] OS diversity compliance MUST be verified quarterly through automated scanning and manual validation.
[VALIDATION] IF last_diversity_check > 90_days THEN violation

[RULE-05] Backup audit storage systems MUST also maintain operating system diversity from both source and primary storage systems.
[VALIDATION] IF backup_os = source_os OR backup_os = primary_storage_os THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] OS Diversity Assessment - Quarterly verification of operating system differences between audit sources and storage
- [PROC-02] Audit Storage Configuration - Standard process for configuring cross-platform audit forwarding
- [PROC-03] Diversity Compliance Monitoring - Continuous monitoring of OS diversity requirements
- [PROC-04] Exception Management - Process for handling temporary diversity violations during maintenance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New system deployments, OS upgrades, audit storage changes, security incidents involving audit systems

## 7. SCENARIO PATTERNS
[SCENARIO-01: Same OS Audit Storage]
IF source_system_os = "Windows Server 2019"
AND audit_storage_os = "Windows Server 2022"
AND os_family = "Windows"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Compliant Cross-Platform Setup]
IF source_system_os = "RHEL 8"
AND audit_storage_os = "Windows Server 2019"
AND audit_forwarding_active = TRUE
THEN compliance = TRUE

[SCENARIO-03: Container Platform Diversity]
IF source_container_host_os = "Ubuntu"
AND audit_storage_os = "Windows"
AND log_forwarding_configured = TRUE
THEN compliance = TRUE

[SCENARIO-04: Cloud Service Audit Storage]
IF source_system_os = "Amazon Linux"
AND audit_storage_service = "Azure Log Analytics"
AND underlying_storage_os ≠ "Amazon Linux"
THEN compliance = TRUE

[SCENARIO-05: Backup Storage Violation]
IF primary_storage_os = "CentOS"
AND backup_storage_os = "RHEL"
AND os_kernel_family = "Linux"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Audit information stored on different OS component | RULE-01, RULE-05 |
| OS diversity documentation and verification | RULE-02, RULE-04 |
| Timely configuration of diverse storage | RULE-03 |
| Continuous compliance monitoring | RULE-04 |