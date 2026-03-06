```markdown
# POLICY: RA-2.1: Impact-level Prioritization

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_RA-2.1 |
| NIST Control | RA-2.1: Impact-level Prioritization |
| Version | 1.0 |
| Owner | Chief Risk Officer |
| Keywords | impact assessment, system categorization, risk prioritization, FIPS 199, high value assets |

## 1. POLICY STATEMENT
The organization SHALL conduct impact-level prioritization of all organizational systems to obtain additional granularity beyond the standard FIPS 199 low/moderate/high categorization. This prioritization enables risk-based decision-making for security control selection and resource allocation.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems with FIPS 199 categorization |
| Cloud Services | YES | Including hybrid and multi-cloud environments |
| Legacy Systems | YES | Must be prioritized within 180 days |
| Development Systems | CONDITIONAL | Only if processing production data |
| Contractor Systems | YES | If processing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owners | • Provide system impact data<br>• Validate prioritization results<br>• Implement required controls based on sub-category |
| Risk Assessment Team | • Conduct impact-level prioritization analysis<br>• Document sub-categorization methodology<br>• Maintain prioritization matrix |
| CISO | • Approve prioritization methodology<br>• Review high value asset designations<br>• Authorize resource allocation decisions |

## 4. RULES
[RULE-01] All organizational systems MUST be sub-categorized within their existing FIPS 199 impact level using a three-tier approach (low-[impact], moderate-[impact], high-[impact]).
[VALIDATION] IF system_has_fips199_categorization = TRUE AND sub_categorization = NULL THEN violation

[RULE-02] Impact-level prioritization MUST be completed within 90 days of initial FIPS 199 categorization for new systems.
[VALIDATION] IF days_since_fips199_categorization > 90 AND sub_categorization_complete = FALSE THEN violation

[RULE-03] High value assets MUST be identified and designated during the prioritization process based on adversary interest, mission criticality, or enterprise impact.
[VALIDATION] IF system_impact_level = "high" AND high_value_asset_assessment = NULL THEN violation

[RULE-04] Prioritization methodology and criteria MUST be documented and approved by the CISO before implementation.
[VALIDATION] IF prioritization_methodology_approved = FALSE AND prioritization_active = TRUE THEN critical_violation

[RULE-05] Impact-level prioritization MUST be reviewed and updated annually or when significant system changes occur.
[VALIDATION] IF last_prioritization_review > 365_days OR significant_system_change = TRUE AND prioritization_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Impact Sub-Categorization - Process for analyzing and assigning sub-categories within FIPS 199 levels
- [PROC-02] High Value Asset Identification - Methodology for identifying systems of heightened adversary interest
- [PROC-03] Prioritization Review and Update - Annual review process and change-triggered updates
- [PROC-04] Resource Allocation Based on Priority - Process for allocating security resources based on impact prioritization

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system acquisitions, significant threat landscape changes, regulatory requirement updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Moderate System Prioritization]
IF system_fips199_level = "moderate"
AND system_age < 90_days
AND sub_categorization = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: High Value Asset Without Enhanced Controls]
IF system_designated_hva = TRUE
AND enhanced_security_controls = FALSE
AND risk_acceptance_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Outdated Prioritization Assessment]
IF last_impact_prioritization > 365_days
AND system_changes_documented = TRUE
AND prioritization_review_initiated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Contractor System Missing Prioritization]
IF system_owner_type = "contractor"
AND processes_org_data = TRUE
AND impact_prioritization_complete = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Approved Methodology Compliance]
IF prioritization_methodology_approved = TRUE
AND sub_categorization_follows_methodology = TRUE
AND annual_review_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Impact-level prioritization conducted for additional granularity | RULE-01, RULE-02 |
| High value assets identified and prioritized | RULE-03 |
| Documented and approved methodology | RULE-04 |
| Regular review and updates | RULE-05 |
```