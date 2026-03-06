# POLICY: RA-2: Security Categorization

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-2 |
| NIST Control | RA-2: Security Categorization |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | security categorization, risk assessment, confidentiality, integrity, availability, FIPS 199, system classification |

## 1. POLICY STATEMENT
All information systems and the data they process, store, and transmit must be categorized according to FIPS 199 standards based on potential adverse impacts to confidentiality, integrity, and availability. Security categorization decisions must be documented, reviewed, and approved by authorized officials before system operation.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing organizational data |
| Cloud Services | YES | Including SaaS, PaaS, IaaS implementations |
| Development Systems | YES | Including test and staging environments |
| Legacy Systems | YES | Must be categorized within 90 days |
| Contractor Systems | CONDITIONAL | If processing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Initiate security categorization process<br>• Provide business impact analysis<br>• Ensure categorization accuracy throughout lifecycle |
| Information Owner | • Define data sensitivity levels<br>• Validate impact assessments<br>• Approve categorization for owned data types |
| CISO | • Review categorization methodology<br>• Approve HIGH impact categorizations<br>• Ensure compliance with organizational standards |
| Authorizing Official | • Review and approve security categorization decisions<br>• Validate supporting rationale<br>• Accept residual risks based on categorization |

## 4. RULES
[RULE-01] All information systems MUST be categorized using FIPS 199 methodology within 30 days of system identification or before processing organizational data.
[VALIDATION] IF system_identified = TRUE AND categorization_complete = FALSE AND days_elapsed > 30 THEN violation

[RULE-02] Security categorization MUST assess potential adverse impacts for confidentiality, integrity, and availability using LOW, MODERATE, or HIGH impact levels.
[VALIDATION] IF categorization_exists = TRUE AND (confidentiality_impact = NULL OR integrity_impact = NULL OR availability_impact = NULL) THEN violation

[RULE-03] Security categorization results and supporting rationale MUST be documented in the system security plan within 15 days of categorization completion.
[VALIDATION] IF categorization_complete = TRUE AND ssp_documented = FALSE AND days_elapsed > 15 THEN violation

[RULE-04] Authorizing Official or designated representative MUST review and approve security categorization decisions before system authorization.
[VALIDATION] IF categorization_complete = TRUE AND ao_approval = FALSE AND system_authorized = TRUE THEN critical_violation

[RULE-05] Security categorization MUST be reviewed and updated when significant system changes occur or during annual system reviews.
[VALIDATION] IF (major_change_occurred = TRUE OR annual_review_due = TRUE) AND categorization_reviewed = FALSE THEN violation

[RULE-06] HIGH impact systems MUST undergo additional review by the CISO and senior leadership before approval.
[VALIDATION] IF system_impact_level = "HIGH" AND ciso_review = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security Categorization Assessment - Standard methodology for conducting FIPS 199 categorization
- [PROC-02] Impact Level Determination - Process for assessing LOW/MODERATE/HIGH impact levels
- [PROC-03] Categorization Documentation - Requirements for documenting results in security plans
- [PROC-04] Approval Workflow - Process for obtaining required approvals based on impact level
- [PROC-05] Categorization Review - Procedures for periodic and change-triggered reviews

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system changes, data type additions, business impact changes, regulatory requirement updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Cloud System]
IF system_type = "cloud"
AND organizational_data = TRUE
AND categorization_complete = FALSE
AND days_since_deployment > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: HIGH Impact Without CISO Review]
IF system_impact_level = "HIGH"
AND ciso_review = FALSE
AND ao_approval = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Undocumented Categorization]
IF categorization_complete = TRUE
AND ssp_documentation = FALSE
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Outdated Categorization After Major Change]
IF major_system_change = TRUE
AND change_date > 90_days_ago
AND categorization_reviewed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Contractor System Processing PII]
IF system_owner = "contractor"
AND processes_pii = TRUE
AND categorization_complete = TRUE
AND ao_approval = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System and information categorization completed | RULE-01, RULE-02 |
| Categorization results documented in security plan | RULE-03 |
| Authorizing official review and approval | RULE-04, RULE-06 |
| Periodic review and updates | RULE-05 |