# POLICY: AC-6.6: Privileged Access by Non-organizational Users

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-6.6 |
| NIST Control | AC-6.6: Privileged Access by Non-organizational Users |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | privileged access, non-organizational users, contractors, guest access, administrative rights |

## 1. POLICY STATEMENT
The organization SHALL prohibit privileged access to information systems by non-organizational users including external contractors, vendors, consultants, and guest researchers. All privileged access MUST be restricted to employees and individuals with documented equivalent organizational status.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, on-premises, and hybrid environments |
| Non-organizational Users | YES | Contractors, vendors, consultants, guest researchers |
| Organizational Users | CONDITIONAL | Must have documented equivalent status for privileged access |
| Emergency Access | CONDITIONAL | Subject to emergency access procedures |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve privileged access policies<br>• Define organizational user equivalency criteria<br>• Oversee compliance monitoring |
| System Administrators | • Implement technical controls<br>• Monitor privileged account usage<br>• Report violations immediately |
| HR Department | • Maintain organizational user status documentation<br>• Notify IT of status changes<br>• Validate contractor equivalency requests |

## 4. RULES
[RULE-01] Non-organizational users MUST NOT be granted privileged access to any information system.
[VALIDATION] IF user_type = "non-organizational" AND privileged_access = TRUE THEN critical_violation

[RULE-02] Organizational user equivalency status MUST be documented and approved by HR and CISO before granting privileged access.
[VALIDATION] IF privileged_access_requested = TRUE AND organizational_status = "equivalent" AND (hr_approval = FALSE OR ciso_approval = FALSE) THEN violation

[RULE-03] All privileged accounts MUST be reviewed quarterly to verify organizational user status remains valid.
[VALIDATION] IF account_type = "privileged" AND last_review_date > 90_days THEN violation

[RULE-04] Emergency privileged access for non-organizational users MUST be terminated within 8 hours and require CISO approval.
[VALIDATION] IF user_type = "non-organizational" AND access_type = "emergency_privileged" AND duration > 8_hours THEN critical_violation

[RULE-05] Contractors with equivalent organizational status MUST have active contracts and security clearance documentation.
[VALIDATION] IF user_type = "contractor" AND privileged_access = TRUE AND (contract_active = FALSE OR clearance_valid = FALSE) THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Organizational User Status Determination - Process for evaluating and documenting equivalent organizational status
- [PROC-02] Privileged Access Review - Quarterly review of all privileged accounts and user status
- [PROC-03] Emergency Access Authorization - Temporary privileged access for critical business needs
- [PROC-04] Access Revocation - Immediate removal of privileged access upon status change

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, organizational changes, regulatory updates, failed audits

## 7. SCENARIO PATTERNS
[SCENARIO-01: External Contractor Admin Access]
IF user_type = "external_contractor"
AND access_level = "administrative"
AND organizational_equivalent_status = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Vendor Emergency Access]
IF user_type = "vendor"
AND access_type = "emergency_privileged"
AND ciso_approval = TRUE
AND duration <= 8_hours
THEN compliance = TRUE

[SCENARIO-03: Guest Researcher Database Admin]
IF user_type = "guest_researcher"
AND system_access = "database_admin_rights"
AND equivalent_status_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Consultant with Equivalent Status]
IF user_type = "consultant"
AND organizational_equivalent_status = TRUE
AND hr_approval = TRUE
AND ciso_approval = TRUE
AND contract_active = TRUE
THEN compliance = TRUE

[SCENARIO-05: Expired Contractor Privileged Access]
IF user_type = "contractor"
AND privileged_access = TRUE
AND contract_expiration_date < current_date
AND access_revoked = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Privileged access to the system by non-organizational users is prohibited | [RULE-01], [RULE-02], [RULE-05] |
| Emergency access controls and time limits | [RULE-04] |
| Regular review and validation of privileged accounts | [RULE-03] |
| Documentation of organizational equivalent status | [RULE-02], [RULE-05] |