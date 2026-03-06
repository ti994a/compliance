# POLICY: PL-2: System Security and Privacy Plans

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PL-2 |
| NIST Control | PL-2: System Security and Privacy Plans |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | system security plan, privacy plan, authorization, enterprise architecture, risk assessment, control documentation |

## 1. POLICY STATEMENT
All information systems MUST have comprehensive security and privacy plans that document system components, operational context, security controls, and risk determinations before receiving authorization to operate. These plans MUST be reviewed, approved by the authorizing official, regularly updated, and protected from unauthorized access or modification.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, hybrid, and on-premises systems |
| System Components | YES | All constituent components within authorization boundary |
| Development Projects | YES | Plans required before deployment |
| Legacy Systems | YES | Must have current plans or remediation timeline |
| Contractor Systems | CONDITIONAL | When processing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Ensure plan development and maintenance<br>• Coordinate with stakeholders<br>• Submit for authorization |
| Authorizing Official | • Review and approve plans<br>• Make authorization decisions<br>• Oversee plan compliance |
| Information System Security Officer | • Develop security plan content<br>• Conduct security assessments<br>• Monitor plan implementation |
| Privacy Officer | • Develop privacy plan content<br>• Conduct privacy risk assessments<br>• Ensure PII protection requirements |

## 4. RULES

[RULE-01] System security and privacy plans MUST be developed for all information systems before authorization to operate.
[VALIDATION] IF system_status = "pre-authorization" AND (security_plan_exists = FALSE OR privacy_plan_exists = FALSE) THEN violation

[RULE-02] Plans MUST explicitly define all constituent system components within the authorization boundary.
[VALIDATION] IF system_components_documented = FALSE OR authorization_boundary_defined = FALSE THEN violation

[RULE-03] Plans MUST include security categorization with supporting rationale based on information types processed.
[VALIDATION] IF security_categorization_missing = TRUE OR categorization_rationale_missing = TRUE THEN violation

[RULE-04] Plans MUST identify system roles, responsibilities, and assigned personnel.
[VALIDATION] IF roles_responsibilities_documented = FALSE OR personnel_assignments_missing = TRUE THEN violation

[RULE-05] Plans MUST include results of privacy risk assessment for systems processing PII.
[VALIDATION] IF processes_pii = TRUE AND privacy_risk_assessment_missing = TRUE THEN violation

[RULE-06] Plans MUST describe operational environment and system dependencies/connections.
[VALIDATION] IF operational_environment_documented = FALSE OR system_dependencies_missing = TRUE THEN violation

[RULE-07] Plans MUST document selected controls with implementation details and tailoring rationale.
[VALIDATION] IF control_documentation_incomplete = TRUE OR tailoring_rationale_missing = TRUE THEN violation

[RULE-08] Plans MUST be reviewed and approved by the authorizing official before implementation.
[VALIDATION] IF authorizing_official_approval = FALSE AND system_operational = TRUE THEN critical_violation

[RULE-09] Plans MUST be reviewed at least annually and updated when system changes occur.
[VALIDATION] IF last_review_date > 365_days OR (system_changes = TRUE AND plan_updated = FALSE) THEN violation

[RULE-10] Plans MUST be protected from unauthorized disclosure and modification with appropriate access controls.
[VALIDATION] IF plan_access_controls = FALSE OR unauthorized_modifications_possible = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Security Plan Development - Template-based plan creation with required elements
- [PROC-02] Privacy Plan Development - PII-specific risk assessment and control documentation  
- [PROC-03] Plan Review and Approval - Authorizing official review and decision process
- [PROC-04] Plan Distribution and Communication - Controlled distribution to authorized personnel
- [PROC-05] Plan Maintenance and Updates - Change management and version control process

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or when NIST guidance updates
- Triggering events: System modifications, security incidents, failed assessments, organizational changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: New System Deployment]
IF system_status = "ready_for_production"
AND security_plan_approved = FALSE
AND privacy_plan_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: System Modification Without Plan Update]
IF system_modification_date > plan_last_updated_date
AND modification_impact = "significant"
AND plan_update_initiated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: PII Processing Without Privacy Assessment]
IF system_processes_pii = TRUE
AND privacy_risk_assessment_completed = FALSE
AND privacy_plan_includes_assessment = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Outdated Plan Review]
IF plan_last_review_date > 365_days
AND annual_review_scheduled = FALSE
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Unauthorized Plan Access]
IF plan_access_controls_implemented = FALSE
AND unauthorized_personnel_access = TRUE
AND plan_contains_sensitive_info = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Assessment Objective | Rule Reference |
|---------------------|----------------|
| Security plan developed consistent with enterprise architecture | RULE-01, RULE-02 |
| Privacy plan developed consistent with enterprise architecture | RULE-01, RULE-02 |
| Plans explicitly define constituent system components | RULE-02 |
| Plans describe operational context and mission/business processes | RULE-06 |
| Plans identify individuals fulfilling system roles | RULE-04 |
| Plans identify information types processed/stored/transmitted | RULE-03 |
| Plans provide security categorization with rationale | RULE-03 |
| Plans describe specific threats of concern | RULE-07 |
| Plans provide privacy risk assessment results for PII systems | RULE-05 |
| Plans describe operational environment and dependencies | RULE-06 |
| Plans provide security and privacy requirements overview | RULE-07 |
| Plans identify relevant control baselines or overlays | RULE-07 |
| Plans describe controls and tailoring rationale | RULE-07 |
| Plans include risk determinations for architecture decisions | RULE-07 |
| Plans reviewed and approved by authorizing official | RULE-08 |
| Plans distributed to appropriate personnel | RULE-10 |
| Plans reviewed at defined frequency | RULE-09 |
| Plans updated for system/environment changes | RULE-09 |
| Plans protected from unauthorized disclosure/modification | RULE-10 |