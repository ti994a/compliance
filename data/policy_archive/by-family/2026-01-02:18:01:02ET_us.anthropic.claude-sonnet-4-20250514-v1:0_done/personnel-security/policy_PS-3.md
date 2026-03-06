# POLICY: PS-3: Personnel Screening

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-3 |
| NIST Control | PS-3: Personnel Screening |
| Version | 1.0 |
| Owner | Chief Human Resources Officer |
| Keywords | personnel screening, background investigation, rescreening, access authorization, security clearance |

## 1. POLICY STATEMENT
All individuals MUST undergo appropriate screening prior to being granted access to organizational systems. Personnel MUST be rescreened at defined intervals and when specific conditions occur to maintain their access authorization.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Full-time employees | YES | All positions requiring system access |
| Contractors | YES | Based on contract duration and access requirements |
| Temporary staff | YES | Screening level based on access needs |
| Visitors | CONDITIONAL | Only if requiring unescorted system access |
| Vendors | YES | When accessing organizational systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| HR Security Team | • Conduct initial personnel screening<br>• Maintain screening records<br>• Execute rescreening programs<br>• Validate screening requirements by position |
| Information Security Officer | • Define screening requirements by system sensitivity<br>• Approve access based on screening results<br>• Monitor compliance with screening policies |
| Hiring Managers | • Identify position risk levels<br>• Ensure screening completion before access<br>• Report personnel status changes |

## 4. RULES

[RULE-01] Personnel screening MUST be completed and approved before granting any system access authorization.
[VALIDATION] IF access_granted = TRUE AND screening_status != "completed_approved" THEN critical_violation

[RULE-02] Background investigations MUST be conducted for all positions with access to HIGH or MODERATE impact systems within 30 days of hire date.
[VALIDATION] IF system_impact IN ["HIGH", "MODERATE"] AND days_since_hire > 30 AND background_investigation != "completed" THEN violation

[RULE-03] Personnel with access to financial systems MUST undergo credit checks and criminal background verification for SOX and PCI-DSS compliance.
[VALIDATION] IF system_type = "financial" AND (credit_check != "completed" OR criminal_background != "completed") THEN compliance_violation

[RULE-04] Rescreening MUST occur every 5 years for HIGH impact systems, every 10 years for MODERATE impact systems, and every 15 years for LOW impact systems.
[VALIDATION] IF system_impact = "HIGH" AND days_since_last_screening > 1825 THEN violation
[VALIDATION] IF system_impact = "MODERATE" AND days_since_last_screening > 3650 THEN violation
[VALIDATION] IF system_impact = "LOW" AND days_since_last_screening > 5475 THEN violation

[RULE-05] Immediate rescreening MUST be triggered by arrests, financial issues, foreign travel exceeding 90 days, or security incidents involving the individual.
[VALIDATION] IF trigger_event IN ["arrest", "financial_issue", "extended_travel", "security_incident"] AND rescreening_initiated = FALSE THEN critical_violation

[RULE-06] Contractors MUST complete screening appropriate to their access level and contract duration exceeding 90 days.
[VALIDATION] IF user_type = "contractor" AND contract_days > 90 AND screening_level < required_level THEN violation

[RULE-07] Access MUST be suspended immediately if screening results indicate disqualifying factors or if rescreening is overdue by more than 60 days.
[VALIDATION] IF (screening_result = "disqualified" OR rescreening_overdue_days > 60) AND access_status = "active" THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Personnel Screening Process - Defines screening requirements by position risk level and system sensitivity
- [PROC-02] Background Investigation Procedures - Details investigation scope, approved vendors, and adjudication criteria
- [PROC-03] Rescreening Program - Establishes triggers, frequencies, and processes for ongoing personnel evaluation
- [PROC-04] Screening Records Management - Governs retention, access, and protection of screening documentation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Regulatory changes, security incidents involving personnel, audit findings, organizational restructuring

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Employee System Access]
IF employee_status = "new_hire"
AND system_access_requested = TRUE
AND screening_status != "completed_approved"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Contractor Long-term Access]
IF user_type = "contractor"
AND contract_duration > 90_days
AND system_impact = "HIGH"
AND background_investigation = "not_completed"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Overdue Rescreening]
IF system_impact = "HIGH"
AND last_screening_date < (current_date - 5_years)
AND access_status = "active"
AND rescreening_in_progress = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Triggered Rescreening Event]
IF security_incident_involving_user = TRUE
AND incident_date < (current_date - 30_days)
AND rescreening_initiated = FALSE
AND access_suspended = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Financial System Access]
IF system_type IN ["financial", "sox_scope", "pci_environment"]
AND (credit_check_status != "completed" OR criminal_background != "completed")
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Individuals screened prior to system access | RULE-01, RULE-02 |
| Rescreening conditions defined | RULE-04, RULE-05 |
| Rescreening frequency established | RULE-04 |
| Screening appropriate to risk level | RULE-02, RULE-03, RULE-06 |
| Access suspension for screening issues | RULE-07 |