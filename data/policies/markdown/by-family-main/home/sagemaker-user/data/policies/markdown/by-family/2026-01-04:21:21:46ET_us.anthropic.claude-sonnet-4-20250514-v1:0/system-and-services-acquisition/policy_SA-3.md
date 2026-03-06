# POLICY: SA-3: System Development Life Cycle

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-3 |
| NIST Control | SA-3: System Development Life Cycle |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | SDLC, security engineering, privacy engineering, risk management, roles responsibilities, system acquisition |

## 1. POLICY STATEMENT
All systems SHALL be acquired, developed, and managed using a defined system development life cycle (SDLC) that incorporates information security and privacy considerations throughout all phases. Security and privacy roles, responsibilities, and risk management processes MUST be formally integrated into SDLC activities from initiation through disposal.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, hybrid, and on-premises |
| Third-party Developed Systems | YES | Vendor SDLC must meet requirements |
| Commercial Off-the-Shelf (COTS) | CONDITIONAL | Integration and customization phases |
| System Components | YES | Hardware, software, firmware |
| Legacy Systems | YES | During major updates or refreshes |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Ensure SDLC compliance for assigned systems<br>• Approve security and privacy requirements<br>• Oversee integration of risk management processes |
| Security Architect | • Define security requirements for each SDLC phase<br>• Review and approve security designs<br>• Conduct security assessments throughout SDLC |
| Privacy Engineer | • Integrate privacy requirements into SDLC<br>• Conduct privacy impact assessments<br>• Ensure data protection controls implementation |
| Development Teams | • Follow secure coding practices<br>• Implement required security and privacy controls<br>• Document security and privacy decisions |

## 4. RULES
[RULE-01] All systems MUST follow a documented SDLC process that explicitly incorporates security and privacy considerations in each phase.
[VALIDATION] IF system_development = TRUE AND documented_sdlc = FALSE THEN critical_violation

[RULE-02] Security and privacy roles and responsibilities MUST be formally defined and documented for each SDLC phase within 30 days of SDLC initiation.
[VALIDATION] IF sdlc_initiated = TRUE AND roles_documented_days > 30 THEN violation

[RULE-03] Qualified security and privacy personnel MUST be assigned to SDLC activities before design phase begins.
[VALIDATION] IF design_phase_started = TRUE AND security_personnel_assigned = FALSE THEN critical_violation

[RULE-04] Organizational risk management processes MUST be integrated into all SDLC phases with documented risk assessments.
[VALIDATION] IF sdlc_phase_complete = TRUE AND risk_assessment_documented = FALSE THEN violation

[RULE-05] Third-party vendors MUST demonstrate SDLC compliance through documentation review and assessment before contract award.
[VALIDATION] IF vendor_selected = TRUE AND sdlc_compliance_verified = FALSE THEN critical_violation

[RULE-06] Security and privacy requirements MUST be defined and approved before system design phase completion.
[VALIDATION] IF design_phase_complete = TRUE AND security_requirements_approved = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] SDLC Security Integration Procedure - Defines security activities for each SDLC phase
- [PROC-02] Privacy Engineering Process - Incorporates privacy requirements throughout SDLC
- [PROC-03] Risk Management Integration - Integrates organizational risk processes into SDLC
- [PROC-04] Vendor SDLC Assessment - Evaluates third-party SDLC compliance
- [PROC-05] Role Assignment and Training - Assigns and trains personnel in SDLC security roles

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Bi-annually
- Triggering events: Major system incidents, regulatory changes, SDLC methodology updates, failed assessments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Agile Development Without Security Integration]
IF development_methodology = "agile"
AND security_integrated_sprints = FALSE
AND system_criticality >= "moderate"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Third-party System Acquisition]
IF system_source = "third_party"
AND vendor_sdlc_assessed = TRUE
AND security_requirements_defined = TRUE
AND privacy_requirements_defined = TRUE
THEN compliance = TRUE

[SCENARIO-03: Legacy System Major Update]
IF system_type = "legacy"
AND update_scope = "major"
AND current_sdlc_applied = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: COTS Implementation]
IF system_type = "COTS"
AND customization_required = TRUE
AND sdlc_applied_customization = TRUE
AND security_roles_assigned = TRUE
THEN compliance = TRUE

[SCENARIO-05: Emergency System Deployment]
IF deployment_type = "emergency"
AND security_requirements_waived = TRUE
AND risk_acceptance_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System acquired/developed using defined SDLC with security considerations | [RULE-01] |
| System acquired/developed using defined SDLC with privacy considerations | [RULE-01] |
| Information security roles and responsibilities defined and documented | [RULE-02] |
| Privacy roles and responsibilities defined and documented | [RULE-02] |
| Individuals with security roles and responsibilities identified | [RULE-03] |
| Individuals with privacy roles and responsibilities identified | [RULE-03] |
| Security risk management processes integrated into SDLC activities | [RULE-04] |
| Privacy risk management processes integrated into SDLC activities | [RULE-04] |