# POLICY: IA-12.1: Supervisor Authorization

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-12.1 |
| NIST Control | IA-12.1: Supervisor Authorization |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | supervisor authorization, account registration, logical access, sponsor approval, identity proofing |

## 1. POLICY STATEMENT
All requests for logical access accounts must include explicit supervisor or sponsor authorization as part of the registration process. This authorization ensures management awareness and validates that requested privileges align with organizational roles and responsibilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Includes full-time, part-time, temporary |
| Contractors | YES | Requires sponsor authorization |
| Vendors | YES | Requires business sponsor approval |
| Service accounts | YES | Requires system owner authorization |
| Emergency accounts | CONDITIONAL | May use expedited approval process |
| Guest accounts | YES | Requires host employee authorization |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supervisors/Sponsors | • Validate business justification for access requests<br>• Verify employee role and responsibilities<br>• Approve appropriate privilege levels<br>• Maintain accountability for authorized access |
| Identity Management Team | • Verify supervisor authorization before provisioning<br>• Document authorization in access management system<br>• Escalate requests lacking proper authorization<br>• Maintain audit trail of authorization decisions |
| System Administrators | • Validate authorization requirements before account creation<br>• Ensure proper documentation exists<br>• Report unauthorized account creation attempts |

## 4. RULES
[RULE-01] All logical access account registration requests MUST include documented supervisor or sponsor authorization before account provisioning.
[VALIDATION] IF account_request_submitted = TRUE AND supervisor_authorization = NULL THEN violation

[RULE-02] Supervisor authorization MUST be obtained from the requestor's direct supervisor or an authorized sponsor with appropriate organizational authority.
[VALIDATION] IF authorizer_role NOT IN ["direct_supervisor", "authorized_sponsor"] THEN violation

[RULE-03] Authorization documentation MUST include supervisor identity, approval date, business justification, and requested privilege level.
[VALIDATION] IF authorization_missing_required_fields = TRUE THEN violation

[RULE-04] Account provisioning MUST NOT proceed without valid supervisor authorization except for pre-approved emergency procedures.
[VALIDATION] IF account_created = TRUE AND authorization_verified = FALSE AND emergency_exception = FALSE THEN critical_violation

[RULE-05] Emergency account creation without prior authorization MUST receive retroactive supervisor approval within 24 hours.
[VALIDATION] IF emergency_account = TRUE AND retroactive_approval_time > 24_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Account Request Authorization - Process for obtaining and documenting supervisor approval
- [PROC-02] Authorization Verification - Validation of supervisor identity and authority
- [PROC-03] Emergency Account Approval - Expedited process for time-sensitive access needs
- [PROC-04] Authorization Audit Trail - Documentation and retention of approval records

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Organizational restructure, security incidents involving unauthorized access, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Standard Employee Account Request]
IF user_type = "employee"
AND supervisor_authorization = "documented"
AND business_justification = "provided"
THEN compliance = TRUE

[SCENARIO-02: Contractor Without Sponsor Approval]
IF user_type = "contractor"
AND sponsor_authorization = NULL
AND account_provisioned = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Emergency Account with Delayed Approval]
IF account_type = "emergency"
AND creation_time = "immediate"
AND retroactive_approval_time > 24_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Service Account Without System Owner Authorization]
IF account_type = "service"
AND system_owner_approval = FALSE
AND account_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Self-Authorized Account Request]
IF requestor_id = authorizer_id
AND account_type != "emergency"
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Registration process includes supervisor authorization | RULE-01, RULE-02 |
| Proper documentation of authorization | RULE-03 |
| No unauthorized account provisioning | RULE-04 |
| Emergency account oversight | RULE-05 |