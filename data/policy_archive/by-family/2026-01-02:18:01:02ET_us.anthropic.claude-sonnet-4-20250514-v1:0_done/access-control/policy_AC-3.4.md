# POLICY: AC-3.4: Discretionary Access Control

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-3.4 |
| NIST Control | AC-3.4: Discretionary Access Control |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | discretionary access control, privilege delegation, information sharing, security attributes, access enforcement |

## 1. POLICY STATEMENT
The organization SHALL enforce discretionary access control policies that allow authorized subjects to share information, delegate privileges, and modify security attributes within defined boundaries. Subjects with granted access MAY exercise discretionary control over information sharing and access management according to organizational policy constraints.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing organizational data |
| Cloud Services | YES | Hybrid cloud infrastructure components |
| Applications | YES | Custom and commercial applications |
| Databases | YES | All database systems and repositories |
| Network Resources | CONDITIONAL | Where discretionary controls are applicable |
| External Systems | NO | Outside organizational control boundary |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owners | • Define discretionary access control policies for their data<br>• Approve privilege delegation rules<br>• Monitor information sharing activities |
| System Administrators | • Implement discretionary access control mechanisms<br>• Configure security attribute management<br>• Maintain audit logs of discretionary actions |
| Security Officers | • Review discretionary access policies<br>• Monitor policy compliance<br>• Investigate unauthorized privilege delegations |

## 4. RULES
[RULE-01] Organizations MUST define and document discretionary access control policies specifying covered subjects and objects.
[VALIDATION] IF discretionary_policy_documented = FALSE THEN violation

[RULE-02] Systems MUST enforce discretionary access control policies over all specified subjects and objects.
[VALIDATION] IF system_enforces_dac = FALSE AND subject_in_scope = TRUE THEN violation

[RULE-03] Subjects MAY pass information to other subjects or objects only when explicitly permitted by the discretionary access control policy.
[VALIDATION] IF information_passed = TRUE AND policy_permits_sharing = FALSE THEN violation

[RULE-04] Privilege delegation MUST be restricted to authorized subjects and documented according to organizational policy.
[VALIDATION] IF privilege_delegated = TRUE AND delegation_authorized = FALSE THEN violation

[RULE-05] Security attribute modifications MUST be limited to subjects with appropriate permissions and logged for audit purposes.
[VALIDATION] IF security_attributes_modified = TRUE AND modifier_authorized = FALSE THEN critical_violation

[RULE-06] Newly created objects MUST have security attributes assigned according to organizational discretionary access control policy.
[VALIDATION] IF new_object_created = TRUE AND security_attributes_assigned = FALSE THEN violation

[RULE-07] Changes to access control rules MUST be authorized by data owners and documented with justification.
[VALIDATION] IF access_rules_changed = TRUE AND owner_approval = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Discretionary Access Control Policy Development - Define and document DAC policies for each system
- [PROC-02] Privilege Delegation Management - Establish processes for authorized privilege sharing
- [PROC-03] Security Attribute Assignment - Procedures for setting and modifying object security attributes
- [PROC-04] Information Sharing Authorization - Process for approving discretionary information sharing
- [PROC-05] Access Control Rule Management - Procedures for modifying access control rules

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving unauthorized sharing, system changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Authorized Information Sharing]
IF user_has_access = TRUE
AND sharing_policy_permits = TRUE
AND recipient_clearance_adequate = TRUE
THEN compliance = TRUE

[SCENARIO-02: Unauthorized Privilege Delegation]
IF user_delegates_privileges = TRUE
AND delegation_policy_exists = FALSE
AND audit_log_created = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Security Attribute Modification]
IF user_modifies_attributes = TRUE
AND user_authorized_for_modification = TRUE
AND modification_logged = TRUE
THEN compliance = TRUE

[SCENARIO-04: Unauthorized Access Rule Changes]
IF access_rules_modified = TRUE
AND data_owner_approval = FALSE
AND change_documentation = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: New Object Creation Without Attributes]
IF new_object_created = TRUE
AND security_attributes_assigned = FALSE
AND creation_time > 24_hours
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Discretionary access control policy defined for subjects | RULE-01, RULE-02 |
| Discretionary access control policy defined for objects | RULE-01, RULE-02 |
| Information passing controls enforced | RULE-03 |
| Privilege delegation controls enforced | RULE-04 |
| Security attribute modification controls enforced | RULE-05 |
| New object security attribute assignment enforced | RULE-06 |
| Access control rule change controls enforced | RULE-07 |