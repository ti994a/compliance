# POLICY: PE-3.3: Continuous Guards

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-3.3 |
| NIST Control | PE-3.3: Continuous Guards |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | physical access, guards, 24x7, facility protection, continuous monitoring |

## 1. POLICY STATEMENT
The organization SHALL employ guards to control physical access points to facilities where information systems reside on a continuous 24 hours per day, 7 days per week basis. Guards provide immediate response capability and human surveillance for areas not covered by automated systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Data Centers | YES | All Tier III/IV facilities |
| Server Rooms | YES | Housing critical systems |
| Network Operations Centers | YES | 24x7 operational facilities |
| Office Buildings | CONDITIONAL | Only if housing regulated systems |
| Backup Facilities | YES | Per CP-6/CP-7 requirements |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facility Security Manager | • Define guard posts and coverage requirements<br>• Ensure 24x7 staffing schedules<br>• Monitor guard performance |
| Security Guards | • Control physical access at assigned points<br>• Verify visitor authorization<br>• Respond to security incidents |
| CISO | • Approve guard deployment strategy<br>• Review security effectiveness |

## 4. RULES
[RULE-01] Guards MUST be stationed at all defined physical access points to facilities housing information systems 24 hours per day, 7 days per week without interruption.
[VALIDATION] IF facility_houses_systems = TRUE AND guard_coverage_hours < 168_per_week THEN violation

[RULE-02] Guard posts MUST be established at primary entry points, loading docks, and any unmanned access points to system facilities.
[VALIDATION] IF access_point_type IN ["primary_entry", "loading_dock", "unmanned_access"] AND guard_assigned = FALSE THEN violation

[RULE-03] Guards MUST maintain continuous visual surveillance of assigned access points and SHALL NOT leave posts unattended.
[VALIDATION] IF post_abandonment_time > 0_minutes AND relief_guard_present = FALSE THEN violation

[RULE-04] All guard shifts MUST have documented handover procedures including incident logs, visitor status, and facility condition reports.
[VALIDATION] IF shift_change = TRUE AND handover_documented = FALSE THEN violation

[RULE-05] Guards MUST verify identity and authorization for all personnel seeking facility access through controlled access points.
[VALIDATION] IF access_granted = TRUE AND (identity_verified = FALSE OR authorization_verified = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Guard Post Assignment - Define coverage areas and responsibilities
- [PROC-02] Shift Scheduling - Ensure 24x7 coverage without gaps
- [PROC-03] Access Verification - Identity and authorization validation process
- [PROC-04] Incident Response - Guard response to security events
- [PROC-05] Performance Monitoring - Guard effectiveness assessment

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, facility changes, system relocations

## 7. SCENARIO PATTERNS
[SCENARIO-01: Night Shift Gap]
IF time_of_day BETWEEN "22:00" AND "06:00"
AND guard_on_duty = FALSE
AND facility_houses_critical_systems = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Multiple Access Points]
IF facility_access_points > 1
AND guarded_access_points < total_access_points
AND unguarded_points_secured = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Guard Break Coverage]
IF guard_on_break = TRUE
AND break_duration > 30_minutes
AND relief_guard_present = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Visitor Access Without Verification]
IF visitor_access_granted = TRUE
AND identity_verification = FALSE
AND guard_override_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Emergency Evacuation]
IF emergency_status = "active"
AND guard_abandons_post = TRUE
AND post_security_maintained = FALSE
THEN compliance = CONDITIONAL
violation_severity = "Review Required"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Guards employed at physical access points | [RULE-01], [RULE-02] |
| 24x7 continuous coverage | [RULE-01], [RULE-03] |
| Access control verification | [RULE-05] |
| Operational procedures | [RULE-04] |