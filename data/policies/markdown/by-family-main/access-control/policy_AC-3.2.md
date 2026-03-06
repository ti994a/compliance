# POLICY: AC-3.2: Dual Authorization

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-3.2 |
| NIST Control | AC-3.2: Dual Authorization |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | dual authorization, two-person control, privileged commands, insider threats, approval |

## 1. POLICY STATEMENT
The organization SHALL enforce dual authorization (two-person control) for all privileged commands and critical actions that could significantly impact system security, data integrity, or business operations. Dual authorization requires approval from two separate authorized individuals before execution to reduce insider threat risks and prevent unauthorized actions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT Systems | YES | Production, staging, and critical development systems |
| Cloud Infrastructure | YES | AWS, Azure, GCP privileged operations |
| Database Systems | YES | Production databases containing sensitive data |
| Network Infrastructure | YES | Core routers, firewalls, security appliances |
| End User Workstations | NO | Standard user operations excluded |
| Development Systems | CONDITIONAL | Only if processing production data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Implement dual authorization controls<br>• Maintain approved authorizer lists<br>• Execute second-person verification |
| Security Team | • Define privileged commands requiring dual authorization<br>• Monitor dual authorization compliance<br>• Rotate authorization duties quarterly |
| IT Management | • Approve dual authorization procedures<br>• Ensure adequate staffing for coverage<br>• Review emergency override procedures |

## 4. RULES

[RULE-01] All privileged commands affecting production systems MUST require approval from two separate authorized individuals before execution.
[VALIDATION] IF command_type = "privileged" AND system_environment = "production" AND approver_count < 2 THEN violation

[RULE-02] The two authorizing individuals MUST NOT have reporting relationships or shared financial interests to prevent collusion.
[VALIDATION] IF authorizer_1_reports_to = authorizer_2 OR shared_financial_interest = TRUE THEN violation

[RULE-03] Dual authorization duties MUST be rotated quarterly to minimize collusion risks.
[VALIDATION] IF last_rotation_date < (current_date - 90_days) THEN violation

[RULE-04] Emergency overrides of dual authorization MUST be documented, approved by IT management within 4 hours, and reviewed within 24 hours.
[VALIDATION] IF emergency_override = TRUE AND management_approval_time > 4_hours THEN violation

[RULE-05] All dual authorization actions MUST be logged with timestamps, user identities, and justification.
[VALIDATION] IF dual_auth_action = TRUE AND (log_entry = FALSE OR timestamp = NULL OR justification = NULL) THEN violation

[RULE-06] Systems MUST technically enforce dual authorization and prevent single-person execution of defined privileged commands.
[VALIDATION] IF privileged_command_executed = TRUE AND technical_enforcement = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Privileged Command Classification - Annual review and classification of commands requiring dual authorization
- [PROC-02] Authorizer Management - Quarterly rotation and approval of dual authorization personnel
- [PROC-03] Emergency Override Process - Documented procedure for emergency situations requiring immediate action
- [PROC-04] Audit and Monitoring - Monthly review of dual authorization logs and compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, system changes, personnel changes, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Standard Privileged Command]
IF command_type = "privileged"
AND system_environment = "production"
AND approver_count = 2
AND approvers_independent = TRUE
THEN compliance = TRUE

[SCENARIO-02: Single Person Override]
IF command_type = "privileged"
AND approver_count = 1
AND emergency_override = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Emergency Override with Proper Documentation]
IF command_type = "privileged"
AND approver_count = 1
AND emergency_override = TRUE
AND management_approval_time <= 4_hours
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-04: Collusion Risk - Related Approvers]
IF approver_count = 2
AND (authorizer_1_reports_to = authorizer_2 OR shared_department = TRUE)
AND independent_verification = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Missing Technical Enforcement]
IF privileged_command_executed = TRUE
AND manual_approval_only = TRUE
AND technical_enforcement = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Dual authorization is enforced for privileged commands | RULE-01, RULE-06 |
| Actions requiring dual authorization are defined | PROC-01 |
| Two-person control prevents collusion | RULE-02, RULE-03 |
| Emergency procedures are documented | RULE-04 |
| Audit trail maintained | RULE-05 |