```markdown
POLICY: SC-34.2: Integrity Protection on Read-only Media

METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-34.2 |
| NIST Control | SC-34.2: Integrity Protection on Read-only Media |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | read-only media, integrity protection, media control, firmware, BIOS, executable programs |

1. POLICY STATEMENT
The organization must protect the integrity of information before storage on read-only media and maintain strict control over such media after information has been recorded. This includes preventing unauthorized substitution or modification of read-only media used in organizational systems.

2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All read-only media | YES | Including ROM, PROM, EPROM, firmware, BIOS |
| Programmable read-only media | YES | Special controls for reprogramming prevention |
| Removable read-only media | YES | Physical and logical access controls required |
| Third-party supplied media | YES | Verification required before installation |
| Development/test media | CONDITIONAL | When used in production systems |

3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Verify media integrity before installation<br>• Implement access controls for media storage<br>• Document media handling procedures |
| Security Team | • Define integrity verification requirements<br>• Monitor for unauthorized media substitution<br>• Conduct periodic media integrity assessments |
| IT Asset Management | • Maintain inventory of authorized read-only media<br>• Control media procurement and distribution<br>• Track media lifecycle and disposal |

4. RULES
[RULE-01] Information integrity MUST be verified using cryptographic hashes or digital signatures before storage on read-only media.
[VALIDATION] IF media_type = "read-only" AND integrity_verification = FALSE THEN violation

[RULE-02] Read-only media MUST be stored in physically secured locations with access limited to authorized personnel only.
[VALIDATION] IF media_storage_location = "unsecured" OR unauthorized_access = TRUE THEN violation

[RULE-03] Programmable read-only media MUST be write-protected immediately after authorized programming is complete.
[VALIDATION] IF media_type = "programmable_ROM" AND write_protection = FALSE AND programming_complete = TRUE THEN violation

[RULE-04] All read-only media MUST be inventoried and tracked from creation through disposal with chain of custody documentation.
[VALIDATION] IF media_inventory_status = "untracked" OR chain_of_custody = FALSE THEN violation

[RULE-05] Third-party supplied read-only media MUST undergo integrity verification and security assessment before installation in production systems.
[VALIDATION] IF media_source = "third-party" AND security_assessment = FALSE THEN critical_violation

[RULE-06] Substitution of read-only media MUST be detected through automated monitoring and integrity checking mechanisms.
[VALIDATION] IF substitution_detection = FALSE OR integrity_monitoring = "disabled" THEN violation

[RULE-07] Access to programmable read-only media programming equipment MUST be restricted to authorized personnel with documented approval.
[VALIDATION] IF programming_access = "unrestricted" OR authorization_documented = FALSE THEN violation

5. REQUIRED PROCEDURES
- [PROC-01] Media Integrity Verification - Cryptographic verification before storage
- [PROC-02] Secure Media Storage - Physical security and access control procedures
- [PROC-03] Media Chain of Custody - Tracking and documentation requirements
- [PROC-04] Third-party Media Assessment - Security evaluation and approval process
- [PROC-05] Substitution Detection - Monitoring and alerting procedures

6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving media, technology changes, regulatory updates

7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Media Substitution]
IF media_integrity_check = "failed"
AND media_source = "unknown"
AND system_boot_media = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Third-party Firmware Installation]
IF media_source = "third-party"
AND security_assessment = "completed"
AND integrity_verified = TRUE
AND authorization = "documented"
THEN compliance = TRUE

[SCENARIO-03: Programmable Media Write Protection]
IF media_type = "EPROM"
AND programming_complete = TRUE
AND write_protection = FALSE
AND production_system = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Media Storage Security]
IF media_storage = "secured_facility"
AND access_control = "implemented"
AND inventory_tracked = TRUE
AND chain_of_custody = "documented"
THEN compliance = TRUE

[SCENARIO-05: Development Media in Production]
IF media_environment = "development"
AND current_location = "production_system"
AND security_assessment = FALSE
THEN compliance = FALSE
violation_severity = "High"

8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Integrity protection prior to storage | [RULE-01] |
| Media control after recording | [RULE-02], [RULE-04] |
| Prevention of unauthorized substitution | [RULE-05], [RULE-06] |
| Programmable media protection | [RULE-03], [RULE-07] |
```