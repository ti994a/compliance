# POLICY: SR-4.1: Supply Chain Identity

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-4.1 |
| NIST Control | SR-4.1: Supply Chain Identity |
| Version | 1.0 |
| Owner | Chief Supply Chain Risk Officer |
| Keywords | supply chain, identity, unique identification, vendor management, provenance, supply chain elements |

## 1. POLICY STATEMENT
The organization SHALL establish and maintain unique identification of all supply chain elements, processes, and personnel associated with systems and critical system components. This identification system MUST provide sufficient detail to support investigations and maintain visibility into supply chain activities throughout the system lifecycle.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems | YES | Including development, test, and production |
| Critical system components | YES | As defined by system categorization |
| Supply chain vendors | YES | Direct and indirect suppliers |
| Third-party software | YES | Including open source components |
| Cloud service providers | YES | All service layers (IaaS, PaaS, SaaS) |
| Internal development teams | YES | When acting as supply chain elements |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Risk Manager | • Maintain supply chain identification registry<br>• Define identification requirements<br>• Monitor supply chain changes |
| System Owners | • Identify critical system components<br>• Report supply chain element changes<br>• Validate supplier identification data |
| Procurement Team | • Collect supplier identification data<br>• Verify supplier identity credentials<br>• Maintain vendor management records |
| Security Team | • Define security requirements for identification<br>• Monitor for supply chain security events<br>• Validate identification mechanisms |

## 4. RULES

[RULE-01] All supply chain elements associated with systems and critical components MUST have unique identifiers assigned within 5 business days of engagement.
[VALIDATION] IF supply_chain_element_exists = TRUE AND unique_identifier_assigned = FALSE AND days_since_engagement > 5 THEN violation

[RULE-02] Supply chain identification records MUST include organization name, contact information, role/function, geographic location, and security clearance level where applicable.
[VALIDATION] IF identification_record_exists = TRUE AND (org_name = NULL OR contact_info = NULL OR role = NULL OR location = NULL) THEN violation

[RULE-03] Supply chain personnel with access to critical components MUST undergo identity verification including background checks appropriate to system impact level.
[VALIDATION] IF personnel_access_level = "critical" AND background_check_completed = FALSE THEN critical_violation

[RULE-04] Changes to supply chain elements, processes, or personnel MUST be updated in the identification system within 48 hours of notification.
[VALIDATION] IF supply_chain_change_occurred = TRUE AND hours_since_notification > 48 AND identification_updated = FALSE THEN violation

[RULE-05] Supply chain identification data MUST be reviewed and validated quarterly for accuracy and completeness.
[VALIDATION] IF last_review_date < (current_date - 90_days) THEN violation

[RULE-06] Unique identifiers MUST support traceability for investigations and MUST NOT be reused for different supply chain elements.
[VALIDATION] IF identifier_reused = TRUE OR traceability_supported = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Element Registration - Process for assigning and maintaining unique identifiers
- [PROC-02] Identity Verification - Procedures for validating supplier and personnel identities  
- [PROC-03] Change Management - Process for updating identification records when changes occur
- [PROC-04] Quarterly Review - Systematic review of identification data accuracy and completeness
- [PROC-05] Investigation Support - Procedures for using identification data during security investigations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Supply chain security incidents, major vendor changes, system categorization changes, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Critical Component Supplier]
IF system_component_criticality = "high"
AND new_supplier_engaged = TRUE
AND unique_identifier_assigned = FALSE
AND days_since_engagement > 5
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Personnel Access Without Verification]
IF supply_chain_personnel = TRUE
AND access_to_critical_components = TRUE
AND identity_verification_completed = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Outdated Identification Records]
IF supply_chain_element_active = TRUE
AND last_identification_review > 90_days
AND quarterly_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Supply Chain Change Not Updated]
IF supplier_acquisition_occurred = TRUE
AND notification_received = TRUE
AND hours_since_notification > 48
AND identification_records_updated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Reused Identifier Investigation Impact]
IF security_investigation_active = TRUE
AND identifier_reused = TRUE
AND investigation_hindered = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Establish unique identification of supply chain elements | [RULE-01], [RULE-02] |
| Maintain unique identification of supply chain elements | [RULE-04], [RULE-05] |
| Support investigation capabilities | [RULE-06] |
| Identity verification for personnel | [RULE-03] |
| Identification data completeness | [RULE-02] |