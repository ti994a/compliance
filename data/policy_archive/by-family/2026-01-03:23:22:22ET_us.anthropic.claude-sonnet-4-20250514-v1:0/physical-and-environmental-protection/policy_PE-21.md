# POLICY: PE-21: Electromagnetic Pulse Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-21 |
| NIST Control | PE-21: Electromagnetic Pulse Protection |
| Version | 1.0 |
| Owner | Chief Physical Security Officer |
| Keywords | electromagnetic pulse, EMP, shielding, surge protection, critical infrastructure, equipment protection |

## 1. POLICY STATEMENT
The organization SHALL implement protective measures against electromagnetic pulse (EMP) damage for systems and components requiring such protection. All EMP protection measures MUST be documented, implemented, and regularly tested to ensure effectiveness against natural and man-made electromagnetic interference.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical Infrastructure Systems | YES | All systems supporting essential operations |
| Data Centers | YES | Primary and backup facilities |
| Network Equipment | CONDITIONAL | Equipment supporting critical operations only |
| End-User Devices | NO | Unless specifically designated as critical |
| Cloud Infrastructure | CONDITIONAL | Only organization-controlled cloud facilities |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Physical Security Officer | • Define EMP protection requirements<br>• Approve protective measures<br>• Oversee compliance monitoring |
| Facilities Manager | • Implement physical EMP protections<br>• Maintain shielding and grounding systems<br>• Coordinate testing activities |
| IT Operations Manager | • Identify systems requiring protection<br>• Implement technical safeguards<br>• Monitor system resilience |

## 4. RULES
[RULE-01] Organizations MUST identify and document all systems and components requiring EMP protection based on criticality assessment and operational impact analysis.
[VALIDATION] IF system_criticality >= "HIGH" AND emp_assessment_documented = FALSE THEN violation

[RULE-02] Protective measures against EMP damage MUST include at least two of the following: electromagnetic shielding, surge suppressors, ferro-resonant transformers, or proper earth grounding.
[VALIDATION] IF emp_protection_methods_count < 2 AND system_requires_emp_protection = TRUE THEN violation

[RULE-03] EMP protection measures MUST be tested annually and after any significant infrastructure changes to verify effectiveness.
[VALIDATION] IF last_emp_test_date > 365_days AND system_has_emp_protection = TRUE THEN violation

[RULE-04] All EMP protective measures SHALL be documented in the system security plan with specific implementation details and maintenance schedules.
[VALIDATION] IF emp_protection_documented_in_ssp = FALSE AND emp_protection_required = TRUE THEN violation

[RULE-05] Critical infrastructure systems MUST maintain EMP protection that can withstand pulses up to the facility's defined threat level as determined by risk assessment.
[VALIDATION] IF emp_protection_rating < facility_threat_level AND system_type = "critical_infrastructure" THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] EMP Risk Assessment - Annual evaluation of EMP threats and system vulnerabilities
- [PROC-02] Protection Implementation - Installation and configuration of EMP protective measures
- [PROC-03] Testing and Validation - Regular testing of EMP protection effectiveness
- [PROC-04] Incident Response - Procedures for EMP events and recovery operations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: EMP incidents, facility changes, new critical systems deployment, threat assessment updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Critical System Deployment]
IF system_criticality = "HIGH"
AND emp_assessment_completed = FALSE
AND system_deployment_date <= current_date
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Inadequate Protection Methods]
IF system_requires_emp_protection = TRUE
AND emp_protection_methods_count = 1
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Overdue Testing]
IF emp_protection_installed = TRUE
AND last_test_date > 365_days
AND no_approved_extension = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Critical Infrastructure Without Protection]
IF system_type = "critical_infrastructure"
AND emp_protection_installed = FALSE
AND risk_assessment_complete = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Compliant Implementation]
IF system_requires_emp_protection = TRUE
AND emp_protection_methods_count >= 2
AND last_test_date <= 365_days
AND documented_in_ssp = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Protective measures employed against electromagnetic pulse damage are defined | [RULE-01], [RULE-04] |
| Systems and components requiring protection are identified | [RULE-01] |
| Protective measures are implemented for identified systems | [RULE-02], [RULE-05] |
| Protection effectiveness is validated | [RULE-03] |