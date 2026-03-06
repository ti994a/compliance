# POLICY: SI-19.8: Motivated Intruder

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-19.8 |
| NIST Control | SI-19.8: Motivated Intruder |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | motivated intruder, de-identification, re-identification, privacy testing, dataset security |

## 1. POLICY STATEMENT
The organization SHALL perform motivated intruder testing on all de-identified datasets to validate that personally identifiable information cannot be re-identified through adversarial analysis. Testing MUST be conducted by qualified personnel using realistic attack scenarios and resources to ensure de-identification effectiveness.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| De-identified datasets | YES | All datasets containing originally identifiable information |
| Public data releases | YES | Prior to public release or sharing |
| Internal analytics datasets | YES | When containing sensitive personal information |
| Synthetic datasets | CONDITIONAL | Only if derived from real personal data |
| Fully anonymized data | NO | Data that never contained identifiable information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee motivated intruder testing program<br>• Approve testing methodologies and scope<br>• Review test results and remediation plans |
| Data Protection Team | • Conduct motivated intruder tests<br>• Document testing procedures and results<br>• Coordinate with data custodians on remediation |
| Data Custodians | • Provide datasets for testing<br>• Implement remediation measures<br>• Maintain testing documentation |

## 4. RULES
[RULE-01] Motivated intruder testing MUST be performed on all de-identified datasets before release, sharing, or production use.
[VALIDATION] IF dataset_status = "de-identified" AND motivated_intruder_test = "not_performed" THEN violation

[RULE-02] Testing SHALL specify and document the assumed intruder capabilities including inside knowledge, computational resources, financial resources, available data, and technical skills.
[VALIDATION] IF test_conducted = TRUE AND intruder_profile_documented = FALSE THEN violation

[RULE-03] Tests MUST be conducted by personnel independent from the original de-identification process with appropriate privacy and security expertise.
[VALIDATION] IF tester_independence = FALSE OR tester_qualified = FALSE THEN violation

[RULE-04] If motivated intruder testing successfully re-identifies any individuals, the dataset MUST NOT be released and SHALL undergo additional de-identification measures.
[VALIDATION] IF re_identification_successful = TRUE AND dataset_released = TRUE THEN critical_violation

[RULE-05] Testing results and methodologies MUST be documented and retained for audit purposes for minimum 7 years.
[VALIDATION] IF test_completed = TRUE AND documentation_retained = FALSE THEN violation

[RULE-06] Motivated intruder testing SHALL be repeated when datasets are updated, combined with other data sources, or when new re-identification techniques become available.
[VALIDATION] IF dataset_modified = TRUE AND retest_performed = FALSE AND days_since_modification > 90 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Motivated Intruder Test Planning - Define test scope, intruder profiles, and success criteria
- [PROC-02] Re-identification Attack Execution - Systematic attempt to re-identify individuals using specified resources
- [PROC-03] Test Results Analysis - Evaluate re-identification success and document findings
- [PROC-04] Dataset Remediation - Apply additional de-identification measures when tests fail
- [PROC-05] Testing Documentation - Maintain comprehensive records of all testing activities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Successful re-identification, new attack techniques, regulatory changes, significant data breaches

## 7. SCENARIO PATTERNS
[SCENARIO-01: Untested Dataset Release]
IF dataset_contains_deidentified_data = TRUE
AND motivated_intruder_test = "not_performed"
AND dataset_status = "approved_for_release"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Insufficient Intruder Profile]
IF motivated_intruder_test = "performed"
AND intruder_capabilities_specified = FALSE
AND test_documentation = "incomplete"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Failed Test with Release]
IF re_identification_attempts = "successful"
AND additional_deidentification = "not_applied"
AND dataset_released = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Outdated Testing]
IF dataset_last_modified > test_date
AND days_since_modification > 90
AND retest_performed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Unqualified Tester]
IF tester_independence = FALSE
AND tester_privacy_expertise = "insufficient"
AND test_results = "dataset_approved"
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Motivated intruder test performed on de-identified datasets | [RULE-01] |
| Test determines if identified data remains or can be re-identified | [RULE-04] |
| Intruder capabilities and resources specified | [RULE-02] |
| Independent qualified testing personnel | [RULE-03] |
| Test documentation and retention | [RULE-05] |
| Periodic retesting requirements | [RULE-06] |