# POLICY: PM-5.1: Inventory of Personally Identifiable Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-5.1 |
| NIST Control | PM-5.1: Inventory of Personally Identifiable Information |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | PII, inventory, data mapping, privacy, systems, applications, projects |

## 1. POLICY STATEMENT
The organization SHALL establish, maintain, and regularly update a comprehensive inventory of all systems, applications, and projects that process personally identifiable information (PII). This inventory supports data mapping, privacy notices, and ensures PII processing is limited to authorized operational purposes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing PII |
| Applications | YES | All applications handling PII |
| Projects | YES | All projects involving PII processing |
| Third-party Services | YES | When processing organizational PII |
| Development/Test Systems | YES | If containing production PII |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee PII inventory program<br>• Define inventory update frequency<br>• Ensure compliance with privacy requirements |
| System Owners | • Identify PII processing in their systems<br>• Maintain accurate inventory records<br>• Report changes within required timeframes |
| Privacy Team | • Maintain centralized PII inventory<br>• Validate inventory accuracy<br>• Coordinate inventory updates |

## 4. RULES
[RULE-01] Organizations MUST establish a comprehensive inventory that includes all systems, applications, and projects processing PII.
[VALIDATION] IF system_processes_PII = TRUE AND system_in_inventory = FALSE THEN violation

[RULE-02] The PII inventory MUST be updated at the defined frequency, not to exceed quarterly intervals.
[VALIDATION] IF last_inventory_update > defined_frequency THEN violation

[RULE-03] System owners MUST report new PII processing activities within 30 days of implementation.
[VALIDATION] IF PII_processing_start_date + 30_days < current_date AND inventory_updated = FALSE THEN violation

[RULE-04] The inventory MUST include data elements, processing purposes, data sources, and retention periods for each entry.
[VALIDATION] IF inventory_entry_missing_required_fields = TRUE THEN violation

[RULE-05] Organizations MUST validate inventory accuracy through annual reviews and system assessments.
[VALIDATION] IF last_validation_date > 365_days THEN violation

[RULE-06] PII processing activities that are no longer operationally necessary MUST be identified and remediated within 90 days.
[VALIDATION] IF processing_purpose_obsolete = TRUE AND remediation_date > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Inventory Management - Establish and maintain centralized inventory database
- [PROC-02] System Assessment - Regular evaluation of systems for PII processing
- [PROC-03] Change Management - Process for reporting new PII processing activities
- [PROC-04] Data Mapping - Document PII flows and processing purposes
- [PROC-05] Inventory Validation - Annual accuracy verification process

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New system deployments, significant data processing changes, privacy incidents, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Application Deployment]
IF application_processes_PII = TRUE
AND deployment_date + 30_days < current_date
AND inventory_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Quarterly Inventory Update]
IF current_date - last_inventory_update > quarterly_frequency
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-03: Obsolete PII Processing]
IF processing_purpose = "no_longer_needed"
AND identification_date + 90_days < current_date
AND remediation_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Missing Inventory Fields]
IF inventory_entry_exists = TRUE
AND (data_elements = NULL OR processing_purpose = NULL OR retention_period = NULL)
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Third-party Service Assessment]
IF third_party_processes_org_PII = TRUE
AND service_in_inventory = TRUE
AND data_mapping_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Inventory establishment | [RULE-01] |
| Inventory maintenance | [RULE-02], [RULE-05] |
| Inventory updates | [RULE-02], [RULE-03] |
| Update frequency definition | [RULE-02] |
| Data mapping completeness | [RULE-04] |
| Operational necessity review | [RULE-06] |