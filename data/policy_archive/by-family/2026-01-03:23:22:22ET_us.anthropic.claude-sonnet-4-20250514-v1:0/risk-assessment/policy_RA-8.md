# POLICY: RA-8: Privacy Impact Assessments

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-8 |
| NIST Control | RA-8: Privacy Impact Assessments |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | privacy impact assessment, PIA, personally identifiable information, PII, privacy risk, data collection |

## 1. POLICY STATEMENT
The organization SHALL conduct privacy impact assessments (PIAs) before developing, procuring, or deploying information technology that processes personally identifiable information (PII). PIAs SHALL be conducted before initiating new PII collections that meet specified criteria and SHALL be maintained as living documents throughout the system lifecycle.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing PII |
| IT Procurement | YES | Before acquiring PII-processing technology |
| Data Collection Programs | CONDITIONAL | When meeting collection criteria thresholds |
| Third-party Services | YES | When processing organizational PII |
| Development Projects | YES | Before deployment of PII-processing capabilities |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee PIA process and approval<br>• Ensure PIA quality and completeness<br>• Coordinate with legal counsel and stakeholders |
| System Owners | • Initiate PIA requirements<br>• Provide system and data flow information<br>• Implement PIA recommendations |
| Program Managers | • Ensure PIA completion before project milestones<br>• Allocate resources for PIA activities<br>• Coordinate with privacy office |

## 4. RULES
[RULE-01] Organizations MUST conduct PIAs before developing or procuring information technology that processes PII.
[VALIDATION] IF system_processes_PII = TRUE AND development_started = TRUE AND PIA_completed = FALSE THEN violation

[RULE-02] Organizations MUST conduct PIAs before initiating new PII collections processed using information technology.
[VALIDATION] IF new_PII_collection = TRUE AND uses_IT = TRUE AND PIA_completed = FALSE THEN violation

[RULE-03] Organizations MUST conduct PIAs for PII collections that permit contacting individuals when identical questions are posed to 10 or more non-government individuals.
[VALIDATION] IF collection_permits_contact = TRUE AND identical_questions = TRUE AND respondent_count >= 10 AND respondent_type != "government" AND PIA_completed = FALSE THEN violation

[RULE-04] PIAs MUST be updated when changes to technology, practices, or other factors alter privacy risks.
[VALIDATION] IF (system_change = TRUE OR practice_change = TRUE OR risk_change = TRUE) AND PIA_update_completed = FALSE THEN violation

[RULE-05] PIAs MUST include analysis of PII handling conformance to privacy requirements and risk mitigation strategies.
[VALIDATION] IF PIA_exists = TRUE AND (privacy_requirements_analysis = FALSE OR risk_mitigation_analysis = FALSE) THEN violation

[RULE-06] PIAs MUST be initiated and conducted with participation from privacy officials, program managers, system owners, and relevant stakeholders.
[VALIDATION] IF PIA_initiated = TRUE AND (privacy_official_involved = FALSE OR program_manager_involved = FALSE OR system_owner_involved = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PIA Initiation Process - Triggers and stakeholder notification procedures
- [PROC-02] PIA Development Methodology - Assessment framework and analysis requirements
- [PROC-03] PIA Review and Approval - Quality assurance and approval workflow
- [PROC-04] PIA Update Process - Change management and update triggers
- [PROC-05] PIA Publication Process - Public disclosure requirements and procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Regulatory changes, significant privacy incidents, organizational restructuring

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Customer Portal Development]
IF system_type = "customer_portal"
AND processes_customer_PII = TRUE
AND development_phase = "requirements"
AND PIA_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Third-party Analytics Service]
IF service_type = "analytics"
AND vendor_processes_PII = TRUE
AND procurement_approved = TRUE
AND PIA_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Employee Survey Platform]
IF collection_type = "survey"
AND respondent_count = 15
AND respondent_type = "employees"
AND identical_questions = TRUE
THEN compliance = TRUE
violation_severity = "None"

[SCENARIO-04: Customer Feedback System Change]
IF system_exists = TRUE
AND PII_processing_expanded = TRUE
AND system_change_date < current_date - 30_days
AND PIA_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Public Research Data Collection]
IF collection_type = "research"
AND respondent_count = 25
AND respondent_type = "public"
AND permits_individual_contact = TRUE
AND PIA_completed = TRUE
THEN compliance = TRUE
violation_severity = "None"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| PIAs conducted before IT development/procurement | [RULE-01] |
| PIAs conducted before new PII collections using IT | [RULE-02] |
| PIAs conducted for collections meeting contact criteria | [RULE-03] |
| PIAs updated when risks change | [RULE-04] |
| PIAs include required analysis components | [RULE-05] |
| PIAs involve appropriate stakeholders | [RULE-06] |