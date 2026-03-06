# POLICY: PT-5: Privacy Notice

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-5 |
| NIST Control | PT-5: Privacy Notice |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | privacy notice, PII processing, transparency, plain language, authority disclosure |

## 1. POLICY STATEMENT
The organization SHALL provide clear, accessible privacy notices to individuals that explain how their personally identifiable information (PII) is processed, under what authority, and for what purposes. Privacy notices MUST be available at first interaction and maintained according to defined frequencies thereafter.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing PII | YES | Includes customer, employee, and third-party PII |
| Public-facing applications | YES | Must display notices before PII collection |
| Internal HR systems | YES | Employee PII processing requires notices |
| Marketing platforms | YES | Customer data processing requires notices |
| Development/test systems | CONDITIONAL | Only if processing production PII |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Approve privacy notice content and format<br>• Define notice update frequencies<br>• Ensure legal compliance |
| System Owners | • Implement privacy notices in their systems<br>• Maintain current notice versions<br>• Report processing changes |
| Legal Counsel | • Review notices for regulatory compliance<br>• Validate authority citations<br>• Approve plain language content |

## 4. RULES
[RULE-01] Privacy notices MUST be available to individuals upon first interaction with any system or service that processes their PII.
[VALIDATION] IF system_processes_PII = TRUE AND first_interaction = TRUE AND privacy_notice_displayed = FALSE THEN violation

[RULE-02] Privacy notices MUST be written in clear, plain language that avoids technical jargon and is easily understandable by the general public.
[VALIDATION] IF notice_readability_score > grade_12_level OR technical_jargon_present = TRUE THEN violation

[RULE-03] Privacy notices MUST identify the specific legal authority that authorizes the processing of PII.
[VALIDATION] IF privacy_notice_exists = TRUE AND legal_authority_cited = FALSE THEN violation

[RULE-04] Privacy notices MUST clearly state all purposes for which PII will be processed by the organization.
[VALIDATION] IF PII_processing_purposes_documented = FALSE OR purposes_vague = TRUE THEN violation

[RULE-05] Privacy notices MUST be reviewed and updated at least annually or when PII processing practices change materially.
[VALIDATION] IF last_notice_update > 365_days OR material_processing_change = TRUE AND notice_updated = FALSE THEN violation

[RULE-06] Updated privacy notices MUST be communicated to affected individuals within 30 days of changes taking effect.
[VALIDATION] IF notice_updated = TRUE AND communication_to_users > 30_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Privacy Notice Development - Standard process for creating compliant privacy notices
- [PROC-02] Plain Language Review - Procedure for ensuring notices meet readability requirements
- [PROC-03] Notice Update Management - Process for maintaining current notices across all systems
- [PROC-04] User Communication - Procedure for notifying users of privacy notice changes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New PII processing activities, regulatory changes, legal authority changes, material processing purpose modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Customer Registration]
IF system_type = "customer_facing"
AND user_action = "first_registration"
AND privacy_notice_displayed = TRUE
AND notice_includes_authority = TRUE
AND notice_includes_purposes = TRUE
THEN compliance = TRUE

[SCENARIO-02: Missing Authority Citation]
IF privacy_notice_exists = TRUE
AND legal_authority_section = "missing"
AND PII_processing_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Outdated Notice After Processing Change]
IF processing_purposes_changed = TRUE
AND change_date > 30_days_ago
AND privacy_notice_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Technical Jargon in Notice]
IF privacy_notice_exists = TRUE
AND readability_score = "college_level"
AND technical_terms_undefined = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Internal Employee System]
IF system_type = "HR_internal"
AND processes_employee_PII = TRUE
AND privacy_notice_available = FALSE
AND first_employee_login = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Notice available at first interaction | RULE-01 |
| Clear and easy-to-understand language | RULE-02 |
| Authority identification | RULE-03 |
| Purpose identification | RULE-04 |
| Regular notice updates | RULE-05 |
| Change communication | RULE-06 |