```markdown
POLICY: RA-2.1: Impact-level Prioritization

METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-2.1 |
| NIST Control | RA-2.1: Impact-level Prioritization |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | impact-level, system categorization, risk prioritization, FIPS 199, high value assets |

1. POLICY STATEMENT
The organization SHALL conduct impact-level prioritization of all organizational systems to obtain additional granularity beyond the standard FIPS 199 low/moderate/high categorizations. This prioritization enables risk-based decision-making for security control selection, investment allocation, and identification of high value assets requiring enhanced protection.

2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems with FIPS 199 categorization |
| Cloud Services | YES | Including hybrid and multi-cloud environments |
| Legacy Systems | YES | Must be prioritized within 180 days |
| Development Systems | CONDITIONAL | If processing production data |
| Vendor Systems | YES | Systems processing organizational data |

3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owners | • Provide system impact data and business context<br>• Validate sub-categorization assignments<br>• Update prioritization when system changes occur |
| Risk Assessment Team | • Conduct impact-level prioritization analysis<br>• Document sub-categorization methodology<br>• Maintain prioritization matrix and criteria |
| CISO | • Approve prioritization methodology<br>• Review high value asset designations<br>• Ensure alignment with organizational risk strategy |

4. RULES
[RULE-01] All organizational systems with existing FIPS 199 categorizations MUST undergo impact-level prioritization within 90 days of policy implementation.
[VALIDATION] IF system_fips199_status = "categorized" AND prioritization_date = NULL AND days_since_policy > 90 THEN violation

[RULE-02] Impact-level prioritization SHALL create sub-categories using the format [sub-level]-[base-level] (e.g., low-moderate, moderate-moderate, high-moderate).
[VALIDATION] IF prioritization_format NOT MATCH "[low|moderate|high]-[low|moderate|high]" THEN violation

[RULE-03] Systems designated as high value assets MUST be identified and documented with justification based on adversary interest, critical loss potential, or mission impact.
[VALIDATION] IF system_criticality = "high" AND high_value_asset_documented = FALSE THEN violation

[RULE-04] Impact-level prioritization MUST be reviewed and updated within 30 days of any significant system changes affecting confidentiality, integrity, or availability.
[VALIDATION] IF system_change_date > prioritization_review_date AND days_between > 30 THEN violation

[RULE-05] Prioritization methodology and criteria MUST be documented and approved by the CISO before implementation.
[VALIDATION] IF prioritization_methodology_approved = FALSE AND systems_prioritized > 0 THEN critical_violation

5. REQUIRED PROCEDURES
- [PROC-01] Impact-Level Prioritization Methodology - Defines criteria and process for sub-categorizing systems
- [PROC-02] High Value Asset Identification - Process for identifying and documenting systems of heightened value
- [PROC-03] Prioritization Review and Update - Procedures for maintaining current prioritization levels
- [PROC-04] Risk-Based Investment Planning - Using prioritization data for security control and resource decisions

6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 6 months
- Triggering events: Major system implementations, significant threat landscape changes, regulatory requirement updates

7. SCENARIO PATTERNS
[SCENARIO-01: New System Prioritization]
IF system_fips199_category = "moderate"
AND system_deployment_date < 90_days_ago
AND impact_level_prioritization = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: High Value Asset Documentation]
IF system_criticality_score > 8.5
AND processes_sensitive_data = TRUE
AND high_value_asset_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Prioritization After System Change]
IF system_major_change_date = "2024-01-15"
AND current_date = "2024-03-01"
AND prioritization_review_date < "2024-02-14"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Valid Sub-Categorization]
IF system_base_category = "high"
AND system_sub_category = "moderate-high"
AND methodology_approved = TRUE
THEN compliance = TRUE

[SCENARIO-05: Investment Decision Alignment]
IF system_priority = "high-high"
AND security_control_baseline = "standard"
AND enhanced_controls_implemented = FALSE
THEN compliance = FALSE
violation_severity = "High"

8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Impact-level prioritization conducted for additional granularity | [RULE-01], [RULE-02] |
| Sub-categorization methodology documented | [RULE-05] |
| High value assets identified | [RULE-03] |
| Prioritization maintained current | [RULE-04] |
```