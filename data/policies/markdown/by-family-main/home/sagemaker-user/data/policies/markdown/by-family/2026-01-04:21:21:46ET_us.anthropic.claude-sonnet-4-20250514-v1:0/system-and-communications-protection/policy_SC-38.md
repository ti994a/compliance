# POLICY: SC-38: Operations Security

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-38 |
| NIST Control | SC-38: Operations Security |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | operations security, OPSEC, critical information, threat analysis, vulnerability analysis, countermeasures, SDLC |

## 1. POLICY STATEMENT
The organization SHALL implement operations security (OPSEC) controls to protect key organizational information throughout the system development life cycle by identifying critical information, analyzing threats and vulnerabilities, assessing risks, and applying appropriate countermeasures. OPSEC controls MUST prevent potential adversaries from obtaining information about organizational capabilities, intentions, and sensitive activities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Throughout entire SDLC |
| Development Teams | YES | All phases of development |
| Third-party Suppliers | YES | When accessing organizational information |
| Contractors | YES | When involved in system development |
| Testing Environments | YES | Including evaluation protocols |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define OPSEC controls framework<br>• Approve critical information classifications<br>• Oversee OPSEC program implementation |
| System Owners | • Implement OPSEC controls for assigned systems<br>• Conduct regular threat and vulnerability assessments<br>• Apply appropriate countermeasures |
| Development Teams | • Follow OPSEC procedures during SDLC<br>• Protect design specifications and requirements<br>• Limit information sharing with unauthorized parties |

## 4. RULES
[RULE-01] Organizations MUST define and document operations security controls to protect key organizational information throughout the system development life cycle.
[VALIDATION] IF opsec_controls_defined = FALSE OR opsec_documentation = "incomplete" THEN violation

[RULE-02] The organization SHALL implement a five-step OPSEC process including: identification of critical information, threat analysis, vulnerability analysis, risk assessment, and countermeasure application.
[VALIDATION] IF opsec_steps_implemented < 5 OR process_documentation = "missing" THEN violation

[RULE-03] Critical organizational information including user identities, suppliers, functional requirements, security requirements, system designs, and testing protocols MUST be identified and protected.
[VALIDATION] IF critical_info_inventory = "incomplete" OR protection_controls = "undefined" THEN violation

[RULE-04] Information sharing with suppliers, potential suppliers, and non-organizational elements MUST be limited and controlled through documented procedures.
[VALIDATION] IF third_party_access = TRUE AND access_controls = "undefined" THEN violation

[RULE-05] OPSEC controls MUST be applied to organizational systems and their operating environments throughout all SDLC phases.
[VALIDATION] IF sdlc_phase_coverage < 100% OR opsec_controls_applied = FALSE THEN violation

[RULE-06] Threat and vulnerability assessments MUST be conducted regularly to support OPSEC risk assessments and countermeasure selection.
[VALIDATION] IF threat_assessment_age > 365_days OR vulnerability_assessment_age > 180_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Critical Information Identification - Process for identifying and classifying key organizational information
- [PROC-02] Threat Analysis - Systematic analysis of potential adversaries and their capabilities
- [PROC-03] Vulnerability Assessment - Regular evaluation of information exposure risks
- [PROC-04] Risk Assessment - Assessment of risks to critical information throughout SDLC
- [PROC-05] Countermeasure Implementation - Application and monitoring of protective measures
- [PROC-06] Third-party Information Sharing - Controls for external information sharing

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, system changes, new threats, supplier changes, SDLC methodology updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Design Document Sharing]
IF document_type = "system_design"
AND shared_with_external = TRUE
AND approval_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Critical Information Inventory]
IF system_status = "in_development"
AND critical_info_identified = FALSE
AND sdlc_phase > "requirements"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Outdated Threat Assessment]
IF threat_assessment_last_update > 365_days
AND system_classification >= "moderate"
AND countermeasures_current = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Supplier Access Without Controls]
IF supplier_access = TRUE
AND opsec_controls_applied = FALSE
AND critical_info_accessible = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Complete OPSEC Implementation]
IF opsec_steps_completed = 5
AND critical_info_protected = TRUE
AND assessments_current = TRUE
AND countermeasures_active = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Operations security controls defined | [RULE-01] |
| OPSEC controls employed throughout SDLC | [RULE-02], [RULE-05] |
| Critical information identification | [RULE-03] |
| Information sharing controls | [RULE-04] |
| Threat and vulnerability analysis | [RULE-06] |