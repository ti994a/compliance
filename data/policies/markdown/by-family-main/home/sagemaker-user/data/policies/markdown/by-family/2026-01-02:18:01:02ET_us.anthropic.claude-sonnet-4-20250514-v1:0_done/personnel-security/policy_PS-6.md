# POLICY: PS-6: Access Agreements

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-6 |
| NIST Control | PS-6: Access Agreements |
| Version | 1.0 |
| Owner | Chief Human Resources Officer |
| Keywords | access agreements, nondisclosure, acceptable use, rules of behavior, conflict of interest, electronic signatures |

## 1. POLICY STATEMENT
All individuals requiring access to organizational information systems must sign appropriate access agreements prior to being granted access and re-sign when agreements are updated. Access agreements include nondisclosure agreements, acceptable use agreements, rules of behavior, and conflict-of-interest agreements that must be reviewed and updated annually.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Employees | YES | All full-time and part-time employees |
| Contractors | YES | Including temporary and consulting staff |
| Third-party users | YES | Vendors, partners with system access |
| Organizational systems | YES | All information systems and applications |
| Guest/visitor access | CONDITIONAL | Only if accessing organizational systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CHRO/HR Director | • Develop and maintain access agreement templates<br>• Ensure compliance with legal requirements<br>• Track signature compliance |
| System Administrators | • Verify signed agreements before provisioning access<br>• Maintain access logs tied to agreements<br>• Suspend access for unsigned agreements |
| Legal Counsel | • Review agreement content for legal compliance<br>• Approve updates to agreement language<br>• Advise on electronic signature policies |

## 4. RULES
[RULE-01] All individuals MUST sign appropriate access agreements before being granted access to any organizational system.
[VALIDATION] IF system_access_granted = TRUE AND signed_agreement = FALSE THEN critical_violation

[RULE-02] Access agreements MUST be reviewed and updated annually or when significant changes occur to systems or policies.
[VALIDATION] IF agreement_last_updated > 365_days THEN violation

[RULE-03] Individuals MUST re-sign access agreements within 30 days when agreements have been updated.
[VALIDATION] IF agreement_updated = TRUE AND days_since_update > 30 AND re_signed = FALSE THEN violation

[RULE-04] Electronic signatures MAY be used for access agreements unless specifically prohibited by organizational policy.
[VALIDATION] IF electronic_signature_used = TRUE AND policy_prohibits_electronic = TRUE THEN violation

[RULE-05] Access agreements MUST include nondisclosure, acceptable use, rules of behavior, and conflict-of-interest provisions.
[VALIDATION] IF agreement_missing_required_sections > 0 THEN violation

[RULE-06] System access MUST be immediately suspended for individuals who fail to sign required agreements within the specified timeframe.
[VALIDATION] IF signature_overdue = TRUE AND access_suspended = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Access Agreement Development - Process for creating and updating agreement templates
- [PROC-02] Signature Tracking - System for monitoring signature status and compliance
- [PROC-03] Access Provisioning Verification - Validation of signed agreements before access grants
- [PROC-04] Agreement Update Notification - Process for notifying users of updated agreements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Significant system changes, legal requirement updates, security incidents involving access misuse

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Employee Access]
IF user_type = "new_employee"
AND system_access_requested = TRUE
AND signed_agreement = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Updated Agreement Re-signing]
IF agreement_version = "updated"
AND days_since_update = 45
AND user_resigned = FALSE
AND access_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Contractor Electronic Signature]
IF user_type = "contractor"
AND signature_type = "electronic"
AND policy_allows_electronic = TRUE
AND agreement_complete = TRUE
THEN compliance = TRUE

[SCENARIO-04: Expired Agreement Review]
IF agreement_last_reviewed > 400_days
AND agreement_status = "active"
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Missing Agreement Components]
IF nondisclosure_clause = FALSE
OR acceptable_use_clause = FALSE
OR rules_of_behavior_clause = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Access agreements are developed and documented | [RULE-05] |
| Access agreements are reviewed and updated annually | [RULE-02] |
| Individuals sign agreements prior to access | [RULE-01] |
| Individuals re-sign when agreements are updated | [RULE-03] |