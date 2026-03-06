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
All system media transported outside of controlled areas MUST be accompanied by an identified custodian who maintains accountability throughout the transport process. Custodial responsibilities can be transferred between authorized individuals with proper documentation and handoff procedures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| System Media | YES | All media containing organizational data |
| Controlled Areas | YES | Facilities with physical security controls |
| Transport Activities | YES | Any movement outside controlled areas |
| Custodians | YES | Authorized personnel with transport responsibilities |
| Third-party Couriers | CONDITIONAL | Only when accompanied by organizational custodian |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Media Custodian | • Maintain physical control of media during transport<br>• Document transport activities and chain of custody<br>• Ensure secure delivery to authorized recipients |
| Security Officer | • Approve custodian assignments<br>• Monitor transport compliance<br>• Investigate transport incidents |
| Data Owner | • Authorize media transport requests<br>• Define handling requirements<br>• Validate recipient authorization |

## 4. RULES
[RULE-01] System media MUST NOT be transported outside controlled areas without an identified custodian maintaining physical control.
[VALIDATION] IF media_location = "outside_controlled_area" AND custodian_assigned = FALSE THEN critical_violation

[RULE-02] Custodians MUST be formally identified and documented before transport activities begin.
[VALIDATION] IF transport_initiated = TRUE AND custodian_documentation = "incomplete" THEN violation

[RULE-03] Custodial responsibility transfers MUST be documented with signatures from both transferring and receiving custodians.
[VALIDATION] IF custody_transfer = TRUE AND (transferring_signature = FALSE OR receiving_signature = FALSE) THEN violation

[RULE-04] Custodians MUST maintain continuous accountability of media during transport with no unattended periods exceeding 15 minutes.
[VALIDATION] IF unattended_duration > 15_minutes AND controlled_environment = FALSE THEN violation

[RULE-05] Transport activities MUST be logged with custodian identity, departure time, destination, and arrival confirmation.
[VALIDATION] IF transport_complete = TRUE AND (custodian_id = NULL OR departure_time = NULL OR arrival_confirmation = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Custodian Assignment - Process for identifying and authorizing media transport custodians
- [PROC-02] Chain of Custody - Documentation requirements for media accountability during transport
- [PROC-03] Custody Transfer - Handoff procedures between custodians during extended transport
- [PROC-04] Incident Response - Actions required for transport security incidents or custody breaks

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Transport incidents, custodian violations, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unaccompanied Media Transport]
IF system_media = "classified_data"
AND transport_location = "outside_controlled_area"
AND custodian_present = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Undocumented Custodian]
IF media_transport = "initiated"
AND custodian_assigned = TRUE
AND custodian_documentation = "missing"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Custody Transfer Without Documentation]
IF custody_transfer = "occurred"
AND transfer_documentation = "incomplete"
AND media_sensitivity = "high"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Compliant Custodial Transport]
IF custodian_identified = TRUE
AND transport_logged = TRUE
AND continuous_custody = TRUE
AND destination_authorized = TRUE
THEN compliance = TRUE

[SCENARIO-05: Extended Unattended Period]
IF media_unattended = TRUE
AND unattended_duration = "30_minutes"
AND location_type = "public_area"
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Custodian identification during transport | RULE-01, RULE-02 |
| Employment of identified custodian | RULE-01, RULE-04 |
| Accountability maintenance | RULE-03, RULE-05 |
| Documentation requirements | RULE-02, RULE-03, RULE-05 |
```