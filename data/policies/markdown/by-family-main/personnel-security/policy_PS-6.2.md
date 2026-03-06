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
Access to classified information requiring special protection (collateral information, Special Access Program information, and Sensitive Compartmented Information) SHALL be granted only to individuals who meet strict authorization, security, and agreement requirements. All access decisions must be verified through established personnel security processes and documented appropriately.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal employees | YES | All levels accessing classified information |
| Contractors | YES | When requiring classified access |
| Temporary personnel | YES | Subject to same requirements |
| Visitors | CONDITIONAL | Only with escort and temporary authorization |
| Cloud systems | YES | Systems processing classified information |
| Mobile devices | YES | When accessing classified information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Control Assessor | • Verify access authorization validity<br>• Validate personnel security criteria compliance<br>• Audit nondisclosure agreement execution |
| Personnel Security Officer | • Evaluate personnel security criteria<br>• Maintain access authorization records<br>• Process security clearance requirements |
| Information System Security Manager | • Implement technical access controls<br>• Monitor classified information access<br>• Coordinate with personnel security team |

## 4. RULES
[RULE-01] Access to classified information requiring special protection MUST be granted only to individuals with valid access authorization demonstrated by assigned official government duties.
[VALIDATION] IF access_requested = TRUE AND (valid_authorization = FALSE OR official_duties = FALSE) THEN access_denied

[RULE-02] Personnel security criteria MUST be satisfied and verified before granting access to classified information requiring special protection.
[VALIDATION] IF personnel_security_check = "incomplete" OR security_criteria_met = FALSE THEN access_denied

[RULE-03] Individuals MUST read, understand, and sign a nondisclosure agreement before accessing classified information requiring special protection.
[VALIDATION] IF nda_signed = FALSE OR nda_date = NULL OR understanding_verified = FALSE THEN access_denied

[RULE-04] Access authorizations MUST be revalidated annually and when official duties change significantly.
[VALIDATION] IF last_validation_date > 365_days OR duties_changed = TRUE AND revalidation_complete = FALSE THEN access_suspended

[RULE-05] All access grants to classified information requiring special protection MUST be documented and maintained in official personnel security records.
[VALIDATION] IF access_granted = TRUE AND documentation_complete = FALSE THEN compliance_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Access Authorization Verification - Validate government duties and clearance levels
- [PROC-02] Personnel Security Criteria Assessment - Evaluate background investigations and security requirements  
- [PROC-03] Nondisclosure Agreement Processing - Execute and maintain signed agreements
- [PROC-04] Access Documentation Management - Maintain comprehensive access records
- [PROC-05] Periodic Revalidation Process - Annual review of access requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, personnel changes, classification changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Contractor Access Request]
IF user_type = "contractor"
AND classified_access_requested = TRUE
AND security_clearance = "valid"
AND nda_signed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Employee Duty Change]
IF employee_duties_changed = TRUE
AND classified_access_active = TRUE
AND revalidation_completed = FALSE
AND change_date > 30_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Expired Authorization]
IF access_authorization_date < current_date - 365_days
AND classified_access_active = TRUE
AND revalidation_pending = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Complete Compliance Check]
IF valid_authorization = TRUE
AND official_duties_verified = TRUE
AND personnel_security_met = TRUE
AND nda_signed = TRUE
AND documentation_complete = TRUE
THEN compliance = TRUE

[SCENARIO-05: Temporary Access Request]
IF access_type = "temporary"
AND classified_level = "special_protection"
AND escort_assigned = FALSE
AND temporary_authorization = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Valid access authorization demonstrated by official government duties | [RULE-01] |
| Personnel security criteria satisfaction | [RULE-02] |
| Nondisclosure agreement execution | [RULE-03] |
| Access authorization maintenance | [RULE-04] |
| Access documentation requirements | [RULE-05] |