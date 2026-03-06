# POLICY: AC-14: Permitted Actions Without Identification or Authentication

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-14 |
| NIST Control | AC-14: Permitted Actions Without Identification or Authentication |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | unauthenticated access, public access, identification bypass, authentication waiver, anonymous actions |

## 1. POLICY STATEMENT
The organization SHALL identify, document, and provide rationale for all user actions that can be performed on systems without identification or authentication. All unauthenticated access MUST align with organizational mission and business functions and be explicitly approved through the security planning process.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid |
| Public-facing websites | YES | Special consideration for public access |
| Internal applications | YES | Must justify any unauthenticated features |
| Mobile applications | YES | Including publicly accessible functions |
| Third-party systems | CONDITIONAL | When organization controls access policies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owners | • Define unauthenticated actions for their systems<br>• Document business justification<br>• Maintain security plan documentation |
| Security Team | • Review and approve unauthenticated access requests<br>• Validate alignment with security requirements<br>• Monitor compliance through assessments |
| System Administrators | • Implement approved unauthenticated access controls<br>• Configure systems according to documented permissions<br>• Report unauthorized unauthenticated access |

## 4. RULES
[RULE-01] All user actions that can be performed without identification or authentication MUST be explicitly defined and documented in the system security plan.
[VALIDATION] IF system_allows_unauthenticated_actions = TRUE AND documented_in_security_plan = FALSE THEN violation

[RULE-02] Each unauthenticated action MUST have documented business justification that aligns with organizational mission and business functions.
[VALIDATION] IF unauthenticated_action_exists = TRUE AND business_justification = NULL THEN violation

[RULE-03] Systems MUST NOT permit unauthenticated actions beyond those explicitly documented and approved in the security plan.
[VALIDATION] IF actual_unauthenticated_actions > documented_unauthenticated_actions THEN critical_violation

[RULE-04] Physical bypass mechanisms for authentication MUST be protected from accidental or unmonitored use and documented in security procedures.
[VALIDATION] IF physical_bypass_exists = TRUE AND (protection_controls = FALSE OR documentation = FALSE) THEN violation

[RULE-05] Organizations MAY determine that no user actions can be performed without identification and authentication, in which case the value SHALL be documented as "none."
[VALIDATION] IF unauthenticated_actions = "none" AND actual_unauthenticated_access = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Unauthenticated Access Assessment - Annual review of all systems for unauthenticated functionality
- [PROC-02] Security Plan Documentation - Process for documenting and updating unauthenticated actions
- [PROC-03] Business Justification Review - Validation that unauthenticated access supports mission requirements
- [PROC-04] Physical Bypass Control - Management of hardware-based authentication bypass mechanisms

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: New system deployment, system modifications affecting access controls, security incidents involving unauthenticated access

## 7. SCENARIO PATTERNS
[SCENARIO-01: Public Website Access]
IF system_type = "public_website"
AND unauthenticated_actions = "browse_public_content"
AND documented_in_security_plan = TRUE
AND business_justification = "public_information_sharing"
THEN compliance = TRUE

[SCENARIO-02: Undocumented Anonymous Access]
IF system_allows_unauthenticated_actions = TRUE
AND documented_in_security_plan = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Physical Bypass Without Protection]
IF physical_authentication_bypass = TRUE
AND physical_protection_controls = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Excessive Unauthenticated Functionality]
IF system_type = "internal_application"
AND unauthenticated_actions = "data_modification"
AND business_justification = "convenience"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Properly Documented No Access Policy]
IF unauthenticated_actions_policy = "none"
AND documented_in_security_plan = TRUE
AND actual_unauthenticated_access = FALSE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| User actions without authentication are defined | RULE-01 |
| Actions consistent with mission/business functions | RULE-02 |
| Actions documented in security plan | RULE-01, RULE-02 |
| Supporting rationale provided in security plan | RULE-02 |