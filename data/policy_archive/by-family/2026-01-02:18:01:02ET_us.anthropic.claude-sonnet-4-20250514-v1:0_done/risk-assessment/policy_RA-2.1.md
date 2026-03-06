```markdown
POLICY: RA-2.1: Impact-level Prioritization

METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-2.1 |
| NIST Control | RA-2.1: Impact-level Prioritization |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | impact-level, prioritization, system categorization, FIPS 199, high value assets, risk assessment |

1. POLICY STATEMENT
The organization SHALL conduct impact-level prioritization of all organizational systems to obtain additional granularity beyond the standard FIPS 199 low/moderate/high categorizations. This sub-categorization enables more precise risk-based decision-making for security control selection and resource allocation.

2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, hybrid, and on-premises systems |
| High Value Assets | YES | Require mandatory sub-categorization |
| Third-party Systems | CONDITIONAL | When processing organizational data |
| Development/Test Systems | YES | Based on data sensitivity |

3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owners | • Provide system impact data<br>• Validate sub-categorization results<br>• Update categorization when systems change |
| Risk Assessment Team | • Conduct impact-level prioritization analysis<br>• Document sub-categorization methodology<br>• Maintain prioritization inventory |
| CISO | • Approve impact-level prioritization framework<br>• Review high value asset designations<br>• Ensure compliance with federal requirements |

4. RULES
[RULE-01] All organizational systems MUST undergo impact-level prioritization within 90 days of initial FIPS 199 categorization.
[VALIDATION] IF system_categorized = TRUE AND prioritization_completed = FALSE AND days_since_categorization > 90 THEN violation

[RULE-02] Impact-level prioritization MUST create sub-categories using the format [impact_level]-[priority_level] (e.g., low-moderate, moderate-high, high-high).
[VALIDATION] IF prioritization_format NOT MATCH "[low|moderate|high]-[low|moderate|high]" THEN violation

[RULE-03] Systems identified as high value assets MUST receive high-high sub-categorization and additional security analysis.
[VALIDATION] IF high_value_asset = TRUE AND sub_category != "high-high" THEN critical_violation

[RULE-04] Impact-level prioritization documentation MUST include justification for sub-category assignment and risk factors considered.
[VALIDATION] IF prioritization_documented = TRUE AND justification_provided = FALSE THEN violation

[RULE-05] Sub-categorization results MUST be reviewed and updated within 30 days of any significant system changes or annual assessment.
[VALIDATION] IF (system_change_significant = TRUE OR annual_review_due = TRUE) AND review_completed = FALSE AND days_overdue > 30 THEN violation

5. REQUIRED PROCEDURES
- [PROC-01] Impact-Level Prioritization Assessment - Methodology for conducting sub-categorization analysis
- [PROC-02] High Value Asset Identification - Process for identifying and designating critical systems
- [PROC-03] Sub-Category Documentation - Requirements for documenting prioritization decisions
- [PROC-04] Prioritization Review and Update - Process for maintaining current sub-categorizations

6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Significant system changes, new threat intelligence, regulatory updates, major incidents

7. SCENARIO PATTERNS
[SCENARIO-01: New System Deployment]
IF system_deployed = TRUE
AND fips_199_categorization = "complete"
AND impact_prioritization = "not_started"
AND days_since_deployment > 90
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: High Value Asset Without Proper Classification]
IF system_contains_critical_data = TRUE
AND revenue_impact > 10_million
AND sub_category != "high-high"
AND high_value_designation = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Outdated Prioritization After System Change]
IF system_modification_date > prioritization_date
AND modification_significance = "major"
AND days_since_modification > 30
AND prioritization_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Documentation]
IF impact_prioritization = "complete"
AND sub_category_assigned = TRUE
AND justification_documented = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Compliant Sub-Categorization]
IF fips_199_category = "moderate"
AND sub_category = "moderate-high"
AND justification_documented = TRUE
AND review_current = TRUE
THEN compliance = TRUE

8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Impact-level prioritization conducted for additional granularity | RULE-01, RULE-02 |
| Sub-categorization methodology documented | RULE-04 |
| High value assets properly identified and categorized | RULE-03 |
| Prioritization maintained current | RULE-05 |
```