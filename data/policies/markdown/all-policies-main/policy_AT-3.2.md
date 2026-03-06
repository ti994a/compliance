# POLICY: AT-3.2: Physical Security Controls Training

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AT-3.2 |
| NIST Control | AT-3.2: Physical Security Controls Training |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | physical security, training, access control, facility security, surveillance |

## 1. POLICY STATEMENT
All personnel responsible for employing and operating physical security controls must receive initial training before assignment and periodic refresher training. Training must cover proper operation of physical access controls, intrusion detection systems, surveillance equipment, and security procedures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Security Guards | YES | All facility security personnel |
| Facilities Management | YES | Personnel managing physical controls |
| Data Center Staff | YES | Personnel with physical system access |
| Reception/Front Desk | YES | Personnel controlling visitor access |
| Maintenance Staff | YES | Personnel with facility access |
| Remote Workers | NO | No physical security responsibilities |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Training Manager | • Develop physical security training curriculum<br>• Schedule and track training completion<br>• Maintain training records |
| Facilities Security Manager | • Define training requirements for physical controls<br>• Validate training effectiveness<br>• Update training based on control changes |
| HR Manager | • Ensure training completion before role assignment<br>• Track refresher training schedules<br>• Document training in personnel files |

## 4. RULES

[RULE-01] Personnel with physical security control responsibilities MUST complete initial training before being granted access to physical security systems or assigned security duties.
[VALIDATION] IF role_requires_physical_security = TRUE AND initial_training_completed = FALSE AND access_granted = TRUE THEN violation

[RULE-02] Refresher training for physical security controls MUST be provided annually for all personnel with ongoing physical security responsibilities.
[VALIDATION] IF last_refresher_training_date > 365_days AND active_physical_security_role = TRUE THEN violation

[RULE-03] Training curriculum MUST cover operation of physical access control devices, intrusion detection alarms, surveillance equipment, and facility security procedures.
[VALIDATION] IF training_curriculum_missing_component = TRUE THEN violation

[RULE-04] Training completion records MUST be maintained for all personnel with physical security responsibilities for a minimum of 3 years.
[VALIDATION] IF training_record_age > 3_years AND personnel_active = TRUE THEN violation

[RULE-05] Personnel MUST demonstrate competency in physical security control operation before independent assignment to security duties.
[VALIDATION] IF competency_assessment_passed = FALSE AND independent_assignment = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Physical Security Training Program - Establish curriculum and delivery methods
- [PROC-02] Training Record Management - Maintain and track training completion
- [PROC-03] Competency Assessment - Evaluate personnel proficiency in security controls
- [PROC-04] Training Content Updates - Regular review and update of training materials

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New physical security controls, security incidents, regulatory changes, personnel role changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Security Guard Assignment]
IF role_type = "security_guard"
AND start_date <= current_date
AND initial_physical_security_training = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Annual Refresher Training Overdue]
IF physical_security_role = TRUE
AND last_training_date > 365_days_ago
AND training_exemption = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Incomplete Training Curriculum]
IF training_covers_access_controls = FALSE
OR training_covers_alarms = FALSE
OR training_covers_surveillance = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Training Records]
IF personnel_has_physical_security_role = TRUE
AND training_records_available = FALSE
AND role_start_date > 30_days_ago
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Competency Not Verified]
IF independent_security_duties = TRUE
AND competency_assessment_completed = FALSE
AND role_assignment_date <= current_date
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Initial training provided before assignment | [RULE-01] |
| Refresher training frequency defined and followed | [RULE-02] |
| Training covers physical security control operation | [RULE-03] |
| Training records maintained | [RULE-04] |
| Personnel competency verified | [RULE-05] |