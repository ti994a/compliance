# POLICY: CM-5.4: Dual Authorization

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-5.4 |
| NIST Control | CM-5.4: Dual Authorization |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | dual authorization, two-person control, change management, system components, configuration management |

## 1. POLICY STATEMENT
All changes to critical system components and system-level information MUST be implemented using dual authorization requiring approval and implementation by two qualified individuals. This control ensures that no single person can make unauthorized changes to systems that could compromise security, integrity, or availability.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All production environments |
| Critical System Components | YES | As defined in asset inventory |
| System-Level Information | YES | Operational procedures, configurations |
| Development Systems | CONDITIONAL | Only if processing production data |
| Test Systems | NO | Unless containing production data |
| Emergency Changes | CONDITIONAL | Expedited process with post-implementation review |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Change Approver | • Review and approve change requests<br>• Validate technical correctness<br>• Document approval rationale |
| Change Implementer | • Execute approved changes<br>• Verify implementation success<br>• Document implementation details |
| Change Manager | • Define dual authorization requirements<br>• Maintain authorized personnel lists<br>• Monitor compliance with dual authorization |

## 4. RULES

[RULE-01] Critical system components requiring dual authorization MUST be formally defined and documented in the asset inventory with appropriate classification.
[VALIDATION] IF component_classification = "critical" AND dual_auth_required = FALSE THEN violation

[RULE-02] Changes to dual authorization components MUST be approved by one qualified individual and implemented by a different qualified individual.
[VALIDATION] IF approver_id = implementer_id THEN critical_violation

[RULE-03] Both approver and implementer MUST possess documented technical competency for the specific system component being changed.
[VALIDATION] IF approver_competency = FALSE OR implementer_competency = FALSE THEN violation

[RULE-04] Dual authorization personnel assignments MUST be rotated at least every 12 months to reduce collusion risk.
[VALIDATION] IF personnel_rotation_date > 365_days THEN violation

[RULE-05] Emergency changes bypassing dual authorization MUST undergo post-implementation review within 24 hours.
[VALIDATION] IF emergency_change = TRUE AND post_review_time > 24_hours THEN violation

[RULE-06] All dual authorization activities MUST be logged with timestamps, personnel identities, and change details.
[VALIDATION] IF dual_auth_log = NULL OR incomplete_log_fields > 0 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Dual Authorization Component Classification - Process for identifying and classifying components requiring dual authorization
- [PROC-02] Personnel Qualification Verification - Validation of technical competencies for dual authorization roles
- [PROC-03] Emergency Change Management - Expedited process with mandatory post-implementation review
- [PROC-04] Personnel Rotation Management - Systematic rotation of dual authorization assignments

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving unauthorized changes, personnel changes in critical roles, system architecture changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Standard Dual Authorization Change]
IF component_type = "critical"
AND approver_id ≠ implementer_id
AND both_qualified = TRUE
AND change_logged = TRUE
THEN compliance = TRUE

[SCENARIO-02: Same Person Approval and Implementation]
IF component_type = "critical"
AND approver_id = implementer_id
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Unqualified Personnel]
IF component_type = "critical"
AND (approver_qualified = FALSE OR implementer_qualified = FALSE)
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Emergency Change with Timely Review]
IF change_type = "emergency"
AND dual_auth_bypassed = TRUE
AND post_review_completed = TRUE
AND review_time ≤ 24_hours
THEN compliance = TRUE

[SCENARIO-05: Overdue Personnel Rotation]
IF personnel_assignment_duration > 365_days
AND rotation_exception = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Dual authorization for system components is defined | [RULE-01] |
| Dual authorization for system components is enforced | [RULE-02], [RULE-06] |
| Dual authorization for system-level information is defined | [RULE-01] |
| Dual authorization for system-level information is enforced | [RULE-02], [RULE-06] |
| Personnel qualification requirements | [RULE-03] |
| Collusion risk mitigation | [RULE-04] |
| Emergency change controls | [RULE-05] |