# POLICY: PS-3.2: Formal Indoctrination

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-3.2 |
| NIST Control | PS-3.2: Formal Indoctrination |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | classified information, formal indoctrination, SAP, RD, SCI, access verification, personnel security |

## 1. POLICY STATEMENT
All individuals accessing systems that process, store, or transmit classified information requiring formal indoctrination must complete verified formal indoctrination for each relevant classification type before system access is granted. Access verification must confirm indoctrination status matches the classification levels of information accessible through assigned system permissions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal Employees | YES | All clearance levels |
| Contractors | YES | When accessing classified systems |
| Temporary Personnel | YES | Including short-term assignments |
| Systems Processing Classified Data | YES | SAP, RD, SCI systems only |
| Unclassified Systems | NO | Standard background checks apply |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Control Assessor | • Verify indoctrination documentation completeness<br>• Validate access permissions align with indoctrination levels<br>• Conduct periodic compliance audits |
| System Administrator | • Implement access controls based on indoctrination verification<br>• Maintain current indoctrination status records<br>• Report indoctrination discrepancies immediately |
| Personnel Security Manager | • Coordinate formal indoctrination processes<br>• Maintain authoritative indoctrination records<br>• Provide indoctrination status to system administrators |

## 4. RULES
[RULE-01] Individuals MUST complete formal indoctrination for each classification type (SAP, RD, SCI) before accessing systems containing that information type.
[VALIDATION] IF user_access_granted = TRUE AND formal_indoctrination_complete = FALSE THEN critical_violation

[RULE-02] System administrators MUST verify current indoctrination status before provisioning access to classified systems.
[VALIDATION] IF access_provisioned = TRUE AND indoctrination_verification_date > 30_days_old THEN violation

[RULE-03] Access permissions SHALL NOT exceed the scope of completed formal indoctrination programs.
[VALIDATION] IF system_classification_level > user_indoctrination_level THEN critical_violation

[RULE-04] Indoctrination status verification MUST be documented and retained for audit purposes.
[VALIDATION] IF system_access = TRUE AND indoctrination_documentation = NULL THEN violation

[RULE-05] Formal indoctrination requirements MUST be reassessed when user roles change or additional classified information types are introduced.
[VALIDATION] IF role_change_date > indoctrination_assessment_date AND classified_access = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Indoctrination Verification Process - Validate and document completion of required formal indoctrination programs
- [PROC-02] Access Provisioning Workflow - Ensure indoctrination verification precedes classified system access grants
- [PROC-03] Periodic Compliance Audit - Review indoctrination status alignment with current access permissions
- [PROC-04] Role Change Assessment - Evaluate indoctrination requirements when personnel responsibilities change

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New classification types introduced, personnel role changes, security incidents involving indoctrination gaps

## 7. SCENARIO PATTERNS
[SCENARIO-01: Contractor SAP Access]
IF user_type = "contractor"
AND system_contains = "SAP_information"
AND SAP_indoctrination_complete = FALSE
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Multi-Classification System Access]
IF system_contains = ["SCI", "RD"]
AND user_SCI_indoctrination = TRUE
AND user_RD_indoctrination = FALSE
AND RD_access_permissions = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Expired Indoctrination Verification]
IF indoctrination_verification_date < (current_date - 30_days)
AND classified_system_access = TRUE
AND re_verification_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Role Elevation Without Assessment]
IF previous_clearance_level = "Secret"
AND current_clearance_level = "TS/SCI"
AND SCI_indoctrination_complete = TRUE
AND indoctrination_reassessment_date = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Indoctrination Alignment]
IF user_indoctrination_types = ["SAP", "SCI"]
AND system_classification_types = ["SAP"]
AND access_permissions_scope <= indoctrination_scope
AND verification_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Individuals accessing classified systems are formally indoctrinated for relevant information types | [RULE-01], [RULE-03] |
| Indoctrination verification occurs before access provisioning | [RULE-02] |
| Access scope aligns with indoctrination completion | [RULE-03] |
| Indoctrination status documentation is maintained | [RULE-04] |
| Reassessment occurs with role or system changes | [RULE-05] |