# POLICY: SC-38: Operations Security

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-38 |
| NIST Control | SC-38: Operations Security |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | operations security, OPSEC, system development lifecycle, critical information, threat analysis, vulnerability analysis |

## 1. POLICY STATEMENT
The organization SHALL implement operations security (OPSEC) controls to protect key organizational information throughout the system development life cycle. OPSEC controls MUST follow a systematic five-step process to deny potential adversaries access to critical organizational capabilities and intentions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Throughout entire SDLC |
| Development teams | YES | All phases of development |
| Third-party suppliers | YES | When accessing organizational information |
| System environments | YES | Development, test, and production |
| Organizational personnel | YES | All roles handling critical information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define OPSEC program requirements<br>• Approve OPSEC controls and countermeasures<br>• Oversee OPSEC compliance monitoring |
| System Owners | • Implement OPSEC controls for assigned systems<br>• Conduct periodic OPSEC assessments<br>• Maintain OPSEC documentation |
| Development Teams | • Apply OPSEC controls during SDLC phases<br>• Protect critical information during development<br>• Report OPSEC incidents and vulnerabilities |

## 4. RULES

[RULE-01] Organizations MUST define and document specific OPSEC controls to protect key organizational information throughout the system development life cycle.
[VALIDATION] IF opsec_controls_defined = FALSE OR opsec_documentation_exists = FALSE THEN violation

[RULE-02] OPSEC processes SHALL implement all five required steps: identification of critical information, threat analysis, vulnerability analysis, risk assessment, and countermeasure application.
[VALIDATION] IF opsec_steps_implemented < 5 THEN violation

[RULE-03] Critical information identification MUST include user identities, suppliers, supply chain processes, functional requirements, security requirements, system design specifications, testing protocols, and security control implementation details.
[VALIDATION] IF critical_info_categories_identified < 7 THEN violation

[RULE-04] OPSEC controls MUST limit sharing of critical information with suppliers, potential suppliers, and non-organizational elements through documented access restrictions.
[VALIDATION] IF external_sharing_controls = FALSE OR sharing_documentation = FALSE THEN violation

[RULE-05] Threat and vulnerability analyses MUST be conducted and documented for each system development phase to identify potential adversary capabilities.
[VALIDATION] IF threat_analysis_current = FALSE OR vulnerability_analysis_current = FALSE THEN violation

[RULE-06] OPSEC countermeasures MUST be applied based on risk assessment results and updated when system or threat landscape changes occur.
[VALIDATION] IF countermeasures_applied = FALSE OR countermeasures_current = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] OPSEC Control Definition - Systematic identification and documentation of OPSEC controls for each system
- [PROC-02] Critical Information Classification - Process for identifying and categorizing information requiring OPSEC protection
- [PROC-03] Threat and Vulnerability Assessment - Regular analysis of potential adversary capabilities and system vulnerabilities
- [PROC-04] OPSEC Countermeasure Implementation - Application and monitoring of appropriate protective measures
- [PROC-05] External Information Sharing Controls - Procedures for limiting critical information exposure to third parties

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or upon significant system changes
- Triggering events: New system deployment, threat landscape changes, security incidents, supplier changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Incomplete OPSEC Process]
IF opsec_steps_implemented < 5
AND system_in_development = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Uncontrolled External Sharing]
IF critical_information_shared = TRUE
AND recipient_type = "external"
AND sharing_controls_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Outdated Threat Analysis]
IF threat_analysis_age > 12_months
AND system_changes_occurred = TRUE
AND countermeasures_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Critical Information Categories]
IF critical_info_categories_identified < 7
AND opsec_process_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper OPSEC Implementation]
IF opsec_controls_defined = TRUE
AND opsec_steps_implemented = 5
AND threat_analysis_current = TRUE
AND countermeasures_applied = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Operations security controls defined | RULE-01 |
| Controls employed throughout SDLC | RULE-02, RULE-06 |
| Critical information protection | RULE-03, RULE-04 |
| Threat and vulnerability analysis | RULE-05 |
| Countermeasure implementation | RULE-06 |