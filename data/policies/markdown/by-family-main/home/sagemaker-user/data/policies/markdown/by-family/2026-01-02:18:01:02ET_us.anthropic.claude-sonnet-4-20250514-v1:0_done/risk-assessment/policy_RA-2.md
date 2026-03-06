# POLICY: RA-2: Security Categorization

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-2 |
| NIST Control | RA-2: Security Categorization |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | security categorization, FIPS 199, CIA triad, impact levels, system classification, authorization |

## 1. POLICY STATEMENT
All organizational systems and the information they process, store, and transmit must be categorized according to FIPS 199 security categories based on potential adverse impacts to confidentiality, integrity, and availability. Security categorization decisions must be documented, reviewed, and approved by the appropriate authorizing official before system operation.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing organizational data |
| Cloud Services | YES | Including SaaS, PaaS, IaaS implementations |
| Development Systems | YES | Systems in all SDLC phases |
| Third-party Systems | YES | Systems processing organizational data |
| Personal Devices | CONDITIONAL | Only if processing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Initiate security categorization process<br>• Provide system and data inventory<br>• Validate categorization accuracy |
| Information Owner | • Define information sensitivity levels<br>• Approve impact determinations<br>• Review categorization decisions |
| Authorizing Official | • Review security categorization documentation<br>• Approve final categorization decisions<br>• Ensure alignment with organizational risk tolerance |

## 4. RULES
[RULE-01] System owners MUST categorize all systems and information according to FIPS 199 methodology within 30 days of system deployment or data classification changes.
[VALIDATION] IF system_deployed = TRUE AND categorization_complete = FALSE AND days_elapsed > 30 THEN violation

[RULE-02] Security categorization MUST assess confidentiality, integrity, and availability impacts using Low, Moderate, or High designations based on FIPS 199 criteria.
[VALIDATION] IF categorization_exists = TRUE AND (confidentiality_impact NOT IN [Low, Moderate, High] OR integrity_impact NOT IN [Low, Moderate, High] OR availability_impact NOT IN [Low, Moderate, High]) THEN violation

[RULE-03] Security categorization results and supporting rationale MUST be documented in the system security plan before system authorization.
[VALIDATION] IF system_authorization_requested = TRUE AND (categorization_documented = FALSE OR rationale_documented = FALSE) THEN critical_violation

[RULE-04] Authorizing officials or designated representatives MUST review and formally approve security categorization decisions before granting system authorization.
[VALIDATION] IF system_operational = TRUE AND ao_approval_documented = FALSE THEN critical_violation

[RULE-05] Security categorization MUST be reviewed and updated within 90 days of significant system changes, data type modifications, or annually.
[VALIDATION] IF (significant_change_date < current_date - 90_days OR last_review_date < current_date - 365_days) AND categorization_updated = FALSE THEN violation

[RULE-06] Systems processing PII or PHI MUST consider privacy impact assessments in the security categorization process.
[VALIDATION] IF (processes_PII = TRUE OR processes_PHI = TRUE) AND privacy_assessment_considered = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security Categorization Assessment - FIPS 199-based impact analysis methodology
- [PROC-02] Categorization Documentation - Security plan integration and rationale documentation
- [PROC-03] Approval Workflow - Authorizing official review and approval process
- [PROC-04] Categorization Review - Periodic and event-driven reassessment procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: System changes, data classification changes, regulatory updates, security incidents affecting categorization

## 7. SCENARIO PATTERNS
[SCENARIO-01: New System Deployment]
IF system_status = "newly_deployed"
AND categorization_completed = FALSE
AND days_since_deployment > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Missing AO Approval]
IF system_status = "operational"
AND categorization_documented = TRUE
AND ao_approval_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Outdated Categorization]
IF last_categorization_date < (current_date - 365_days)
AND system_changes_occurred = TRUE
AND recategorization_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: PII System Without Privacy Assessment]
IF processes_PII = TRUE
AND security_categorization_exists = TRUE
AND privacy_impact_considered = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Compliant Categorization]
IF categorization_documented = TRUE
AND fips199_methodology_used = TRUE
AND ao_approval_documented = TRUE
AND last_review_date < (current_date - 365_days) = FALSE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System and information categorization completed | RULE-01, RULE-02 |
| Categorization results documented in security plan | RULE-03 |
| Authorizing official reviews and approves categorization | RULE-04 |
| Categorization maintained current | RULE-05 |
| Privacy considerations integrated | RULE-06 |