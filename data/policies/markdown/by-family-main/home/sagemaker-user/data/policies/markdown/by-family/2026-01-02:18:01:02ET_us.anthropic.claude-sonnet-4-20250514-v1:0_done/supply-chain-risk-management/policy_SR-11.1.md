# POLICY: SR-11.1: Anti-counterfeit Training

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-11-1 |
| NIST Control | SR-11.1: Anti-counterfeit Training |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | counterfeit, training, supply chain, hardware, software, firmware, detection |

## 1. POLICY STATEMENT
All personnel and roles requiring training must receive appropriate instruction to detect counterfeit system components including hardware, software, and firmware. Training programs must be established, maintained, and regularly updated to address evolving counterfeit threats in the supply chain.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| IT Personnel | YES | All technical staff handling system components |
| Procurement Staff | YES | Personnel involved in vendor selection and acquisition |
| Security Teams | YES | Information security and supply chain risk management roles |
| Contractors | YES | Third-party personnel with component access |
| End Users | CONDITIONAL | Only if handling sensitive system components |
| Executive Leadership | NO | Unless directly involved in procurement decisions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Oversee anti-counterfeit training program<br>• Approve training curriculum and updates<br>• Ensure compliance with training requirements |
| Supply Chain Risk Manager | • Develop counterfeit detection training materials<br>• Coordinate with vendors on threat intelligence<br>• Track training completion and effectiveness |
| IT Security Manager | • Identify personnel requiring training<br>• Schedule and deliver training sessions<br>• Maintain training records and documentation |
| Procurement Manager | • Ensure procurement staff receive specialized training<br>• Implement counterfeit detection in acquisition processes<br>• Report suspected counterfeit components |

## 4. RULES
[RULE-01] All personnel in roles requiring counterfeit detection capabilities MUST complete anti-counterfeit training within 30 days of role assignment.
[VALIDATION] IF role_requires_training = TRUE AND training_completion_date > (role_start_date + 30_days) THEN violation

[RULE-02] Anti-counterfeit training MUST be refreshed annually for all personnel in scope.
[VALIDATION] IF last_training_date < (current_date - 365_days) AND role_requires_training = TRUE THEN violation

[RULE-03] Training curriculum MUST cover detection methods for hardware, software, and firmware counterfeits.
[VALIDATION] IF training_covers_hardware = FALSE OR training_covers_software = FALSE OR training_covers_firmware = FALSE THEN violation

[RULE-04] Training completion records MUST be maintained for a minimum of 3 years.
[VALIDATION] IF training_record_age > 3_years AND record_deleted = TRUE THEN violation

[RULE-05] Personnel who fail counterfeit detection assessments MUST receive remedial training within 15 days.
[VALIDATION] IF assessment_score < passing_threshold AND remedial_training_date > (assessment_date + 15_days) THEN violation

[RULE-06] Suspected counterfeit components MUST be reported within 24 hours of detection.
[VALIDATION] IF counterfeit_suspected = TRUE AND report_time > (detection_time + 24_hours) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Anti-Counterfeit Training Development - Create and maintain training materials addressing current counterfeit threats
- [PROC-02] Training Delivery and Tracking - Schedule, conduct, and document completion of required training
- [PROC-03] Counterfeit Detection Assessment - Evaluate personnel competency in identifying counterfeit components
- [PROC-04] Incident Reporting - Process for reporting and investigating suspected counterfeit components
- [PROC-05] Training Record Management - Maintain and archive training documentation per retention requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Detection of counterfeit components, supply chain incidents, regulatory changes, technology updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New IT Staff Training]
IF employee_role = "IT_personnel"
AND hire_date = current_date
AND counterfeit_training_scheduled = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Expired Training Certification]
IF last_training_completion < (current_date - 365_days)
AND role_requires_training = TRUE
AND training_extension_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Contractor Component Access]
IF user_type = "contractor"
AND component_access_level = "high"
AND counterfeit_training_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Failed Assessment Response]
IF assessment_result = "failed"
AND remedial_training_completed = FALSE
AND days_since_assessment > 15
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Suspected Counterfeit Detection]
IF counterfeit_component_detected = TRUE
AND incident_reported = TRUE
AND report_time <= (detection_time + 24_hours)
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Personnel trained to detect counterfeit hardware components | [RULE-01], [RULE-03] |
| Personnel trained to detect counterfeit software components | [RULE-01], [RULE-03] |
| Personnel trained to detect counterfeit firmware components | [RULE-01], [RULE-03] |
| Training program maintenance and updates | [RULE-02], [RULE-03] |
| Training record retention | [RULE-04] |
| Competency validation | [RULE-05] |
| Incident response capability | [RULE-06] |