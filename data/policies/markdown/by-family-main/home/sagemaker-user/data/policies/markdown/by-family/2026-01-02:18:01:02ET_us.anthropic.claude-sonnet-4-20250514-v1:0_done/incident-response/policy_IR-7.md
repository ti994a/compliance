# POLICY: IR-7: Incident Response Assistance

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IR-7 |
| NIST Control | IR-7: Incident Response Assistance |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | incident response, support resource, help desk, assistance, reporting, ticketing, forensics |

## 1. POLICY STATEMENT
The organization SHALL provide an incident response support resource that is integral to the organizational incident response capability. This resource MUST offer advice and assistance to all system users for proper handling and reporting of security incidents.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Including full-time, part-time, contractors |
| System users | YES | Anyone with access to organizational systems |
| Cloud services | YES | Both public and private cloud environments |
| Third-party vendors | CONDITIONAL | When accessing organizational systems |
| Mobile devices | YES | Company-owned and BYOD devices |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Establish incident response support capability<br>• Ensure resource availability and effectiveness<br>• Review support metrics and performance |
| IT Security Team | • Staff incident response support resource<br>• Provide technical assistance and guidance<br>• Maintain incident tracking systems |
| Help Desk Manager | • Manage day-to-day support operations<br>• Train support staff on incident procedures<br>• Escalate incidents per established procedures |
| All Employees | • Report suspected incidents promptly<br>• Utilize available support resources<br>• Follow guidance provided by support team |

## 4. RULES
[RULE-01] The organization MUST maintain a dedicated incident response support resource available during all business hours with emergency contact procedures for after-hours incidents.
[VALIDATION] IF business_hours = TRUE AND support_available = FALSE THEN critical_violation
[VALIDATION] IF after_hours = TRUE AND emergency_contact_unavailable = TRUE THEN violation

[RULE-02] Incident response support resources MUST include automated ticketing systems that track incident reports from initial submission through resolution.
[VALIDATION] IF incident_reported = TRUE AND ticket_created = FALSE THEN violation
[VALIDATION] IF ticket_exists = TRUE AND tracking_incomplete = TRUE THEN violation

[RULE-03] Support staff MUST provide initial response to incident reports within 30 minutes during business hours and within 2 hours for after-hours incidents.
[VALIDATION] IF business_hours = TRUE AND response_time > 30_minutes THEN violation
[VALIDATION] IF after_hours = TRUE AND response_time > 2_hours THEN violation

[RULE-04] The incident response support resource MUST provide access to forensics services for incidents classified as High or Critical severity.
[VALIDATION] IF incident_severity IN ["High", "Critical"] AND forensics_access = FALSE THEN violation

[RULE-05] Support resources MUST maintain current contact information and escalation procedures for all incident response team members and external service providers.
[VALIDATION] IF contact_info_age > 90_days THEN violation
[VALIDATION] IF escalation_procedure_tested = FALSE AND last_test > 6_months THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Incident Reporting Procedures - Standardized process for users to report suspected incidents
- [PROC-02] Support Triage Procedures - Classification and initial assessment of reported incidents  
- [PROC-03] Escalation Procedures - Guidelines for escalating incidents based on severity and type
- [PROC-04] Forensics Engagement Procedures - Process for engaging internal/external forensics resources
- [PROC-05] Support Resource Training - Regular training requirements for support staff

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major incidents, organizational changes, technology updates, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Basic Incident Reporting]
IF user_reports_incident = TRUE
AND ticketing_system_creates_ticket = TRUE
AND initial_response_time <= 30_minutes
THEN compliance = TRUE

[SCENARIO-02: After-Hours Critical Incident]
IF incident_time = "after_hours"
AND incident_severity = "Critical"
AND emergency_contact_responds = TRUE
AND forensics_engaged = TRUE
THEN compliance = TRUE

[SCENARIO-03: Support Resource Unavailable]
IF business_hours = TRUE
AND incident_reported = TRUE
AND support_resource_unavailable = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Delayed Response to High Severity]
IF incident_severity = "High"
AND business_hours = TRUE
AND response_time > 30_minutes
AND no_documented_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Forensics Not Available for Critical Incident]
IF incident_severity = "Critical"
AND forensics_required = TRUE
AND forensics_access = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Incident response support resource provided | [RULE-01] |
| Support resource offers advice and assistance | [RULE-01], [RULE-03] |
| Support resource integral to IR capability | [RULE-02], [RULE-04], [RULE-05] |
| Users can access incident handling guidance | [RULE-01], [RULE-03] |
| Users can access incident reporting assistance | [RULE-02], [RULE-03] |