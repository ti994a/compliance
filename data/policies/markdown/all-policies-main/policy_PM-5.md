```markdown
# POLICY: PM-5: System Inventory

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-5 |
| NIST Control | PM-5: System Inventory |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | system inventory, asset management, organizational systems, inventory maintenance, system tracking |

## 1. POLICY STATEMENT
The organization SHALL develop and maintain a comprehensive inventory of all organizational systems and update this inventory at defined frequencies. The system inventory serves as the foundation for cybersecurity risk management and compliance activities across the enterprise.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing, storing, or transmitting organizational data |
| Cloud Services | YES | Including SaaS, PaaS, and IaaS implementations |
| Legacy Systems | YES | Including systems pending decommission |
| Development/Test Systems | YES | Systems containing production-like data |
| Personal Devices (BYOD) | CONDITIONAL | Only if accessing organizational systems |
| Vendor Systems | CONDITIONAL | Only if processing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Establish inventory policy and procedures<br>• Approve inventory update frequencies<br>• Ensure compliance with reporting requirements |
| System Owners | • Provide accurate system information<br>• Report system changes within required timeframes<br>• Validate inventory data accuracy |
| IT Asset Management | • Maintain centralized inventory database<br>• Execute periodic inventory updates<br>• Generate compliance reports |

## 4. RULES

[RULE-01] The organization MUST maintain a comprehensive inventory of all organizational systems that includes system name, owner, operational status, data classification, and last update date.
[VALIDATION] IF system_in_environment = TRUE AND system_in_inventory = FALSE THEN critical_violation

[RULE-02] System inventory updates MUST occur at least quarterly for production systems and annually for development/test systems.
[VALIDATION] IF system_type = "production" AND last_update > 90_days THEN violation
[VALIDATION] IF system_type = "development" AND last_update > 365_days THEN violation

[RULE-03] New systems MUST be added to the inventory within 30 days of deployment or go-live.
[VALIDATION] IF system_deployment_date + 30_days < current_date AND system_in_inventory = FALSE THEN violation

[RULE-04] Decommissioned systems MUST be marked as retired in the inventory within 15 days of decommission and retained for audit purposes for 3 years.
[VALIDATION] IF system_status = "decommissioned" AND inventory_update_date > decommission_date + 15_days THEN violation

[RULE-05] System inventory data MUST include criticality level, data types processed, regulatory requirements, and technical points of contact.
[VALIDATION] IF required_fields_complete = FALSE THEN violation

[RULE-06] Inventory accuracy MUST be validated through automated discovery tools at least monthly and manual verification annually.
[VALIDATION] IF automated_scan_date > 30_days THEN violation
[VALIDATION] IF manual_verification_date > 365_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Registration Process - Standardized process for adding new systems to inventory
- [PROC-02] Inventory Update Procedures - Regular update and validation procedures
- [PROC-03] Discovery Tool Configuration - Automated scanning and discovery processes
- [PROC-04] Decommission Tracking - Process for managing end-of-life systems
- [PROC-05] Inventory Reporting - Compliance and management reporting procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major infrastructure changes, merger/acquisition, significant security incidents, regulatory changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Cloud Service Deployment]
IF system_type = "cloud_service"
AND deployment_date + 30_days < current_date
AND inventory_status = "not_registered"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Quarterly Update Missing]
IF system_type = "production"
AND last_inventory_update > 90_days
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Decommissioned System Still Active]
IF system_status = "decommissioned"
AND automated_scan_result = "active"
AND decommission_date + 15_days < current_date
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Incomplete System Information]
IF system_in_inventory = TRUE
AND (criticality_level = NULL OR data_classification = NULL OR owner = NULL)
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Discovery Tool Gap]
IF automated_discovery_scan = FALSE
AND last_scan_date > 30_days
AND manual_verification_only = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Inventory development | RULE-01, RULE-03 |
| Inventory maintenance | RULE-02, RULE-04 |
| Update frequency definition | RULE-02, RULE-06 |
| Completeness validation | RULE-05, RULE-06 |
| Organizational coverage | RULE-01, RULE-03 |
```