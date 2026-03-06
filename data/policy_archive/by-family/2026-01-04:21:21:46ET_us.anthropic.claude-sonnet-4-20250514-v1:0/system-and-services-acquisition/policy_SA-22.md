# POLICY: SA-22: Unsupported System Components

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-22 |
| NIST Control | SA-22: Unsupported System Components |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | unsupported components, vendor support, patches, firmware updates, replacement parts, maintenance contracts, alternative support |

## 1. POLICY STATEMENT
System components MUST be replaced when support is no longer available from the original developer, vendor, or manufacturer. When replacement is not feasible for critical mission systems, alternative support sources including in-house support MUST be established with documented risk mitigation measures.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT Systems | YES | Including cloud, on-premises, and hybrid |
| Third-party Components | YES | Software, firmware, hardware components |
| Legacy Systems | YES | Special consideration for mission-critical |
| Development Tools | YES | Including compilers, frameworks, libraries |
| Network Equipment | YES | Routers, switches, firewalls, appliances |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Asset Manager | • Maintain inventory of system components and support status<br>• Monitor vendor support lifecycle announcements<br>• Coordinate component replacement activities |
| Security Team | • Assess security risks of unsupported components<br>• Review and approve alternative support arrangements<br>• Implement isolation measures for unsupported systems |
| System Owners | • Identify critical components requiring continued operation<br>• Justify business need for retaining unsupported components<br>• Implement approved risk mitigation measures |

## 4. RULES

[RULE-01] System components MUST be replaced within 90 days of vendor end-of-support date unless an approved exception exists.
[VALIDATION] IF component_support_end_date + 90_days < current_date AND replacement_completed = FALSE AND approved_exception = FALSE THEN violation

[RULE-02] Components reaching end-of-support MUST have documented alternative support arrangements established before the support termination date.
[VALIDATION] IF support_end_date <= current_date AND alternative_support_documented = FALSE AND component_active = TRUE THEN violation

[RULE-03] Unsupported components with approved exceptions MUST be isolated from public networks and uncontrolled network segments.
[VALIDATION] IF component_supported = FALSE AND exception_approved = TRUE AND (public_network_access = TRUE OR uncontrolled_network_access = TRUE) THEN critical_violation

[RULE-04] Risk assessments for retaining unsupported components MUST be reviewed and reapproved annually.
[VALIDATION] IF component_supported = FALSE AND last_risk_assessment_date + 365_days < current_date THEN violation

[RULE-05] In-house support capabilities MUST include documented patch development and testing procedures for critical unsupported components.
[VALIDATION] IF support_type = "in-house" AND (patch_procedures_documented = FALSE OR testing_procedures_documented = FALSE) THEN violation

[RULE-06] Alternative support contracts MUST specify response times for critical security vulnerabilities not exceeding 72 hours for high-risk systems.
[VALIDATION] IF support_type = "external_contract" AND system_risk_level = "high" AND contract_response_time > 72_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Support Lifecycle Monitoring - Track vendor support timelines and end-of-life announcements
- [PROC-02] Unsupported Component Risk Assessment - Evaluate security and operational risks of retaining components
- [PROC-03] Alternative Support Evaluation - Assess and approve in-house or third-party support options
- [PROC-04] Component Isolation Implementation - Deploy network and system-level isolation controls
- [PROC-05] Emergency Patch Development - Develop critical security patches for unsupported components

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Major security incidents involving unsupported components, changes in regulatory requirements, significant changes to IT infrastructure

## 7. SCENARIO PATTERNS

[SCENARIO-01: Standard Component End-of-Support]
IF component_support_end_date < current_date
AND replacement_available = TRUE
AND replacement_completed = FALSE
AND days_past_deadline > 90
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Mission-Critical Legacy System]
IF component_supported = FALSE
AND business_criticality = "mission_critical"
AND replacement_feasible = FALSE
AND alternative_support_documented = TRUE
AND isolation_implemented = TRUE
THEN compliance = TRUE

[SCENARIO-03: Unsupported Component on Public Network]
IF component_supported = FALSE
AND network_exposure = "public"
AND exception_approved = TRUE
AND isolation_implemented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Expired Risk Assessment]
IF component_supported = FALSE
AND exception_status = "approved"
AND last_risk_review_date + 365_days < current_date
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Inadequate Alternative Support Contract]
IF support_type = "external_contract"
AND system_classification = "high_risk"
AND contract_security_response_time > 72_hours
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Replace unsupported system components | [RULE-01] |
| Establish alternative support sources | [RULE-02], [RULE-05], [RULE-06] |
| Implement risk mitigation for retained components | [RULE-03], [RULE-04] |
| Maintain documented support procedures | [RULE-05] |
| Ensure adequate support response capabilities | [RULE-06] |