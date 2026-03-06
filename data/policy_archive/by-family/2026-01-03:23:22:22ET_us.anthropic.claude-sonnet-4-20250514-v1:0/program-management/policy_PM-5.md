# POLICY: PM-5: System Inventory

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-5 |
| NIST Control | PM-5: System Inventory |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | system inventory, organizational systems, asset management, FISMA reporting, system tracking |

## 1. POLICY STATEMENT
The organization SHALL develop and maintain a comprehensive inventory of all organizational systems and update this inventory at defined frequencies. This inventory supports risk management, compliance reporting, and security oversight across the enterprise.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Production, development, test environments |
| Cloud systems | YES | All deployment models (public, private, hybrid) |
| Third-party hosted systems | YES | Systems processing organizational data |
| Personal devices | CONDITIONAL | Only if used for business purposes |
| Decommissioned systems | YES | Until data destruction verified |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owners | • Register systems in inventory within 30 days<br>• Maintain accurate system information<br>• Report system changes within 15 days |
| IT Asset Management | • Maintain centralized system inventory<br>• Validate inventory accuracy quarterly<br>• Generate compliance reports |
| CISO Office | • Define inventory update frequencies<br>• Oversee inventory compliance<br>• Approve inventory procedures |

## 4. RULES
[RULE-01] All organizational systems MUST be registered in the centralized system inventory within 30 days of deployment or acquisition.
[VALIDATION] IF system_deployment_date + 30_days < current_date AND system_in_inventory = FALSE THEN violation

[RULE-02] The system inventory MUST be updated at least quarterly for all systems and monthly for systems processing sensitive data.
[VALIDATION] IF system_classification = "sensitive" AND last_inventory_update > 30_days THEN violation
[VALIDATION] IF system_classification = "standard" AND last_inventory_update > 90_days THEN violation

[RULE-03] Each inventory entry MUST include system name, owner, classification, location, operational status, and last update date.
[VALIDATION] IF required_fields_complete = FALSE THEN violation

[RULE-04] System changes affecting inventory data MUST be reported within 15 business days of the change.
[VALIDATION] IF system_change_date + 15_business_days < current_date AND inventory_updated = FALSE THEN violation

[RULE-05] Decommissioned systems MUST remain in inventory with "decommissioned" status until data destruction is verified and documented.
[VALIDATION] IF system_status = "decommissioned" AND data_destruction_verified = FALSE AND removal_from_inventory = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Registration Process - Standardized process for adding new systems to inventory
- [PROC-02] Inventory Validation Process - Quarterly validation of inventory accuracy and completeness
- [PROC-03] Change Management Integration - Process for updating inventory based on system changes
- [PROC-04] Decommissioning Process - Process for managing decommissioned systems in inventory

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Organizational restructure, major system acquisitions, compliance findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Cloud System Deployment]
IF system_type = "cloud"
AND deployment_date + 30_days < current_date
AND inventory_registration = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Sensitive System Update Overdue]
IF system_classification = "sensitive"
AND last_inventory_update > 30_days
AND system_status = "operational"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Incomplete Inventory Entry]
IF inventory_entry_exists = TRUE
AND (system_owner = NULL OR system_classification = NULL OR operational_status = NULL)
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unreported System Decommission]
IF system_status = "decommissioned"
AND decommission_date + 15_business_days < current_date
AND inventory_status_updated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Complete Compliant System]
IF system_in_inventory = TRUE
AND required_fields_complete = TRUE
AND update_frequency_met = TRUE
AND change_reporting_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Inventory of organizational systems is developed | [RULE-01], [RULE-03] |
| Inventory update frequency is defined | [RULE-02] |
| Inventory of organizational systems is updated per defined frequency | [RULE-02], [RULE-04] |
| System changes are reflected in inventory | [RULE-04] |
| Decommissioned systems are properly managed | [RULE-05] |