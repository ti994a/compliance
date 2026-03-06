# POLICY: SR-2: Supply Chain Risk Management Plan

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-2 |
| NIST Control | SR-2: Supply Chain Risk Management Plan |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | supply chain, risk management, SCRM plan, vendor management, third-party risk |

## 1. POLICY STATEMENT
The organization SHALL develop, maintain, and protect comprehensive supply chain risk management (SCRM) plans that address risks across the entire system lifecycle from research and development through disposal. SCRM plans MUST be reviewed regularly and updated to address evolving threats, organizational changes, and environmental factors.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, hybrid, and on-premises |
| System components | YES | Hardware, software, firmware |
| System services | YES | Managed services, SaaS, outsourced functions |
| Third-party vendors | YES | All suppliers in the technology supply chain |
| Development projects | YES | Custom and commercial off-the-shelf |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Risk Manager | • Develop and maintain SCRM plans<br>• Coordinate supply chain risk assessments<br>• Monitor supply chain threat landscape |
| System Owners | • Implement system-specific SCRM requirements<br>• Report supply chain incidents<br>• Ensure contractor compliance |
| Procurement Team | • Integrate SCRM requirements into contracts<br>• Validate supplier security capabilities<br>• Maintain approved vendor lists |

## 4. RULES
[RULE-01] Organizations MUST develop a comprehensive SCRM plan that addresses risks across all lifecycle phases: research and development, design, manufacturing, acquisition, delivery, integration, operations and maintenance, and disposal.
[VALIDATION] IF system_in_scope = TRUE AND scrm_plan_exists = FALSE THEN critical_violation

[RULE-02] SCRM plans MUST be reviewed and updated at least annually or within 30 days of significant threat, organizational, or environmental changes.
[VALIDATION] IF last_review_date > 365_days OR (significant_change = TRUE AND update_date > 30_days) THEN violation

[RULE-03] SCRM plans SHALL be protected from unauthorized disclosure and modification through appropriate access controls and classification handling.
[VALIDATION] IF scrm_plan_access_controls = FALSE OR unauthorized_modification_detected = TRUE THEN violation

[RULE-04] SCRM plans MUST include risk tolerance statements, mitigation strategies, evaluation processes, implementation approaches, and defined roles and responsibilities.
[VALIDATION] IF missing_required_elements > 0 THEN violation

[RULE-05] System-level SCRM plans MUST be tailored to specific program, organizational, and operational contexts and integrated with system security and privacy plans.
[VALIDATION] IF scrm_plan_tailored = FALSE OR integration_with_security_plan = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain Risk Assessment - Systematic evaluation of supplier risks across lifecycle phases
- [PROC-02] SCRM Plan Development - Standardized methodology for creating tailored SCRM plans
- [PROC-03] Supplier Evaluation - Due diligence process for vetting supply chain partners
- [PROC-04] Supply Chain Incident Response - Procedures for responding to supply chain compromises
- [PROC-05] SCRM Plan Protection - Controls for safeguarding SCRM plan confidentiality and integrity

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Supply chain incidents, new threat intelligence, organizational restructuring, regulatory changes, major system acquisitions

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing SCRM Plan]
IF system_classification = "moderate" OR "high"
AND scrm_plan_documented = FALSE
AND system_age > 90_days
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Outdated SCRM Plan]
IF scrm_plan_exists = TRUE
AND last_review_date > 365_days
AND no_approved_extension = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Unauthorized SCRM Plan Access]
IF scrm_plan_access_log = TRUE
AND accessor_authorization = FALSE
AND access_detected = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Incomplete Lifecycle Coverage]
IF scrm_plan_exists = TRUE
AND lifecycle_phases_covered < 8
AND no_documented_exemption = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Supply Chain Change Without Update]
IF major_supplier_change = TRUE
AND change_date < 30_days_ago
AND scrm_plan_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| SCRM plan development covering all lifecycle phases | [RULE-01] |
| Regular review and update of SCRM plans | [RULE-02] |
| Protection from unauthorized disclosure | [RULE-03] |
| Protection from unauthorized modification | [RULE-03] |
| Inclusion of required SCRM plan elements | [RULE-04] |
| System-specific tailoring and integration | [RULE-05] |