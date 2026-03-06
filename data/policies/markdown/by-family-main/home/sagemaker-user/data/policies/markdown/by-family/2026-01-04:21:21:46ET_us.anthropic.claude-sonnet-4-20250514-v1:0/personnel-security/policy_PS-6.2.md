# POLICY: PS-6.2: Classified Information Requiring Special Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-6.2 |
| NIST Control | PS-6.2: Classified Information Requiring Special Protection |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | classified information, special protection, access authorization, personnel security, nondisclosure agreement, SAP, SCI, collateral |

## 1. POLICY STATEMENT
Access to classified information requiring special protection (collateral, SAP, SCI) SHALL only be granted to individuals who have valid access authorization demonstrated by official government duties, satisfy personnel security criteria, and have executed required nondisclosure agreements. All access decisions MUST be documented and regularly validated.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Government employees | YES | All clearance levels |
| Contractors | YES | When handling classified information |
| Temporary staff | YES | If requiring classified access |
| Visitors | CONDITIONAL | Only with escort and limited access |
| Remote workers | YES | Same requirements apply |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Officer | • Verify access authorizations<br>• Validate personnel security criteria<br>• Maintain nondisclosure agreement records |
| Personnel Security Manager | • Conduct background investigations<br>• Monitor clearance status<br>• Process access requests |
| Facility Security Officer | • Implement access controls<br>• Monitor classified information handling<br>• Report security violations |

## 4. RULES
[RULE-01] Access to classified information requiring special protection MUST only be granted to individuals with valid access authorization demonstrated by assigned official government duties.
[VALIDATION] IF access_requested = TRUE AND valid_authorization = FALSE THEN violation

[RULE-02] Personnel MUST satisfy all applicable personnel security criteria including background investigations, clearance adjudication, and periodic reinvestigation requirements.
[VALIDATION] IF clearance_status != "current" AND classified_access = TRUE THEN critical_violation

[RULE-03] Individuals MUST read, understand, and sign appropriate nondisclosure agreements before accessing classified information requiring special protection.
[VALIDATION] IF nda_signed = FALSE AND classified_access_granted = TRUE THEN violation

[RULE-04] Access authorizations MUST be validated every 90 days for active users with special protection access.
[VALIDATION] IF last_validation > 90_days AND special_access = TRUE THEN violation

[RULE-05] Revocation of access MUST occur within 24 hours when personnel security criteria are no longer met or official duties no longer require access.
[VALIDATION] IF criteria_unmet = TRUE AND revocation_time > 24_hours THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Access Authorization Verification - Validate government duties and need-to-know
- [PROC-02] Personnel Security Screening - Conduct required background investigations
- [PROC-03] Nondisclosure Agreement Management - Execute and maintain NDA records
- [PROC-04] Periodic Access Review - Quarterly validation of access requirements
- [PROC-05] Access Revocation - Immediate removal when criteria not met

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, clearance changes, organizational restructure, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Contractor Special Access]
IF user_type = "contractor"
AND clearance_level = "TS/SCI"
AND nda_signed = TRUE
AND government_sponsor = TRUE
THEN compliance = TRUE

[SCENARIO-02: Expired Clearance Access]
IF clearance_status = "expired"
AND special_access_active = TRUE
AND grace_period > 0_days
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Missing Nondisclosure Agreement]
IF classified_access = "SAP"
AND nda_executed = FALSE
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Unauthorized Duty Assignment]
IF official_duties = "unclassified_role"
AND special_access_requested = TRUE
AND justification_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Overdue Access Review]
IF last_access_review > 90_days
AND special_protection_access = TRUE
AND user_status = "active"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Valid access authorization demonstrated by official duties | [RULE-01] |
| Personnel security criteria satisfaction | [RULE-02] |
| Nondisclosure agreement execution | [RULE-03] |
| Periodic validation of access requirements | [RULE-04] |
| Timely revocation when criteria unmet | [RULE-05] |