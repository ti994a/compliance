# POLICY: PE-22: Component Marking

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-22 |
| NIST Control | PE-22: Component Marking |
| Version | 1.0 |
| Owner | Physical Security Manager |
| Keywords | hardware marking, classification labels, impact levels, component identification, physical security |

## 1. POLICY STATEMENT
All system hardware components that process, store, or transmit organizational information MUST be clearly marked with appropriate impact level or classification level indicators. These markings SHALL reflect the highest level of information that the component is authorized to handle.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Desktop computers | YES | All organizational workstations |
| Laptop computers | YES | Including remote work devices |
| Mobile devices | YES | Tablets, smartphones with org data |
| Input devices | YES | Keyboards, mice, biometric readers |
| Output devices | YES | Printers, monitors, speakers |
| Network equipment | YES | Switches, routers in secure areas |
| Storage devices | YES | External drives, USB devices |
| Public domain systems | CONDITIONAL | Only if org requires marking |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Physical Security Manager | • Establish marking standards and procedures<br>• Oversee compliance monitoring<br>• Approve marking exceptions |
| IT Asset Manager | • Maintain component inventory with marking status<br>• Coordinate marking during procurement<br>• Track marking compliance |
| System Administrators | • Apply markings during system deployment<br>• Verify markings during maintenance<br>• Report marking discrepancies |

## 4. RULES
[RULE-01] All hardware components that process, store, or transmit information at MODERATE or HIGH impact levels MUST display visible markings indicating the maximum authorized impact level.
[VALIDATION] IF component_impact_level IN ["MODERATE", "HIGH"] AND marking_present = FALSE THEN violation

[RULE-02] Component markings MUST be human-readable, durable, and positioned where they are clearly visible during normal operation.
[VALIDATION] IF marking_readable = FALSE OR marking_visible = FALSE THEN violation

[RULE-03] Markings SHALL reflect the highest impact level of information the component is authorized to process, not necessarily the current information level.
[VALIDATION] IF marking_level < max_authorized_level THEN violation

[RULE-04] Components relocated between environments with different impact levels MUST have markings updated within 24 hours of relocation.
[VALIDATION] IF component_relocated = TRUE AND marking_update_time > 24_hours THEN violation

[RULE-05] Mobile devices and portable equipment MUST include contact information for the owning organization in addition to impact level markings.
[VALIDATION] IF device_portable = TRUE AND contact_info_present = FALSE THEN violation

[RULE-06] Output devices shared across multiple impact levels MUST be marked with the highest impact level they are authorized to process.
[VALIDATION] IF device_shared = TRUE AND marking_level < highest_authorized_level THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Marking Standards - Define marking formats, materials, and placement requirements
- [PROC-02] Marking Application Process - Steps for applying markings during procurement and deployment
- [PROC-03] Marking Verification - Regular audits to ensure marking compliance and accuracy
- [PROC-04] Marking Updates - Process for updating markings when component authorization changes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New impact level classifications, regulatory changes, security incidents involving unmarked components

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unmarked High Impact Workstation]
IF component_type = "workstation"
AND max_authorized_impact = "HIGH"
AND marking_present = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incorrect Marking on Relocated Device]
IF component_relocated = TRUE
AND new_environment_impact = "HIGH"
AND current_marking = "MODERATE"
AND days_since_relocation > 1
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Shared Printer Missing Contact Info]
IF device_type = "printer"
AND device_shared = TRUE
AND impact_level_marked = TRUE
AND contact_info_present = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Public Domain System Exception]
IF information_classification = "public_domain"
AND organization_requires_marking = FALSE
AND marking_present = FALSE
THEN compliance = TRUE

[SCENARIO-05: Mobile Device Proper Marking]
IF device_type = "mobile"
AND impact_level_marked = TRUE
AND contact_info_present = TRUE
AND marking_readable = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Hardware components marked with impact/classification level | RULE-01, RULE-03 |
| Markings indicate permitted information levels | RULE-03, RULE-06 |
| Marking visibility and durability | RULE-02 |
| Timely marking updates | RULE-04 |
| Mobile device identification | RULE-05 |