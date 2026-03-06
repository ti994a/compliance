# POLICY: SA-3: System Development Life Cycle

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-3 |
| NIST Control | SA-3: System Development Life Cycle |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | SDLC, development, security engineering, privacy engineering, roles, responsibilities, risk management, enterprise architecture |

## 1. POLICY STATEMENT
All organizational systems MUST be acquired, developed, and managed using a defined system development life cycle (SDLC) that incorporates information security and privacy considerations throughout all phases. Security and privacy roles and responsibilities MUST be clearly defined, documented, and assigned to qualified personnel who are integrated into SDLC activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Projects | YES | All phases from planning to disposal |
| Third-Party Development | YES | Contractual requirements apply |
| COTS/SaaS Acquisitions | YES | Evaluation and integration phases |
| System Modifications | YES | Major changes requiring SDLC process |
| Prototype/POC Systems | CONDITIONAL | If intended for production use |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Ensure SDLC process compliance<br>• Approve security/privacy requirements<br>• Validate role assignments |
| Security Architect | • Define security requirements in SDLC<br>• Review design and implementation<br>• Conduct security assessments |
| Privacy Officer | • Define privacy requirements in SDLC<br>• Review data handling practices<br>• Conduct privacy impact assessments |
| Development Manager | • Implement SDLC security/privacy controls<br>• Ensure qualified personnel assignments<br>• Coordinate with security/privacy teams |

## 4. RULES

[RULE-01] All systems MUST follow a documented SDLC process that incorporates security and privacy considerations in each phase.
[VALIDATION] IF system_development = TRUE AND sdlc_security_integration = FALSE THEN violation

[RULE-02] Security and privacy roles and responsibilities MUST be defined and documented for each SDLC phase before project initiation.
[VALIDATION] IF project_status = "initiated" AND roles_documented = FALSE THEN violation

[RULE-03] Qualified personnel MUST be identified and assigned to security and privacy roles within 5 business days of project approval.
[VALIDATION] IF project_approved = TRUE AND personnel_assigned = FALSE AND days_elapsed > 5 THEN violation

[RULE-04] Security and privacy risk management processes MUST be integrated into all SDLC activities and documented in project plans.
[VALIDATION] IF sdlc_activity = TRUE AND risk_management_integrated = FALSE THEN violation

[RULE-05] Security and privacy requirements MUST be established during the requirements phase and traceable through implementation.
[VALIDATION] IF requirements_phase = "complete" AND security_privacy_requirements = "undefined" THEN violation

[RULE-06] Role-based security and privacy training MUST be completed by assigned personnel before engaging in SDLC activities.
[VALIDATION] IF sdlc_role_assigned = TRUE AND training_completed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] SDLC Security Integration Procedure - Defines how security controls are incorporated at each SDLC phase
- [PROC-02] Privacy-by-Design Implementation Procedure - Ensures privacy considerations are built into system design
- [PROC-03] Role Assignment and Qualification Procedure - Establishes criteria for security/privacy role assignments
- [PROC-04] Risk Management Integration Procedure - Details integration of risk management into SDLC activities

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 2 years
- Triggering events: Major SDLC process changes, significant security incidents, regulatory changes, enterprise architecture updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: New System Development]
IF system_type = "new_development"
AND sdlc_process_defined = TRUE
AND security_privacy_integrated = TRUE
AND qualified_personnel_assigned = TRUE
THEN compliance = TRUE

[SCENARIO-02: Third-Party Development Missing Security Integration]
IF development_type = "third_party"
AND contract_includes_security_requirements = FALSE
AND sdlc_security_integration = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Personnel Assignment Delay]
IF project_approved = TRUE
AND security_privacy_roles_assigned = FALSE
AND days_since_approval > 5
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Legacy System Modification]
IF system_type = "legacy_modification"
AND modification_scope = "major"
AND sdlc_process_followed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Training Requirements Not Met]
IF personnel_assigned_to_sdlc = TRUE
AND role_based_training_completed = FALSE
AND sdlc_activities_started = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| SDLC incorporates information security considerations | [RULE-01] |
| SDLC incorporates privacy considerations | [RULE-01] |
| Information security roles defined and documented | [RULE-02] |
| Privacy roles defined and documented | [RULE-02] |
| Security personnel identified | [RULE-03] |
| Privacy personnel identified | [RULE-03] |
| Security risk management integrated into SDLC | [RULE-04] |
| Privacy risk management integrated into SDLC | [RULE-04] |