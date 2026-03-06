# POLICY: SR-11.1: Anti-counterfeit Training

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-11.1 |
| NIST Control | SR-11.1: Anti-counterfeit Training |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | counterfeit, training, supply chain, hardware, software, firmware |

## 1. POLICY STATEMENT
Personnel in roles requiring anti-counterfeit detection capabilities MUST receive training to identify counterfeit system components including hardware, software, and firmware. Training programs SHALL ensure personnel can effectively detect and respond to counterfeit components throughout the supply chain lifecycle.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| IT Procurement Staff | YES | Primary detection responsibility |
| Supply Chain Managers | YES | Vendor oversight and validation |
| Security Personnel | YES | Incident response and investigation |
| Hardware Technicians | YES | Physical component inspection |
| Software Engineers | YES | Code and license validation |
| Contractors with procurement access | YES | Same requirements as employees |
| End users | NO | Unless specifically designated |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Establish anti-counterfeit training program<br>• Define training requirements and frequency<br>• Monitor compliance metrics |
| Supply Chain Manager | • Implement vendor verification procedures<br>• Conduct component authentication<br>• Report suspected counterfeits |
| Training Manager | • Develop training curriculum<br>• Track completion rates<br>• Update materials based on emerging threats |

## 4. RULES
[RULE-01] Personnel in designated roles MUST complete initial anti-counterfeit detection training within 30 days of role assignment.
[VALIDATION] IF role_requires_training = TRUE AND days_in_role > 30 AND initial_training_complete = FALSE THEN violation

[RULE-02] Anti-counterfeit training MUST be refreshed annually with updated threat intelligence and detection techniques.
[VALIDATION] IF last_training_date > 365_days AND role_active = TRUE THEN violation

[RULE-03] Training programs MUST cover identification of counterfeit hardware, software, and firmware components with hands-on exercises.
[VALIDATION] IF training_curriculum_missing_component_type = TRUE THEN program_violation

[RULE-04] Training completion records MUST be maintained for audit purposes for minimum 3 years.
[VALIDATION] IF training_record_age > 3_years AND record_retention = FALSE THEN compliance_violation

[RULE-05] Personnel MUST demonstrate competency through practical assessment before being authorized for independent procurement activities.
[VALIDATION] IF procurement_authorization = TRUE AND competency_assessment_passed = FALSE THEN authorization_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Anti-counterfeit Training Development - Create and maintain curriculum covering current threats
- [PROC-02] Role-based Training Assignment - Identify personnel requiring training based on job functions
- [PROC-03] Competency Assessment - Evaluate practical detection skills through testing
- [PROC-04] Training Record Management - Document and track completion status
- [PROC-05] Incident Response Training - Procedures for reporting suspected counterfeits

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major counterfeit incidents, new threat intelligence, regulatory changes, supply chain security incidents

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Procurement Staff]
IF role = "procurement_specialist"
AND hire_date < 30_days_ago
AND anti_counterfeit_training_complete = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Annual Training Overdue]
IF role_requires_training = TRUE
AND last_training_completion > 365_days
AND employee_status = "active"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Incomplete Training Curriculum]
IF training_program_exists = TRUE
AND (hardware_detection_module = FALSE OR software_detection_module = FALSE OR firmware_detection_module = FALSE)
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Missing Competency Assessment]
IF procurement_authorization_granted = TRUE
AND practical_assessment_completed = FALSE
AND independent_purchasing_access = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Contractor Training Gap]
IF user_type = "contractor"
AND supply_chain_access = TRUE
AND anti_counterfeit_training_complete = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Personnel requiring training are trained to detect counterfeit components | RULE-01, RULE-02 |
| Training covers hardware, software, and firmware detection | RULE-03 |
| Training effectiveness is validated | RULE-05 |
| Training records are maintained | RULE-04 |