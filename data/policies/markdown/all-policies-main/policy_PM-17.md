# POLICY: PM-17: Protecting Controlled Unclassified Information on External Systems

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-17 |
| NIST Control | PM-17: Protecting Controlled Unclassified Information on External Systems |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | CUI, controlled unclassified information, external systems, third-party, contractors, data protection |

## 1. POLICY STATEMENT
The organization SHALL establish and maintain policies and procedures to ensure controlled unclassified information (CUI) processed, stored, or transmitted on external systems receives protection consistent with applicable laws, executive orders, directives, policies, regulations, and standards. These requirements SHALL be implemented through organizational procedures including contracting processes and vendor management.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| External service providers | YES | All third-party systems processing CUI |
| Cloud service providers | YES | Including SaaS, PaaS, IaaS handling CUI |
| Contractors and subcontractors | YES | When accessing or processing CUI |
| Business partners | YES | Joint ventures or partnerships involving CUI |
| Internal systems | NO | Covered by other controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Information Security Officer | • Establish CUI protection policies<br>• Oversee compliance monitoring<br>• Approve external system CUI processing |
| Procurement Officer | • Include CUI requirements in contracts<br>• Validate vendor CUI capabilities<br>• Monitor contract compliance |
| Data Owner | • Classify information as CUI<br>• Approve external processing arrangements<br>• Define protection requirements |
| Vendor Management | • Assess third-party CUI controls<br>• Monitor ongoing compliance<br>• Manage vendor relationships |

## 4. RULES

[RULE-01] Organizations MUST establish written policies defining requirements for CUI protection on external systems in accordance with 32 CFR 2002.
[VALIDATION] IF external_system_processes_CUI = TRUE AND written_policy_exists = FALSE THEN critical_violation

[RULE-02] All contracts with external parties processing CUI MUST include specific CUI protection requirements and compliance verification mechanisms.
[VALIDATION] IF contract_involves_CUI = TRUE AND CUI_requirements_included = FALSE THEN violation

[RULE-03] External systems processing CUI MUST implement safeguarding controls equivalent to or exceeding organizational requirements.
[VALIDATION] IF external_CUI_controls < internal_CUI_controls THEN violation

[RULE-04] CUI protection policies MUST be reviewed and updated at least annually or when significant changes occur to regulations or organizational requirements.
[VALIDATION] IF policy_last_review > 365_days AND no_triggering_events = TRUE THEN violation

[RULE-05] Organizations MUST verify external party compliance with CUI protection requirements through assessments, audits, or certifications before authorizing CUI processing.
[VALIDATION] IF CUI_processing_authorized = TRUE AND compliance_verification_completed = FALSE THEN critical_violation

[RULE-06] Procedures MUST address CUI handling requirements including marking, storage, transmission, and disposal on external systems.
[VALIDATION] IF CUI_procedures_documented = FALSE OR required_elements_missing > 0 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] CUI Classification and Marking - Standardized process for identifying and marking CUI
- [PROC-02] External System Assessment - Evaluation methodology for third-party CUI capabilities  
- [PROC-03] Contract CUI Requirements - Template clauses and verification requirements
- [PROC-04] Incident Response for External CUI - Procedures for CUI breaches on third-party systems
- [PROC-05] CUI Compliance Monitoring - Ongoing oversight and assessment of external parties

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Regulatory changes, significant CUI incidents, new external partnerships, audit findings

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unauthorized Cloud CUI Storage]
IF cloud_service_stores_CUI = TRUE
AND CUI_protection_verified = FALSE
AND contract_includes_CUI_terms = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Contractor CUI Access Without Assessment]
IF contractor_accesses_CUI = TRUE
AND security_assessment_completed = FALSE
AND contract_execution_date < current_date
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Outdated CUI Protection Policy]
IF policy_last_updated > 365_days
AND regulatory_changes_occurred = TRUE
AND policy_update_initiated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: External System CUI Incident]
IF CUI_incident_on_external_system = TRUE
AND incident_response_executed = TRUE
AND contractual_notification_completed = TRUE
AND remediation_verified = TRUE
THEN compliance = TRUE

[SCENARIO-05: Third-Party CUI Subprocessing]
IF third_party_uses_subprocessors = TRUE
AND subprocessor_CUI_controls_verified = FALSE
AND written_authorization_exists = FALSE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Policy establishment for CUI protection on external systems | [RULE-01] |
| Procedures for CUI protection implementation | [RULE-06] |
| Contract requirements for external CUI processing | [RULE-02] |
| Compliance verification mechanisms | [RULE-05] |
| Policy and procedure review frequency | [RULE-04] |
| External system control equivalency | [RULE-03] |