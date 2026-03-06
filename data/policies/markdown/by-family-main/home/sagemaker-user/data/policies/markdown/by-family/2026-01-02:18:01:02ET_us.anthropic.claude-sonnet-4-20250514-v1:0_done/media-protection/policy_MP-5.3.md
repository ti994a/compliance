```markdown
# POLICY: MP-5.3: Custodians

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-5.3 |
| NIST Control | MP-5.3: Custodians |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | media transport, custodian, controlled areas, accountability, system media |

## 1. POLICY STATEMENT
The organization SHALL employ an identified custodian during transport of system media outside of controlled areas. Custodians provide specific points of contact during media transport and facilitate individual accountability throughout the transport process.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| System Media | YES | All digital storage devices containing organizational data |
| Controlled Areas | YES | Designated secure facilities and authorized work locations |
| Transport Activities | YES | Any movement of system media outside controlled boundaries |
| Third-party Couriers | CONDITIONAL | Only when transporting organizational system media |
| Personal Devices | CONDITIONAL | Only when containing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Media Custodian | • Maintain physical custody of system media during transport<br>• Document chain of custody throughout transport process<br>• Ensure secure handling and protection of media<br>• Report any incidents or anomalies during transport |
| Security Officer | • Approve custodian assignments and transport requests<br>• Maintain registry of authorized custodians<br>• Monitor compliance with transport procedures |
| Data Owner | • Authorize media transport outside controlled areas<br>• Define handling requirements for specific media types |

## 4. RULES
[RULE-01] System media transport outside controlled areas MUST have an identified custodian assigned before transport begins.
[VALIDATION] IF media_transport = TRUE AND location_outside_controlled_area = TRUE AND custodian_assigned = FALSE THEN violation

[RULE-02] Media custodians MUST be formally designated and documented in the custodian registry before assuming transport responsibilities.
[VALIDATION] IF custodian_role_assigned = TRUE AND registry_documentation = FALSE THEN violation

[RULE-03] Custodial responsibility transfers MUST be documented with clear identification of receiving custodian and acknowledgment of custody transfer.
[VALIDATION] IF custody_transfer = TRUE AND (receiving_custodian_id = NULL OR transfer_acknowledgment = FALSE) THEN violation

[RULE-04] Media custodians MUST maintain continuous accountability for assigned media throughout the entire transport process.
[VALIDATION] IF transport_in_progress = TRUE AND custody_gap_documented = TRUE THEN violation

[RULE-05] Transport of system media outside controlled areas without an assigned custodian is PROHIBITED.
[VALIDATION] IF media_contains_org_data = TRUE AND transport_outside_controlled_area = TRUE AND custodian_present = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Custodian Assignment Process - Formal designation and documentation of media custodians
- [PROC-02] Media Transport Authorization - Approval workflow for transporting media outside controlled areas
- [PROC-03] Chain of Custody Documentation - Recording and tracking custodial responsibility throughout transport
- [PROC-04] Custodian Training Program - Required training for personnel assigned custodial responsibilities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving media transport, changes to controlled area boundaries, custodian role changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unassigned Media Transport]
IF system_media = TRUE
AND transport_destination_outside_controlled_area = TRUE
AND assigned_custodian = NULL
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Undocumented Custody Transfer]
IF media_transport_in_progress = TRUE
AND custody_change_occurred = TRUE
AND transfer_documentation = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Authorized Custodian Transport]
IF system_media = TRUE
AND transport_outside_controlled_area = TRUE
AND custodian_assigned = TRUE
AND custodian_registry_current = TRUE
THEN compliance = TRUE

[SCENARIO-04: Courier Service Without Custodian]
IF third_party_courier = TRUE
AND organizational_media = TRUE
AND custodian_accompanying = FALSE
AND custodian_designation_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Emergency Media Transport]
IF emergency_transport = TRUE
AND system_media = TRUE
AND custodian_assigned = TRUE
AND transport_authorization_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Custodian identification for media transport | [RULE-01] |
| Employment of identified custodian during transport | [RULE-04], [RULE-05] |
| Custodian accountability and documentation | [RULE-02], [RULE-03] |
```