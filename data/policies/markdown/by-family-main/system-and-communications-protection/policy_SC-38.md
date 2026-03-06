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
The organization SHALL implement a systematic Operations Security (OPSEC) program to identify, control, and protect critical organizational information throughout the system development life cycle. OPSEC controls MUST deny potential adversaries access to information about organizational capabilities, intentions, and sensitive activities through a structured five-step process and appropriate countermeasures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Throughout entire SDLC |
| Development Teams | YES | All phases of development |
| Third-party Suppliers | YES | When accessing critical information |
| System Operators | YES | Production and testing environments |
| Business Partners | CONDITIONAL | Only when handling critical information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define OPSEC program requirements<br>• Approve critical information classifications<br>• Oversee threat and vulnerability assessments |
| System Owners | • Implement OPSEC controls for their systems<br>• Identify critical information within their domain<br>• Apply appropriate countermeasures |
| Development Teams | • Follow OPSEC procedures during SDLC<br>• Protect design specifications and requirements<br>• Limit information sharing with non-organizational elements |

## 4. RULES
[RULE-01] Organizations MUST implement a five-step OPSEC process: identification of critical information, analysis of threats, analysis of vulnerabilities, assessment of risks, and application of appropriate countermeasures.
[VALIDATION] IF opsec_process_steps < 5 OR any_step_missing = TRUE THEN violation

[RULE-02] Critical organizational information MUST be formally identified and classified before system development activities commence.
[VALIDATION] IF development_started = TRUE AND critical_info_identified = FALSE THEN violation

[RULE-03] OPSEC controls MUST be applied to both organizational systems and their operating environments throughout the entire SDLC.
[VALIDATION] IF sdlc_phase IN [planning, design, implementation, testing, deployment, maintenance] AND opsec_controls_applied = FALSE THEN violation

[RULE-04] Information sharing with suppliers, potential suppliers, and non-organizational elements MUST be limited and controlled through documented procedures.
[VALIDATION] IF external_sharing = TRUE AND (approval_documented = FALSE OR controls_applied = FALSE) THEN violation

[RULE-05] Threat and vulnerability assessments MUST be conducted and documented as part of the OPSEC process.
[VALIDATION] IF threat_assessment_current = FALSE OR vulnerability_assessment_current = FALSE THEN violation

[RULE-06] OPSEC countermeasures MUST be implemented based on risk assessment results and SHALL be reviewed annually.
[VALIDATION] IF countermeasures_implemented = FALSE OR last_review > 365_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Critical Information Identification - Systematic process to identify and classify information critical to mission and business functions
- [PROC-02] Threat Analysis Methodology - Standardized approach for analyzing potential adversaries and their capabilities
- [PROC-03] Vulnerability Assessment Process - Regular evaluation of information exposure points and weaknesses
- [PROC-04] External Information Sharing Controls - Approval and monitoring procedures for sharing information with non-organizational entities
- [PROC-05] OPSEC Countermeasure Implementation - Selection and deployment of appropriate protective measures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or when significant changes occur
- Triggering events: Security incidents involving information disclosure, new system deployments, major SDLC phase transitions, changes in threat landscape

## 7. SCENARIO PATTERNS
[SCENARIO-01: Incomplete OPSEC Process]
IF opsec_steps_implemented < 5
AND system_in_development = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Uncontrolled External Sharing]
IF information_shared_externally = TRUE
AND sharing_approval = FALSE
AND information_classification = "critical"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Missing Threat Assessment]
IF threat_assessment_exists = FALSE
AND system_sdlc_phase IN ["design", "implementation", "testing"]
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Outdated OPSEC Controls]
IF opsec_controls_last_updated > 365_days
AND threat_landscape_changed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper OPSEC Implementation]
IF critical_info_identified = TRUE
AND five_step_process_complete = TRUE
AND countermeasures_applied = TRUE
AND external_sharing_controlled = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Operations security controls defined | [RULE-01], [RULE-02] |
| Controls employed throughout SDLC | [RULE-03], [RULE-06] |
| Critical information protection | [RULE-02], [RULE-04] |
| Threat and vulnerability analysis | [RULE-05] |
| Countermeasure implementation | [RULE-06] |