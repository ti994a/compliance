```markdown
# POLICY: PS-6: Access Agreements

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-6 |
| NIST Control | PS-6: Access Agreements |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | access agreements, nondisclosure, acceptable use, rules of behavior, conflict of interest, personnel security |

## 1. POLICY STATEMENT
All individuals requiring access to organizational information systems must sign appropriate access agreements prior to being granted access. Access agreements must be regularly reviewed, updated, and re-signed to maintain current authorization and acknowledgment of security responsibilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Employees | YES | All full-time and part-time employees |
| Contractors | YES | All external contractors and consultants |
| Vendors | YES | Third-party personnel requiring system access |
| Temporary Staff | YES | Includes interns and seasonal workers |
| Guests | YES | Any individual granted temporary system access |
| Privileged Users | YES | Enhanced agreements required for elevated access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve access agreement templates<br>• Define review frequencies<br>• Oversee compliance monitoring |
| HR Manager | • Coordinate agreement signing during onboarding<br>• Track agreement status and renewals<br>• Maintain signed agreement records |
| System Owners | • Identify system-specific agreement requirements<br>• Validate access alignment with agreements<br>• Report agreement violations |
| Legal Counsel | • Review agreement language for enforceability<br>• Update agreements for regulatory changes<br>• Support violation enforcement actions |

## 4. RULES

[RULE-01] All individuals MUST sign appropriate access agreements before being granted any access to organizational information systems.
[VALIDATION] IF user_access_granted = TRUE AND access_agreement_signed = FALSE THEN critical_violation

[RULE-02] Access agreements MUST be reviewed and updated annually or when significant system changes occur.
[VALIDATION] IF agreement_last_review > 365_days OR system_major_change = TRUE AND agreement_updated = FALSE THEN violation

[RULE-03] Individuals MUST re-sign access agreements within 30 days when agreements are updated or every 2 years for continuous access.
[VALIDATION] IF agreement_updated = TRUE AND days_since_update > 30 AND user_resigned = FALSE THEN violation
[VALIDATION] IF agreement_age > 730_days AND user_resigned = FALSE THEN violation

[RULE-04] Access agreements MUST include nondisclosure, acceptable use, rules of behavior, and conflict-of-interest components.
[VALIDATION] IF agreement_type NOT IN ["nda", "aup", "rob", "coi"] THEN incomplete_agreement

[RULE-05] Electronic signatures MAY be used for access agreements unless specifically prohibited by organizational policy.
[VALIDATION] IF signature_type = "electronic" AND electronic_signatures_prohibited = TRUE THEN policy_violation

[RULE-06] Access MUST be revoked immediately for individuals who refuse to sign required access agreements.
[VALIDATION] IF agreement_signature_refused = TRUE AND access_active = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Access Agreement Development - Standardized process for creating and updating agreement templates
- [PROC-02] Agreement Signing Workflow - Systematic process for obtaining signatures during onboarding and renewals
- [PROC-03] Agreement Review Process - Regular assessment of agreement adequacy and currency
- [PROC-04] Compliance Monitoring - Ongoing verification of agreement status and access alignment
- [PROC-05] Violation Response - Actions for non-compliance with agreement requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system changes, regulatory updates, security incidents involving agreement violations, organizational restructuring

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Employee Onboarding]
IF user_type = "new_employee"
AND onboarding_date = current_date
AND access_agreement_signed = FALSE
AND system_access_requested = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Contractor Agreement Expiration]
IF user_type = "contractor"
AND agreement_expiration_date < current_date
AND active_system_access = TRUE
AND renewal_in_progress = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Updated Agreement Re-signing]
IF agreement_updated = TRUE
AND update_date < (current_date - 25_days)
AND user_resigned = TRUE
AND access_maintained = TRUE
THEN compliance = TRUE

[SCENARIO-04: Privileged User Enhanced Requirements]
IF user_privilege_level = "administrative"
AND standard_agreement_only = TRUE
AND enhanced_agreement_required = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Electronic Signature Usage]
IF signature_method = "electronic"
AND electronic_signatures_approved = TRUE
AND signature_authentication_verified = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Access agreements developed and documented | [RULE-04] |
| Access agreements reviewed and updated per defined frequency | [RULE-02] |
| Individuals sign agreements prior to access | [RULE-01] |
| Individuals re-sign agreements when updated or per schedule | [RULE-03] |
| Access revocation for non-compliance | [RULE-06] |
| Electronic signature authorization | [RULE-05] |
```