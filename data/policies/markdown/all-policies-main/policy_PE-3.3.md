# POLICY: PE-3.3: Continuous Guards

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-3.3 |
| NIST Control | PE-3.3: Continuous Guards |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | physical access, guards, 24x7, facility security, continuous monitoring |

## 1. POLICY STATEMENT
The organization SHALL employ security guards to control physical access points to facilities housing information systems 24 hours per day, 7 days per week. Guards provide continuous human oversight and rapid response capabilities for physical security incidents.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All Tier 3/4 facilities |
| Corporate Offices | CONDITIONAL | Only those housing critical systems |
| Cloud Provider Facilities | YES | Must verify provider compliance |
| Remote Offices | NO | Unless housing critical infrastructure |
| Warehouse/Storage | CONDITIONAL | If containing sensitive equipment |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Coordinate guard staffing and schedules<br>• Ensure 24x7 coverage without gaps<br>• Manage guard training and certification |
| Security Operations | • Define access control procedures for guards<br>• Monitor guard performance and incidents<br>• Coordinate with guards on security events |
| System Owners | • Identify facilities requiring continuous guard coverage<br>• Define specific access control requirements<br>• Approve guard access procedures |

## 4. RULES
[RULE-01] Facilities housing critical information systems MUST have security guards present 24 hours per day, 7 days per week with no coverage gaps exceeding 15 minutes during shift changes.
[VALIDATION] IF facility_criticality = "high" AND guard_coverage_gap > 15_minutes THEN violation

[RULE-02] Guards MUST be trained and certified in physical access control procedures, emergency response, and incident reporting within 30 days of assignment.
[VALIDATION] IF guard_assignment_date + 30_days < current_date AND training_complete = FALSE THEN violation

[RULE-03] Guard posts SHALL maintain visual oversight of all designated physical access points and MUST NOT be left unattended during active shifts.
[VALIDATION] IF access_point_monitored = FALSE OR guard_post_abandoned = TRUE THEN critical_violation

[RULE-04] Guards MUST verify identity and authorization for all personnel accessing controlled areas using approved authentication methods and access lists.
[VALIDATION] IF access_granted = TRUE AND (identity_verified = FALSE OR authorization_checked = FALSE) THEN violation

[RULE-05] Security incidents identified by guards MUST be reported to the Security Operations Center within 15 minutes of detection.
[VALIDATION] IF incident_detected = TRUE AND reporting_time > 15_minutes THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Guard Staffing and Scheduling - Ensure continuous 24x7 coverage with backup personnel
- [PROC-02] Physical Access Verification - Standard procedures for identity and authorization checks
- [PROC-03] Incident Response and Reporting - Guard protocols for security event handling
- [PROC-04] Guard Training and Certification - Required training programs and ongoing education
- [PROC-05] Shift Change Protocols - Procedures to minimize coverage gaps during transitions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, facility changes, regulatory updates, staffing issues

## 7. SCENARIO PATTERNS
[SCENARIO-01: Shift Change Gap]
IF shift_change_time = TRUE
AND coverage_gap > 15_minutes
AND facility_criticality = "high"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Untrained Guard Assignment]
IF guard_assigned = TRUE
AND assignment_duration > 30_days
AND training_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Access Granted Without Verification]
IF access_request = TRUE
AND identity_verification = FALSE
AND guard_present = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Delayed Incident Reporting]
IF security_incident = TRUE
AND guard_detection = TRUE
AND report_time > 15_minutes
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Unmonitored Access Point]
IF access_point_designated = TRUE
AND guard_visual_oversight = FALSE
AND shift_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Guards employed 24x7 at facility access points | [RULE-01] |
| Guards control physical access to system facilities | [RULE-03], [RULE-04] |
| Continuous coverage without gaps | [RULE-01] |
| Proper guard training and procedures | [RULE-02] |
| Incident detection and response capability | [RULE-05] |