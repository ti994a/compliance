# POLICY: AU-9.1: Hardware Write-once Media

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AU-9.1 |
| NIST Control | AU-9.1: Hardware Write-once Media |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | audit trails, write-once media, WORM, hardware-enforced, immutable storage |

## 1. POLICY STATEMENT
All audit trails MUST be written to hardware-enforced, write-once media to ensure immutability and integrity of audit records. This requirement applies to both initial generation of audit trails and backup copies of audit data.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems generating audit trails |
| Audit Trail Storage | YES | Primary and backup audit storage |
| WORM Media Devices | YES | CD-R, BD-R, DVD-R, WORM drives |
| Rewriteable Media | NO | CD-RW, DVD-RW, USB drives prohibited for audit storage |
| Cloud Services | CONDITIONAL | Only if hardware-enforced WORM capability verified |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure audit systems to write to WORM media<br>• Verify hardware write-once enforcement<br>• Monitor audit trail storage capacity |
| Security Operations | • Validate WORM media integrity<br>• Manage audit trail backup procedures<br>• Ensure continuous audit trail generation |
| IT Procurement | • Source compliant WORM storage solutions<br>• Verify hardware write-once capabilities<br>• Maintain approved media inventory |

## 4. RULES
[RULE-01] All audit trails MUST be written exclusively to hardware-enforced, write-once media that prevents any modification or deletion of stored audit records.
[VALIDATION] IF audit_storage_media != "hardware_enforced_WORM" THEN violation

[RULE-02] Systems MUST NOT use switchable write-protection media (CD-RW, DVD-RW, USB drives, tape cartridges) for audit trail storage.
[VALIDATION] IF audit_media_type IN ["CD-RW", "DVD-RW", "USB", "tape_cartridge"] THEN critical_violation

[RULE-03] Backup copies of audit trails MUST also be stored on hardware-enforced, write-once media with the same immutability requirements as primary storage.
[VALIDATION] IF backup_audit_media != "hardware_enforced_WORM" THEN violation

[RULE-04] WORM media hardware enforcement MUST be verified through technical testing before deployment for audit storage.
[VALIDATION] IF WORM_verification_test = "failed" OR WORM_verification_date > 365_days_ago THEN violation

[RULE-05] Cloud-based audit storage SHALL only be used if the provider demonstrates hardware-enforced write-once capabilities with third-party verification.
[VALIDATION] IF storage_type = "cloud" AND hardware_WORM_verified = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] WORM Media Verification - Technical validation of hardware write-once enforcement
- [PROC-02] Audit Trail Storage Configuration - System setup for WORM-only audit writing
- [PROC-03] Media Capacity Management - Monitoring and replacement of full WORM media
- [PROC-04] Backup Audit Trail Creation - Procedures for creating immutable backup copies

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New audit systems deployment, WORM technology changes, compliance audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard WORM Implementation]
IF audit_storage_type = "BD-R"
AND hardware_enforcement = TRUE
AND backup_media = "CD-R"
THEN compliance = TRUE

[SCENARIO-02: Prohibited Rewriteable Media]
IF audit_storage_type = "DVD-RW"
AND system_in_production = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Cloud Storage Without WORM Verification]
IF storage_location = "cloud"
AND hardware_WORM_verified = FALSE
AND audit_trails_stored = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Switchable Write Protection]
IF media_type = "tape_cartridge"
AND write_protection = "switchable"
AND used_for_audit_storage = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Expired WORM Verification]
IF WORM_media_deployed = TRUE
AND last_verification_date > 365_days_ago
AND system_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Audit trails written to hardware-enforced write-once media | RULE-01, RULE-04 |
| Backup audit trails use WORM media | RULE-03 |
| Prohibition of rewriteable media for audit storage | RULE-02 |
| Cloud storage WORM capability verification | RULE-05 |