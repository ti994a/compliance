# POLICY: SA-11.2: Threat Modeling and Vulnerability Analyses

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-11.2 |
| NIST Control | SA-11.2: Threat Modeling and Vulnerability Analyses |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | threat modeling, vulnerability analysis, developer testing, SDLC, security testing, risk assessment |

## 1. POLICY STATEMENT
All system developers, component providers, and service vendors MUST perform comprehensive threat modeling and vulnerability analyses during both development and testing phases. These analyses MUST use organization-defined contextual information, approved tools and methods, specified rigor levels, and produce evidence meeting established acceptance criteria.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All systems and components |
| Third-party Vendors | YES | Contractual requirement |
| System Integrators | YES | For custom integrations |
| COTS Products | CONDITIONAL | When customization occurs |
| Cloud Service Providers | YES | For custom configurations |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define acceptance criteria and rigor levels<br>• Approve threat modeling methodologies<br>• Review critical system analyses |
| Development Managers | • Ensure developer compliance with requirements<br>• Validate analysis completion before releases<br>• Maintain evidence repositories |
| Security Architects | • Define contextual information requirements<br>• Review threat models and vulnerability analyses<br>• Validate tool and method selections |
| Procurement Team | • Include requirements in vendor contracts<br>• Verify vendor capability during selection<br>• Monitor contract compliance |

## 4. RULES
[RULE-01] Developers MUST perform threat modeling during both development and testing phases using organization-defined contextual information including impact levels, operational environment, known threats, and acceptable risk levels.
[VALIDATION] IF development_phase = "active" OR testing_phase = "active" AND threat_model_completed = FALSE THEN violation

[RULE-02] Vulnerability analyses MUST be conducted using approved tools and methods defined by the organization for each system classification level.
[VALIDATION] IF vulnerability_analysis_tools NOT IN approved_tools_list THEN violation

[RULE-03] Threat modeling and vulnerability analyses MUST be performed at the organization-defined level of rigor based on system impact level (Low: Basic, Moderate: Comprehensive, High: Extensive).
[VALIDATION] IF system_impact_level = "High" AND analysis_rigor != "Extensive" THEN violation

[RULE-04] All analyses MUST produce evidence that meets organization-defined acceptance criteria including documentation completeness, methodology adherence, and risk coverage thresholds.
[VALIDATION] IF evidence_score < acceptance_threshold THEN violation

[RULE-05] Threat modeling and vulnerability analyses MUST be updated when design or implementation changes occur during development.
[VALIDATION] IF design_change_date > last_analysis_date AND days_difference > 30 THEN violation

[RULE-06] Third-party developers MUST provide threat modeling and vulnerability analysis deliverables before system acceptance.
[VALIDATION] IF vendor_type = "third_party" AND deliverables_received = FALSE AND acceptance_pending = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Threat Modeling Methodology - Standardized approach using STRIDE or equivalent framework
- [PROC-02] Vulnerability Analysis Standards - Tools, frequency, and reporting requirements
- [PROC-03] Evidence Review Process - Validation of deliverables against acceptance criteria
- [PROC-04] Vendor Compliance Monitoring - Tracking and verification of third-party analyses
- [PROC-05] Analysis Update Triggers - Change management integration requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, new threat intelligence, regulatory changes, significant methodology updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Development Phase Analysis]
IF development_phase = "active"
AND threat_model_status = "not_started"
AND project_milestone = "design_complete"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Outdated Analysis After Changes]
IF major_design_change = TRUE
AND change_date > last_threat_model_date
AND days_since_change > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Inadequate Tool Usage]
IF system_impact_level = "High"
AND vulnerability_scan_tool NOT IN approved_high_impact_tools
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Missing Vendor Deliverables]
IF vendor_type = "third_party"
AND contract_requires_threat_model = TRUE
AND deliverable_status = "not_received"
AND acceptance_date < current_date + 30_days
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Insufficient Analysis Rigor]
IF system_classification = "Moderate"
AND analysis_depth = "Basic"
AND required_depth = "Comprehensive"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer threat modeling during development | [RULE-01] |
| Developer vulnerability analysis during development | [RULE-01], [RULE-02] |
| Developer threat modeling during testing | [RULE-01] |
| Developer vulnerability analysis during testing | [RULE-01], [RULE-02] |
| Use of defined tools and methods | [RULE-02] |
| Appropriate rigor level | [RULE-03] |
| Evidence meeting acceptance criteria | [RULE-04] |
| Analysis updates for changes | [RULE-05] |
| Third-party compliance | [RULE-06] |