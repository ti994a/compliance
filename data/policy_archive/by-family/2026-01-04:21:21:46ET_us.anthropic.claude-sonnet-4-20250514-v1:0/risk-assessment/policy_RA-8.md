# POLICY: RA-8: Privacy Impact Assessments

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-8 |
| NIST Control | RA-8: Privacy Impact Assessments |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | privacy impact assessment, PII, personally identifiable information, privacy analysis, risk assessment |

## 1. POLICY STATEMENT
The organization SHALL conduct privacy impact assessments (PIAs) before developing, procuring, or deploying information technology that processes personally identifiable information (PII). PIAs SHALL analyze privacy risks and evaluate mitigation strategies throughout the system and PII lifecycle.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing PII |
| IT Procurement | YES | Technology that will process PII |
| Data Collection Programs | CONDITIONAL | Collections meeting PII criteria |
| Third-party Services | YES | Vendors processing organizational PII |
| Mobile Applications | YES | Apps collecting or processing PII |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee PIA program governance<br>• Review and approve PIAs<br>• Ensure regulatory compliance |
| System Owners | • Initiate PIA process for their systems<br>• Provide system documentation and requirements<br>• Implement PIA recommendations |
| Privacy Team | • Conduct PIA analysis<br>• Document privacy risks and mitigations<br>• Maintain PIA repository |
| Legal Counsel | • Review regulatory requirements<br>• Validate legal compliance<br>• Approve public-facing PIAs |

## 4. RULES
[RULE-01] Organizations MUST conduct PIAs before developing or procuring information technology that processes PII.
[VALIDATION] IF system_processes_PII = TRUE AND pia_completed = FALSE AND system_status IN ["development", "procurement"] THEN violation

[RULE-02] Organizations MUST conduct PIAs before initiating new PII collections that will be processed using information technology.
[VALIDATION] IF new_pii_collection = TRUE AND uses_information_technology = TRUE AND pia_completed = FALSE THEN violation

[RULE-03] PIAs MUST be conducted for PII collections that permit contacting specific individuals when identical questions are posed to 10 or more non-government individuals.
[VALIDATION] IF collection_permits_contact = TRUE AND identical_questions = TRUE AND individual_count >= 10 AND non_government = TRUE AND pia_completed = FALSE THEN violation

[RULE-04] PIAs MUST be updated as living documents whenever changes to technology, practices, or other factors alter privacy risks.
[VALIDATION] IF (technology_change = TRUE OR practice_change = TRUE OR risk_factors_changed = TRUE) AND pia_update_completed = FALSE THEN violation

[RULE-05] PIAs MUST include analysis of privacy risks, handling conformance to requirements, and mitigation strategies.
[VALIDATION] IF pia_exists = TRUE AND (privacy_risk_analysis = FALSE OR handling_conformance_analysis = FALSE OR mitigation_strategies = FALSE) THEN violation

[RULE-06] PIAs MUST be completed with sufficient clarity and specificity to demonstrate full privacy consideration from earliest stages.
[VALIDATION] IF pia_clarity_score < minimum_threshold OR privacy_consideration_timing != "earliest_stages" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PIA Initiation Process - Trigger assessment based on system lifecycle events
- [PROC-02] PIA Conduct Methodology - Standardized analysis framework and documentation
- [PROC-03] PIA Review and Approval - Multi-stakeholder validation process
- [PROC-04] PIA Update Management - Change-triggered review and revision process
- [PROC-05] PIA Repository Management - Centralized storage and access controls

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New privacy regulations, significant data breaches, organizational restructuring, technology platform changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New CRM System Procurement]
IF system_type = "CRM"
AND processes_customer_pii = TRUE
AND procurement_phase = "active"
AND pia_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Mobile App Data Collection]
IF application_type = "mobile"
AND collects_contact_information = TRUE
AND user_count >= 10
AND users_are_external = TRUE
AND pia_conducted = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: System Enhancement with New PII Fields]
IF system_change_type = "enhancement"
AND new_pii_fields_added = TRUE
AND pia_updated = FALSE
AND days_since_change > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Third-party Service Integration]
IF integration_type = "third_party_service"
AND service_processes_pii = TRUE
AND pia_covers_third_party = FALSE
AND integration_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Internal Employee Survey System]
IF collection_type = "survey"
AND target_audience = "employees"
AND identical_questions = TRUE
AND employee_count >= 10
THEN compliance = TRUE
Notes = "Government employees exempt from 10+ rule"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| PIAs conducted before IT development/procurement processing PII | [RULE-01] |
| PIAs conducted before initiating PII collections using IT | [RULE-02] |
| PIAs conducted for collections permitting individual contact (10+ non-gov) | [RULE-03] |
| PIAs maintained as living documents with updates | [RULE-04] |
| PIAs include comprehensive privacy risk analysis | [RULE-05] |
| PIAs demonstrate thorough privacy consideration | [RULE-06] |