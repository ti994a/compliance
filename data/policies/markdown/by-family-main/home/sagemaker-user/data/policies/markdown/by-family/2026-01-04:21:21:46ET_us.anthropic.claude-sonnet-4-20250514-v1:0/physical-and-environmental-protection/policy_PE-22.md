# POLICY: PE-22: Component Marking

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-22 |
| NIST Control | PE-22: Component Marking |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | hardware marking, classification labels, impact levels, physical security, component inventory |

## 1. POLICY STATEMENT
All system hardware components that process, store, or transmit classified or sensitive information MUST be physically marked to indicate the impact level or classification level of information they are authorized to handle. Components SHALL be marked with human-readable security attributes that reflect applicable laws, regulations, and organizational policies.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Input Devices | YES | Computers, keyboards, tablets, smartphones |
| Output Devices | YES | Printers, monitors, scanners, copiers, audio devices |
| Storage Devices | YES | External drives, removable media, network storage |
| Network Components | CONDITIONAL | Only if processing classified/sensitive data |
| Public Domain Systems | NO | Unless organization requires public release marking |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Asset Manager | • Maintain component inventory with marking requirements<br>• Ensure new components receive appropriate markings<br>• Coordinate marking updates when classification changes |
| Information Security Officer | • Define marking standards and procedures<br>• Validate marking compliance during audits<br>• Approve exceptions to marking requirements |
| Facility Security Officer | • Implement physical marking procedures<br>• Train personnel on marking requirements<br>• Monitor marking compliance in secure areas |

## 4. RULES
[RULE-01] Hardware components processing Moderate or High impact information MUST display visible markings indicating the maximum impact level authorized.
[VALIDATION] IF component_impact_level IN ["Moderate", "High"] AND visible_marking = FALSE THEN violation

[RULE-02] Component markings MUST be updated within 5 business days when the authorized impact level changes.
[VALIDATION] IF impact_level_changed = TRUE AND marking_update_days > 5 THEN violation

[RULE-03] Marking labels SHALL use organization-approved templates and materials that remain legible for the component's operational lifetime.
[VALIDATION] IF marking_template = "unapproved" OR marking_legible = FALSE THEN violation

[RULE-04] Components in classified environments MUST display classification markings consistent with the highest level of information they are authorized to process.
[VALIDATION] IF environment_classification > component_marking_level THEN critical_violation

[RULE-05] Public domain components MAY be marked to indicate public releasability when required by organizational policy.
[VALIDATION] IF public_marking_required = TRUE AND public_marking_present = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Marking Standards - Define approved marking formats, materials, and placement requirements
- [PROC-02] New Component Marking - Process for marking components before deployment
- [PROC-03] Marking Verification - Quarterly verification of component marking accuracy
- [PROC-04] Marking Updates - Process for updating markings when classifications change

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Classification policy changes, new component types, security incidents involving unmarked components

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unmarked Printer in Classified Area]
IF component_type = "printer"
AND location_classification = "SECRET"
AND component_marking = "none"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Outdated Component Marking]
IF component_marking_level = "Confidential"
AND current_authorized_level = "Secret"
AND marking_update_overdue = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Public System with Required Marking]
IF information_type = "public_domain"
AND org_policy_requires_public_marking = TRUE
AND public_release_marking = "present"
THEN compliance = TRUE

[SCENARIO-04: Mobile Device Classification Mismatch]
IF device_type = "smartphone"
AND processes_cui = TRUE
AND marking_indicates_cui = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Temporary Component Exception]
IF component_marking = "missing"
AND documented_exception = TRUE
AND exception_expiry_date > current_date
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Hardware components marked with impact/classification level | RULE-01, RULE-04 |
| Markings indicate authorized information levels | RULE-01, RULE-04 |
| Component inventory includes marking requirements | RULE-02, RULE-03 |
| Marking procedures implemented | RULE-03, RULE-05 |