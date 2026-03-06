```markdown
# POLICY: PM-17: Protecting Controlled Unclassified Information on External Systems

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-17 |
| NIST Control | PM-17: Protecting Controlled Unclassified Information on External Systems |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | controlled unclassified information, CUI, external systems, third-party, contractors, policy review |

## 1. POLICY STATEMENT
The organization SHALL establish and maintain policies and procedures to ensure controlled unclassified information (CUI) processed, stored, or transmitted on external systems meets protection requirements per applicable laws, regulations, and standards. These policies and procedures SHALL be reviewed and updated at defined intervals to maintain compliance with evolving requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All CUI data | YES | Regardless of classification level |
| External systems | YES | Third-party, contractor, cloud systems |
| Internal systems | NO | Covered by other controls |
| Vendor contracts | YES | Must include CUI protection clauses |
| Cloud service providers | YES | Including SaaS, PaaS, IaaS |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Information Security Officer | • Establish CUI protection policies<br>• Approve external system CUI processing<br>• Oversee policy review and updates |
| Data Protection Officer | • Define CUI handling procedures<br>• Validate external system compliance<br>• Monitor CUI protection implementation |
| Procurement Manager | • Include CUI requirements in contracts<br>• Verify vendor CUI compliance capabilities<br>• Manage contract CUI protection clauses |
| System Owners | • Implement CUI protection controls<br>• Report CUI processing on external systems<br>• Maintain system-specific procedures |

## 4. RULES

[RULE-01] Organizations MUST establish written policies defining CUI protection requirements for external systems in accordance with 32 CFR 2002.14h and applicable federal regulations.
[VALIDATION] IF cui_policy_exists = FALSE OR cui_policy_covers_external_systems = FALSE THEN critical_violation

[RULE-02] CUI protection procedures MUST specify technical, administrative, and physical safeguards required for external systems processing CUI data.
[VALIDATION] IF cui_procedures_exist = FALSE OR safeguard_specifications = "incomplete" THEN violation

[RULE-03] External systems processing CUI MUST be approved through formal assessment demonstrating compliance with organizational CUI protection requirements.
[VALIDATION] IF external_system_processes_cui = TRUE AND formal_approval = FALSE THEN critical_violation

[RULE-04] Contracts with external parties processing CUI MUST include specific CUI protection requirements, audit rights, and incident reporting obligations.
[VALIDATION] IF contract_processes_cui = TRUE AND cui_clauses = FALSE THEN violation

[RULE-05] CUI protection policies MUST be reviewed and updated at least annually or when regulatory requirements change.
[VALIDATION] IF policy_last_review > 365_days OR regulatory_change_occurred = TRUE AND policy_updated = FALSE THEN violation

[RULE-06] External systems MUST implement CUI marking, handling, and disposal procedures consistent with organizational requirements.
[VALIDATION] IF external_system_processes_cui = TRUE AND (marking_procedures = FALSE OR disposal_procedures = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] CUI Classification and Marking - Standardized process for identifying and marking CUI
- [PROC-02] External System Assessment - Evaluation methodology for external system CUI capabilities
- [PROC-03] Contract CUI Requirements - Template clauses and requirements for vendor agreements
- [PROC-04] CUI Incident Response - Procedures for CUI breaches on external systems
- [PROC-05] Policy Review and Update - Process for maintaining current CUI protection policies

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Regulatory changes, significant CUI incidents, new external system deployments, contract renewals

## 7. SCENARIO PATTERNS

[SCENARIO-01: Cloud Provider CUI Processing]
IF cloud_service_processes_cui = TRUE
AND contract_includes_cui_requirements = TRUE
AND provider_assessment_completed = TRUE
AND annual_policy_review_current = TRUE
THEN compliance = TRUE

[SCENARIO-02: Unapproved External CUI Processing]
IF external_system_processes_cui = TRUE
AND formal_approval = FALSE
AND cui_data_sensitivity = "moderate"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Outdated CUI Policy]
IF cui_policy_exists = TRUE
AND policy_last_review > 365_days
AND regulatory_changes_occurred = TRUE
AND policy_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Contractor Missing CUI Clauses]
IF contractor_processes_cui = TRUE
AND contract_includes_cui_protection = FALSE
AND data_classification = "cui_basic"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Compliant External Processing]
IF external_system_processes_cui = TRUE
AND formal_approval = TRUE
AND contract_cui_compliant = TRUE
AND incident_reporting_established = TRUE
AND audit_rights_defined = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Policy established for CUI protection on external systems | RULE-01 |
| Procedures established for CUI protection implementation | RULE-02 |
| Policy reviewed and updated at defined frequency | RULE-05 |
| Procedures reviewed and updated at defined frequency | RULE-05 |
| External system CUI processing approval | RULE-03 |
| Contract CUI protection requirements | RULE-04 |
| CUI handling procedures implementation | RULE-06 |
```