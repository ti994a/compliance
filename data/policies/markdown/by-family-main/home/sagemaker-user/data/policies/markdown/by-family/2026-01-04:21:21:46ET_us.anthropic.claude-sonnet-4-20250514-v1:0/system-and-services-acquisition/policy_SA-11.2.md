# POLICY: SA-11.2: Threat Modeling and Vulnerability Analyses

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-11.2 |
| NIST Control | SA-11.2: Threat Modeling and Vulnerability Analyses |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | threat modeling, vulnerability analysis, developer requirements, SDLC security, testing evaluation |

## 1. POLICY STATEMENT
All system, component, and service developers MUST perform comprehensive threat modeling and vulnerability analyses during both development and testing phases using organizationally-defined contextual information, tools, and acceptance criteria. These analyses MUST account for design changes and implementation deviations that occur throughout the development lifecycle.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All systems developed internally |
| External Vendors/Contractors | YES | All contracted development work |
| COTS Products | CONDITIONAL | When customization/integration occurs |
| Cloud Services | YES | Custom configurations and integrations |
| System Components | YES | All security-relevant components |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Development Teams | • Conduct threat modeling and vulnerability analyses<br>• Use approved tools and methods<br>• Produce required evidence and documentation |
| Security Architecture Team | • Define contextual information requirements<br>• Approve tools and methods<br>• Establish acceptance criteria |
| Procurement Office | • Include requirements in contracts<br>• Verify compliance before acceptance<br>• Maintain vendor compliance records |

## 4. RULES
[RULE-01] Developers MUST perform threat modeling during initial development using defined contextual information including impact levels, operational environment, known threats, and acceptable risk levels.
[VALIDATION] IF development_phase = "active" AND threat_model_completed = FALSE THEN violation

[RULE-02] Developers MUST perform vulnerability analyses during initial development using the same contextual information as threat modeling.
[VALIDATION] IF development_phase = "active" AND vulnerability_analysis_completed = FALSE THEN violation

[RULE-03] Developers MUST perform updated threat modeling during testing and evaluation phases to account for design and implementation changes.
[VALIDATION] IF testing_phase = "active" AND updated_threat_model = FALSE AND design_changes = TRUE THEN violation

[RULE-04] Developers MUST perform updated vulnerability analyses during testing and evaluation phases when implementation deviations occur.
[VALIDATION] IF testing_phase = "active" AND updated_vuln_analysis = FALSE AND implementation_changes = TRUE THEN violation

[RULE-05] All threat modeling and vulnerability analyses MUST use organizationally-approved tools and methods as defined in the security architecture standards.
[VALIDATION] IF analysis_tools NOT IN approved_tools_list THEN violation

[RULE-06] Analyses MUST be conducted at the organizationally-defined level of rigor appropriate for the system's risk classification.
[VALIDATION] IF analysis_depth < required_depth_for_risk_level THEN violation

[RULE-07] All analyses MUST produce evidence that meets organizationally-defined acceptance criteria before system acceptance.
[VALIDATION] IF evidence_quality < acceptance_criteria THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Threat Modeling Methodology - Standardized approach for conducting threat analysis
- [PROC-02] Vulnerability Analysis Process - Systematic vulnerability identification and assessment
- [PROC-03] Evidence Review and Acceptance - Validation of analysis outputs and documentation
- [PROC-04] Tool Approval and Management - Maintenance of approved analysis tools and methods

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Bi-annually
- Triggering events: Major security incidents, new threat intelligence, tool updates, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Development Without Threat Model]
IF development_status = "in_progress"
AND threat_model_status = "not_started"
AND development_progress > 25%
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Testing Phase Missing Updates]
IF testing_phase = "active"
AND design_changes = TRUE
AND threat_model_last_updated < design_change_date
AND days_since_change > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Unapproved Analysis Tools]
IF analysis_tool_used NOT IN approved_tools_list
AND analysis_status = "completed"
AND security_classification >= "Moderate"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Insufficient Evidence Quality]
IF evidence_completeness < acceptance_threshold
AND system_ready_for_deployment = TRUE
AND risk_level = "High"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Vendor Compliance Gap]
IF vendor_type = "external"
AND contract_includes_sa11_2 = TRUE
AND threat_model_delivered = FALSE
AND delivery_date_passed = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Threat modeling during development with contextual information | RULE-01 |
| Vulnerability analysis during development with contextual information | RULE-02 |
| Threat modeling during testing/evaluation | RULE-03 |
| Vulnerability analysis during testing/evaluation | RULE-04 |
| Use of approved tools and methods | RULE-05 |
| Appropriate analysis rigor level | RULE-06 |
| Evidence meeting acceptance criteria | RULE-07 |