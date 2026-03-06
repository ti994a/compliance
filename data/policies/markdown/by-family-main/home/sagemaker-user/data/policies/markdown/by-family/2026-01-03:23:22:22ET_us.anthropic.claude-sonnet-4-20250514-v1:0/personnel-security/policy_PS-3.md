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
All individuals MUST undergo appropriate screening prior to being granted access to organizational systems. Rescreening MUST be conducted at defined intervals and when specific conditions warrant additional verification of personnel trustworthiness.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Full-time employees | YES | All positions requiring system access |
| Contractors | YES | Based on contract duration and access level |
| Temporary staff | YES | Screening level varies by access requirements |
| Vendors | CONDITIONAL | Only if requiring privileged or extended access |
| Visitors | NO | Covered under separate visitor management policy |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| HR Security Team | • Conduct initial personnel screening<br>• Maintain screening records<br>• Schedule and execute rescreening activities |
| System Owners | • Define screening requirements for their systems<br>• Validate screening completion before access authorization |
| Security Office | • Establish screening criteria and procedures<br>• Monitor compliance with screening requirements |

## 4. RULES
[RULE-01] All personnel MUST complete appropriate background screening before being granted initial system access.
[VALIDATION] IF personnel_status = "new" AND system_access_granted = TRUE AND background_screening_complete = FALSE THEN critical_violation

[RULE-02] Screening level MUST be commensurate with the highest risk level of systems the individual will access.
[VALIDATION] IF system_risk_level > personnel_screening_level THEN violation

[RULE-03] Personnel with privileged access MUST undergo enhanced screening including criminal background check and employment verification.
[VALIDATION] IF access_type = "privileged" AND (criminal_check = FALSE OR employment_verification = FALSE) THEN violation

[RULE-04] Rescreening MUST occur every 5 years for standard positions and every 3 years for privileged access positions.
[VALIDATION] IF days_since_last_screening > (screening_frequency * 365) AND no_valid_exception THEN violation

[RULE-05] Immediate rescreening MUST be triggered by reportable incidents, security violations, or significant life events.
[VALIDATION] IF trigger_event_reported = TRUE AND rescreening_initiated = FALSE AND days_since_event > 30 THEN violation

[RULE-06] Personnel MUST NOT retain system access if screening expires or reveals disqualifying information.
[VALIDATION] IF (screening_expired = TRUE OR disqualifying_information = TRUE) AND active_access = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Background Investigation Process - Standardized screening procedures based on position risk level
- [PROC-02] Rescreening Workflow - Automated triggers and manual processes for periodic rescreening
- [PROC-03] Screening Documentation - Records management and retention requirements
- [PROC-04] Adverse Information Handling - Process for addressing disqualifying screening results

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Regulatory changes, security incidents involving unscreened personnel, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Contractor Access]
IF user_type = "contractor"
AND contract_duration > 90_days
AND system_access_requested = TRUE
AND background_screening_complete = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Expired Screening with Active Access]
IF last_screening_date < (current_date - 5_years)
AND position_type = "standard"
AND active_system_access = TRUE
AND rescreening_in_progress = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Privileged User Screening Requirements]
IF access_level = "privileged"
AND criminal_background_check = "completed"
AND employment_verification = "completed"
AND screening_date < 3_years_ago
THEN compliance = TRUE

[SCENARIO-04: Security Incident Trigger]
IF security_incident_involving_user = TRUE
AND incident_date > (current_date - 30_days)
AND rescreening_initiated = FALSE
AND incident_severity >= "moderate"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: System Risk Mismatch]
IF user_screening_level = "basic"
AND system_classification = "high"
AND access_granted = TRUE
AND risk_exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Screen individuals prior to system access | [RULE-01], [RULE-02] |
| Rescreen per defined conditions | [RULE-04], [RULE-05] |
| Rescreen at defined frequencies | [RULE-04] |
| Maintain screening records | [RULE-01], [RULE-04] |
| Enforce screening-based access decisions | [RULE-06] |