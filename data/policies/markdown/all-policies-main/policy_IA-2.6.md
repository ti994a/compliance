# POLICY: IA-2.6: Access to Accounts — Separate Device

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-2.6 |
| NIST Control | IA-2.6: Access to Accounts — Separate Device |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | multi-factor authentication, privileged accounts, separate device, hardware token, local access |

## 1. POLICY STATEMENT
All local access to privileged accounts MUST implement multi-factor authentication where one authentication factor is provided by a device physically separate from the target system. The separate authentication device MUST meet organizational strength of mechanism requirements to ensure adequate security assurance.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Privileged user accounts | YES | All accounts with elevated system privileges |
| Standard user accounts | NO | Covered under base IA-2 control |
| Service accounts | CONDITIONAL | Only if used for interactive privileged access |
| Emergency accounts | YES | Must comply when used for local privileged access |
| Local system access | YES | Physical or console access to systems |
| Remote system access | NO | Covered under separate controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Implement MFA solutions with separate devices<br>• Configure authentication strength requirements<br>• Monitor privileged account access attempts |
| Security Team | • Define strength of mechanism requirements<br>• Approve separate device technologies<br>• Audit MFA implementation compliance |
| Privileged Users | • Use assigned separate authentication devices<br>• Report device loss or compromise immediately<br>• Comply with authentication procedures |

## 4. RULES
[RULE-01] Multi-factor authentication MUST be implemented for all local access to privileged accounts using at least one factor from a device separate from the target system.
[VALIDATION] IF account_type = "privileged" AND access_type = "local" AND separate_device_factor = FALSE THEN violation

[RULE-02] Separate authentication devices MUST meet minimum strength requirements including FIPS 140-2 Level 2 or equivalent certification.
[VALIDATION] IF device_certification_level < "FIPS_140-2_Level_2" AND device_approved = TRUE THEN violation

[RULE-03] Authentication SHALL NOT be permitted if the separate device factor is unavailable or compromised until alternative approved device is provided.
[VALIDATION] IF separate_device_status = "unavailable" AND authentication_permitted = TRUE THEN critical_violation

[RULE-04] Separate authentication devices MUST be physically distinct from the system being accessed and SHALL NOT share the same hardware platform.
[VALIDATION] IF device_hardware_platform = system_hardware_platform THEN violation

[RULE-05] Emergency bypass procedures for separate device authentication MUST require documented approval from security team and CISO.
[VALIDATION] IF bypass_used = TRUE AND (security_approval = FALSE OR ciso_approval = FALSE) THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Separate Device Provisioning - Process for issuing and configuring approved authentication devices
- [PROC-02] Device Strength Validation - Verification that devices meet certification requirements
- [PROC-03] Device Compromise Response - Actions when separate devices are lost, stolen, or compromised
- [PROC-04] Emergency Access Authorization - Approval process for bypassing separate device requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving privileged accounts, new authentication technologies, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Privileged Access]
IF account_type = "privileged"
AND access_type = "local"
AND mfa_enabled = TRUE
AND separate_device_used = TRUE
AND device_certified = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Separate Device Factor]
IF account_type = "privileged"
AND access_type = "local"
AND mfa_enabled = TRUE
AND separate_device_used = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Same Hardware Platform]
IF account_type = "privileged"
AND device_hardware = system_hardware
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Emergency Bypass Without Approval]
IF emergency_bypass = TRUE
AND security_team_approval = FALSE
AND privileged_access_granted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Non-Certified Device Usage]
IF separate_device_used = TRUE
AND device_fips_level < "Level_2"
AND device_approved = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Multi-factor authentication implemented for local privileged access with separate device factor | [RULE-01] |
| Separate device meets strength of mechanism requirements | [RULE-02] |
| Device physically separate from target system | [RULE-04] |
| Authentication controls when device unavailable | [RULE-03] |
| Emergency bypass authorization requirements | [RULE-05] |