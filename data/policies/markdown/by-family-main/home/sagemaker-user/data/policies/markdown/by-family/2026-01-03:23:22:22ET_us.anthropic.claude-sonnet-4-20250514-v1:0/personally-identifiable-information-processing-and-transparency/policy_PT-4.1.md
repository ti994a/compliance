# POLICY: PT-4.1: Tailored Consent

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-4.1 |
| NIST Control | PT-4.1: Tailored Consent |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | tailored consent, PII processing, individual permissions, privacy controls, consent mechanisms |

## 1. POLICY STATEMENT
The organization must provide tailoring mechanisms that allow individuals to selectively control processing permissions for specific elements of their personally identifiable information (PII). These mechanisms must distinguish between necessary processing for basic functionality and optional processing activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Must implement tailored consent mechanisms |
| Third-party processors | YES | Must support tailored consent requirements |
| Emergency processing systems | CONDITIONAL | May have limited tailoring for life safety functions |
| Anonymous data systems | NO | No PII processing requiring consent |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Define tailoring mechanism requirements<br>• Approve consent interface designs<br>• Monitor compliance with tailored consent policies |
| Product Managers | • Implement tailored consent mechanisms in systems<br>• Ensure user interface supports granular permissions<br>• Document PII processing categories |
| Development Teams | • Build consent management interfaces<br>• Implement granular permission controls<br>• Maintain consent preference databases |

## 4. RULES
[RULE-01] Systems processing PII MUST provide tailoring mechanisms that allow individuals to grant or deny permissions for specific PII elements beyond those required for basic functionality.
[VALIDATION] IF system_processes_PII = TRUE AND tailored_consent_mechanism = FALSE THEN violation

[RULE-02] Tailoring mechanisms MUST clearly distinguish between PII processing that is necessary for basic service functionality and optional processing activities.
[VALIDATION] IF consent_interface_deployed = TRUE AND necessary_vs_optional_distinction = FALSE THEN violation

[RULE-03] Individuals MUST be able to modify their tailored consent preferences at any time through accessible mechanisms.
[VALIDATION] IF consent_modification_available = FALSE OR consent_modification_accessible = FALSE THEN violation

[RULE-04] Systems MUST honor tailored consent preferences within 24 hours of any changes made by individuals.
[VALIDATION] IF consent_change_time > 24_hours AND processing_updated = FALSE THEN violation

[RULE-05] Tailored consent mechanisms MUST maintain audit logs of all permission grants, denials, and modifications for at least 3 years.
[VALIDATION] IF consent_audit_log = FALSE OR log_retention < 3_years THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Consent Interface Design - Design and implement user interfaces for tailored consent management
- [PROC-02] PII Processing Classification - Categorize PII processing as necessary vs. optional
- [PROC-03] Consent Preference Management - Maintain and update individual consent preferences
- [PROC-04] Consent Audit Review - Regular review of consent logs and compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New PII processing activities, privacy incidents, regulatory changes, user interface updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Marketing Email Preferences]
IF system_collects_email = TRUE
AND email_used_for_marketing = TRUE
AND tailored_consent_for_marketing = TRUE
AND individual_opted_out = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Consent Granularity]
IF system_processes_multiple_PII_types = TRUE
AND consent_mechanism = "all_or_nothing"
AND optional_processing_exists = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Delayed Consent Processing]
IF individual_updated_preferences = TRUE
AND time_since_update = 48_hours
AND old_preferences_still_active = TRUE
THEN compliance = FALSE
violation_severity = "Minor"

[SCENARIO-04: Accessible Consent Management]
IF tailored_consent_deployed = TRUE
AND consent_modification_interface = "available"
AND accessibility_compliant = TRUE
AND user_can_change_preferences = TRUE
THEN compliance = TRUE

[SCENARIO-05: Audit Trail Gap]
IF consent_changes_logged = FALSE
OR consent_log_retention < 3_years
AND audit_requested = TRUE
THEN compliance = FALSE
violation_severity = "Major"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Tailoring mechanisms for processing selected PII elements are defined | RULE-01, RULE-02 |
| Mechanisms allow individuals to tailor processing permissions | RULE-01, RULE-03 |
| Processing permissions apply to selected PII elements | RULE-02, RULE-04 |