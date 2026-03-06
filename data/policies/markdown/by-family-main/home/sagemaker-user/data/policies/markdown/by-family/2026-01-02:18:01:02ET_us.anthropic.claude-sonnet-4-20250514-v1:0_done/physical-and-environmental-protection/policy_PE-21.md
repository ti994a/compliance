# POLICY: PE-21: Electromagnetic Pulse Protection

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-21 |
| NIST Control | PE-21: Electromagnetic Pulse Protection |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | electromagnetic pulse, EMP protection, shielding, critical infrastructure, physical protection |

## 1. POLICY STATEMENT
The organization SHALL implement protective measures against electromagnetic pulse (EMP) damage for systems and components that require such protection. All EMP protection measures MUST be documented, implemented, and maintained according to organizational risk assessments and critical infrastructure requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical Infrastructure Systems | YES | All systems supporting critical operations |
| Data Centers | YES | Primary and backup facilities |
| Network Equipment | CONDITIONAL | Based on criticality assessment |
| End User Devices | NO | Unless specifically designated as critical |
| Cloud Services | CONDITIONAL | Customer responsibility in hybrid model |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Facilities Manager | • Implement physical EMP protection measures<br>• Maintain shielding and grounding systems<br>• Coordinate with vendors for protective equipment |
| Security Operations | • Conduct EMP risk assessments<br>• Define protection requirements<br>• Monitor protective measure effectiveness |
| System Owners | • Identify systems requiring EMP protection<br>• Validate protection implementation<br>• Report protection failures |

## 4. RULES
[RULE-01] Systems and components requiring EMP protection MUST be identified through documented risk assessment within 90 days of deployment.
[VALIDATION] IF system_deployed = TRUE AND emp_risk_assessment_completed = FALSE AND days_since_deployment > 90 THEN violation

[RULE-02] Protective measures against EMP damage MUST be implemented for all systems identified as requiring protection within 180 days of identification.
[VALIDATION] IF emp_protection_required = TRUE AND protective_measures_implemented = FALSE AND days_since_identification > 180 THEN violation

[RULE-03] EMP protective measures MUST include at least one of the following: electromagnetic shielding, surge suppressors, ferro-resonant transformers, or proper earth grounding.
[VALIDATION] IF emp_protection_required = TRUE AND (shielding = FALSE AND surge_suppressors = FALSE AND transformers = FALSE AND grounding = FALSE) THEN critical_violation

[RULE-04] All EMP protection measures MUST be documented in the system security plan and updated within 30 days of any changes.
[VALIDATION] IF emp_protection_implemented = TRUE AND documentation_updated = FALSE AND days_since_change > 30 THEN violation

[RULE-05] EMP protection effectiveness MUST be tested annually for critical infrastructure systems and after any modification to protective measures.
[VALIDATION] IF system_criticality = "critical" AND days_since_last_test > 365 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] EMP Risk Assessment - Systematic evaluation of EMP threats and system vulnerabilities
- [PROC-02] Protection Implementation - Installation and configuration of EMP protective measures
- [PROC-03] Effectiveness Testing - Annual validation of protective measure performance
- [PROC-04] Incident Response - Response procedures for EMP events and protection failures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: EMP incidents, facility modifications, new critical system deployment, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Critical System Deployment]
IF system_criticality = "critical"
AND system_status = "newly_deployed"
AND emp_risk_assessment_completed = FALSE
AND days_since_deployment > 90
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Missing Protection Implementation]
IF emp_protection_required = TRUE
AND protective_measures_implemented = FALSE
AND days_since_identification > 180
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Inadequate Protection Measures]
IF emp_protection_required = TRUE
AND shielding = FALSE
AND surge_suppressors = FALSE
AND transformers = FALSE
AND grounding = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Outdated Documentation]
IF emp_protection_implemented = TRUE
AND system_security_plan_updated = FALSE
AND days_since_last_change > 30
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Overdue Testing]
IF system_criticality = "critical"
AND emp_protection_implemented = TRUE
AND days_since_last_effectiveness_test > 365
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Protective measures employed against EMP damage are defined | [RULE-01], [RULE-04] |
| Protection employed for systems requiring EMP protection | [RULE-02], [RULE-03] |
| Systems and components requiring protection are defined | [RULE-01] |
| Effectiveness of protective measures is validated | [RULE-05] |