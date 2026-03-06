# POLICY: PT-7.1: Social Security Numbers

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-7.1 |
| NIST Control | PT-7.1: Social Security Numbers |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | social security numbers, SSN, PII, personal identifier, disclosure, collection, alternatives |

## 1. POLICY STATEMENT
Systems processing Social Security numbers (SSNs) MUST eliminate unnecessary collection and use, explore alternative identifiers, and provide mandatory disclosure notifications. Individuals SHALL NOT be denied services for refusing to provide SSNs unless legally required.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | CONDITIONAL | Only systems that collect, process, or store SSNs |
| HR Systems | YES | Employee records containing SSNs |
| Customer Databases | CONDITIONAL | If collecting SSNs from customers |
| Third-Party Services | YES | If processing SSNs on organization's behalf |
| Development/Test Systems | YES | No production SSNs allowed |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee SSN usage policies<br>• Approve SSN collection requirements<br>• Conduct periodic SSN usage reviews |
| System Owners | • Document SSN usage justification<br>• Implement alternative identifiers<br>• Ensure proper disclosure notifications |
| Data Protection Team | • Review SSN collection requests<br>• Monitor SSN usage compliance<br>• Maintain SSN inventory |

## 4. RULES
[RULE-01] Systems MUST eliminate unnecessary collection, maintenance, and use of Social Security numbers and document business justification for any retained SSN usage.
[VALIDATION] IF system_collects_ssn = TRUE AND business_justification = NULL THEN violation

[RULE-02] Organizations MUST explore and implement alternatives to SSNs as personal identifiers where technically feasible.
[VALIDATION] IF ssn_used_as_identifier = TRUE AND alternative_explored = FALSE THEN violation

[RULE-03] Systems SHALL NOT deny individuals any right, benefit, or privilege because of refusal to disclose SSN unless disclosure is legally mandated.
[VALIDATION] IF service_denied = TRUE AND ssn_refused = TRUE AND legal_requirement = FALSE THEN critical_violation

[RULE-04] When requesting SSNs, systems MUST inform individuals whether disclosure is mandatory or voluntary, the legal authority for collection, and intended uses.
[VALIDATION] IF ssn_requested = TRUE AND disclosure_notice = FALSE THEN violation

[RULE-05] Development and testing environments MUST NOT contain production SSNs and SHALL use synthetic data or data masking techniques.
[VALIDATION] IF environment_type = "non-production" AND contains_real_ssn = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] SSN Usage Assessment - Annual review of all SSN collection and usage
- [PROC-02] Alternative Identifier Implementation - Process for replacing SSNs with alternatives
- [PROC-03] SSN Disclosure Notification - Standard notices for SSN collection
- [PROC-04] Data Masking for Non-Production - Procedures for sanitizing SSNs in test data

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New system deployment, regulatory changes, privacy incidents involving SSNs

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unnecessary SSN Collection]
IF system_collects_ssn = TRUE
AND business_justification = "convenience"
AND alternative_identifier_available = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Missing Disclosure Notice]
IF ssn_collection_form = TRUE
AND mandatory_voluntary_notice = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Service Denial for SSN Refusal]
IF customer_refused_ssn = TRUE
AND service_denied = TRUE
AND legal_requirement_exists = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Production SSNs in Test Environment]
IF environment = "development"
AND real_ssn_present = TRUE
AND data_masking_applied = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Compliant Alternative Implementation]
IF previous_ssn_identifier = TRUE
AND alternative_implemented = TRUE
AND ssn_usage_eliminated = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Eliminate unnecessary SSN collection, maintenance, and use | [RULE-01] |
| Explore alternatives to SSN as personal identifier | [RULE-02] |
| Do not deny services for SSN refusal | [RULE-03] |
| Inform individuals of mandatory/voluntary disclosure | [RULE-04] |
| Inform individuals of legal authority for collection | [RULE-04] |
| Inform individuals of intended SSN uses | [RULE-04] |