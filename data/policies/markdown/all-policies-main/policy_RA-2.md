# POLICY: RA-2: Security Categorization

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-2 |
| NIST Control | RA-2: Security Categorization |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | security categorization, FIPS 199, confidentiality, integrity, availability, authorization, security plan |

## 1. POLICY STATEMENT
All information systems and the data they process, store, and transmit must be categorized according to FIPS 199 security impact levels (Low, Moderate, High) based on potential adverse impacts to confidentiality, integrity, and availability. Security categorization decisions must be documented, reviewed, and approved by the authorizing official before system operation.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing organizational data |
| Cloud Services | YES | Including SaaS, PaaS, IaaS deployments |
| Mobile Applications | YES | Apps handling corporate data |
| Development Systems | YES | Including test/staging environments |
| Personal Devices | CONDITIONAL | Only when accessing corporate data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Initiate security categorization process<br>• Provide business context and mission criticality<br>• Approve categorization recommendations |
| Information Owner | • Define data sensitivity and classification<br>• Identify potential business impacts<br>• Validate categorization accuracy |
| CISO/Security Team | • Conduct categorization analysis<br>• Document rationale and methodology<br>• Ensure compliance with FIPS 199 |
| Authorizing Official | • Review categorization documentation<br>• Approve final categorization decision<br>• Accept residual risks |

## 4. RULES
[RULE-01] All information systems MUST be categorized using FIPS 199 methodology within 30 days of system identification or before processing any organizational data.
[VALIDATION] IF system_identified = TRUE AND categorization_completed = FALSE AND days_elapsed > 30 THEN violation

[RULE-02] Security categorization MUST assess potential adverse impacts to confidentiality, integrity, and availability using Low, Moderate, or High impact levels.
[VALIDATION] IF categorization_exists = TRUE AND (confidentiality_impact = NULL OR integrity_impact = NULL OR availability_impact = NULL) THEN violation

[RULE-03] The overall system security category MUST be determined by the highest impact level among the three security objectives (confidentiality, integrity, availability).
[VALIDATION] IF system_category ≠ MAX(confidentiality_impact, integrity_impact, availability_impact) THEN violation

[RULE-04] Security categorization results and supporting rationale MUST be documented in the system security plan within 15 days of categorization completion.
[VALIDATION] IF categorization_completed = TRUE AND security_plan_updated = FALSE AND days_elapsed > 15 THEN violation

[RULE-05] The authorizing official or designated representative MUST review and formally approve the security categorization decision before system authorization.
[VALIDATION] IF categorization_documented = TRUE AND ao_approval = FALSE AND system_authorized = TRUE THEN critical_violation

[RULE-06] Security categorization MUST be reviewed and updated when significant system changes occur or during periodic reviews at least annually.
[VALIDATION] IF (system_changes = "significant" OR last_review_date > 365_days) AND categorization_reviewed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security Categorization Methodology - FIPS 199 assessment process and impact analysis
- [PROC-02] Categorization Documentation - Templates and requirements for security plan updates  
- [PROC-03] Review and Approval Workflow - AO review and approval process
- [PROC-04] Recategorization Triggers - Events requiring categorization updates

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or upon regulatory changes
- Triggering events: System modifications, data classification changes, regulatory updates, security incidents

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Cloud System Deployment]
IF system_type = "cloud_service"
AND data_classification = "confidential"
AND categorization_completed = FALSE
AND deployment_date < current_date
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: System Modification Impact]
IF system_changes = "significant"
AND original_category = "Moderate"
AND new_data_types_added = TRUE
AND recategorization_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing AO Approval]
IF categorization_documented = TRUE
AND security_plan_updated = TRUE
AND ao_approval_date = NULL
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Outdated Categorization]
IF last_categorization_date > 365_days
AND annual_review_completed = FALSE
AND system_status = "operational"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Incorrect Impact Assessment]
IF data_contains_pii = TRUE
AND confidentiality_impact = "Low"
AND business_justification = NULL
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System and information categorization completed | [RULE-01], [RULE-02] |
| Security categorization documented in security plan | [RULE-04] |
| AO review and approval of categorization decision | [RULE-05] |
| Categorization follows FIPS 199 methodology | [RULE-02], [RULE-03] |
| Periodic review and updates performed | [RULE-06] |