# POLICY: SR-4.1: Identity

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-4.1 |
| NIST Control | SR-4.1: Identity |
| Version | 1.0 |
| Owner | Chief Supply Chain Officer |
| Keywords | supply chain, identification, personnel, elements, processes, tracking, visibility, provenance |

## 1. POLICY STATEMENT
The organization SHALL establish and maintain unique identification of all supply chain elements, processes, and personnel associated with systems and critical system components. This identification system MUST provide sufficient visibility to support risk management and incident investigation activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems and critical components | YES | Including development, production, and operational systems |
| Supply chain vendors and contractors | YES | Direct and indirect suppliers |
| Internal personnel with supply chain roles | YES | Development, procurement, and oversight staff |
| Third-party service providers | YES | Cloud providers, managed services, consultants |
| Supply chain processes | YES | All lifecycle phases from design to disposal |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Supply Chain Officer | • Define identification requirements<br>• Approve identification standards<br>• Oversee compliance monitoring |
| Supply Chain Manager | • Implement identification procedures<br>• Maintain identification records<br>• Coordinate with vendors on requirements |
| System Owner | • Identify critical system components<br>• Define component-specific requirements<br>• Validate supplier compliance |

## 4. RULES
[RULE-01] All supply chain elements associated with systems and critical components MUST have unique identifiers assigned within 5 business days of engagement.
[VALIDATION] IF supply_chain_element_exists = TRUE AND unique_id_assigned = FALSE AND days_since_engagement > 5 THEN violation

[RULE-02] Supply chain personnel with access to critical systems MUST maintain current identification records including role, responsibilities, and access levels.
[VALIDATION] IF personnel_role = "supply_chain" AND critical_system_access = TRUE AND identification_current = FALSE THEN violation

[RULE-03] Supply chain processes MUST be documented with unique process identifiers and maintained in the centralized tracking system.
[VALIDATION] IF supply_chain_process_exists = TRUE AND (unique_process_id = NULL OR centralized_tracking = FALSE) THEN violation

[RULE-04] Identification records MUST be updated within 10 business days of any supply chain changes including acquisitions, mergers, or role modifications.
[VALIDATION] IF supply_chain_change_date < (current_date - 10_business_days) AND identification_updated = FALSE THEN violation

[RULE-05] Organizations MUST maintain identification methods sufficient to support supply chain investigations and forensic analysis.
[VALIDATION] IF investigation_capability = FALSE OR forensic_traceability = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Element Registration - Process for assigning and recording unique identifiers
- [PROC-02] Personnel Identification Management - Procedures for tracking supply chain personnel
- [PROC-03] Process Documentation Standards - Requirements for documenting and identifying processes
- [PROC-04] Change Management Integration - Updating identifications during supply chain changes
- [PROC-05] Investigation Support Procedures - Maintaining records to support incident response

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Supply chain incidents, vendor changes, system modifications, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Vendor Onboarding]
IF vendor_type = "new"
AND critical_system_involvement = TRUE
AND unique_id_assigned = FALSE
AND onboarding_days > 5
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Vendor Acquisition Impact]
IF vendor_ownership_change = TRUE
AND identification_updated = FALSE
AND days_since_change > 10
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Supply Chain Investigation]
IF investigation_required = TRUE
AND identification_records_available = FALSE
AND forensic_traceability = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Personnel Role Change]
IF personnel_role_modified = TRUE
AND supply_chain_access = TRUE
AND identification_current = TRUE
AND update_within_timeframe = TRUE
THEN compliance = TRUE

[SCENARIO-05: Process Documentation Gap]
IF supply_chain_process_active = TRUE
AND unique_process_id = NULL
AND centralized_tracking = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Supply chain elements identification is defined | RULE-01, RULE-03 |
| Supply chain elements identification is established | RULE-01, RULE-02 |
| Supply chain elements identification is maintained | RULE-04, RULE-05 |
| Personnel identification requirements | RULE-02 |
| Process identification requirements | RULE-03 |
| Investigation support capability | RULE-05 |