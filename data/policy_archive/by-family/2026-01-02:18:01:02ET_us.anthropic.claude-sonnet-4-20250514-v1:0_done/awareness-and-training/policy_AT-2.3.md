# POLICY: AT-2.3: Social Engineering and Mining

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AT-2.3 |
| NIST Control | AT-2.3: Social Engineering and Mining |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | social engineering, phishing, training, awareness, social mining, reporting |

## 1. POLICY STATEMENT
All personnel must receive literacy training on recognizing and reporting potential and actual instances of social engineering and social mining attacks. Training must cover identification techniques, organizational reporting channels, and response procedures to protect organizational information and systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Employees | YES | Including full-time, part-time, temporary |
| Contractors | YES | With system access or organizational data access |
| Third-party Users | YES | With privileged or extended access |
| Visitors | CONDITIONAL | If accessing systems or sensitive areas |
| Executive Leadership | YES | High-value targets requiring specialized training |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve training curriculum and materials<br>• Define reporting procedures<br>• Monitor training effectiveness |
| HR Director | • Ensure training completion tracking<br>• Integrate training into onboarding<br>• Coordinate with Security team on scheduling |
| Security Awareness Manager | • Develop and deliver training content<br>• Track completion rates<br>• Update materials based on threat landscape |
| IT Managers | • Ensure team participation<br>• Reinforce training concepts<br>• Report suspected incidents |

## 4. RULES
[RULE-01] All personnel MUST complete social engineering and social mining literacy training within 30 days of hire or role change requiring system access.
[VALIDATION] IF hire_date OR role_change_date > 30_days_ago AND training_completed = FALSE THEN violation

[RULE-02] Social engineering literacy training MUST cover recognition techniques for phishing, pretexting, impersonation, baiting, quid pro quo, thread-jacking, social media exploitation, and tailgating.
[VALIDATION] IF training_curriculum_includes ALL required_attack_types = FALSE THEN violation

[RULE-03] Social mining literacy training MUST cover information gathering techniques and organizational information protection methods.
[VALIDATION] IF training_curriculum_includes social_mining_content = FALSE THEN violation

[RULE-04] Training MUST include specific procedures for reporting suspected social engineering and social mining attempts through established organizational channels.
[VALIDATION] IF training_includes reporting_procedures = FALSE THEN violation

[RULE-05] Personnel MUST report suspected social engineering or social mining incidents within 2 hours of detection.
[VALIDATION] IF incident_detected = TRUE AND report_time > 2_hours THEN violation

[RULE-06] Refresher training MUST be completed annually by all in-scope personnel.
[VALIDATION] IF last_training_date > 365_days_ago THEN violation

[RULE-07] Training completion rates MUST be tracked and maintained at 95% or higher for all in-scope personnel.
[VALIDATION] IF completion_rate < 95% THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Social Engineering Training Delivery - Standardized curriculum delivery and tracking
- [PROC-02] Incident Reporting Process - Clear escalation paths for suspected attacks
- [PROC-03] Training Effectiveness Assessment - Regular evaluation of training impact
- [PROC-04] Threat Intelligence Integration - Updating training based on current threats

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, new attack vectors, regulatory changes, organizational restructuring

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Employee Training]
IF employee_status = "new_hire"
AND system_access_required = TRUE
AND days_since_hire > 30
AND social_engineering_training_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Contractor Access Without Training]
IF user_type = "contractor"
AND system_access = TRUE
AND social_engineering_training_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Delayed Incident Reporting]
IF social_engineering_attempt_detected = TRUE
AND time_since_detection > 2_hours
AND incident_reported = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Incomplete Training Curriculum]
IF training_curriculum_delivered = TRUE
AND phishing_coverage = FALSE
OR pretexting_coverage = FALSE
OR reporting_procedures_covered = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Low Completion Rates]
IF total_required_personnel > 0
AND training_completion_rate < 95%
AND reporting_period = "current"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Literacy training on recognizing social engineering provided | RULE-02, RULE-06 |
| Literacy training on reporting social engineering provided | RULE-04, RULE-05 |
| Literacy training on recognizing social mining provided | RULE-03, RULE-06 |
| Literacy training on reporting social mining provided | RULE-04, RULE-05 |