# POLICY: PT-7.1: Social Security Numbers

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-7.1 |
| NIST Control | PT-7.1: Social Security Numbers |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | SSN, social security numbers, PII, personal identifiers, privacy notice, mandatory disclosure |

## 1. POLICY STATEMENT
When systems process Social Security numbers (SSNs), the organization must eliminate unnecessary collection and use, explore alternative identifiers, and provide proper disclosure notices to individuals. No individual shall be denied rights, benefits, or privileges for refusing to disclose their SSN unless legally required.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | CONDITIONAL | Only systems that collect, process, or store SSNs |
| Web applications | CONDITIONAL | Only those requesting SSN input |
| HR systems | YES | Typically process employee SSNs |
| Customer databases | CONDITIONAL | Only if SSNs are collected |
| Third-party processors | YES | When processing SSNs on organization's behalf |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee SSN minimization program<br>• Approve SSN collection justifications<br>• Review privacy notices |
| System Owners | • Eliminate unnecessary SSN collection<br>• Implement alternative identifiers<br>• Ensure proper disclosure notices |
| Legal Counsel | • Determine legal requirements for SSN collection<br>• Review statutory authorities<br>• Validate disclosure language |

## 4. RULES

[RULE-01] Systems MUST eliminate unnecessary collection, maintenance, and use of Social Security numbers and implement alternative identifiers where feasible.
[VALIDATION] IF system_collects_ssn = TRUE AND business_justification = "not_documented" THEN violation

[RULE-02] Organizations MUST NOT deny any individual rights, benefits, or privileges provided by law because of the individual's refusal to disclose their Social Security number unless disclosure is legally mandated.
[VALIDATION] IF ssn_refusal = TRUE AND service_denied = TRUE AND legal_requirement = FALSE THEN violation

[RULE-03] When requesting SSN disclosure, organizations MUST inform individuals whether disclosure is mandatory or voluntary, the statutory authority for collection, and intended uses.
[VALIDATION] IF ssn_requested = TRUE AND (mandatory_notice = FALSE OR authority_notice = FALSE OR use_notice = FALSE) THEN violation

[RULE-04] SSN collection forms and interfaces MUST include privacy notices that specify disclosure requirements, legal authority, and data usage before collection occurs.
[VALIDATION] IF ssn_collection_point = TRUE AND privacy_notice_present = FALSE THEN violation

[RULE-05] Systems processing SSNs MUST undergo annual review to identify opportunities for SSN elimination and alternative identifier implementation.
[VALIDATION] IF system_processes_ssn = TRUE AND last_review_date > 365_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] SSN Minimization Assessment - Annual review of SSN usage and elimination opportunities
- [PROC-02] Privacy Notice Management - Creation and maintenance of SSN disclosure notices
- [PROC-03] Alternative Identifier Evaluation - Assessment of non-SSN identifier options
- [PROC-04] Legal Authority Documentation - Validation of statutory requirements for SSN collection

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New system deployment, regulatory changes, privacy incident involving SSNs

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unnecessary SSN Collection]
IF system_collects_ssn = TRUE
AND alternative_identifier_available = TRUE
AND legal_requirement = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Missing Privacy Notice]
IF ssn_collection_form = TRUE
AND privacy_notice_displayed = FALSE
AND user_ssn_entered = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Service Denial for SSN Refusal]
IF individual_refused_ssn = TRUE
AND service_denied = TRUE
AND ssn_legally_required = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Incomplete Disclosure Notice]
IF ssn_requested = TRUE
AND mandatory_voluntary_notice = TRUE
AND legal_authority_notice = FALSE
AND usage_notice = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Alternative Implementation]
IF system_previously_used_ssn = TRUE
AND alternative_identifier_implemented = TRUE
AND ssn_collection_eliminated = TRUE
AND privacy_notice_updated = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Eliminate unnecessary SSN collection, maintenance, and use | [RULE-01] |
| Explore alternatives to SSN as personal identifier | [RULE-01] |
| Do not deny rights/benefits for SSN refusal | [RULE-02] |
| Inform individuals if disclosure is mandatory or voluntary | [RULE-03] |
| Inform individuals of statutory authority for SSN collection | [RULE-03] |
| Inform individuals of intended SSN uses | [RULE-03] |