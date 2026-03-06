# POLICY: AT-4: Training Records

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AT-4 |
| NIST Control | AT-4: Training Records |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | training records, documentation, monitoring, retention, awareness training, role-based training |

## 1. POLICY STATEMENT
The organization SHALL document and monitor all information security and privacy training activities including general awareness training and role-specific training. Individual training records MUST be retained for the organizationally-defined retention period to demonstrate compliance and track employee competency.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Full-time, part-time, temporary |
| Contractors | YES | With system access |
| Vendors | YES | With privileged access |
| Training administrators | YES | Record management responsibilities |
| HR systems | YES | Training record storage |
| Learning management systems | YES | Training delivery and tracking |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve training record retention policies<br>• Ensure compliance monitoring<br>• Review training effectiveness metrics |
| Training Administrator | • Document all training activities<br>• Maintain individual training records<br>• Generate compliance reports<br>• Monitor training completion rates |
| HR Manager | • Coordinate with training administrators<br>• Ensure records retention compliance<br>• Support audit activities |
| Supervisors | • Monitor subordinate training completion<br>• Maintain specialized training documentation<br>• Report training gaps |

## 4. RULES
[RULE-01] All security and privacy training activities MUST be documented with participant names, training content, completion dates, and instructor information.
[VALIDATION] IF training_activity_exists = TRUE AND (participant_name = NULL OR completion_date = NULL OR content_description = NULL) THEN violation

[RULE-02] Individual training records MUST be retained for a minimum of 7 years from completion date or employee separation, whichever is later.
[VALIDATION] IF record_age > 7_years AND employee_status = "active" THEN violation
[VALIDATION] IF record_age > 7_years AND separation_date + 7_years < current_date THEN violation

[RULE-03] Training completion rates MUST be monitored monthly and reported quarterly to management.
[VALIDATION] IF monitoring_frequency > 30_days OR reporting_frequency > 90_days THEN violation

[RULE-04] Role-based training records MUST include specific competencies achieved and assessment scores where applicable.
[VALIDATION] IF role_based_training = TRUE AND (competencies = NULL OR assessment_score = NULL) THEN violation

[RULE-05] Training records MUST be stored in systems with appropriate access controls and backup procedures.
[VALIDATION] IF storage_system_access_controls = FALSE OR backup_procedures = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Training Documentation - Standardized process for recording all training activities
- [PROC-02] Records Retention Management - Automated retention and disposal procedures
- [PROC-03] Training Monitoring - Monthly completion tracking and gap analysis
- [PROC-04] Audit Support - Procedures for providing training records during assessments
- [PROC-05] Records Backup and Recovery - Ensuring training data availability and integrity

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Bi-annually
- Triggering events: Regulatory changes, audit findings, retention period updates, system changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Training Documentation]
IF training_conducted = TRUE
AND documentation_complete = FALSE
AND training_type IN ["security_awareness", "role_based"]
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Expired Record Retention]
IF employee_separation_date + 7_years < current_date
AND training_records_exist = TRUE
AND records_disposed = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-03: Inadequate Monitoring]
IF last_monitoring_date > current_date - 45_days
AND training_program_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Role-Based Training Gaps]
IF employee_role = "privileged_user"
AND role_based_training_completed = FALSE
AND hire_date < current_date - 90_days
AND training_records_complete = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Backup System Failure]
IF training_records_backup_date > current_date - 30_days
AND primary_system_available = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Document security and privacy training activities | [RULE-01] |
| Monitor training activities | [RULE-03] |
| Retain individual training records for defined period | [RULE-02] |
| Maintain role-based training documentation | [RULE-04] |
| Ensure training record system security | [RULE-05] |