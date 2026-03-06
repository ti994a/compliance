# POLICY: CA-2: Control Assessments

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CA-2 |
| NIST Control | CA-2: Control Assessments |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | control assessment, assessment plan, assessor independence, control effectiveness, assessment report, continuous monitoring |

## 1. POLICY STATEMENT
The organization SHALL conduct systematic assessments of security and privacy controls to determine their effectiveness and compliance with established requirements. All control assessments MUST be performed by qualified assessors using approved assessment plans and documented through formal assessment reports.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems requiring ATO |
| Cloud Services | YES | Including hybrid deployments |
| Third-party Services | YES | Where organization has control assessment responsibility |
| Development Systems | YES | During SDLC phases |
| Legacy Systems | YES | Subject to continuous monitoring |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Authorizing Official | • Approve assessment plans<br>• Review assessment reports<br>• Make authorization decisions |
| Control Assessor | • Develop assessment plans<br>• Execute control assessments<br>• Produce assessment reports |
| System Owner | • Support assessment activities<br>• Implement remediation actions<br>• Maintain assessment artifacts |
| CISO | • Define assessment standards<br>• Ensure assessor qualifications<br>• Oversee assessment program |

## 4. RULES

[RULE-01] Control assessors MUST possess appropriate technical expertise and independence for the type of assessment being conducted.
[VALIDATION] IF assessor_independence_level < required_independence_level OR assessor_qualifications = "insufficient" THEN violation

[RULE-02] Control assessment plans MUST be developed and include scope, procedures, environment, team composition, and roles/responsibilities before assessment execution.
[VALIDATION] IF assessment_plan_approved = FALSE OR required_plan_elements < 5 THEN violation

[RULE-03] Assessment plans MUST be reviewed and approved by the Authorizing Official or designated representative prior to assessment execution.
[VALIDATION] IF assessment_plan_approval = FALSE OR approver_authority = "insufficient" THEN violation

[RULE-04] Control assessments MUST be conducted at organization-defined frequencies to determine implementation correctness, operational effectiveness, and outcome achievement.
[VALIDATION] IF days_since_last_assessment > max_assessment_interval THEN violation

[RULE-05] Control assessment reports MUST document assessment results in sufficient detail to determine control effectiveness and compliance status.
[VALIDATION] IF assessment_report_completeness < "adequate" OR control_effectiveness_determination = "missing" THEN violation

[RULE-06] Assessment results MUST be provided to appropriate individuals and roles based on assessment type and organizational requirements.
[VALIDATION] IF required_recipients_notified = FALSE OR notification_timeframe > 30_days THEN violation

[RULE-07] Assessment results MUST be current, relevant, and obtained with appropriate assessor independence for reuse in authorization decisions.
[VALIDATION] IF assessment_age > 12_months AND reuse_justification = "missing" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Assessor Selection and Qualification - Process for selecting qualified assessors with appropriate independence
- [PROC-02] Assessment Plan Development - Standard methodology for creating comprehensive assessment plans  
- [PROC-03] Assessment Execution - Standardized procedures for conducting control assessments
- [PROC-04] Assessment Reporting - Format and content requirements for assessment reports
- [PROC-05] Results Distribution - Process for delivering assessment results to appropriate stakeholders

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Regulatory changes, significant security incidents, organizational restructuring, technology changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Independent Assessor Required]
IF assessment_type = "initial_authorization"
AND system_impact_level = "high"
AND proposed_assessor_independence = "internal"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Outdated Assessment Reuse]
IF previous_assessment_age > 12_months
AND reuse_justification = "missing"
AND authorization_decision = "pending"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Incomplete Assessment Plan]
IF assessment_plan_elements < 5
AND assessment_execution = "started"
AND ao_approval = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Continuous Monitoring Assessment]
IF system_status = "operational"
AND days_since_last_assessment > 365
AND continuous_monitoring_strategy = "annual"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Qualified Assessor Assignment]
IF assessor_certification = "valid"
AND assessor_experience_years >= 3
AND conflict_of_interest = FALSE
AND assessment_complexity = "standard"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Assessment Objective | Rule Reference |
|---------------------|---------------|
| Appropriate assessor selection | [RULE-01] |
| Assessment plan scope - controls and enhancements | [RULE-02] |
| Assessment plan scope - procedures | [RULE-02] |
| Assessment plan scope - environment | [RULE-02] |
| Assessment plan scope - team composition | [RULE-02] |
| Assessment plan scope - roles and responsibilities | [RULE-02] |
| Assessment plan approval | [RULE-03] |
| Control assessment execution - security requirements | [RULE-04] |
| Control assessment execution - privacy requirements | [RULE-04] |
| Assessment report production | [RULE-05] |
| Results distribution | [RULE-06] |