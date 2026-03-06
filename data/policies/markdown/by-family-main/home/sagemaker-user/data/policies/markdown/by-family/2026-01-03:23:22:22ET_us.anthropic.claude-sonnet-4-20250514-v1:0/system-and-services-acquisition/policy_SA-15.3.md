# POLICY: SA-15.3: Criticality Analysis

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-15.3 |
| NIST Control | SA-15.3: Criticality Analysis |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | criticality analysis, developer requirements, SDLC, supply chain, high value assets |

## 1. POLICY STATEMENT
All developers of systems, system components, or system services must perform criticality analysis at defined decision points in the system development life cycle with organization-defined breadth and depth. This analysis is essential for supply chain risk management and protection of high value assets.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All systems and components |
| Third-party Vendors | YES | Contractual requirement |
| COTS Products | YES | Vendor documentation required |
| High Value Assets | YES | Enhanced rigor required |
| Moderate/High Impact Systems | YES | Mandatory analysis |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define criticality analysis requirements<br>• Approve analysis methodologies<br>• Review high value asset analyses |
| Procurement Manager | • Include criticality analysis requirements in contracts<br>• Validate vendor compliance<br>• Maintain analysis documentation |
| System Developers | • Perform criticality analysis at defined checkpoints<br>• Document analysis findings<br>• Provide design documentation access |

## 4. RULES

[RULE-01] Developers MUST perform criticality analysis at the following SDLC decision points: requirements definition, design review, implementation milestone, integration testing, and pre-deployment approval.
[VALIDATION] IF sdlc_checkpoint IN [requirements, design, implementation, integration, pre-deployment] AND criticality_analysis_performed = FALSE THEN violation

[RULE-02] Criticality analysis for high value assets MUST include functional specifications, high-level designs, low-level designs, source code analysis, and hardware schematics review.
[VALIDATION] IF asset_classification = "high_value" AND analysis_components < 5_required_elements THEN violation

[RULE-03] Third-party vendors MUST provide criticality analysis documentation within 30 days of contract execution and update analysis within 15 days of any design changes.
[VALIDATION] IF vendor_type = "third_party" AND (analysis_delivery_days > 30 OR update_delivery_days > 15) THEN violation

[RULE-04] Criticality analysis MUST identify single points of failure, security-critical functions, and potential supply chain vulnerabilities with risk ratings.
[VALIDATION] IF analysis_complete = TRUE AND (spof_identified = FALSE OR critical_functions_identified = FALSE OR supply_chain_risks_identified = FALSE) THEN violation

[RULE-05] COTS products MUST have vendor-provided criticality analysis or organizational assessment completed before deployment to production environments.
[VALIDATION] IF product_type = "COTS" AND production_deployment = TRUE AND (vendor_analysis = FALSE AND org_assessment = FALSE) THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Criticality Analysis Methodology - Standard approach for conducting analysis
- [PROC-02] Vendor Assessment Process - Evaluation of third-party analysis quality
- [PROC-03] High Value Asset Classification - Criteria for enhanced analysis requirements
- [PROC-04] Supply Chain Risk Integration - Incorporating analysis into SCRM processes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Bi-annually
- Triggering events: New high value asset designation, major supply chain incidents, regulatory changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Missing SDLC Checkpoint Analysis]
IF system_development = TRUE
AND sdlc_checkpoint = "design_review"
AND criticality_analysis_performed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete High Value Asset Analysis]
IF asset_classification = "high_value"
AND analysis_components = 3
AND required_components = 5
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Delayed Vendor Documentation]
IF vendor_contract_signed = TRUE
AND days_since_execution = 45
AND criticality_analysis_received = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: COTS Deployment Without Analysis]
IF product_type = "COTS"
AND environment = "production"
AND vendor_analysis = FALSE
AND organizational_assessment = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Outdated Analysis After Changes]
IF design_change_date < current_date - 15_days
AND criticality_analysis_updated = FALSE
AND system_classification IN ["moderate", "high"]
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer performs analysis at defined SDLC decision points | [RULE-01] |
| Analysis includes required breadth of components | [RULE-02] |
| Analysis includes required depth of rigor | [RULE-02], [RULE-04] |
| Vendor compliance with analysis requirements | [RULE-03] |
| COTS product analysis coverage | [RULE-05] |