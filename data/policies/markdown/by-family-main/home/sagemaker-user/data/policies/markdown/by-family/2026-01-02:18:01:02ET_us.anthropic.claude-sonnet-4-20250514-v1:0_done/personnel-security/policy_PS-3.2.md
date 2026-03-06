```markdown
# POLICY: PS-3.2: Formal Indoctrination

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-3.2 |
| NIST Control | PS-3.2: Formal Indoctrination |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | classified information, formal indoctrination, SAP, RD, SCI, personnel security, access verification |

## 1. POLICY STATEMENT
All individuals accessing systems that process, store, or transmit classified information requiring formal indoctrination MUST be formally indoctrinated for every type of classified information they will access. Verification of proper indoctrination MUST occur before granting system access and be maintained throughout the access period.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal employees | YES | All classifications |
| Contractors | YES | When accessing classified systems |
| Visitors | YES | If granted classified system access |
| Systems processing SAP/RD/SCI | YES | All such systems regardless of location |
| Development/test systems | YES | If containing classified data |
| Cloud systems | YES | If processing classified information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Control Assessor | • Verify indoctrination documentation completeness<br>• Validate access authorization alignment<br>• Conduct periodic compliance reviews |
| System Administrator | • Implement access controls based on indoctrination status<br>• Maintain current indoctrination records<br>• Report access violations immediately |
| Personnel Security Officer | • Verify formal indoctrination completion<br>• Maintain indoctrination documentation<br>• Coordinate with security managers on access decisions |

## 4. RULES
[RULE-01] Personnel MUST complete formal indoctrination for Special Access Program (SAP), Restricted Data (RD), or Sensitive Compartmented Information (SCI) before accessing systems containing such information.
[VALIDATION] IF user_access_granted = TRUE AND (SAP_indoctrination = FALSE OR RD_indoctrination = FALSE OR SCI_indoctrination = FALSE) AND system_contains_matching_classification = TRUE THEN critical_violation

[RULE-02] System administrators MUST verify current indoctrination status before provisioning access to classified systems.
[VALIDATION] IF access_provisioned = TRUE AND indoctrination_verification_date > 30_days_ago THEN violation

[RULE-03] Indoctrination documentation MUST be maintained and accessible for verification throughout the duration of system access.
[VALIDATION] IF user_has_classified_access = TRUE AND indoctrination_documentation_available = FALSE THEN violation

[RULE-04] Access MUST be immediately revoked when indoctrination expires or is withdrawn.
[VALIDATION] IF indoctrination_status = "expired" OR indoctrination_status = "revoked" AND system_access_active = TRUE THEN critical_violation

[RULE-05] Personnel accessing multiple classification types MUST have formal indoctrination for each specific type accessed on the system.
[VALIDATION] IF system_classification_types > user_indoctrination_types THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Indoctrination Verification Process - Validate completion before access provisioning
- [PROC-02] Access Provisioning Controls - Link system access to verified indoctrination status
- [PROC-03] Periodic Indoctrination Review - Quarterly verification of continued indoctrination validity
- [PROC-04] Emergency Access Revocation - Immediate removal when indoctrination status changes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, indoctrination program changes, new classification types, system modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Contractor SAP Access]
IF user_type = "contractor"
AND system_contains = "SAP"
AND SAP_indoctrination_verified = FALSE
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Multiple Classification Access]
IF system_classifications = ["SAP", "SCI"]
AND user_indoctrinations = ["SAP"]
AND SCI_access_attempted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Expired Indoctrination]
IF RD_indoctrination_expiry < current_date
AND system_contains = "RD"
AND user_access_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Proper Indoctrination Match]
IF user_indoctrinations = ["SAP", "SCI"]
AND system_classifications = ["SAP", "SCI"]
AND all_indoctrinations_current = TRUE
AND verification_completed = TRUE
THEN compliance = TRUE

[SCENARIO-05: Documentation Missing]
IF user_has_classified_access = TRUE
AND indoctrination_claimed = TRUE
AND documentation_available = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Individuals accessing classified systems are formally indoctrinated for relevant information types | RULE-01, RULE-05 |
| Verification occurs before access provisioning | RULE-02 |
| Documentation maintained throughout access period | RULE-03 |
| Access revoked when indoctrination invalid | RULE-04 |
```