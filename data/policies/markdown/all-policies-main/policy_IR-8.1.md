# POLICY: IR-8.1: Breaches

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IR-8.1 |
| NIST Control | IR-8.1: Breaches |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | breach, PII, incident response, notification, privacy, harm assessment |

## 1. POLICY STATEMENT
The organization must maintain comprehensive incident response procedures for breaches involving personally identifiable information (PII) that include notification determination processes, harm assessment procedures, and privacy requirement identification. These procedures ensure legal compliance and minimize harm to affected individuals through structured breach response protocols.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Systems processing, storing, or transmitting PII |
| Cloud services | YES | Including third-party services handling PII |
| Mobile applications | YES | Apps collecting or processing PII |
| Backup systems | YES | Systems containing PII backups |
| Development/test environments | CONDITIONAL | Only if containing production PII |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee breach response procedures<br>• Determine notification requirements<br>• Coordinate with legal and compliance teams |
| Incident Response Team | • Execute breach response procedures<br>• Conduct harm assessments<br>• Document breach activities |
| Legal Counsel | • Identify applicable privacy requirements<br>• Review notification decisions<br>• Ensure regulatory compliance |
| CISO | • Coordinate security aspects of breach response<br>• Approve incident response plan updates<br>• Interface with oversight organizations |

## 4. RULES
[RULE-01] The incident response plan MUST include documented procedures for determining notification requirements to individuals, organizations, and oversight bodies for all PII breaches.
[VALIDATION] IF breach_involves_PII = TRUE AND notification_process_documented = FALSE THEN violation

[RULE-02] Harm assessment procedures MUST be established to evaluate the extent of harm, embarrassment, inconvenience, or unfairness to affected individuals within 24 hours of breach confirmation.
[VALIDATION] IF PII_breach_confirmed = TRUE AND harm_assessment_initiated = FALSE AND hours_elapsed > 24 THEN violation

[RULE-03] The incident response plan MUST identify all applicable privacy requirements including federal, state, and contractual obligations for PII breach response.
[VALIDATION] IF incident_response_plan_exists = TRUE AND privacy_requirements_identified = FALSE THEN violation

[RULE-04] Mitigation mechanisms MUST be documented and implemented to address identified harms to affected individuals within 72 hours of harm assessment completion.
[VALIDATION] IF harm_assessment_complete = TRUE AND mitigation_implemented = FALSE AND hours_elapsed > 72 THEN violation

[RULE-05] Breach notification decisions MUST be documented with justification and reviewed by legal counsel within 48 hours of breach confirmation.
[VALIDATION] IF PII_breach_confirmed = TRUE AND notification_decision_documented = FALSE AND hours_elapsed > 48 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] PII Breach Classification - Procedures for identifying and classifying breaches involving PII
- [PROC-02] Notification Decision Matrix - Framework for determining required notifications based on breach characteristics
- [PROC-03] Harm Assessment Protocol - Standardized process for evaluating potential harm to individuals
- [PROC-04] Privacy Requirement Mapping - Process for identifying applicable privacy laws and regulations
- [PROC-05] Mitigation Response Procedures - Standard mitigation mechanisms for different types of harm

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Privacy law changes, significant breaches, regulatory guidance updates, organizational structure changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Healthcare Data Breach]
IF data_type = "healthcare_PII"
AND breach_confirmed = TRUE
AND HIPAA_notification_required = TRUE
AND notification_decision_time > 48_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Employee PII Exposure]
IF affected_individuals = "employees"
AND PII_types = ["SSN", "financial_data"]
AND harm_assessment_completed = TRUE
AND mitigation_plan_exists = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Third-Party Breach Notification]
IF breach_source = "third_party_vendor"
AND customer_PII_affected = TRUE
AND oversight_notification_required = TRUE
AND notification_process_followed = TRUE
THEN compliance = TRUE

[SCENARIO-04: Minor PII Incident]
IF PII_sensitivity = "low"
AND affected_count < 100
AND harm_assessment_complete = TRUE
AND no_notification_justified = TRUE
AND legal_review_completed = TRUE
THEN compliance = TRUE

[SCENARIO-05: Regulatory Reporting Failure]
IF breach_severity = "major"
AND regulatory_notification_required = TRUE
AND privacy_requirements_identified = FALSE
AND reporting_deadline_missed = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Process to determine if notice to individuals or organizations is needed | [RULE-01], [RULE-05] |
| Assessment process to determine extent of harm and mitigation mechanisms | [RULE-02], [RULE-04] |
| Identification of applicable privacy requirements | [RULE-03] |