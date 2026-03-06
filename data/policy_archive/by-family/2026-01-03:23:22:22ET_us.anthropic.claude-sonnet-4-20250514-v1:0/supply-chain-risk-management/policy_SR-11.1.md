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
All personnel and roles requiring training to detect counterfeit system components MUST receive comprehensive training to identify counterfeit hardware, software, and firmware components. Training programs SHALL ensure personnel can effectively detect and prevent counterfeit components from entering organizational systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| IT Personnel | YES | All technical staff handling system components |
| Procurement Staff | YES | Personnel involved in component acquisition |
| Supply Chain Managers | YES | Personnel managing vendor relationships |
| Security Team | YES | Personnel responsible for component validation |
| Contractors | CONDITIONAL | Only if handling system components |
| End Users | NO | Unless specifically designated roles |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve anti-counterfeit training program<br>• Ensure adequate training resources<br>• Monitor training effectiveness |
| Training Manager | • Develop anti-counterfeit training curriculum<br>• Schedule and deliver training sessions<br>• Maintain training records and certifications |
| Supply Chain Manager | • Identify personnel requiring training<br>• Validate training completion before component handling<br>• Report counterfeit detection incidents |

## 4. RULES
[RULE-01] Personnel in roles requiring counterfeit detection capabilities MUST complete anti-counterfeit training before handling system components.
[VALIDATION] IF role_requires_training = TRUE AND training_completed = FALSE AND component_access = TRUE THEN violation

[RULE-02] Anti-counterfeit training MUST cover detection of counterfeit hardware, software, and firmware components.
[VALIDATION] IF training_content_missing = ["hardware", "software", "firmware"] THEN violation

[RULE-03] Training records MUST be maintained for all personnel completing anti-counterfeit training for minimum 3 years.
[VALIDATION] IF training_record_age > 3_years AND record_retention = TRUE THEN violation

[RULE-04] Anti-counterfeit training MUST be refreshed every 24 months or when significant threats emerge.
[VALIDATION] IF last_training_date > 24_months AND no_refresh_completed = TRUE THEN violation

[RULE-05] Training effectiveness MUST be validated through practical exercises or assessments.
[VALIDATION] IF training_completed = TRUE AND assessment_passed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Training Needs Assessment - Identify roles requiring anti-counterfeit training
- [PROC-02] Curriculum Development - Create comprehensive training materials covering all component types
- [PROC-03] Training Delivery - Conduct training sessions and practical exercises
- [PROC-04] Competency Validation - Assess personnel ability to detect counterfeit components
- [PROC-05] Record Maintenance - Document and maintain training completion records

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 18 months
- Triggering events: New counterfeit threats identified, supply chain incidents, regulatory changes, failed training assessments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Untrained Personnel Handling Components]
IF role_requires_training = TRUE
AND training_completed = FALSE
AND component_handling_access = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Outdated Training]
IF last_training_date > 24_months
AND no_refresh_training = TRUE
AND active_component_role = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Incomplete Training Coverage]
IF training_completed = TRUE
AND training_covers_hardware = FALSE
AND role_handles_hardware = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Training Records]
IF training_claimed_completed = TRUE
AND training_record_exists = FALSE
AND audit_requested = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Failed Competency Assessment]
IF training_completed = TRUE
AND competency_assessment_passed = FALSE
AND component_access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Personnel trained to detect counterfeit hardware components | [RULE-01], [RULE-02] |
| Personnel trained to detect counterfeit software components | [RULE-01], [RULE-02] |
| Personnel trained to detect counterfeit firmware components | [RULE-01], [RULE-02] |
| Training records maintained and accessible | [RULE-03] |
| Training effectiveness validated | [RULE-05] |
| Training currency maintained | [RULE-04] |