# POLICY: AC-20.2: Portable Storage Devices — Restricted Use

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-20.2 |
| NIST Control | AC-20.2: Portable Storage Devices — Restricted Use |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | portable storage, external systems, USB devices, removable media, data transfer |

## 1. POLICY STATEMENT
The organization restricts the use of organization-controlled portable storage devices by authorized individuals on external systems through defined usage limitations and conditions. These restrictions protect organizational data and prevent unauthorized data exposure when portable storage devices are used outside the organization's controlled environment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Includes full-time, part-time, temporary |
| Contractors | YES | When using organization-controlled devices |
| Vendors | YES | When provided organization storage devices |
| Organization-controlled portable storage | YES | USB drives, external drives, mobile devices |
| Personal portable storage devices | NO | Covered under separate policy |
| External systems | YES | Non-organization controlled systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Team | • Define portable storage device restrictions<br>• Monitor compliance with usage policies<br>• Investigate policy violations |
| System Administrators | • Implement technical controls for device restrictions<br>• Maintain approved device inventory<br>• Configure external system connection policies |
| Device Users | • Follow all portable storage usage restrictions<br>• Report lost or compromised devices immediately<br>• Obtain approval before using devices on external systems |

## 4. RULES

[RULE-01] Organization-controlled portable storage devices MUST NOT be used on external systems unless explicitly authorized through the portable device usage approval process.
[VALIDATION] IF device_type = "org_portable_storage" AND system_type = "external" AND approval_status != "approved" THEN violation

[RULE-02] All organization-controlled portable storage devices MUST be encrypted with AES-256 or equivalent encryption before use on any external system.
[VALIDATION] IF device_usage_location = "external" AND encryption_status != "AES-256_or_equivalent" THEN critical_violation

[RULE-03] Usage of organization-controlled portable storage devices on external systems MUST be limited to pre-approved business purposes and duration not exceeding 30 days without reauthorization.
[VALIDATION] IF external_usage_duration > 30_days AND reauthorization_status != "approved" THEN violation

[RULE-04] Users MUST obtain written approval from IT Security before connecting organization-controlled portable storage devices to external systems.
[VALIDATION] IF external_connection = TRUE AND written_approval = FALSE THEN violation

[RULE-05] Organization-controlled portable storage devices used on external systems MUST undergo malware scanning before reconnection to organization systems.
[VALIDATION] IF previous_external_use = TRUE AND malware_scan_status != "completed" AND org_reconnection = TRUE THEN critical_violation

[RULE-06] Lost or compromised organization-controlled portable storage devices MUST be reported to IT Security within 2 hours of discovery.
[VALIDATION] IF device_status = "lost_or_compromised" AND report_time > 2_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Portable Device External Usage Approval - Process for requesting and approving external system usage
- [PROC-02] Device Encryption and Security Configuration - Standards for encrypting and securing portable devices
- [PROC-03] External System Risk Assessment - Evaluation process for external systems before device connection
- [PROC-04] Incident Response for Lost/Compromised Devices - Response procedures for device security incidents
- [PROC-05] Device Scanning and Sanitization - Malware scanning requirements after external use

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving portable devices, changes to external system landscape, regulatory requirement updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unauthorized External Usage]
IF device_type = "organization_controlled_portable"
AND usage_location = "external_system"
AND approval_status = "none"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unencrypted Device on External System]
IF device_encryption = "none"
AND system_type = "external"
AND data_classification >= "confidential"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Expired Authorization]
IF external_usage_approval_date < (current_date - 30_days)
AND current_external_usage = TRUE
AND reauthorization_status = "pending"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Proper Approved Usage]
IF device_encryption = "AES-256"
AND approval_status = "current"
AND business_justification = "documented"
AND usage_duration <= 30_days
THEN compliance = TRUE

[SCENARIO-05: Missing Post-External Scan]
IF previous_external_usage = TRUE
AND reconnection_to_org_network = TRUE
AND malware_scan_completion = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Restrict use of organization-controlled portable storage devices on external systems | [RULE-01] |
| Define usage restrictions and conditions | [RULE-03], [RULE-04] |
| Implement security controls for external usage | [RULE-02], [RULE-05] |
| Establish incident response for device compromise | [RULE-06] |