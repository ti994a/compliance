# POLICY: PM-17: Protecting Controlled Unclassified Information on External Systems

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-17 |
| NIST Control | PM-17: Protecting Controlled Unclassified Information on External Systems |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | controlled unclassified information, CUI, external systems, third-party, contracting, data protection |

## 1. POLICY STATEMENT
The organization SHALL establish and maintain comprehensive policies and procedures to ensure controlled unclassified information (CUI) processed, stored, or transmitted on external systems receives protection consistent with applicable laws, executive orders, directives, policies, regulations, and standards. These requirements SHALL be implemented through organizational procedures and contracting processes with external service providers.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All CUI data | YES | Regardless of classification level |
| External cloud providers | YES | Including SaaS, PaaS, IaaS |
| Third-party contractors | YES | Processing any CUI |
| Vendor systems | YES | With CUI access |
| Partner organizations | YES | Handling shared CUI |
| Public systems | NO | CUI prohibited |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Establish CUI protection policies<br>• Oversee external system compliance<br>• Approve CUI processing agreements |
| Data Protection Officer | • Review CUI handling procedures<br>• Validate external system controls<br>• Monitor compliance with 32 CFR 2002 |
| Procurement Officer | • Include CUI requirements in contracts<br>• Validate vendor CUI capabilities<br>• Ensure contractual compliance mechanisms |
| System Owners | • Implement CUI protection controls<br>• Monitor external system usage<br>• Report CUI incidents |

## 4. RULES
[RULE-01] All external systems processing CUI MUST implement safeguarding requirements specified in 32 CFR 2002.14h and organizational CUI protection standards.
[VALIDATION] IF external_system = TRUE AND cui_data = TRUE AND cfr_2002_compliance = FALSE THEN critical_violation

[RULE-02] Contracts with external service providers MUST include specific CUI protection requirements, audit rights, and incident notification procedures before CUI processing begins.
[VALIDATION] IF external_provider = TRUE AND cui_processing = TRUE AND contract_cui_clauses = FALSE THEN violation

[RULE-03] CUI protection policies and procedures MUST be reviewed and updated at least annually or when regulatory requirements change.
[VALIDATION] IF policy_last_review > 365_days OR regulatory_change = TRUE AND policy_updated = FALSE THEN violation

[RULE-04] External systems MUST provide evidence of CUI protection control implementation through security assessments or certifications before CUI data placement.
[VALIDATION] IF external_system = TRUE AND cui_authorized = TRUE AND security_assessment_current = FALSE THEN violation

[RULE-05] Organizations MUST maintain inventory of all external systems processing CUI with current authorization status and control implementation evidence.
[VALIDATION] IF cui_external_system = TRUE AND inventory_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] CUI External System Authorization - Process for evaluating and authorizing external systems for CUI processing
- [PROC-02] Contract CUI Requirements Integration - Procedure for incorporating CUI protection clauses in vendor agreements
- [PROC-03] External System CUI Monitoring - Ongoing oversight and compliance verification for external CUI processing
- [PROC-04] CUI Incident Response Coordination - Process for managing CUI incidents on external systems

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Regulatory changes, significant CUI incidents, new external system types, contract renewals

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Service CUI Processing]
IF service_type = "cloud"
AND cui_data = TRUE
AND cfr_2002_compliance = "verified"
AND contract_cui_clauses = TRUE
THEN compliance = TRUE

[SCENARIO-02: Unauthorized External CUI Storage]
IF external_system = TRUE
AND cui_data = TRUE
AND authorization_status = "none"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Vendor Contract Without CUI Clauses]
IF vendor_contract = TRUE
AND cui_processing = TRUE
AND contract_cui_requirements = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Outdated CUI Policy]
IF policy_last_review > 365_days
AND regulatory_updates = TRUE
AND policy_version = "outdated"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: External System Assessment Gap]
IF external_system = TRUE
AND cui_authorized = TRUE
AND security_assessment_age > 365_days
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| CUI policy establishment for external systems | RULE-01, RULE-03 |
| CUI procedures for external system protection | RULE-02, RULE-04 |
| Policy review and update frequency | RULE-03 |
| Procedure review and update frequency | RULE-03 |
| External system CUI control implementation | RULE-01, RULE-04 |
| Contractual CUI protection requirements | RULE-02 |
| CUI external system inventory maintenance | RULE-05 |