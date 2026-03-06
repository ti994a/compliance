# POLICY: CM-12: Information Location

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-12 |
| NIST Control | CM-12: Information Location |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | information location, data mapping, system components, user access, change documentation, data inventory |

## 1. POLICY STATEMENT
The organization SHALL identify and document the location of sensitive information, the system components where it is processed and stored, and users who have access to those components. All changes to information location MUST be documented to maintain accurate data mapping and ensure appropriate protection controls.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, on-premises, and hybrid |
| Sensitive Data | YES | PII, PHI, financial, classified, proprietary |
| System Components | YES | Servers, databases, storage, network devices |
| All Users | YES | Employees, contractors, service accounts |
| Third-party Systems | YES | When processing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owners | • Define information requiring location tracking<br>• Approve access to sensitive information<br>• Review location documentation quarterly |
| System Administrators | • Maintain accurate system component inventories<br>• Document user access to system components<br>• Report location changes within 24 hours |
| Security Team | • Validate information location documentation<br>• Assess protection controls based on data location<br>• Monitor compliance with location requirements |

## 4. RULES
[RULE-01] Organizations MUST identify and document the location of all sensitive information as defined by data classification policy.
[VALIDATION] IF data_classification IN ["confidential", "restricted", "PII", "PHI"] AND location_documented = FALSE THEN violation

[RULE-02] System components that process or store sensitive information MUST be identified and documented with specific location details.
[VALIDATION] IF component_processes_sensitive_data = TRUE AND component_location_documented = FALSE THEN violation

[RULE-03] All users with access to system components containing sensitive information MUST be identified and documented.
[VALIDATION] IF user_has_access = TRUE AND sensitive_data_present = TRUE AND user_access_documented = FALSE THEN violation

[RULE-04] Changes to information processing or storage locations MUST be documented within 24 hours of implementation.
[VALIDATION] IF location_change_date < current_date AND documentation_date > (location_change_date + 24_hours) THEN violation

[RULE-05] Information location documentation MUST include data classification, system component identifiers, physical/logical location, and access control requirements.
[VALIDATION] IF location_record_missing_required_fields = TRUE THEN violation

[RULE-06] Cross-border data transfers MUST be documented with specific jurisdictional and regulatory compliance requirements.
[VALIDATION] IF data_crosses_borders = TRUE AND jurisdiction_requirements_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Location Inventory - Quarterly comprehensive review of all sensitive data locations
- [PROC-02] System Component Mapping - Continuous maintenance of component-to-data relationships
- [PROC-03] User Access Documentation - Real-time tracking of user access to sensitive data locations
- [PROC-04] Location Change Management - Process for documenting and approving location changes
- [PROC-05] Cross-Border Data Assessment - Evaluation of regulatory requirements for international data transfers

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: System architecture changes, new data types, regulatory changes, security incidents involving data location

## 7. SCENARIO PATTERNS
[SCENARIO-01: Undocumented Cloud Migration]
IF data_migrated_to_cloud = TRUE
AND migration_date < current_date
AND new_location_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Contractor Access Without Documentation]
IF user_type = "contractor"
AND access_to_sensitive_components = TRUE
AND access_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Cross-Border Data Transfer]
IF data_location_country != "US"
AND data_classification = "PII"
AND jurisdiction_compliance_documented = TRUE
AND data_owner_approved = TRUE
THEN compliance = TRUE

[SCENARIO-04: System Decommission Without Update]
IF system_status = "decommissioned"
AND decommission_date < (current_date - 30_days)
AND location_records_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Emergency Data Relocation]
IF relocation_reason = "emergency"
AND relocation_date < current_date
AND temporary_documentation_completed = TRUE
AND formal_documentation_date <= (relocation_date + 72_hours)
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information location identification and documentation | RULE-01 |
| System component processing location documentation | RULE-02 |
| System component storage location documentation | RULE-02 |
| User access to processing components documentation | RULE-03 |
| User access to storage components documentation | RULE-03 |
| Processing location change documentation | RULE-04 |
| Storage location change documentation | RULE-04 |