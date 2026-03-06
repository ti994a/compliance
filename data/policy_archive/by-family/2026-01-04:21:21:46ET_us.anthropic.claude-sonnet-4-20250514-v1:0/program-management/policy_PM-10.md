# POLICY: PM-10: Authorization Process

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-10 |
| NIST Control | PM-10: Authorization Process |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | authorization, risk management, authorizing official, continuous monitoring, security state, privacy state |

## 1. POLICY STATEMENT
The organization SHALL manage the security and privacy state of all organizational systems through formal authorization processes integrated with organization-wide risk management. Designated individuals MUST fulfill specific roles and responsibilities within the risk management process to ensure ongoing understanding and acceptance of security and privacy risks.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Including cloud, on-premises, and hybrid systems |
| Common control providers | YES | Shared services and infrastructure |
| Third-party hosted systems | YES | Where organization maintains data ownership |
| Development/test environments | CONDITIONAL | If processing production data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Risk Executive | • Oversee organization-wide risk management program<br>• Approve risk management strategy<br>• Ensure integration of authorization processes |
| Authorizing Official | • Make risk-based authorization decisions<br>• Accept security and privacy risks<br>• Oversee continuous monitoring activities |
| System Owner | • Implement security and privacy controls<br>• Maintain system authorization documentation<br>• Report security and privacy posture changes |

## 4. RULES
[RULE-01] Each organizational system MUST have a designated Authorizing Official with documented authority to accept security and privacy risks.
[VALIDATION] IF system_in_production = TRUE AND authorizing_official = NULL THEN violation

[RULE-02] Authorization processes MUST be integrated with the organization-wide risk management program and documented in security and privacy program plans.
[VALIDATION] IF authorization_process_documented = FALSE OR risk_management_integration = FALSE THEN violation

[RULE-03] System authorization decisions MUST be based on current risk assessments completed within the last 365 days.
[VALIDATION] IF authorization_date > risk_assessment_date + 365_days THEN violation

[RULE-04] Continuous monitoring processes MUST be established for all authorized systems to maintain ongoing risk awareness.
[VALIDATION] IF system_authorized = TRUE AND continuous_monitoring = FALSE THEN violation

[RULE-05] Authorization documentation MUST be updated within 30 days of significant system changes that affect security or privacy posture.
[VALIDATION] IF significant_change_date + 30_days < current_date AND authorization_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Authorization Process - Define steps for initial system authorization including risk assessment, control implementation, and AO decision
- [PROC-02] Continuous Monitoring Process - Establish ongoing monitoring, assessment, and reporting requirements
- [PROC-03] Role Assignment Process - Document procedures for designating and training risk management personnel
- [PROC-04] Risk Management Integration - Define integration points between authorization and enterprise risk management

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or upon significant organizational changes
- Triggering events: Major system implementations, regulatory changes, significant security incidents, organizational restructuring

## 7. SCENARIO PATTERNS
[SCENARIO-01: New System Deployment]
IF system_status = "ready_for_production"
AND authorizing_official_assigned = TRUE
AND risk_assessment_current = TRUE
AND authorization_decision = "approved"
THEN compliance = TRUE

[SCENARIO-02: Unauthorized System Operation]
IF system_in_production = TRUE
AND authorization_decision = NULL
AND days_in_production > 30
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Outdated Risk Assessment]
IF system_authorized = TRUE
AND risk_assessment_age > 365_days
AND reauthorization_initiated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Continuous Monitoring]
IF system_authorized = TRUE
AND continuous_monitoring_plan = FALSE
AND authorization_date > 90_days_ago
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Unaddressed Significant Change]
IF significant_system_change = TRUE
AND change_date + 30_days < current_date
AND authorization_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Security state managed through authorization processes | [RULE-01], [RULE-03] |
| Privacy state managed through authorization processes | [RULE-01], [RULE-03] |
| Individuals designated for risk management roles | [RULE-01] |
| Authorization processes integrated into risk management program | [RULE-02], [RULE-04] |