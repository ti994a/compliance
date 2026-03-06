# POLICY: MA-5.1: Individuals Without Appropriate Access

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MA-5.1 |
| NIST Control | MA-5.1: Individuals Without Appropriate Access |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | maintenance personnel, security clearances, escort supervision, sanitization, access authorization |

## 1. POLICY STATEMENT
All maintenance personnel lacking appropriate security clearances or U.S. citizenship MUST be escorted and supervised by authorized personnel during system maintenance activities. Prior to maintenance activities, volatile storage components MUST be sanitized and non-volatile media MUST be removed or physically disconnected from systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems containing classified or controlled information |
| Maintenance Personnel | YES | Third-party, contractor, and uncleared internal staff |
| Escort Personnel | YES | Must have appropriate clearances and technical qualifications |
| Storage Components | YES | Both volatile and non-volatile storage media |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Identify maintenance personnel clearance requirements<br>• Approve escort personnel<br>• Ensure alternate controls are defined |
| Security Officer | • Verify clearance status of maintenance personnel<br>• Oversee sanitization procedures<br>• Document alternate control measures |
| Escort Personnel | • Provide continuous supervision during maintenance<br>• Ensure no unauthorized access to sensitive information<br>• Report any security incidents |

## 4. RULES
[RULE-01] Maintenance personnel without appropriate security clearances or U.S. citizenship MUST be escorted and supervised at all times during maintenance activities by approved organizational personnel who are fully cleared, have appropriate access authorizations, and are technically qualified.
[VALIDATION] IF maintenance_personnel_clearance = "insufficient" AND escort_present = FALSE THEN critical_violation

[RULE-02] All volatile information storage components within the system MUST be sanitized prior to initiating maintenance activities by uncleared personnel.
[VALIDATION] IF maintenance_start = TRUE AND personnel_clearance = "insufficient" AND volatile_storage_sanitized = FALSE THEN critical_violation

[RULE-03] All non-volatile storage media MUST be removed or physically disconnected from the system and secured prior to maintenance by uncleared personnel.
[VALIDATION] IF maintenance_start = TRUE AND personnel_clearance = "insufficient" AND nonvolatile_media_secured = FALSE THEN critical_violation

[RULE-04] Alternate controls MUST be developed and implemented when system components cannot be sanitized, removed, or disconnected from the system.
[VALIDATION] IF component_removable = FALSE AND sanitization_possible = FALSE AND alternate_controls_implemented = FALSE THEN violation

[RULE-05] Escort personnel MUST possess appropriate security clearances, access authorizations, and technical qualifications for the system being maintained.
[VALIDATION] IF escort_clearance_level < required_clearance_level OR escort_technical_qualified = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Maintenance Personnel Clearance Verification - Verify security clearance status and citizenship before system access
- [PROC-02] Pre-Maintenance Sanitization - Sanitize volatile components and secure non-volatile media
- [PROC-03] Escort Assignment and Supervision - Assign qualified escorts for continuous supervision
- [PROC-04] Alternate Control Implementation - Deploy alternate controls when sanitization/removal is not possible

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving maintenance personnel, changes to clearance requirements, system classification changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unescorted Foreign National Maintenance]
IF maintenance_personnel_citizenship = "non-US"
AND security_clearance = "none"
AND escort_present = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Unsanitized System Maintenance]
IF maintenance_required = TRUE
AND personnel_clearance = "insufficient"
AND volatile_storage_sanitized = FALSE
AND nonvolatile_media_removed = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Unqualified Escort Personnel]
IF maintenance_personnel_clearance = "insufficient"
AND escort_assigned = TRUE
AND escort_clearance_adequate = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: No Alternate Controls for Non-Removable Components]
IF system_component_removable = FALSE
AND sanitization_feasible = FALSE
AND alternate_controls_defined = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Escorted Maintenance]
IF maintenance_personnel_clearance = "insufficient"
AND escort_present = TRUE
AND escort_clearance_adequate = TRUE
AND volatile_storage_sanitized = TRUE
AND nonvolatile_media_secured = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Escort and supervision of uncleared maintenance personnel | [RULE-01], [RULE-05] |
| Sanitization of volatile storage components | [RULE-02] |
| Removal/disconnection of non-volatile storage media | [RULE-03] |
| Implementation of alternate controls | [RULE-04] |