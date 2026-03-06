# POLICY: AU-9.5: Dual Authorization

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AU-9.5 |
| NIST Control | AU-9.5: Dual Authorization |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | audit, dual authorization, two-person control, audit information movement, collusion prevention |

## 1. POLICY STATEMENT
The organization SHALL enforce dual authorization (two-person control) for the movement of audit information as defined by risk classification and regulatory requirements. Dual authorization mechanisms require approval from two authorized individuals before audit information can be moved, transferred, or relocated.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Audit logs and records | YES | All audit information classified as sensitive or critical |
| System administrators | YES | Personnel with audit system access |
| Security operations staff | YES | Personnel handling audit information |
| Automated audit transfers | CONDITIONAL | When transferring sensitive audit data |
| Emergency response actions | NO | When immediate response required for safety |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define audit information requiring dual authorization<br>• Approve dual authorization procedures<br>• Monitor compliance with dual authorization requirements |
| Security Operations Manager | • Implement dual authorization controls<br>• Maintain authorized personnel lists<br>• Rotate dual authorization duties |
| System Administrators | • Execute dual authorization procedures<br>• Document all dual authorization activities<br>• Report dual authorization violations |

## 4. RULES
[RULE-01] Dual authorization MUST be enforced for movement of audit information classified as sensitive, critical, or containing PII/PHI.
[VALIDATION] IF audit_classification IN ["sensitive", "critical", "PII", "PHI"] AND movement_requested = TRUE AND dual_authorization_completed = FALSE THEN violation

[RULE-02] Two authorized individuals MUST approve audit information movement before execution, with neither individual having subordinate relationship to the other.
[VALIDATION] IF approver_1_id = approver_2_id OR subordinate_relationship(approver_1, approver_2) = TRUE THEN critical_violation

[RULE-03] Dual authorization duties MUST be rotated among qualified personnel at least every 90 days to reduce collusion risk.
[VALIDATION] IF days_since_last_rotation > 90 AND personnel_pool_size >= 4 THEN violation

[RULE-04] All dual authorization activities MUST be logged with timestamps, personnel identities, and justification within 24 hours.
[VALIDATION] IF dual_auth_executed = TRUE AND log_entry_time - execution_time > 24_hours THEN violation

[RULE-05] Emergency exceptions to dual authorization MUST be documented, approved by CISO within 72 hours, and reviewed monthly.
[VALIDATION] IF emergency_exception = TRUE AND ciso_approval_time > 72_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Dual Authorization Request Process - Standardized workflow for requesting and approving audit information movement
- [PROC-02] Personnel Rotation Schedule - Process for rotating dual authorization responsibilities among qualified staff
- [PROC-03] Emergency Exception Handling - Procedures for bypassing dual authorization during emergencies
- [PROC-04] Audit Information Classification - Process for determining which audit information requires dual authorization

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving audit data, regulatory changes, personnel changes in security roles

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Sensitive Audit Transfer]
IF audit_classification = "sensitive"
AND movement_type = "transfer_to_archive"
AND dual_authorization_completed = TRUE
AND approvers_independent = TRUE
THEN compliance = TRUE

[SCENARIO-02: Single Approval Attempt]
IF audit_classification = "critical"
AND movement_requested = TRUE
AND approval_count = 1
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Emergency Safety Override]
IF emergency_type = "public_safety"
AND immediate_response_required = TRUE
AND dual_authorization_bypassed = TRUE
AND post_incident_documentation = TRUE
THEN compliance = TRUE

[SCENARIO-04: Collusion Risk - Same Department]
IF approver_1_department = approver_2_department
AND department_size < 3
AND alternative_approvers_available = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Expired Rotation Period]
IF current_date - last_rotation_date > 90
AND dual_auth_personnel_count >= 4
AND rotation_not_performed = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Dual authorization enforcement for defined audit information | [RULE-01] |
| Two-person control mechanism implementation | [RULE-02] |
| Collusion prevention through duty rotation | [RULE-03] |
| Documentation and logging of dual authorization activities | [RULE-04] |
| Emergency exception handling and approval | [RULE-05] |