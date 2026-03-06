# POLICY: MP-7: Media Use

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-7 |
| NIST Control | MP-7: Media Use |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | media protection, portable storage, removable media, USB drives, external devices |

## 1. POLICY STATEMENT
This policy restricts and prohibits the use of specific types of system media on organizational systems and components to protect against data exfiltration, malware introduction, and unauthorized data access. All portable storage devices without identifiable owners are prohibited from use on organizational systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Including cloud, on-premises, and hybrid |
| Employee workstations | YES | Desktop and laptop computers |
| Server infrastructure | YES | Physical and virtual servers |
| Mobile devices | YES | Company and BYOD devices with storage |
| Contractor systems | YES | When accessing organizational data |
| Guest networks | CONDITIONAL | If connected to organizational systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Team | • Define restricted media types<br>• Implement technical controls<br>• Monitor compliance<br>• Approve exceptions |
| System Administrators | • Configure media restrictions<br>• Disable unauthorized ports<br>• Maintain approved device lists<br>• Report violations |
| End Users | • Comply with media restrictions<br>• Use only approved devices<br>• Report security incidents<br>• Maintain device accountability |

## 4. RULES

[RULE-01] Organizations MUST define and document specific types of system media that are restricted or prohibited on organizational systems and components.
[VALIDATION] IF media_types_defined = FALSE THEN violation

[RULE-02] Portable storage devices without identifiable owners SHALL be prohibited from use on all organizational systems.
[VALIDATION] IF device_type = "portable_storage" AND owner_identified = FALSE AND device_used = TRUE THEN critical_violation

[RULE-03] Technical controls MUST be implemented to restrict or disable unauthorized media types on systems and components.
[VALIDATION] IF restricted_media_type = TRUE AND technical_controls_enabled = FALSE THEN violation

[RULE-04] Only organization-provided or pre-approved portable storage devices SHALL be permitted for business use.
[VALIDATION] IF device_type = "portable_storage" AND (organization_provided = FALSE AND pre_approved = FALSE) AND business_use = TRUE THEN violation

[RULE-05] Write capabilities to removable media MUST be disabled on systems processing sensitive data unless specifically authorized.
[VALIDATION] IF system_sensitivity = "high" AND removable_media_write_enabled = TRUE AND authorization_documented = FALSE THEN violation

[RULE-06] Physical controls MUST be implemented to prevent unauthorized access to system ports and media interfaces where technically feasible.
[VALIDATION] IF physical_controls_required = TRUE AND physical_controls_implemented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Media Restriction Assessment - Annual review of restricted media types and business justification
- [PROC-02] Device Approval Process - Evaluation and approval workflow for portable storage devices
- [PROC-03] Technical Control Implementation - Configuration standards for disabling unauthorized media
- [PROC-04] Exception Management - Process for documenting and approving media use exceptions
- [PROC-05] Incident Response - Response procedures for unauthorized media use detection

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents, technology changes, regulatory updates, business requirement changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unknown USB Device]
IF device_type = "USB_storage"
AND owner_identified = FALSE
AND connected_to_system = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Personal Device on Sensitive System]
IF device_ownership = "personal"
AND system_classification = "sensitive"
AND device_approved = FALSE
AND device_connected = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Approved Device with Documentation]
IF device_type = "portable_storage"
AND organization_provided = TRUE
AND business_justification = "documented"
AND technical_controls = "configured"
THEN compliance = TRUE

[SCENARIO-04: Disabled Ports on High-Risk System]
IF system_risk_level = "high"
AND USB_ports = "physically_disabled"
AND business_need = "none"
THEN compliance = TRUE

[SCENARIO-05: Contractor Using Personal Drive]
IF user_type = "contractor"
AND device_ownership = "personal"
AND data_classification = "confidential"
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Define restricted media types | [RULE-01] |
| Prohibit unidentifiable devices | [RULE-02] |
| Implement technical controls | [RULE-03] |
| Approve portable devices | [RULE-04] |
| Control write capabilities | [RULE-05] |
| Deploy physical restrictions | [RULE-06] |