# POLICY: SA-3: System Development Life Cycle

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-3 |
| NIST Control | SA-3: System Development Life Cycle |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | SDLC, development, security engineering, privacy engineering, risk management, roles responsibilities |

## 1. POLICY STATEMENT
All organizational systems MUST be acquired, developed, and managed using a defined system development life cycle (SDLC) that incorporates information security and privacy considerations throughout all phases. Security and privacy roles and responsibilities MUST be clearly defined, documented, and assigned to qualified individuals throughout the SDLC process.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT Systems | YES | Including cloud, on-premises, hybrid |
| Custom Applications | YES | Internal and vendor-developed |
| COTS/SaaS Solutions | YES | Configuration and integration activities |
| Legacy Systems | YES | During major updates or migrations |
| Third-party Vendors | YES | When involved in system development |
| All Business Units | YES | Systems supporting business operations |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Define security and privacy requirements<br>• Approve SDLC phase gates<br>• Ensure adequate resources for security activities |
| Security Architect | • Integrate security controls into system design<br>• Review security architecture at each SDLC phase<br>• Validate security requirements implementation |
| Privacy Engineer | • Conduct privacy impact assessments<br>• Design privacy-preserving system features<br>• Ensure privacy requirements compliance |
| Development Team | • Implement security and privacy controls<br>• Follow secure coding practices<br>• Participate in security testing activities |

## 4. RULES

[RULE-01] All systems MUST follow the organization's defined SDLC methodology that incorporates security and privacy considerations in each phase.
[VALIDATION] IF system_development = TRUE AND sdlc_methodology_followed = FALSE THEN violation

[RULE-02] Security and privacy roles and responsibilities MUST be documented and assigned before SDLC initiation phase completion.
[VALIDATION] IF sdlc_phase = "initiation" AND (security_roles_documented = FALSE OR privacy_roles_documented = FALSE) THEN violation

[RULE-03] Qualified personnel with appropriate security and privacy expertise MUST be assigned to SDLC activities based on system categorization.
[VALIDATION] IF system_impact_level = "high" AND (security_architect_assigned = FALSE OR privacy_engineer_assigned = FALSE) THEN critical_violation

[RULE-04] Security and privacy risk management processes MUST be integrated into all SDLC phase gate reviews.
[VALIDATION] IF phase_gate_review = TRUE AND (security_risk_assessment = FALSE OR privacy_risk_assessment = FALSE) THEN violation

[RULE-05] SDLC documentation MUST include security and privacy requirements traceability from requirements through implementation and testing.
[VALIDATION] IF sdlc_documentation_complete = TRUE AND requirements_traceability = FALSE THEN violation

[RULE-06] Third-party vendors involved in system development MUST demonstrate compliance with organizational SDLC security and privacy requirements.
[VALIDATION] IF third_party_involved = TRUE AND vendor_sdlc_compliance_verified = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] SDLC Security Integration - Define security activities and deliverables for each SDLC phase
- [PROC-02] Privacy by Design Implementation - Integrate privacy requirements into system design and development
- [PROC-03] Role Assignment and Training - Assign qualified personnel and ensure adequate security/privacy training
- [PROC-04] Risk Management Integration - Incorporate security and privacy risk assessments into phase gates
- [PROC-05] Vendor SDLC Compliance - Verify third-party adherence to organizational SDLC requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or after major SDLC methodology changes
- Triggering events: New regulatory requirements, significant security incidents, major organizational changes, technology stack changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: High-Impact System Without Security Architect]
IF system_impact_level = "high"
AND security_architect_assigned = FALSE
AND sdlc_phase IN ["design", "development", "implementation"]
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Missing Privacy Role Assignment]
IF system_processes_pii = TRUE
AND privacy_engineer_assigned = FALSE
AND sdlc_phase = "requirements"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Phase Gate Without Risk Assessment]
IF phase_gate_review = TRUE
AND phase IN ["design", "implementation", "deployment"]
AND (security_risk_assessment_completed = FALSE OR privacy_risk_assessment_completed = FALSE)
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Vendor Non-Compliance]
IF third_party_development = TRUE
AND vendor_sdlc_compliance_verified = FALSE
AND development_started = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Requirements Traceability Gap]
IF system_categorization = "moderate" OR system_categorization = "high"
AND security_requirements_traced = FALSE
AND sdlc_phase = "testing"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| System acquired/developed using defined SDLC with security considerations | RULE-01 |
| System acquired/developed using defined SDLC with privacy considerations | RULE-01 |
| Information security roles and responsibilities defined and documented | RULE-02 |
| Privacy roles and responsibilities defined and documented | RULE-02 |
| Individuals with information security roles identified | RULE-03 |
| Individuals with privacy roles identified | RULE-03 |
| Security risk management processes integrated into SDLC | RULE-04 |
| Privacy risk management processes integrated into SDLC | RULE-04 |