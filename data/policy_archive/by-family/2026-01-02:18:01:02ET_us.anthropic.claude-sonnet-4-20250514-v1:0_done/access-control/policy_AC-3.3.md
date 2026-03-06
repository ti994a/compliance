# POLICY: AC-3.3: Mandatory Access Control

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-3.3 |
| NIST Control | AC-3.3: Mandatory Access Control |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | mandatory access control, MAC, nondiscretionary access, Bell-LaPadula, Biba, reference monitor, classified information |

## 1. POLICY STATEMENT
The organization SHALL enforce mandatory access control (MAC) policies over all covered subjects and objects within information systems to prevent unauthorized information disclosure and privilege escalation. MAC policies MUST uniformly constrain subjects from passing information to unauthorized entities, granting privileges to other subjects, or modifying security attributes and access control rules.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Classified information systems | YES | All systems processing classified data |
| Controlled unclassified systems | YES | Systems with CUI or sensitive data |
| Multi-level secure systems | YES | Systems with users at different clearance levels |
| Standard business systems | CONDITIONAL | Only if processing regulated data |
| All system users | YES | Subjects under MAC policy |
| All data objects | YES | Information resources under MAC policy |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Security Officer | • Define MAC policy for system subjects and objects<br>• Monitor MAC policy enforcement<br>• Validate security attribute assignments |
| System Administrator | • Implement MAC controls in system configuration<br>• Maintain reference monitor functionality<br>• Document trusted subject privileges |
| Data Owner | • Classify information objects<br>• Define security attributes for data<br>• Approve access control policies |

## 4. RULES

[RULE-01] Systems processing classified or controlled information MUST implement mandatory access control policies that uniformly constrain all subjects and objects.
[VALIDATION] IF system_processes_classified = TRUE AND mac_policy_implemented = FALSE THEN critical_violation

[RULE-02] MAC policies MUST prevent subjects from passing information to unauthorized subjects or objects based on security attributes.
[VALIDATION] IF information_passed = TRUE AND recipient_clearance < information_classification THEN critical_violation

[RULE-03] Subjects MUST NOT be able to grant their access privileges to other subjects under MAC policy constraints.
[VALIDATION] IF privilege_delegation_attempted = TRUE AND mac_policy_active = TRUE THEN violation

[RULE-04] Subjects MUST NOT modify security attributes on objects, subjects, or system components unless explicitly authorized as trusted subjects.
[VALIDATION] IF security_attribute_modified = TRUE AND subject_trusted_status = FALSE THEN violation

[RULE-05] Subjects MUST NOT change access control rules governing the MAC policy implementation.
[VALIDATION] IF access_control_rules_modified = TRUE AND subject_admin_privilege = FALSE THEN critical_violation

[RULE-06] Trusted subjects with explicit MAC privileges MUST operate under least privilege principles and be formally documented.
[VALIDATION] IF trusted_subject_documented = FALSE AND mac_privileges_granted = TRUE THEN violation

[RULE-07] MAC policy enforcement MUST be implemented through reference monitor mechanisms that cannot be bypassed.
[VALIDATION] IF reference_monitor_bypass_possible = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] MAC Policy Definition - Establish mandatory access control policies for system subjects and objects
- [PROC-02] Security Attribute Management - Assign and maintain security attributes for all covered entities
- [PROC-03] Trusted Subject Authorization - Document and approve subjects requiring MAC privilege exceptions
- [PROC-04] Reference Monitor Validation - Verify MAC enforcement mechanisms cannot be circumvented

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving privilege escalation, system architecture changes, new classification requirements

## 7. SCENARIO PATTERNS

[SCENARIO-01: Information Passing Violation]
IF subject_clearance = "SECRET"
AND information_classification = "SECRET"
AND recipient_clearance = "CONFIDENTIAL"
AND information_transfer_attempted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Privilege Delegation Attempt]
IF user_role = "standard_user"
AND privilege_delegation_attempted = TRUE
AND mac_policy_active = TRUE
AND trusted_subject_status = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Security Attribute Modification]
IF security_attribute_change = TRUE
AND subject_trusted_status = FALSE
AND change_authorization_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Trusted Subject Operations]
IF subject_trusted_status = TRUE
AND privileges_documented = TRUE
AND least_privilege_applied = TRUE
AND mac_constraints_bypassed = FALSE
THEN compliance = TRUE

[SCENARIO-05: Reference Monitor Bypass]
IF mac_policy_active = TRUE
AND reference_monitor_functional = FALSE
AND policy_bypass_possible = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| MAC policy defined for subjects and objects | RULE-01 |
| Policy uniformly enforced across system | RULE-01, RULE-07 |
| Information passing constraints enforced | RULE-02 |
| Privilege granting constraints enforced | RULE-03 |
| Security attribute modification constraints | RULE-04 |
| Access control rule change constraints | RULE-05 |
| Trusted subject privileges defined and limited | RULE-06 |