# POLICY: AT-3.1: Environmental Controls Training

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AT-3.1 |
| NIST Control | AT-3.1: Environmental Controls Training |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | environmental controls, training, fire suppression, HVAC, facility security, personnel training |

## 1. POLICY STATEMENT
All personnel responsible for operating environmental controls must receive initial and refresher training on fire suppression systems, HVAC controls, power systems, and related facility security equipment. Training ensures proper operation and emergency response capabilities for critical environmental systems protecting information technology infrastructure.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Facilities Management Staff | YES | Primary operators of environmental systems |
| Data Center Personnel | YES | Direct interaction with environmental controls |
| Security Operations Staff | YES | Emergency response and monitoring responsibilities |
| IT Infrastructure Teams | YES | Systems dependent on environmental controls |
| Contractors with Facility Access | YES | When operating environmental systems |
| General Office Personnel | NO | Unless specifically assigned environmental control duties |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Identify personnel requiring environmental controls training<br>• Maintain training curriculum and materials<br>• Schedule and track completion of required training |
| CISO | • Define training requirements and frequencies<br>• Ensure compliance with security objectives<br>• Approve training exceptions and waivers |
| Training Coordinator | • Deliver environmental controls training programs<br>• Maintain training records and certifications<br>• Report training compliance status |

## 4. RULES
[RULE-01] All personnel with environmental controls responsibilities MUST receive initial training within 30 days of role assignment or facility access authorization.
[VALIDATION] IF personnel_role = "environmental_controls" AND days_since_assignment > 30 AND initial_training_completed = FALSE THEN violation

[RULE-02] Refresher training for environmental controls operation MUST be completed annually for all in-scope personnel.
[VALIDATION] IF last_refresher_training_date < (current_date - 365_days) AND personnel_scope = "environmental_controls" THEN violation

[RULE-03] Training curriculum MUST cover fire suppression systems, detection devices, HVAC operations, power systems, and emergency procedures.
[VALIDATION] IF training_curriculum_missing ANY OF ["fire_suppression", "detection_systems", "hvac", "power_systems", "emergency_procedures"] THEN violation

[RULE-04] Personnel operating critical environmental systems MUST demonstrate competency through practical assessment before independent operation authorization.
[VALIDATION] IF system_criticality = "high" AND practical_assessment_passed = FALSE AND independent_operation = TRUE THEN critical_violation

[RULE-05] Training records MUST be maintained for minimum of three years and include completion dates, instructor information, and assessment results.
[VALIDATION] IF training_record_age > 3_years OR missing_required_fields = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Environmental Controls Training Program - Standardized curriculum development and delivery
- [PROC-02] Personnel Role Assessment - Identification of staff requiring environmental controls training
- [PROC-03] Competency Evaluation - Practical assessment and certification process
- [PROC-04] Training Records Management - Documentation and retention requirements
- [PROC-05] Emergency Response Training - Incident-specific environmental controls procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Environmental system changes, incident involving environmental controls, regulatory updates, facility modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Data Center Technician]
IF employee_role = "data_center_technician"
AND hire_date = 45_days_ago
AND environmental_training_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Annual Refresher Overdue]
IF personnel_scope = "environmental_controls"
AND last_refresher_date = 400_days_ago
AND no_approved_extension = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Contractor Emergency Response]
IF user_type = "contractor"
AND facility_access_level = "data_center"
AND emergency_procedures_training = FALSE
AND contract_duration > 30_days
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Incomplete Training Curriculum]
IF training_program_covers = ["fire_suppression", "hvac"]
AND missing_topics = ["detection_systems", "power_systems", "emergency_procedures"]
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Competency Without Assessment]
IF system_access = "critical_environmental_controls"
AND practical_assessment_completed = FALSE
AND independent_operation_authorized = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Personnel roles for environmental controls training are defined | [RULE-01], [RULE-02] |
| Initial training provided to defined personnel | [RULE-01] |
| Refresher training frequency is defined and followed | [RULE-02] |
| Training covers employment and operation of environmental controls | [RULE-03] |
| Training effectiveness is demonstrated | [RULE-04] |
| Training records are maintained | [RULE-05] |