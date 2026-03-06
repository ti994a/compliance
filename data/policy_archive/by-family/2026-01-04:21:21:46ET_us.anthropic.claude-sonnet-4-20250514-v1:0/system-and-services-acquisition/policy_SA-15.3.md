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
The organization requires developers of systems, system components, or system services to perform criticality analysis at defined decision points in the system development life cycle with specified breadth and depth of analysis. This requirement ensures critical system elements are identified and properly assessed throughout development.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| System Developers | YES | All contracted and internal developers |
| Component Vendors | YES | COTS and custom component providers |
| Service Providers | YES | Cloud and managed service providers |
| High Value Assets | YES | Mandatory for all HVA systems |
| Low Impact Systems | CONDITIONAL | Based on risk assessment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define criticality analysis requirements<br>• Approve analysis methodologies<br>• Review high-risk findings |
| Procurement Manager | • Include criticality requirements in contracts<br>• Validate developer compliance<br>• Manage vendor relationships |
| System Owner | • Define SDLC decision points<br>• Review analysis results<br>• Approve system deployment |

## 4. RULES
[RULE-01] Developers MUST perform criticality analysis at organization-defined decision points including requirements analysis, design review, implementation milestone, integration testing, and pre-deployment phases.
[VALIDATION] IF sdlc_phase IN ["requirements", "design", "implementation", "integration", "pre-deployment"] AND criticality_analysis_completed = FALSE THEN violation

[RULE-02] Criticality analysis MUST include functional impact assessment, security impact assessment, availability requirements analysis, and dependency mapping with minimum depth requirements defined by system impact level.
[VALIDATION] IF system_impact_level = "high" AND analysis_components < 4 THEN violation

[RULE-03] High Value Asset systems MUST require criticality analysis regardless of impact level and SHALL include supply chain risk considerations.
[VALIDATION] IF system_classification = "HVA" AND criticality_analysis_required = FALSE THEN critical_violation

[RULE-04] Developer criticality analysis documentation MUST be delivered within 30 days of each SDLC decision point and include detailed design documentation, functional specifications, and risk assessments.
[VALIDATION] IF analysis_delivery_date > (decision_point_date + 30_days) THEN violation

[RULE-05] COTS products MUST include vendor-provided criticality analysis or organization SHALL perform independent analysis using available documentation and testing.
[VALIDATION] IF product_type = "COTS" AND (vendor_analysis_provided = FALSE AND independent_analysis_completed = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Criticality Analysis Requirements Definition - Establish analysis scope and methodology
- [PROC-02] Developer Contract Integration - Include analysis requirements in procurement
- [PROC-03] Analysis Review and Validation - Evaluate submitted criticality assessments
- [PROC-04] COTS Product Assessment - Handle commercial product analysis requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: New HVA designation, major acquisition, supply chain incident

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing HVA Analysis]
IF system_classification = "HVA"
AND criticality_analysis_completed = FALSE
AND development_phase = "design_review"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Incomplete COTS Assessment]
IF component_type = "COTS"
AND vendor_analysis_provided = FALSE
AND independent_analysis_completed = FALSE
AND system_impact_level = "high"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Late Analysis Delivery]
IF analysis_delivery_date > (decision_point_date + 30_days)
AND system_deployment_pending = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Adequate Low Impact System]
IF system_impact_level = "low"
AND system_classification != "HVA"
AND basic_analysis_completed = TRUE
THEN compliance = TRUE

[SCENARIO-05: Supply Chain Critical Component]
IF component_source = "foreign_vendor"
AND component_criticality = "high"
AND supply_chain_analysis_completed = TRUE
AND decision_point = "integration_testing"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer performs analysis at defined decision points | [RULE-01] |
| Analysis performed at defined rigor level (breadth) | [RULE-02] |
| Analysis performed at defined rigor level (depth) | [RULE-02] |
| HVA systems receive mandatory analysis | [RULE-03] |
| Timely delivery of analysis documentation | [RULE-04] |