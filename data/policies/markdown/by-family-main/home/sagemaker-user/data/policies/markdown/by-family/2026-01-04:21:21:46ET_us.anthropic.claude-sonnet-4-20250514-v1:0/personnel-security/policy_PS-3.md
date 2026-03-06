# POLICY: PS-3: Personnel Screening

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-3 |
| NIST Control | PS-3: Personnel Screening |
| Version | 1.0 |
| Owner | Chief Human Resources Officer |
| Keywords | personnel screening, background checks, rescreening, access authorization, risk designation |

## 1. POLICY STATEMENT
All individuals MUST undergo appropriate screening prior to being granted access to organizational systems. Personnel MUST be rescreened at defined intervals and when specific conditions warrant additional verification based on their assigned position risk designation and system sensitivity levels.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Full-time employees | YES | All risk designations |
| Contract personnel | YES | Based on system access requirements |
| Temporary staff | YES | Proportional to access level |
| Vendors/Third parties | YES | When requiring system access |
| Interns | YES | Based on data sensitivity |
| Board members | YES | When requiring system access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| HR Security Team | • Conduct initial personnel screening<br>• Schedule and execute rescreening activities<br>• Maintain screening documentation<br>• Coordinate with security for risk designations |
| Information Security | • Define system-specific screening requirements<br>• Establish risk designation criteria<br>• Review and approve access based on screening results |
| Hiring Managers | • Initiate screening requests<br>• Provide position risk assessments<br>• Ensure no access granted before screening completion |

## 4. RULES
[RULE-01] Personnel screening MUST be completed and approved before any system access is granted to new individuals.
[VALIDATION] IF access_granted = TRUE AND screening_status ≠ "approved" THEN critical_violation

[RULE-02] Background investigations MUST be conducted for all personnel accessing systems containing PII, financial data, or classified information.
[VALIDATION] IF system_sensitivity ∈ ["high", "moderate"] AND background_check = FALSE THEN violation

[RULE-03] Personnel in high-risk positions MUST be rescreened every 3 years, moderate-risk positions every 5 years, and low-risk positions every 10 years.
[VALIDATION] IF risk_designation = "high" AND last_screening_date > 3_years THEN violation
[VALIDATION] IF risk_designation = "moderate" AND last_screening_date > 5_years THEN violation
[VALIDATION] IF risk_designation = "low" AND last_screening_date > 10_years THEN violation

[RULE-04] Immediate rescreening MUST be triggered by security incidents, criminal charges, financial distress indicators, or foreign travel to restricted countries.
[VALIDATION] IF trigger_event = TRUE AND rescreening_initiated = FALSE AND days_since_event > 30 THEN violation

[RULE-05] Contractors and vendors MUST undergo screening proportional to their system access level and data sensitivity exposure.
[VALIDATION] IF user_type = "contractor" AND system_access = TRUE AND screening_level < required_screening_level THEN violation

[RULE-06] All screening documentation MUST be maintained in secure personnel files with access restricted to authorized HR and security personnel.
[VALIDATION] IF screening_records_access ∉ authorized_personnel THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Personnel Screening Process - Defines screening requirements by position risk level
- [PROC-02] Background Investigation Standards - Specifies investigation depth and acceptable sources
- [PROC-03] Rescreening Triggers and Frequency - Details conditions requiring immediate rescreening
- [PROC-04] Contractor Screening Requirements - Establishes third-party screening protocols
- [PROC-05] Screening Documentation Management - Governs record retention and access controls

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Regulatory changes, security incidents involving personnel, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Employee System Access]
IF employee_status = "new_hire"
AND system_access_requested = TRUE
AND screening_status ≠ "approved"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Overdue Rescreening]
IF risk_designation = "high"
AND last_screening_date > 1095_days
AND system_access = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Contractor PII Access]
IF user_type = "contractor"
AND data_access_level = "PII"
AND background_check = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Security Incident Rescreening]
IF security_incident_involved = TRUE
AND incident_date < 30_days_ago
AND rescreening_initiated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Low-Risk Screening]
IF risk_designation = "low"
AND last_screening_date < 3650_days
AND screening_type = "basic_check"
AND system_sensitivity = "low"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Individuals screened prior to system access | [RULE-01] |
| Rescreening conditions defined | [RULE-03], [RULE-04] |
| Rescreening frequency established | [RULE-03] |
| Risk-based screening requirements | [RULE-02], [RULE-05] |
| Documentation security | [RULE-06] |