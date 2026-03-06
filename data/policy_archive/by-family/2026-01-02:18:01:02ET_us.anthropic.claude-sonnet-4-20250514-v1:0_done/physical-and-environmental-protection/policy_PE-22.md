# POLICY: PE-22: Component Marking

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-22 |
| NIST Control | PE-22: Component Marking |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | hardware marking, classification levels, impact levels, physical security, component labeling |

## 1. POLICY STATEMENT
All system hardware components that process, store, or transmit organizational information MUST be clearly marked to indicate the impact level or classification level of information they are authorized to handle. Markings SHALL be human-readable and reflect applicable laws, executive orders, directives, policies, regulations, and standards.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Input devices | YES | Desktop computers, laptops, keyboards, tablets, smartphones |
| Output devices | YES | Printers, monitors, displays, fax machines, scanners, copiers, audio devices |
| Network components | YES | Routers, switches, firewalls handling classified/sensitive data |
| Storage devices | YES | Servers, storage arrays, removable media devices |
| Public domain systems | CONDITIONAL | Only if organization requires marking for publicly releasable information |
| Personal devices | CONDITIONAL | Only if used for organizational data processing |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Policy oversight and enforcement<br>• Classification level determination<br>• Marking standard approval |
| IT Asset Manager | • Component inventory maintenance<br>• Marking implementation coordination<br>• Compliance tracking and reporting |
| System Administrators | • Physical marking application<br>• Marking accuracy verification<br>• Component registration in inventory |
| Security Officers | • Marking compliance audits<br>• Violation identification and remediation<br>• Training delivery |

## 4. RULES

[RULE-01] All hardware components that process, store, or transmit organizational information MUST be marked with appropriate impact level or classification level indicators.
[VALIDATION] IF component_handles_org_data = TRUE AND marking_present = FALSE THEN violation

[RULE-02] Component markings MUST be human-readable and permanently affixed to prevent removal or alteration.
[VALIDATION] IF marking_readable = FALSE OR marking_removable = TRUE THEN violation

[RULE-03] Markings SHALL accurately reflect the highest impact level or classification level of information the component is authorized to handle.
[VALIDATION] IF marking_level < max_authorized_level THEN violation

[RULE-04] New hardware components MUST be marked within 24 hours of deployment or before processing organizational data, whichever occurs first.
[VALIDATION] IF deployment_time > 24_hours AND marking_applied = FALSE AND org_data_processed = TRUE THEN violation

[RULE-05] Component markings MUST be updated within 72 hours when authorization levels change.
[VALIDATION] IF authorization_change_date + 72_hours < current_date AND marking_updated = FALSE THEN violation

[RULE-06] All marked components MUST be documented in the hardware inventory with corresponding marking details.
[VALIDATION] IF component_marked = TRUE AND inventory_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Hardware Component Marking Standard - Defines marking formats, materials, and placement requirements
- [PROC-02] Component Classification Assessment - Process for determining appropriate marking levels
- [PROC-03] Marking Verification and Audit - Regular compliance checking procedures
- [PROC-04] Marking Update Process - Procedures for updating markings when authorization changes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 6 months
- Triggering events: Security incidents involving unmarked components, classification system changes, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Printer Deployment]
IF device_type = "printer"
AND deployment_status = "active"
AND marking_applied = FALSE
AND hours_since_deployment > 24
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Laptop Classification Upgrade]
IF device_type = "laptop"
AND authorization_level_changed = TRUE
AND hours_since_change > 72
AND marking_updated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Public Domain System]
IF information_classification = "public_domain"
AND organization_requires_public_marking = FALSE
AND marking_present = FALSE
THEN compliance = TRUE
violation_severity = "None"

[SCENARIO-04: Removable Marking Violation]
IF marking_present = TRUE
AND marking_type = "removable_sticker"
AND component_classification >= "confidential"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Inventory Documentation Gap]
IF component_marked = TRUE
AND inventory_system_entry = FALSE
AND days_since_marking > 1
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Hardware components marked indicating impact/classification level | [RULE-01], [RULE-03] |
| Components defined for marking requirements | [RULE-06] |
| Marking accuracy and permanence | [RULE-02], [RULE-03] |
| Timely marking implementation | [RULE-04], [RULE-05] |