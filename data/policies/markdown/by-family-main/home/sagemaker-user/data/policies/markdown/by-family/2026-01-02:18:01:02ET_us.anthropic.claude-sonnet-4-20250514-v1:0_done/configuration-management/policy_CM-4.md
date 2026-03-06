```markdown
# POLICY: CM-4: Impact Analyses

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-4 |
| NIST Control | CM-4: Impact Analyses |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | impact analysis, change management, security assessment, privacy assessment, risk analysis |

## 1. POLICY STATEMENT
All changes to information systems must undergo security and privacy impact analysis prior to implementation to identify potential risks and required controls. Impact analyses must be conducted by qualified personnel with appropriate security and privacy expertise.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All changes regardless of size |
| Development Systems | YES | When handling production data |
| Cloud Infrastructure | YES | Including third-party services |
| Network Components | YES | Firewalls, routers, switches |
| Applications | YES | Custom and commercial software |
| Emergency Changes | CONDITIONAL | Retrospective analysis required |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Architect | • Conduct security impact analyses<br>• Review system design changes<br>• Assess control effectiveness |
| Privacy Officer | • Conduct privacy impact analyses<br>• Evaluate PII handling changes<br>• Assess privacy control impacts |
| Change Control Board | • Review impact analysis results<br>• Approve/reject changes<br>• Ensure analysis completeness |

## 4. RULES

[RULE-01] Security impact analysis MUST be completed for all system changes before implementation approval.
[VALIDATION] IF change_request_submitted = TRUE AND security_impact_analysis_complete = FALSE THEN violation

[RULE-02] Privacy impact analysis MUST be completed for changes affecting PII processing, storage, or transmission.
[VALIDATION] IF change_affects_PII = TRUE AND privacy_impact_analysis_complete = FALSE THEN violation

[RULE-03] Impact analyses MUST be conducted by personnel with demonstrated security or privacy expertise and appropriate training.
[VALIDATION] IF analyst_certification_current = FALSE OR analyst_training_complete = FALSE THEN violation

[RULE-04] Impact analyses MUST include review of security plans, policies, control requirements, and system design documentation.
[VALIDATION] IF documentation_reviewed < required_documents THEN violation

[RULE-05] Risk assessments MUST be performed when impact analysis identifies new or increased risks requiring additional controls.
[VALIDATION] IF new_risks_identified = TRUE AND risk_assessment_complete = FALSE THEN violation

[RULE-06] Emergency changes MAY proceed without prior impact analysis but MUST undergo retrospective analysis within 72 hours.
[VALIDATION] IF change_type = "emergency" AND retrospective_analysis_time > 72_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Security Impact Analysis - Standardized methodology for evaluating security implications
- [PROC-02] Privacy Impact Analysis - Process for assessing privacy risks and control impacts
- [PROC-03] Risk Assessment - Framework for evaluating and documenting identified risks
- [PROC-04] Emergency Change Analysis - Retrospective impact analysis procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system changes, security incidents, regulatory updates, control failures

## 7. SCENARIO PATTERNS

[SCENARIO-01: Standard Application Update]
IF change_type = "application_update"
AND security_impact_analysis_complete = TRUE
AND privacy_impact_analysis_complete = TRUE
AND analyst_qualified = TRUE
THEN compliance = TRUE

[SCENARIO-02: Database Schema Change Without Privacy Analysis]
IF change_affects_PII = TRUE
AND privacy_impact_analysis_complete = FALSE
AND change_implemented = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Emergency Security Patch]
IF change_type = "emergency"
AND security_risk = "critical"
AND change_implemented = TRUE
AND retrospective_analysis_complete = TRUE
AND analysis_completion_time <= 72_hours
THEN compliance = TRUE

[SCENARIO-04: Unqualified Analyst Conducting Analysis]
IF impact_analysis_complete = TRUE
AND analyst_certification_current = FALSE
AND change_approved = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Incomplete Documentation Review]
IF security_plan_reviewed = FALSE
OR control_requirements_reviewed = FALSE
OR system_design_reviewed = FALSE
AND impact_analysis_marked_complete = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Security impact analysis prior to implementation | [RULE-01] |
| Privacy impact analysis prior to implementation | [RULE-02] |
| Qualified personnel conducting analyses | [RULE-03] |
| Comprehensive documentation review | [RULE-04] |
| Risk assessment for identified risks | [RULE-05] |
```