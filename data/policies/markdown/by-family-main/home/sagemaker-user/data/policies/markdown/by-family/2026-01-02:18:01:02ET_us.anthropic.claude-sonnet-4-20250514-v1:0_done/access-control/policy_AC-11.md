# POLICY: AC-11: Device Lock

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-11 |
| NIST Control | AC-11: Device Lock |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | device lock, session lock, inactivity timeout, authentication, access control |

## 1. POLICY STATEMENT
All organizational systems MUST implement automatic device locks after a defined period of user inactivity to prevent unauthorized access. Device locks MUST remain active until users re-authenticate using established identification and authentication procedures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Workstations | YES | All employee workstations and laptops |
| Servers | YES | Interactive server sessions only |
| Mobile Devices | YES | Company-owned and BYOD devices |
| Kiosks/Shared Systems | YES | Public-facing and shared terminals |
| Service Accounts | NO | Automated system processes excluded |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Team | • Configure device lock policies<br>• Monitor compliance<br>• Define timeout parameters |
| System Administrators | • Implement device lock settings<br>• Validate configuration<br>• Report exceptions |
| End Users | • Comply with device lock requirements<br>• Report malfunctions<br>• Use manual lock when appropriate |

## 4. RULES

[RULE-01] All systems MUST automatically initiate device lock after 15 minutes of inactivity for standard business systems and 5 minutes for systems processing sensitive data.
[VALIDATION] IF inactivity_timeout > 15_minutes AND system_classification = "standard" THEN violation
[VALIDATION] IF inactivity_timeout > 5_minutes AND system_classification = "sensitive" THEN violation

[RULE-02] Device locks MUST prevent all system access and MUST NOT display sensitive information on lock screens.
[VALIDATION] IF lock_screen_shows_sensitive_data = TRUE THEN violation
[VALIDATION] IF system_accessible_during_lock = TRUE THEN critical_violation

[RULE-03] Users MUST re-authenticate using established identification and authentication procedures to unlock devices.
[VALIDATION] IF unlock_method != "established_auth_procedure" THEN violation

[RULE-04] Device lock functionality MUST be enabled on all in-scope systems and SHALL NOT be disabled by end users.
[VALIDATION] IF device_lock_enabled = FALSE THEN critical_violation
[VALIDATION] IF user_can_disable_lock = TRUE THEN violation

[RULE-05] Systems processing PCI or FedRAMP data MUST implement device lock after 5 minutes of inactivity maximum.
[VALIDATION] IF (data_classification = "PCI" OR data_classification = "FedRAMP") AND inactivity_timeout > 5_minutes THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Device Lock Configuration - Standard procedures for configuring timeout values and lock mechanisms
- [PROC-02] Exception Management - Process for documenting and approving device lock exceptions
- [PROC-03] Compliance Monitoring - Regular assessment of device lock implementation and effectiveness
- [PROC-04] User Training - Education on proper device lock usage and manual lock procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving unlocked devices, regulatory changes, technology updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Standard Workstation Timeout]
IF system_type = "workstation"
AND data_classification = "standard"
AND inactivity_timeout = 10_minutes
AND device_lock_enabled = TRUE
THEN compliance = TRUE

[SCENARIO-02: Sensitive Data System Violation]
IF data_classification = "sensitive"
AND inactivity_timeout = 20_minutes
AND system_accessible_during_lock = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: User-Disabled Lock]
IF device_lock_enabled = FALSE
AND disabled_by = "end_user"
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: PCI System Compliance]
IF data_classification = "PCI"
AND inactivity_timeout = 5_minutes
AND unlock_method = "established_auth_procedure"
AND lock_screen_shows_sensitive_data = FALSE
THEN compliance = TRUE

[SCENARIO-05: Mobile Device Exception]
IF device_type = "mobile"
AND inactivity_timeout = 30_minutes
AND exception_documented = TRUE
AND business_justification = "field_operations"
THEN compliance = CONDITIONAL
requires_review = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prevent access after inactivity period | RULE-01, RULE-05 |
| Retain lock until re-authentication | RULE-03 |
| Device lock implementation | RULE-04 |
| Lock screen information protection | RULE-02 |