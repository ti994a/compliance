# POLICY: PL-8.2: Supplier Diversity

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PL-8.2 |
| NIST Control | PL-8.2: Supplier Diversity |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | supplier diversity, security controls, architectural layers, vendor management, malicious code protection, privacy controls |

## 1. POLICY STATEMENT
The organization SHALL require that security and privacy controls allocated to system locations and architectural layers are obtained from different suppliers to enhance protection effectiveness. Control allocation and supplier sourcing decisions MUST be documented and justified based on risk assessment and architectural requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT systems | YES | Includes cloud, hybrid, and on-premises |
| Security controls | YES | Technical, administrative, and physical |
| Privacy controls | YES | PII tracking and protection mechanisms |
| Third-party services | YES | SaaS, PaaS, IaaS providers |
| Legacy systems | CONDITIONAL | When feasible during refresh cycles |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Architect | • Define control allocation strategy<br>• Document architectural layer mapping<br>• Validate supplier diversity requirements |
| Procurement Manager | • Implement supplier diversity sourcing<br>• Maintain approved vendor list<br>• Document supplier selection rationale |
| System Owner | • Identify required controls per system<br>• Coordinate with architects on placement<br>• Ensure operational effectiveness |

## 4. RULES
[RULE-01] Security and privacy controls allocated to different architectural layers MUST be sourced from different suppliers when technically feasible and cost-effective.
[VALIDATION] IF control_type = "same_function" AND architectural_layer != "same" AND supplier_count < 2 THEN violation

[RULE-02] Control allocation to locations and architectural layers SHALL be documented in the system security plan with supplier identification and justification.
[VALIDATION] IF control_documented = FALSE OR supplier_identified = FALSE OR justification_provided = FALSE THEN violation

[RULE-03] Malicious code protection controls MUST utilize at least two different suppliers across network perimeter, endpoint, and email security layers.
[VALIDATION] IF malware_protection = TRUE AND unique_suppliers < 2 AND layers >= 2 THEN violation

[RULE-04] Privacy controls that track personally identifiable information SHALL employ different tracking methods from multiple suppliers when multiple PII discovery tools are deployed.
[VALIDATION] IF pii_tracking_tools > 1 AND unique_suppliers = 1 THEN privacy_violation

[RULE-05] Supplier diversity exceptions MUST be documented with risk acceptance and compensating controls when single-supplier solutions are required.
[VALIDATION] IF single_supplier = TRUE AND (risk_acceptance = FALSE OR compensating_controls = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Control Allocation Planning - Define control placement strategy across architectural layers
- [PROC-02] Supplier Diversity Assessment - Evaluate vendor options for each control category
- [PROC-03] Exception Management - Document and approve single-supplier scenarios
- [PROC-04] Effectiveness Monitoring - Measure protection coverage across diverse suppliers

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major architecture changes, supplier consolidation, security incidents involving supplier products

## 7. SCENARIO PATTERNS
[SCENARIO-01: Endpoint Protection Diversity]
IF system_type = "enterprise_endpoints"
AND malware_protection = "single_supplier"
AND architectural_layers > 1
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Network Security Layering]
IF network_security_controls >= 3
AND unique_suppliers >= 2
AND control_allocation_documented = TRUE
THEN compliance = TRUE

[SCENARIO-03: PII Discovery Tools]
IF pii_discovery_tools = 2
AND supplier_1 = supplier_2
AND exception_documented = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Legacy System Exception]
IF system_age > 5_years
AND single_supplier = TRUE
AND risk_acceptance_signed = TRUE
AND compensating_controls_implemented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Cloud Service Diversity]
IF cloud_security_services > 1
AND cloud_providers = 1
AND architectural_separation = TRUE
AND business_justification_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Controls allocated are defined | [RULE-02] |
| Allocated to locations and architectural layers are defined | [RULE-02] |
| Required to be obtained from different suppliers | [RULE-01], [RULE-03], [RULE-04] |