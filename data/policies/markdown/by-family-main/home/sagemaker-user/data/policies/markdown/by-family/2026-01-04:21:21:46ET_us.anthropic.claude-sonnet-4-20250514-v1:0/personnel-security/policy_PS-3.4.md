# POLICY: PS-3.4: Citizenship Requirements

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-3.4 |
| NIST Control | PS-3.4: Citizenship Requirements |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | citizenship, personnel screening, access control, classified information, national security |

## 1. POLICY STATEMENT
The organization SHALL verify that individuals accessing systems processing, storing, or transmitting information requiring citizenship restrictions meet defined citizenship requirements. All personnel accessing such systems MUST undergo citizenship verification as part of the screening process.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal systems | YES | All systems processing classified/controlled information |
| Commercial systems | CONDITIONAL | Only if handling government contracts requiring citizenship |
| Contractors | YES | Subject to same requirements as employees |
| Temporary personnel | YES | No exceptions for duration of access |
| Remote workers | YES | Location does not affect requirements |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Officer | • Define citizenship requirements for each system classification<br>• Maintain approved citizenship verification procedures<br>• Review and approve citizenship exceptions |
| HR Personnel | • Conduct initial citizenship verification<br>• Maintain citizenship documentation<br>• Report citizenship status changes |
| System Owners | • Identify systems requiring citizenship restrictions<br>• Request citizenship verification for system users<br>• Maintain access authorization records |

## 4. RULES
[RULE-01] Systems processing classified or controlled unclassified information (CUI) MUST have defined citizenship requirements documented in the system security plan.
[VALIDATION] IF system_classification IN ["classified", "CUI"] AND citizenship_requirements = "undefined" THEN violation

[RULE-02] Individuals accessing systems with citizenship requirements MUST provide valid proof of citizenship before access is granted.
[VALIDATION] IF system_requires_citizenship = TRUE AND user_citizenship_verified = FALSE AND access_granted = TRUE THEN critical_violation

[RULE-03] Citizenship verification documentation MUST be reviewed and validated within 30 days of personnel onboarding.
[VALIDATION] IF onboard_date + 30_days < current_date AND citizenship_verification_status = "pending" THEN violation

[RULE-04] Non-citizens SHALL NOT be granted access to systems requiring U.S. citizenship unless a documented exception is approved by the authorizing official.
[VALIDATION] IF user_citizenship != "US" AND system_requires_us_citizenship = TRUE AND exception_approved = FALSE THEN critical_violation

[RULE-05] Citizenship status changes MUST be reported to security personnel within 5 business days of occurrence.
[VALIDATION] IF citizenship_status_changed = TRUE AND notification_delay > 5_business_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Citizenship Verification Process - Standard procedures for validating and documenting citizenship status
- [PROC-02] Exception Request Process - Process for requesting and approving citizenship requirement exceptions
- [PROC-03] Periodic Citizenship Review - Annual review of citizenship requirements and user status
- [PROC-04] Access Revocation Process - Immediate access removal upon citizenship status changes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Changes in classification requirements, security incidents, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Contractor Access to Classified System]
IF user_type = "contractor"
AND system_classification = "classified"
AND citizenship_verified = FALSE
AND access_requested = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Dual Citizen Access]
IF user_citizenship = "dual"
AND system_requires_us_citizenship = TRUE
AND primary_citizenship = "US"
AND security_clearance = "active"
THEN compliance = TRUE

[SCENARIO-03: Naturalized Citizen Documentation]
IF user_citizenship_type = "naturalized"
AND naturalization_certificate_verified = TRUE
AND system_requires_us_citizenship = TRUE
THEN compliance = TRUE

[SCENARIO-04: Emergency Access Without Verification]
IF access_type = "emergency"
AND citizenship_verified = FALSE
AND emergency_duration > 72_hours
AND temporary_exception = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Foreign National with Exception]
IF user_citizenship != "US"
AND system_requires_us_citizenship = TRUE
AND exception_approved = TRUE
AND exception_expiry_date > current_date
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Citizenship requirements are defined for applicable systems | [RULE-01] |
| Individuals meet citizenship requirements before access | [RULE-02] |
| Citizenship verification is completed timely | [RULE-03] |
| Non-citizens are properly restricted or excepted | [RULE-04] |
| Citizenship status changes are reported | [RULE-05] |