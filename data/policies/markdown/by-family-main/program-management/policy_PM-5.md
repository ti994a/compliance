# POLICY: PM-5: System Inventory

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-5 |
| NIST Control | PM-5: System Inventory |
| Version | 1.0 |
| Owner | Chief Information Officer |
| Keywords | system inventory, organizational systems, inventory management, asset tracking, FISMA reporting |

## 1. POLICY STATEMENT
The organization SHALL develop and maintain a comprehensive inventory of all organizational systems and establish a defined frequency for updating this inventory. This inventory supports risk management, compliance reporting, and organizational oversight of information systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Including cloud, on-premises, and hybrid systems |
| System components | NO | Covered under CM-8, not this control |
| Third-party hosted systems | YES | If organization maintains operational control |
| Development/test systems | YES | All systems regardless of environment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Information Officer | • Approve system inventory policy and procedures<br>• Ensure adequate resources for inventory maintenance<br>• Review inventory completeness annually |
| System Inventory Manager | • Maintain organization-wide system inventory<br>• Coordinate with system owners for updates<br>• Generate required compliance reports |
| System Owners | • Provide accurate system information<br>• Notify of system changes within defined timeframes<br>• Validate system inventory entries quarterly |

## 4. RULES
[RULE-01] The organization MUST maintain a comprehensive inventory of all organizational systems.
[VALIDATION] IF system_exists = TRUE AND system_in_inventory = FALSE THEN violation

[RULE-02] The system inventory update frequency MUST be formally defined and documented.
[VALIDATION] IF update_frequency_defined = FALSE OR update_frequency_documented = FALSE THEN violation

[RULE-03] System inventory updates MUST occur at the defined frequency, not to exceed annually.
[VALIDATION] IF days_since_last_update > defined_frequency_days THEN violation

[RULE-04] New systems MUST be added to the inventory within 30 days of deployment to production.
[VALIDATION] IF system_production_date < (current_date - 30_days) AND system_in_inventory = FALSE THEN violation

[RULE-05] Decommissioned systems MUST be removed from the inventory within 15 days of decommissioning.
[VALIDATION] IF system_status = "decommissioned" AND days_since_decommission > 15 AND system_in_inventory = TRUE THEN violation

[RULE-06] System inventory records MUST include minimum required data elements as defined in procedures.
[VALIDATION] IF required_data_elements_complete < 100% THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Inventory Development - Establish initial comprehensive inventory
- [PROC-02] System Inventory Maintenance - Regular update and validation processes
- [PROC-03] System Discovery and Registration - Process for identifying and adding new systems
- [PROC-04] Inventory Reporting - Generate compliance and management reports
- [PROC-05] System Decommissioning Updates - Remove retired systems from inventory

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major organizational changes, system architecture changes, compliance findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Cloud System Not Inventoried]
IF system_type = "cloud"
AND production_deployment_date < (current_date - 45_days)
AND system_in_inventory = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Inventory Update Overdue]
IF last_inventory_update_date < (current_date - 365_days)
AND defined_update_frequency = "annually"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Decommissioned System Still Listed]
IF system_status = "decommissioned"
AND decommission_date < (current_date - 30_days)
AND system_in_inventory = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Missing Required Data Elements]
IF system_in_inventory = TRUE
AND required_data_completeness < 80%
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Quarterly Update]
IF last_inventory_update_date > (current_date - 90_days)
AND defined_update_frequency = "quarterly"
AND inventory_accuracy_validated = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Inventory of organizational systems is developed | [RULE-01], [RULE-06] |
| Update frequency is defined | [RULE-02] |
| Inventory is updated at defined frequency | [RULE-03] |
| New systems are promptly inventoried | [RULE-04] |
| Decommissioned systems are removed | [RULE-05] |