# POLICY: AC-6.10: Prohibit Non-privileged Users from Executing Privileged Functions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-6.10 |
| NIST Control | AC-6.10: Prohibit Non-privileged Users from Executing Privileged Functions |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | privileged functions, non-privileged users, access control, least privilege, security controls |

## 1. POLICY STATEMENT
Non-privileged users SHALL be prevented from executing privileged functions that could compromise system security, privacy controls, or administrative operations. All privileged functions MUST be restricted to authorized users with appropriate privileges and documented justification.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid environments |
| All user accounts | YES | Both human and service accounts |
| Privileged functions | YES | Security controls, system administration, cryptographic operations |
| Third-party applications | YES | Must enforce privilege restrictions |
| Mobile devices | YES | When accessing corporate systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure systems to enforce privilege restrictions<br>• Monitor privileged function usage<br>• Maintain separation of privileged and non-privileged accounts |
| Security Team | • Define privileged functions<br>• Review privilege escalation attempts<br>• Validate access control implementations |
| Identity Management Team | • Implement technical controls preventing privilege escalation<br>• Maintain user privilege assignments<br>• Monitor for unauthorized privilege usage |

## 4. RULES
[RULE-01] Non-privileged users MUST NOT be able to disable, circumvent, or alter security controls, intrusion detection systems, or malicious code protection mechanisms.
[VALIDATION] IF user_privilege_level = "non-privileged" AND attempted_action IN ["disable_security_control", "bypass_ids", "alter_antimalware"] THEN critical_violation

[RULE-02] System account creation and modification SHALL be restricted to users with documented administrative privileges.
[VALIDATION] IF user_privilege_level = "non-privileged" AND action = "create_system_account" THEN violation

[RULE-03] Cryptographic key management activities MUST be restricted to users with specific cryptographic administration privileges.
[VALIDATION] IF user_role NOT IN ["crypto_admin", "key_manager"] AND action CONTAINS "key_management" THEN violation

[RULE-04] System integrity checks and security auditing functions SHALL NOT be executable by non-privileged users.
[VALIDATION] IF user_privilege_level = "non-privileged" AND action IN ["integrity_check", "audit_modification", "log_deletion"] THEN violation

[RULE-05] All attempts by non-privileged users to execute privileged functions MUST be logged and monitored in real-time.
[VALIDATION] IF privilege_escalation_attempt = TRUE AND alert_generated = FALSE THEN violation

[RULE-06] Technical controls MUST prevent privilege escalation through application vulnerabilities or misconfigurations.
[VALIDATION] IF privilege_escalation_successful = TRUE AND user_authorized_privilege = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Privileged Function Inventory - Maintain current list of all privileged functions and authorized users
- [PROC-02] Privilege Escalation Monitoring - Real-time detection and response to unauthorized privilege attempts
- [PROC-03] Access Control Validation - Regular testing of privilege restriction mechanisms
- [PROC-04] Incident Response - Process for responding to successful privilege escalation events

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving privilege escalation, system architecture changes, new privileged functions identified

## 7. SCENARIO PATTERNS
[SCENARIO-01: Developer Attempting Security Control Modification]
IF user_role = "developer"
AND attempted_action = "disable_firewall_rule"
AND user_privilege_level = "non-privileged"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Standard User Creating System Account]
IF user_type = "standard_user"
AND action = "create_service_account"
AND administrative_privilege = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Application Service Account Privilege Escalation]
IF account_type = "service_account"
AND privilege_level = "non-privileged"
AND successful_privilege_escalation = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Contractor Accessing Cryptographic Functions]
IF user_type = "contractor"
AND attempted_function = "certificate_generation"
AND crypto_admin_role = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Authorized Admin with Proper Privileges]
IF user_role = "system_administrator"
AND action = "modify_security_policy"
AND privilege_level = "administrative"
AND authorization_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Non-privileged users prevented from executing privileged functions | [RULE-01], [RULE-02], [RULE-03], [RULE-04] |
| Technical enforcement of privilege restrictions | [RULE-06] |
| Monitoring and detection of privilege escalation attempts | [RULE-05] |
| Protection of security controls from circumvention | [RULE-01] |
| Restriction of administrative functions | [RULE-02], [RULE-04] |