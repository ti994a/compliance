# POLICY: SA-22: Unsupported System Components

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-22 |
| NIST Control | SA-22: Unsupported System Components |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | unsupported components, system replacement, vendor support, alternative support, end-of-life |

## 1. POLICY STATEMENT
Organizations must replace system components when vendor support ends or establish documented alternative support mechanisms. Unsupported components create security vulnerabilities and must be managed through replacement, alternative support arrangements, or risk-based isolation measures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT Systems | YES | Including cloud, on-premises, and hybrid |
| Software Components | YES | Operating systems, applications, middleware |
| Hardware Components | YES | Servers, network devices, endpoints |
| Firmware | YES | All device firmware and embedded systems |
| Third-party Services | YES | SaaS, PaaS components with support dependencies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Asset Manager | • Monitor vendor support lifecycles<br>• Maintain component inventory with support status<br>• Initiate replacement processes |
| CISO | • Approve exceptions for unsupported components<br>• Define risk mitigation requirements<br>• Oversee alternative support arrangements |
| System Owners | • Identify business-critical unsupported components<br>• Implement approved mitigation measures<br>• Coordinate replacement activities |

## 4. RULES

[RULE-01] System components MUST be replaced within 90 days after vendor support termination unless a documented exception is approved.
[VALIDATION] IF support_end_date < current_date - 90_days AND replacement_completed = FALSE AND exception_approved = FALSE THEN violation

[RULE-02] Organizations MUST maintain an inventory of all system components with current support status and end-of-support dates.
[VALIDATION] IF component_in_inventory = FALSE OR support_status = "unknown" OR end_of_support_date = "unknown" THEN violation

[RULE-03] Exceptions for continued use of unsupported components MUST include documented business justification, risk assessment, and compensating controls.
[VALIDATION] IF component_supported = FALSE AND (business_justification = NULL OR risk_assessment = NULL OR compensating_controls = NULL) THEN violation

[RULE-04] Alternative support arrangements for unsupported components MUST be established through contractual agreements or in-house capabilities before vendor support ends.
[VALIDATION] IF support_end_date <= current_date + 30_days AND alternative_support_documented = FALSE AND replacement_planned = FALSE THEN violation

[RULE-05] Unsupported components SHALL NOT be connected to public networks or uncontrolled network segments without additional isolation controls.
[VALIDATION] IF component_supported = FALSE AND network_exposure = "public" AND isolation_controls = FALSE THEN critical_violation

[RULE-06] Risk assessments for unsupported components MUST be reviewed and updated every 6 months or when threat landscape changes.
[VALIDATION] IF component_supported = FALSE AND last_risk_review > 180_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Lifecycle Management - Track vendor support timelines and plan replacements
- [PROC-02] Exception Request Process - Document and approve continued use of unsupported components
- [PROC-03] Alternative Support Evaluation - Assess and establish third-party or in-house support options
- [PROC-04] Risk Mitigation Implementation - Deploy compensating controls for unsupported components

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 6 months
- Triggering events: New unsupported components identified, security incidents involving unsupported components, vendor support policy changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Operating System End-of-Life]
IF component_type = "operating_system"
AND support_end_date < current_date
AND replacement_completed = FALSE
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Approved Exception with Controls]
IF component_supported = FALSE
AND exception_approved = TRUE
AND compensating_controls_implemented = TRUE
AND network_isolation = TRUE
THEN compliance = TRUE

[SCENARIO-03: Alternative Support Arrangement]
IF vendor_support_available = FALSE
AND alternative_support_contract = TRUE
AND support_capabilities_documented = TRUE
THEN compliance = TRUE

[SCENARIO-04: Unsupported Component on Public Network]
IF component_supported = FALSE
AND network_exposure = "internet_facing"
AND isolation_controls = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Missing Component Inventory]
IF system_component_exists = TRUE
AND component_in_inventory = FALSE
AND support_status = "unknown"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Replace unsupported components | RULE-01, RULE-04 |
| Track component support status | RULE-02 |
| Document alternative support options | RULE-03, RULE-04 |
| Implement risk mitigation for exceptions | RULE-03, RULE-05, RULE-06 |