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
All individuals requiring access to organizational information systems must sign appropriate access agreements prior to being granted access and re-sign when agreements are updated. Access agreements must be regularly reviewed and updated to ensure continued relevance and compliance with organizational requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Employees | YES | All full-time, part-time, temporary |
| Contractors | YES | Including subcontractors |
| Vendors | YES | With system access requirements |
| Third-party users | YES | External users requiring access |
| Organizational systems | YES | All systems containing organizational data |
| Cloud services | YES | Hybrid cloud infrastructure |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Human Resources Officer | • Oversee access agreement program<br>• Approve agreement templates<br>• Ensure compliance with employment law |
| Information Security Officer | • Define security requirements in agreements<br>• Review and approve security-related clauses<br>• Monitor compliance with security provisions |
| System Owners | • Identify access agreement requirements for systems<br>• Verify agreements before granting access<br>• Maintain access agreement records |
| Legal Counsel | • Review agreement language for legal compliance<br>• Approve conflict-of-interest provisions<br>• Ensure regulatory alignment |

## 4. RULES

[RULE-01] Organizations MUST develop and document access agreements for all organizational systems containing sensitive data or supporting critical business functions.
[VALIDATION] IF system_classification IN ["sensitive", "critical"] AND access_agreement_exists = FALSE THEN violation

[RULE-02] Access agreements MUST be reviewed and updated annually or when significant organizational changes occur.
[VALIDATION] IF last_review_date > 365_days OR organizational_change = TRUE AND agreement_updated = FALSE THEN violation

[RULE-03] Individuals MUST sign appropriate access agreements prior to being granted any system access.
[VALIDATION] IF access_granted = TRUE AND agreement_signed = FALSE THEN critical_violation

[RULE-04] Individuals MUST re-sign access agreements within 30 days when agreements are updated or every 3 years to maintain access.
[VALIDATION] IF agreement_updated = TRUE AND days_since_update > 30 AND resigned = FALSE THEN violation
[VALIDATION] IF last_signature_date > 1095_days AND resigned = FALSE THEN violation

[RULE-05] Access agreements MUST include nondisclosure, acceptable use, rules of behavior, and conflict-of-interest provisions as applicable to the individual's role.
[VALIDATION] IF agreement_type = "comprehensive" AND (nda_clause = FALSE OR aup_clause = FALSE OR rob_clause = FALSE) THEN violation

[RULE-06] Electronic signatures MAY be used for access agreements unless specifically prohibited by organizational policy.
[VALIDATION] IF electronic_signature_used = TRUE AND policy_prohibition = TRUE THEN violation

[RULE-07] Organizations MUST maintain records of all signed access agreements and re-signing activities for audit purposes.
[VALIDATION] IF agreement_signed = TRUE AND record_maintained = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Access Agreement Development - Create and maintain standardized agreement templates
- [PROC-02] Agreement Review Process - Annual review and update of agreement content
- [PROC-03] Signature Management - Process for obtaining and tracking signatures
- [PROC-04] Access Verification - Verify agreement compliance before granting access
- [PROC-05] Record Retention - Maintain agreement records per retention schedule

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Regulatory changes, significant security incidents, organizational restructuring, legal requirement changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Employee Access]
IF user_type = "new_employee"
AND access_request = TRUE
AND access_agreement_signed = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Contractor System Access]
IF user_type = "contractor"
AND system_access_required = TRUE
AND nda_signed = TRUE
AND acceptable_use_signed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Agreement Update Compliance]
IF agreement_last_updated < 400_days_ago
AND user_access_active = TRUE
AND user_resigned_updated_agreement = TRUE
THEN compliance = TRUE

[SCENARIO-04: Expired Agreement Access]
IF last_agreement_signature > 3_years_ago
AND access_active = TRUE
AND re_signature_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Electronic Signature Usage]
IF electronic_signature_used = TRUE
AND organizational_policy_allows_electronic = TRUE
AND signature_authentication_verified = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Access agreements developed and documented | [RULE-01] |
| Access agreements reviewed and updated per defined frequency | [RULE-02] |
| Individuals sign agreements prior to access | [RULE-03] |
| Individuals re-sign agreements when updated or per schedule | [RULE-04] |
| Agreements include required provisions | [RULE-05] |
| Electronic signature compliance | [RULE-06] |
| Agreement record maintenance | [RULE-07] |