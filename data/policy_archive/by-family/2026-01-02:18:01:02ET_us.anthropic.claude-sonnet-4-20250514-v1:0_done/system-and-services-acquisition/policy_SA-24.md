# POLICY: SA-24: Design For Cyber Resiliency

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-24 |
| NIST Control | SA-24: Design For Cyber Resiliency |
| Version | 1.0 |
| Owner | Chief Technology Officer |
| Keywords | cyber resiliency, system design, risk management, business continuity, threat response |

## 1. POLICY STATEMENT
All organizational systems, system components, and system services MUST be designed with cyber resiliency capabilities to maintain essential functions during adversity and recover from cyber incidents. The organization SHALL define and implement cyber resiliency goals, objectives, techniques, implementation approaches, and design principles as part of the risk management and systems security engineering processes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Mission-critical systems | YES | All systems supporting essential business functions |
| High-value assets | YES | Systems containing sensitive data or critical infrastructure |
| Development projects | YES | New systems and major system modifications |
| Cloud services | YES | Both public and private cloud implementations |
| Legacy systems | CONDITIONAL | During major updates or security reviews |
| Vendor-provided services | YES | Must meet resiliency requirements in contracts |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Architects | • Define cyber resiliency requirements for system designs<br>• Implement resiliency design principles<br>• Document resiliency capabilities in system specifications |
| Risk Management Team | • Establish organizational cyber resiliency goals and objectives<br>• Integrate resiliency requirements into risk assessments<br>• Monitor resiliency effectiveness |
| Development Teams | • Implement cyber resiliency techniques in system development<br>• Follow secure coding practices for resilient systems<br>• Conduct resiliency testing during development |

## 4. RULES
[RULE-01] Organizations MUST define cyber resiliency goals that address mission continuity, asset protection, and recovery capabilities.
[VALIDATION] IF system_classification = "mission_critical" AND resiliency_goals = "undefined" THEN violation

[RULE-02] Cyber resiliency objectives SHALL be documented for each system based on business impact analysis and threat modeling.
[VALIDATION] IF system_deployed = TRUE AND resiliency_objectives = "not_documented" THEN violation

[RULE-03] System designs MUST incorporate at least three cyber resiliency techniques appropriate to the system's risk profile and mission criticality.
[VALIDATION] IF system_risk_level = "high" AND resiliency_techniques < 3 THEN violation

[RULE-04] Implementation approaches for cyber resiliency SHALL be integrated into the systems security engineering process and documented in system security plans.
[VALIDATION] IF system_security_plan = "approved" AND resiliency_implementation = "not_documented" THEN violation

[RULE-05] Cyber resiliency design principles MUST be applied during system specification, design, development, and modification phases.
[VALIDATION] IF development_phase = "active" AND resiliency_principles = "not_applied" THEN violation

[RULE-06] Resiliency requirements SHALL be included in vendor contracts and service level agreements for externally provided services.
[VALIDATION] IF service_type = "external" AND contract_resiliency_clause = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Cyber Resiliency Assessment - Evaluate system resiliency capabilities against defined goals
- [PROC-02] Resiliency Design Review - Review system designs for resiliency implementation
- [PROC-03] Resiliency Testing - Conduct chaos engineering and failure scenario testing
- [PROC-04] Vendor Resiliency Evaluation - Assess third-party service resiliency capabilities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 18 months
- Triggering events: Major cyber incidents, significant threat landscape changes, business model changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Mission Critical System Without Resiliency Goals]
IF system_classification = "mission_critical"
AND resiliency_goals = "undefined"
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: New Development Project]
IF project_phase = "design"
AND system_risk_level = "high"
AND resiliency_techniques_count >= 3
AND design_principles_applied = TRUE
THEN compliance = TRUE

[SCENARIO-03: Vendor Service Contract]
IF service_provider = "external"
AND contract_signed = TRUE
AND resiliency_requirements = "not_specified"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Legacy System Update]
IF system_age > 5_years
AND major_modification = TRUE
AND resiliency_assessment_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Cloud Migration Project]
IF deployment_model = "cloud"
AND resiliency_objectives = "documented"
AND implementation_approaches = "defined"
AND security_plan_updated = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Cyber resiliency goals are defined | [RULE-01] |
| Cyber resiliency objectives are defined | [RULE-02] |
| Cyber resiliency techniques are defined | [RULE-03] |
| Implementation approaches are defined | [RULE-04] |
| Design principles are defined | [RULE-05] |
| Goals implemented in risk management process | [RULE-01], [RULE-04] |
| Objectives implemented in engineering process | [RULE-02], [RULE-05] |
| Techniques implemented in engineering process | [RULE-03], [RULE-05] |
| Implementation approaches integrated | [RULE-04], [RULE-06] |
| Design principles applied | [RULE-05] |