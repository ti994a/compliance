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
All individuals accessing systems that process, store, or transmit classified information requiring formal indoctrination MUST be formally indoctrinated for all relevant types of classified information to which they have system access. Formal indoctrination is required for Special Access Program (SAP), Restricted Data (RD), and Sensitive Compartmented Information (SCI).

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal employees | YES | All classifications |
| Contractors | YES | When accessing classified systems |
| Temporary personnel | YES | When accessing classified systems |
| Consultants | YES | When accessing classified systems |
| Visitors | CONDITIONAL | Only if granted system access |
| Systems processing classified data | YES | All classification levels requiring indoctrination |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Control Assessor | • Verify indoctrination completion before access grants<br>• Maintain indoctrination records<br>• Conduct periodic compliance reviews |
| Personnel Security Manager | • Coordinate formal indoctrination processes<br>• Validate indoctrination requirements<br>• Track indoctrination status |
| System Administrator | • Enforce access controls based on indoctrination status<br>• Implement technical controls for classified systems<br>• Report access violations |

## 4. RULES
[RULE-01] Personnel accessing systems containing SAP, RD, or SCI information MUST complete formal indoctrination for each specific classification type before system access is granted.
[VALIDATION] IF user_access_request = TRUE AND system_classification IN ["SAP", "RD", "SCI"] AND formal_indoctrination_complete = FALSE THEN access_denied

[RULE-02] Indoctrination verification MUST be documented and maintained in personnel security records for the duration of access plus 7 years.
[VALIDATION] IF indoctrination_documented = FALSE OR record_retention < (access_duration + 7_years) THEN violation

[RULE-03] System access permissions MUST be restricted to only the classification types for which the individual has completed formal indoctrination.
[VALIDATION] IF user_classification_access > indoctrination_level THEN critical_violation

[RULE-04] Formal indoctrination status MUST be verified within 30 days prior to initial system access and annually thereafter.
[VALIDATION] IF indoctrination_verification_date > 30_days_old AND access_type = "initial" THEN violation
[VALIDATION] IF indoctrination_verification_date > 365_days_old AND access_type = "ongoing" THEN violation

[RULE-05] Personnel whose indoctrination expires or is revoked MUST have system access immediately suspended until re-indoctrination is completed.
[VALIDATION] IF indoctrination_status = "expired" OR indoctrination_status = "revoked" AND system_access = "active" THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Formal Indoctrination Verification - Process for validating completion of required indoctrination programs
- [PROC-02] Classification-Based Access Control - Procedure for mapping indoctrination levels to system access permissions  
- [PROC-03] Indoctrination Record Management - Process for maintaining and auditing indoctrination documentation
- [PROC-04] Access Suspension Protocol - Procedure for immediate access revocation when indoctrination lapses

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Classification level changes, new indoctrination requirements, security incidents involving classified data

## 7. SCENARIO PATTERNS
[SCENARIO-01: Contractor SAP Access]
IF user_type = "contractor"
AND system_classification = "SAP"
AND SAP_indoctrination = FALSE
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Multi-Classification System]
IF system_contains = ["RD", "SCI"]
AND user_RD_indoctrination = TRUE
AND user_SCI_indoctrination = FALSE
AND user_access_level = "SCI_data"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Expired Indoctrination]
IF indoctrination_expiry_date < current_date
AND system_access = "active"
AND access_suspension = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Proper Indoctrination Match]
IF user_classifications = ["RD", "SCI"]
AND system_classification_requirements = ["RD"]
AND RD_indoctrination = TRUE
THEN compliance = TRUE

[SCENARIO-05: Missing Documentation]
IF formal_indoctrination_completed = TRUE
AND indoctrination_documentation = FALSE
AND system_access = "active"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Individuals accessing classified systems are formally indoctrinated for relevant information types | [RULE-01], [RULE-03] |
| Indoctrination verification and documentation | [RULE-02], [RULE-04] |
| Access control enforcement based on indoctrination level | [RULE-03], [RULE-05] |
| Periodic verification of indoctrination status | [RULE-04] |
```