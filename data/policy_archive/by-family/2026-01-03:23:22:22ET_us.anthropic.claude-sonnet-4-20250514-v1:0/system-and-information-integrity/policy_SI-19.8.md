# POLICY: SI-19.8: Motivated Intruder

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-19.8 |
| NIST Control | SI-19.8: Motivated Intruder |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | de-identification, re-identification, motivated intruder, dataset testing, privacy protection |

## 1. POLICY STATEMENT
The organization MUST perform motivated intruder testing on all de-identified datasets to validate that personal identifiers cannot be reconstructed or re-identified. Testing SHALL assess whether de-identification techniques provide sufficient protection against adversaries with specified resources and capabilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| De-identified datasets | YES | All datasets containing originally identifiable information |
| Public data releases | YES | Any dataset intended for external sharing |
| Internal analytics datasets | YES | When containing sensitive personal information |
| Synthetic datasets | CONDITIONAL | If derived from real personal data |
| Aggregated reports | CONDITIONAL | If granular enough to enable re-identification |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Approve motivated intruder test procedures<br>• Review test results and remediation plans<br>• Authorize dataset releases |
| Data Protection Team | • Conduct motivated intruder tests<br>• Document test methodologies and results<br>• Recommend additional de-identification measures |
| Data Owners | • Provide context about data sensitivity<br>• Implement additional protections based on test results<br>• Maintain records of testing activities |

## 4. RULES
[RULE-01] Motivated intruder testing MUST be performed on all de-identified datasets before initial release or sharing.
[VALIDATION] IF dataset_status = "de-identified" AND motivated_intruder_test = "not_performed" AND release_approved = TRUE THEN violation

[RULE-02] Test scenarios MUST specify intruder capabilities including computational resources, financial resources, inside knowledge, technical skills, and available external data sources.
[VALIDATION] IF test_documentation = "incomplete" AND missing_capability_specification = TRUE THEN violation

[RULE-03] Testing MUST attempt re-identification using at least three different attack methodologies appropriate to the data type and de-identification technique used.
[VALIDATION] IF attack_methodologies < 3 THEN violation

[RULE-04] If motivated intruder testing successfully re-identifies any individuals, the dataset MUST NOT be released until additional de-identification measures are implemented and testing repeated.
[VALIDATION] IF re-identification_successful = TRUE AND dataset_released = TRUE THEN critical_violation

[RULE-05] Motivated intruder test results and methodologies MUST be documented and retained for the lifecycle of the dataset plus three years.
[VALIDATION] IF test_documentation = "missing" OR retention_period < (dataset_lifecycle + 3_years) THEN violation

[RULE-06] Testing MUST be repeated annually for datasets in active use or when significant changes are made to de-identification processes.
[VALIDATION] IF last_test_date > 365_days AND dataset_status = "active" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Motivated Intruder Test Planning - Define test scope, intruder profiles, and success criteria
- [PROC-02] Re-identification Attack Execution - Systematic attempts to re-identify individuals using specified methodologies
- [PROC-03] Test Results Analysis - Evaluation of re-identification success rates and risk assessment
- [PROC-04] Remediation Implementation - Additional de-identification measures when tests indicate insufficient protection

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or after significant re-identification incidents
- Triggering events: Successful re-identification in testing, new attack methodologies discovered, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Successful Re-identification]
IF motivated_intruder_test = "completed"
AND re_identification_rate > 0%
AND dataset_release = "pending"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Incomplete Test Documentation]
IF test_performed = TRUE
AND intruder_capabilities_documented = FALSE
AND attack_methodologies < 3
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Overdue Testing]
IF dataset_status = "active"
AND last_motivated_intruder_test > 365_days
AND no_exception_documented = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Proper Testing Process]
IF motivated_intruder_test = "completed"
AND attack_methodologies >= 3
AND re_identification_rate = 0%
AND documentation = "complete"
THEN compliance = TRUE

[SCENARIO-05: Test After Process Changes]
IF de_identification_process = "modified"
AND motivated_intruder_test = "not_updated"
AND days_since_change > 30
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Motivated intruder test performed on de-identified dataset | [RULE-01] |
| Test determines if identified data remains or can be re-identified | [RULE-03], [RULE-04] |
| Test methodology specifies intruder resources and capabilities | [RULE-02] |
| Test results documented and retained | [RULE-05] |
| Regular testing of active datasets | [RULE-06] |