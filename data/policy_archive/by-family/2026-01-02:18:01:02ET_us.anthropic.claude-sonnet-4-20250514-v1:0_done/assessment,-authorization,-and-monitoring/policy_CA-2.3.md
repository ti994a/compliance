```markdown
POLICY: CA-2(3): Leveraging Results from External Organizations

METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CA-2-3 |
| NIST Control | CA-2(3): Leveraging Results from External Organizations |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | external assessments, third-party validation, assessment reuse, Common Criteria, CMVP, CAVP, accredited testing |

1. POLICY STATEMENT
The organization SHALL leverage control assessment results from qualified external organizations to reduce assessment burden while maintaining security assurance. External assessment results MUST meet defined acceptance criteria and be formally validated before incorporation into organizational compliance programs.

2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Systems seeking assessment efficiency |
| Third-party Assessments | YES | Must meet qualification criteria |
| Vendor Security Certifications | YES | Subject to validation requirements |
| Internal Assessment Teams | YES | Must validate external results |

3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve external assessment acceptance criteria<br>• Authorize use of external assessment results<br>• Oversee validation processes |
| Security Assessment Team | • Evaluate external organization qualifications<br>• Validate external assessment results<br>• Document acceptance decisions |
| System Owners | • Identify applicable external assessments<br>• Ensure system-specific validation<br>• Maintain assessment documentation |

4. RULES
[RULE-01] External organizations providing assessment results MUST be pre-qualified based on defined criteria including accreditation status, reputation, and assessment methodology.
[VALIDATION] IF external_org_qualification_status != "approved" THEN assessment_results_rejected

[RULE-02] External assessment results SHALL only be leveraged when the assessed system configuration substantially matches the organization's system implementation.
[VALIDATION] IF system_configuration_match < 80% THEN external_assessment_invalid

[RULE-03] Acceptance of external assessment results MUST be documented with justification including organization qualifications, assessment scope alignment, and evidence quality evaluation.
[VALIDATION] IF acceptance_documentation = "missing" OR justification = "incomplete" THEN compliance_violation

[RULE-04] External assessment results from accredited testing laboratories (Common Criteria, CMVP, CAVP) SHALL be given preference over non-accredited sources.
[VALIDATION] IF external_org_accreditation = "none" AND accredited_alternative_available = TRUE THEN use_accredited_source

[RULE-05] Leveraged external assessment results MUST be validated within 90 days of acceptance decision and updated when external assessments expire.
[VALIDATION] IF validation_date > acceptance_date + 90_days THEN validation_overdue

[RULE-06] Gap analysis MUST be performed to identify controls not covered by external assessments requiring independent organizational assessment.
[VALIDATION] IF gap_analysis_complete = FALSE AND external_assessment_leveraged = TRUE THEN compliance_violation

5. REQUIRED PROCEDURES
- [PROC-01] External Organization Qualification - Process for evaluating and approving external assessment organizations
- [PROC-02] Assessment Result Validation - Methodology for validating external assessment evidence and conclusions
- [PROC-03] Gap Analysis Execution - Process for identifying assessment gaps requiring organizational testing
- [PROC-04] Documentation and Approval - Workflow for documenting and approving external assessment leverage decisions

6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: New accreditation programs, significant assessment failures, regulatory changes

7. SCENARIO PATTERNS
[SCENARIO-01: Valid Common Criteria Leverage]
IF external_org_type = "Common_Criteria_Lab"
AND system_configuration_match >= 80%
AND assessment_currency <= 3_years
AND gap_analysis_complete = TRUE
THEN compliance = TRUE

[SCENARIO-02: Unqualified External Organization]
IF external_org_qualification_status = "not_approved"
AND assessment_results_leveraged = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Expired External Assessment]
IF external_assessment_date < current_date - 3_years
AND assessment_results_still_leveraged = TRUE
AND revalidation_performed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Incomplete Gap Analysis]
IF external_assessment_leveraged = TRUE
AND gap_analysis_complete = FALSE
AND assessment_finalized = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Insufficient System Match]
IF system_configuration_match < 80%
AND external_assessment_leveraged = TRUE
AND additional_testing_performed = FALSE
THEN compliance = FALSE
violation_severity = "High"

8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| External organization qualification defined | [RULE-01] |
| System configuration alignment verified | [RULE-02] |
| Acceptance criteria documentation | [RULE-03] |
| Preference for accredited sources | [RULE-04] |
| Validation timeline compliance | [RULE-05] |
| Gap analysis completion | [RULE-06] |
```