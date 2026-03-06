# POLICY: SR-4.1: Supply Chain Identity

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-4.1 |
| NIST Control | SR-4.1: Supply Chain Identity |
| Version | 1.0 |
| Owner | Chief Supply Chain Officer |
| Keywords | supply chain, identification, visibility, personnel, processes, elements |

## 1. POLICY STATEMENT
The organization SHALL establish and maintain unique identification of all supply chain elements, processes, and personnel associated with systems and critical system components. This identification system MUST provide sufficient visibility to support risk management and incident investigation activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems | YES | Including development, test, and production |
| Critical system components | YES | As defined in system categorization |
| Supply chain vendors | YES | Direct and indirect suppliers |
| Third-party personnel | YES | With system access or involvement |
| Development processes | YES | Hardware, software, firmware |
| Manufacturing processes | YES | Including assembly and integration |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Supply Chain Officer | • Oversee supply chain identification program<br>• Approve identification standards<br>• Ensure compliance monitoring |
| System Owners | • Identify critical system components<br>• Maintain supplier inventories<br>• Report supply chain changes |
| Procurement Team | • Collect supplier identification data<br>• Verify identification authenticity<br>• Maintain supplier databases |

## 4. RULES
[RULE-01] All supply chain elements associated with systems and critical components MUST have unique identifiers assigned within 30 days of engagement.
[VALIDATION] IF supply_chain_element EXISTS AND unique_identifier = NULL AND days_since_engagement > 30 THEN violation

[RULE-02] Supply chain personnel with system access or security responsibilities MUST be individually identified and tracked in the supplier database.
[VALIDATION] IF personnel_type = "supply_chain" AND (system_access = TRUE OR security_role = TRUE) AND individual_identification = FALSE THEN violation

[RULE-03] Supply chain processes for development, manufacturing, and delivery MUST be documented with unique process identifiers and version control.
[VALIDATION] IF process_type IN ["development", "manufacturing", "delivery"] AND (unique_process_id = NULL OR version_control = FALSE) THEN violation

[RULE-04] Identification records MUST be maintained for the entire lifecycle of the system or component plus 3 years after disposal.
[VALIDATION] IF system_status = "disposed" AND disposal_date + 3_years < current_date AND identification_records = "deleted" THEN violation

[RULE-05] Supply chain identification changes MUST be reported within 72 hours and investigated for security impact.
[VALIDATION] IF identification_change_detected = TRUE AND reporting_time > 72_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Element Registration - Process for assigning unique identifiers to new suppliers
- [PROC-02] Personnel Identification Verification - Validation of individual supplier personnel credentials
- [PROC-03] Process Documentation Standards - Requirements for documenting and identifying supply chain processes
- [PROC-04] Change Notification Protocol - Procedures for reporting and investigating identification changes
- [PROC-05] Records Retention Management - Lifecycle management of identification records

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Supply chain incidents, major supplier changes, system categorization updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Critical Supplier]
IF supplier_type = "new"
AND system_criticality = "high"
AND unique_identifier = NULL
AND days_since_contract > 30
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Undocumented Personnel Access]
IF personnel_type = "supplier"
AND system_access = TRUE
AND individual_identification = FALSE
AND background_check = "not_verified"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Process Change Without Notification]
IF supply_chain_process = "modified"
AND process_criticality = "high"
AND change_notification = FALSE
AND days_since_change > 3
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Expired Identification Records]
IF system_status = "disposed"
AND disposal_date + 3_years < current_date
AND identification_records = "maintained"
AND legal_hold = FALSE
THEN compliance = TRUE

[SCENARIO-05: Supplier Acquisition Event]
IF supplier_ownership_change = TRUE
AND identification_update = "pending"
AND investigation_initiated = TRUE
AND days_since_change <= 30
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Unique identification establishment | [RULE-01] |
| Personnel identification tracking | [RULE-02] |
| Process documentation requirements | [RULE-03] |
| Records maintenance | [RULE-04] |
| Change management | [RULE-05] |