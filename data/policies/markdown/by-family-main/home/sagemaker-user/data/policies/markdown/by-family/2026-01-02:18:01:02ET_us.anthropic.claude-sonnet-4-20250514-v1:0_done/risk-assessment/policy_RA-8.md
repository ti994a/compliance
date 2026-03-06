# POLICY: RA-8: Privacy Impact Assessments

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-8 |
| NIST Control | RA-8: Privacy Impact Assessments |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | privacy impact assessment, PIA, personally identifiable information, PII, privacy analysis, data collection |

## 1. POLICY STATEMENT
The organization SHALL conduct privacy impact assessments (PIAs) before developing or procuring information technology that processes personally identifiable information (PII) and before initiating new PII collections that meet specified criteria. PIAs must analyze privacy risks, evaluate mitigation strategies, and be maintained as living documents throughout the system and data lifecycle.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing PII |
| IT Procurement | YES | Hardware/software processing PII |
| Data Collection Programs | CONDITIONAL | Must meet collection criteria |
| Third-party Services | YES | When processing organizational PII |
| Internal Employee Systems | CONDITIONAL | Excludes routine HR systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee PIA process and methodology<br>• Review and approve all PIAs<br>• Ensure legal compliance |
| System Owners | • Initiate PIA requirements<br>• Provide system/program details<br>• Implement PIA recommendations |
| Privacy Team | • Conduct PIA analysis<br>• Document privacy risks and mitigations<br>• Update PIAs for system changes |

## 4. RULES
[RULE-01] Organizations MUST conduct a PIA before developing or procuring any information technology that processes PII.
[VALIDATION] IF system_processes_pii = TRUE AND pia_completed = FALSE AND system_status IN ["development", "procurement"] THEN violation

[RULE-02] Organizations MUST conduct a PIA before initiating new PII collections that will be processed using information technology.
[VALIDATION] IF new_pii_collection = TRUE AND uses_information_technology = TRUE AND pia_completed = FALSE THEN violation

[RULE-03] Organizations MUST conduct a PIA for PII collections enabling individual contact when identical questions are posed to 10 or more non-government individuals.
[VALIDATION] IF collection_enables_individual_contact = TRUE AND identical_questions_count >= 10 AND target_population != "government_personnel" AND pia_completed = FALSE THEN violation

[RULE-04] PIAs MUST be updated whenever changes to information technology, organizational practices, or other factors alter privacy risks.
[VALIDATION] IF (system_changes = TRUE OR practice_changes = TRUE OR risk_factors_changed = TRUE) AND pia_last_updated < change_date THEN violation

[RULE-05] PIAs MUST include analysis of privacy risks, applicable privacy requirements, and mitigation strategies with sufficient clarity and specificity.
[VALIDATION] IF pia_exists = TRUE AND (privacy_risk_analysis = FALSE OR requirements_analysis = FALSE OR mitigation_strategies = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PIA Initiation Process - Triggers and workflow for starting PIAs
- [PROC-02] PIA Content Standards - Required analysis components and documentation format
- [PROC-03] PIA Review and Approval - Review criteria and approval authority
- [PROC-04] PIA Update Management - Change detection and update procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New privacy regulations, significant organizational changes, privacy incidents

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Customer Portal Development]
IF system_type = "customer_portal"
AND processes_customer_pii = TRUE
AND development_phase = "planning"
AND pia_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Cloud Service Procurement]
IF procurement_type = "cloud_service"
AND service_processes_pii = TRUE
AND contract_signed = FALSE
AND pia_completed = TRUE
THEN compliance = TRUE

[SCENARIO-03: Marketing Survey Launch]
IF activity_type = "survey"
AND respondent_count >= 10
AND collects_contact_information = TRUE
AND target_audience = "external_customers"
AND pia_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: System Enhancement Deployment]
IF system_modification = TRUE
AND privacy_risk_impact = "increased"
AND pia_last_updated < modification_date
AND days_since_modification > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Internal Employee Directory]
IF system_type = "employee_directory"
AND user_base = "internal_employees_only"
AND data_type = "basic_contact_info"
AND routine_hr_function = TRUE
THEN pia_required = FALSE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| PIA before IT development/procurement processing PII | [RULE-01] |
| PIA before new PII collection using IT | [RULE-02] |
| PIA before collection enabling individual contact (10+ non-gov) | [RULE-03] |
| PIA updates for system/practice changes | [RULE-04] |
| PIA content and analysis requirements | [RULE-05] |