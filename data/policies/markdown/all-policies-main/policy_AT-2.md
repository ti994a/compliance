# POLICY: AT-2: Literacy Training and Awareness

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AT-2 |
| NIST Control | AT-2: Literacy Training and Awareness |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | security training, privacy training, awareness, literacy, user education, incident response |

## 1. POLICY STATEMENT
All system users including managers, senior executives, and contractors must receive security and privacy literacy training upon initial access and at regular intervals thereafter. Training content must be updated regularly and incorporate lessons learned from security incidents to maintain organizational security and privacy posture.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Employees | YES | All full-time and part-time employees |
| Contractors | YES | All contractors with system access |
| Temporary Staff | YES | All temporary workers with system access |
| Executives | YES | Including C-level and senior management |
| Vendors | CONDITIONAL | Only if granted system access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve training curriculum and content<br>• Define training frequency requirements<br>• Oversee compliance monitoring |
| Security Training Manager | • Develop and maintain training materials<br>• Track completion rates and compliance<br>• Update content based on incidents |
| HR Department | • Coordinate initial training for new hires<br>• Maintain training records<br>• Trigger training for role changes |
| Line Managers | • Ensure team members complete required training<br>• Report training compliance issues<br>• Reinforce security awareness |

## 4. RULES
[RULE-01] All new users MUST complete initial security and privacy literacy training within 30 days of system access grant.
[VALIDATION] IF user_start_date + 30_days < current_date AND initial_training_complete = FALSE THEN violation

[RULE-02] All users MUST complete refresher security and privacy literacy training annually.
[VALIDATION] IF last_training_date + 365_days < current_date THEN violation

[RULE-03] Additional training MUST be completed within 60 days when triggered by system changes or security incidents.
[VALIDATION] IF triggering_event_date + 60_days < current_date AND event_training_complete = FALSE THEN violation

[RULE-04] Training content MUST be updated at least annually and within 90 days of significant security incidents.
[VALIDATION] IF content_last_updated + 365_days < current_date THEN violation
[VALIDATION] IF major_incident_date + 90_days < current_date AND content_updated_post_incident = FALSE THEN violation

[RULE-05] Training completion rates MUST maintain 95% compliance across all user categories.
[VALIDATION] IF completion_rate < 95% THEN violation

[RULE-06] Lessons learned from internal or external security incidents MUST be incorporated into training materials within 90 days.
[VALIDATION] IF incident_lessons_identified = TRUE AND incorporation_date > incident_date + 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] New User Training Enrollment - Automated enrollment process for new system users
- [PROC-02] Training Content Development - Process for creating and updating training materials
- [PROC-03] Completion Tracking - Monitoring and reporting of training completion status
- [PROC-04] Incident-Based Updates - Process for incorporating incident lessons into training
- [PROC-05] Compliance Reporting - Regular reporting of training metrics to leadership

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major security incidents, regulatory changes, significant system modifications, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Contractor Access]
IF user_type = "contractor"
AND system_access_granted = TRUE
AND days_since_access > 30
AND initial_training_complete = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Post-Incident Training Update]
IF security_incident_severity = "high"
AND incident_date + 90_days < current_date
AND training_content_updated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Annual Training Overdue]
IF user_status = "active"
AND last_annual_training + 365_days < current_date
AND no_valid_exception = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Executive Training Exemption]
IF user_role = "executive"
AND training_exemption_requested = TRUE
AND exemption_approved_by_ciso = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: System Change Training]
IF major_system_change = TRUE
AND change_affects_user_group = TRUE
AND additional_training_provided = FALSE
AND days_since_change > 60
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Initial training for new users | [RULE-01] |
| Recurring training frequency | [RULE-02] |
| Event-triggered training | [RULE-03] |
| Content update frequency | [RULE-04] |
| Compliance rate maintenance | [RULE-05] |
| Incident lessons incorporation | [RULE-06] |