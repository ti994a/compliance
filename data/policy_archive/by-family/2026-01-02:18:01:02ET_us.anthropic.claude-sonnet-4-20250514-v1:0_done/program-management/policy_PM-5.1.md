# POLICY: PM-5.1: Inventory of Personally Identifiable Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-5.1 |
| NIST Control | PM-5.1: Inventory of Personally Identifiable Information |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII inventory, data mapping, privacy controls, system inventory, data processing |

## 1. POLICY STATEMENT
The organization SHALL establish, maintain, and regularly update a comprehensive inventory of all systems, applications, and projects that process personally identifiable information (PII). This inventory supports data mapping, privacy notices, accurate PII maintenance, and ensures processing is limited to authorized operational purposes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT Systems | YES | Including cloud, on-premises, hybrid |
| Applications | YES | Custom, COTS, SaaS applications |
| Projects | YES | Development, research, analytics projects |
| Third-party Systems | YES | Vendor systems processing company PII |
| Test/Dev Environments | YES | If containing real PII data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Establish PII inventory framework<br>• Define update frequencies<br>• Oversee compliance monitoring |
| System Owners | • Identify PII processing in their systems<br>• Report changes to PII processing<br>• Maintain system-level PII documentation |
| Data Protection Team | • Maintain centralized PII inventory<br>• Conduct periodic inventory reviews<br>• Validate inventory accuracy |

## 4. RULES
[RULE-01] All systems, applications, and projects that process PII MUST be included in the centralized PII inventory within 30 days of deployment or PII processing initiation.
[VALIDATION] IF system_processes_PII = TRUE AND inventory_entry_date > (deployment_date + 30_days) THEN violation

[RULE-02] The PII inventory MUST be updated at least quarterly and within 15 days of any material changes to PII processing activities.
[VALIDATION] IF last_inventory_update > 90_days THEN violation
[VALIDATION] IF material_change_date > (last_update_date + 15_days) THEN violation

[RULE-03] Each inventory entry MUST document the types of PII processed, processing purposes, data sources, retention periods, and authorized personnel.
[VALIDATION] IF inventory_entry.required_fields.complete = FALSE THEN violation

[RULE-04] System owners MUST notify the Data Protection Team within 5 business days of new PII processing activities or cessation of PII processing.
[VALIDATION] IF pii_processing_change = TRUE AND notification_delay > 5_business_days THEN violation

[RULE-05] The PII inventory MUST be reviewed annually for accuracy and completeness by system owners and validated by the Data Protection Team.
[VALIDATION] IF annual_review_date > (current_date - 365_days) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Inventory Management - Standardized process for creating and maintaining inventory entries
- [PROC-02] Change Notification Process - Workflow for reporting PII processing changes
- [PROC-03] Quarterly Inventory Review - Systematic review of all inventory entries
- [PROC-04] Data Discovery and Classification - Automated and manual PII identification methods

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New regulatory requirements, major system changes, data breaches involving PII

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Application Deployment]
IF application_deployed = TRUE
AND processes_PII = TRUE
AND inventory_entry_exists = FALSE
AND days_since_deployment > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Quarterly Update Missed]
IF current_date > (last_inventory_update + 90_days)
AND no_material_changes = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-03: Incomplete Inventory Entry]
IF inventory_entry_exists = TRUE
AND required_fields_complete < 100%
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unreported PII Processing Change]
IF pii_processing_modified = TRUE
AND notification_sent = FALSE
AND days_since_change > 5
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Annual Review Overdue]
IF last_annual_review > 365_days_ago
AND system_owner_validation = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Inventory establishment | RULE-01, RULE-03 |
| Inventory maintenance | RULE-02, RULE-04 |
| Update frequency definition | RULE-02, RULE-05 |
| Inventory accuracy validation | RULE-05, PROC-03 |