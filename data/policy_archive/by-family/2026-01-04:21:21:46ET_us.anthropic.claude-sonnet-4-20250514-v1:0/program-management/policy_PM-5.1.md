# POLICY: PM-5.1: Inventory of Personally Identifiable Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-5.1 |
| NIST Control | PM-5.1: Inventory of Personally Identifiable Information |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII inventory, data mapping, privacy compliance, system inventory, data processing |

## 1. POLICY STATEMENT
The organization SHALL establish, maintain, and regularly update a comprehensive inventory of all systems, applications, and projects that process personally identifiable information (PII). This inventory supports data mapping, privacy notices, data accuracy, and ensures PII processing is limited to authorized operational purposes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing PII |
| Applications | YES | Including SaaS, on-premises, and cloud applications |
| Projects | YES | Development, research, and operational projects |
| Third-party Services | YES | Vendors and contractors processing PII |
| Shadow IT | YES | Unauthorized systems discovered processing PII |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee PII inventory program<br>• Define inventory update frequency<br>• Ensure regulatory compliance |
| Data Protection Officer | • Maintain PII inventory accuracy<br>• Coordinate with system owners<br>• Validate data mapping documentation |
| System Owners | • Report PII processing activities<br>• Provide system classification data<br>• Notify of changes to PII processing |

## 4. RULES
[RULE-01] The organization MUST establish and maintain a comprehensive inventory of all systems, applications, and projects that process PII.
[VALIDATION] IF system_processes_pii = TRUE AND system_in_inventory = FALSE THEN violation

[RULE-02] PII inventory update frequency MUST be defined and documented, with updates occurring at minimum quarterly.
[VALIDATION] IF update_frequency_defined = FALSE OR last_update > defined_frequency THEN violation

[RULE-03] Each inventory entry MUST include system/application name, data types processed, processing purposes, data sources, and retention periods.
[VALIDATION] IF inventory_entry_complete = FALSE OR missing_required_fields > 0 THEN violation

[RULE-04] New systems, applications, or projects processing PII MUST be added to the inventory within 30 days of deployment or PII processing initiation.
[VALIDATION] IF pii_processing_start_date + 30_days < current_date AND system_in_inventory = FALSE THEN violation

[RULE-05] Decommissioned systems MUST be removed from the PII inventory within 15 days of confirmed data deletion.
[VALIDATION] IF system_status = "decommissioned" AND data_deletion_confirmed = TRUE AND days_since_deletion > 15 AND system_in_inventory = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Discovery and Classification - Systematic identification and categorization of PII processing activities
- [PROC-02] Inventory Maintenance - Regular updates and validation of inventory accuracy
- [PROC-03] Data Mapping Integration - Linking inventory to detailed data flow documentation
- [PROC-04] Change Management Integration - Automated notifications for new PII processing activities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New regulatory requirements, significant data breaches, major system implementations, organizational restructuring

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Application Deployment]
IF application_deployed = TRUE
AND processes_pii = TRUE
AND days_since_deployment > 30
AND inventory_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: System Decommissioning]
IF system_status = "decommissioned"
AND pii_deletion_confirmed = TRUE
AND days_since_deletion > 15
AND removed_from_inventory = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-03: Quarterly Inventory Update]
IF current_date > last_inventory_update + 90_days
AND update_frequency = "quarterly"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Inventory Fields]
IF inventory_entry_exists = TRUE
AND (data_types_missing = TRUE OR processing_purpose_missing = TRUE OR retention_period_missing = TRUE)
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Shadow IT Discovery]
IF unauthorized_system_discovered = TRUE
AND processes_pii = TRUE
AND discovery_date + 30_days < current_date
AND inventory_updated = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Inventory establishment | [RULE-01] |
| Inventory maintenance | [RULE-02], [RULE-04], [RULE-05] |
| Update frequency definition | [RULE-02] |
| Inventory completeness | [RULE-03] |
| Timely inventory updates | [RULE-04], [RULE-05] |