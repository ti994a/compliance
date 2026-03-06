# POLICY: PS-3.4: Citizenship Requirements

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-3.4 |
| NIST Control | PS-3.4: Citizenship Requirements |
| Version | 1.0 |
| Owner | Chief Human Resources Officer |
| Keywords | citizenship, personnel screening, access control, classified information, sensitive data |

## 1. POLICY STATEMENT
The organization SHALL verify that individuals accessing systems processing, storing, or transmitting information requiring citizenship restrictions meet defined citizenship requirements. All personnel accessing systems with citizenship-sensitive information MUST undergo citizenship verification before system access is granted.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal employees | YES | All federal personnel |
| Contractors | YES | When accessing citizenship-restricted systems |
| Temporary staff | YES | When accessing citizenship-restricted systems |
| Visitors | NO | No access to citizenship-restricted systems |
| Foreign nationals | CONDITIONAL | Only with documented exceptions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CHRO | • Define citizenship requirements for information types<br>• Oversee citizenship verification processes<br>• Maintain personnel screening records |
| System Owners | • Identify systems requiring citizenship restrictions<br>• Coordinate with HR for access decisions<br>• Document system-specific requirements |
| Security Officers | • Validate citizenship verification completion<br>• Monitor compliance with access restrictions<br>• Report citizenship requirement violations |

## 4. RULES
[RULE-01] Information types requiring citizenship restrictions MUST be formally defined and documented in the system security plan.
[VALIDATION] IF information_type = "citizenship_restricted" AND documented_requirements = FALSE THEN violation

[RULE-02] Individuals accessing citizenship-restricted systems MUST have verified citizenship status documented before initial access.
[VALIDATION] IF system_access = TRUE AND citizenship_verified = FALSE AND system_type = "citizenship_restricted" THEN critical_violation

[RULE-03] Citizenship verification MUST be completed within 30 days of access request for citizenship-restricted systems.
[VALIDATION] IF access_request_date + 30_days < current_date AND citizenship_verification = "pending" THEN violation

[RULE-04] Foreign nationals SHALL NOT access systems processing citizenship-restricted information without documented exception approval from the authorizing official.
[VALIDATION] IF citizenship_status = "foreign_national" AND system_access = TRUE AND exception_approved = FALSE THEN critical_violation

[RULE-05] Citizenship verification records MUST be maintained for the duration of employment plus 3 years.
[VALIDATION] IF employment_end_date + 3_years < current_date AND records_retained = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Citizenship Verification Process - Standard process for verifying and documenting citizenship status
- [PROC-02] Information Type Classification - Process for identifying information requiring citizenship restrictions
- [PROC-03] Exception Management - Process for handling foreign national access exceptions
- [PROC-04] Records Management - Process for maintaining citizenship verification documentation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Changes in classification levels, new regulatory requirements, security incidents involving citizenship violations

## 7. SCENARIO PATTERNS
[SCENARIO-01: Contractor Access to Classified System]
IF user_type = "contractor"
AND system_classification = "citizenship_restricted"
AND citizenship_verified = TRUE
AND citizenship_status = "US_citizen"
THEN compliance = TRUE

[SCENARIO-02: Foreign National Exception]
IF citizenship_status = "foreign_national"
AND system_access = TRUE
AND system_type = "citizenship_restricted"
AND exception_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Pending Verification Timeout]
IF access_request_date = "2024-01-01"
AND current_date = "2024-02-15"
AND citizenship_verification = "pending"
AND system_type = "citizenship_restricted"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Proper Documentation]
IF information_type = "export_controlled"
AND citizenship_requirements = "documented"
AND system_security_plan = "updated"
AND verification_process = "implemented"
THEN compliance = TRUE

[SCENARIO-05: Records Retention Violation]
IF employment_end_date = "2020-01-01"
AND current_date = "2024-01-01"
AND citizenship_records_retained = FALSE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information types requiring citizenship restrictions are defined | [RULE-01] |
| Citizenship requirements are met by individuals accessing restricted systems | [RULE-02], [RULE-04] |
| Verification processes are timely and documented | [RULE-03] |
| Records management requirements are met | [RULE-05] |