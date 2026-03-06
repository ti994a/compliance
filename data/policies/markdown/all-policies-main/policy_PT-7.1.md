# POLICY: PT-7.1: Social Security Numbers

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PT-7.1 |
| NIST Control | PT-7.1: Social Security Numbers |
| Version | 1.0 |
| Owner | Chief Privacy Officer |
| Keywords | social security numbers, SSN, PII, privacy, personal identifiers, disclosure |

## 1. POLICY STATEMENT
The organization SHALL eliminate unnecessary collection, maintenance, and use of Social Security Numbers (SSNs) and explore alternative identifiers. When SSN collection is necessary, individuals MUST be informed of disclosure requirements, legal authority, and intended uses, and SHALL NOT be denied services for refusing voluntary disclosure.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All systems processing SSNs | YES | Including cloud and on-premises |
| Third-party processors | YES | When handling organizational data |
| Employee systems | YES | HR, payroll, benefits systems |
| Customer-facing applications | YES | All user-facing systems |
| Development/test environments | YES | When containing real SSN data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Privacy Officer | • Oversee SSN minimization program<br>• Approve SSN collection justifications<br>• Review alternative identifier implementations |
| System Owners | • Assess SSN necessity in their systems<br>• Implement required privacy notices<br>• Document legal authority for collection |
| Data Protection Team | • Conduct SSN usage audits<br>• Validate privacy notice compliance<br>• Monitor alternative identifier adoption |

## 4. RULES
[RULE-01] Systems MUST eliminate unnecessary collection, maintenance, and use of SSNs through documented assessment and remediation within 90 days of policy implementation.
[VALIDATION] IF system_processes_ssn = TRUE AND necessity_assessment_completed = FALSE AND days_since_policy > 90 THEN violation

[RULE-02] Organizations MUST explore and document alternative identifiers to replace SSNs as personal identifiers within 180 days of identifying unnecessary SSN usage.
[VALIDATION] IF ssn_usage_deemed_unnecessary = TRUE AND alternative_identifier_explored = FALSE AND days_since_determination > 180 THEN violation

[RULE-03] Systems SHALL NOT deny individuals any right, benefit, or privilege provided by law because of refusal to disclose SSN when disclosure is voluntary.
[VALIDATION] IF ssn_disclosure_type = "voluntary" AND service_denied_for_ssn_refusal = TRUE THEN critical_violation

[RULE-04] When requesting SSN disclosure, systems MUST inform individuals whether disclosure is mandatory or voluntary, the legal authority for collection, and intended uses.
[VALIDATION] IF ssn_requested = TRUE AND (disclosure_type_communicated = FALSE OR legal_authority_communicated = FALSE OR intended_uses_communicated = FALSE) THEN violation

[RULE-05] Privacy notices for SSN collection MUST be provided at the point of collection and include all required disclosure elements as specified in the SSN Privacy Notice Standard.
[VALIDATION] IF ssn_collection_point_identified = TRUE AND privacy_notice_present = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] SSN Necessity Assessment - Systematic review of all SSN usage to determine business necessity
- [PROC-02] Alternative Identifier Evaluation - Process for identifying and implementing SSN alternatives
- [PROC-03] Privacy Notice Management - Creation and maintenance of SSN-specific privacy notices
- [PROC-04] SSN Collection Approval - Workflow for approving new SSN collection requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Bi-annually
- Triggering events: New system implementations, regulatory changes, privacy incidents involving SSNs

## 7. SCENARIO PATTERNS
[SCENARIO-01: New System SSN Collection]
IF new_system_deployment = TRUE
AND ssn_collection_planned = TRUE
AND necessity_assessment_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Voluntary SSN Disclosure Denial]
IF ssn_disclosure_type = "voluntary"
AND individual_refused_ssn = TRUE
AND service_access_denied = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Missing Privacy Notice]
IF ssn_collection_active = TRUE
AND privacy_notice_displayed = FALSE
AND collection_point_identified = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Alternative Identifier Implementation]
IF ssn_usage_unnecessary = TRUE
AND alternative_identifier_implemented = TRUE
AND ssn_collection_discontinued = TRUE
THEN compliance = TRUE

[SCENARIO-05: Incomplete Disclosure Information]
IF ssn_requested = TRUE
AND mandatory_voluntary_status_communicated = TRUE
AND legal_authority_communicated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Eliminate unnecessary SSN collection, maintenance, and use | [RULE-01] |
| Explore alternatives to SSN as personal identifier | [RULE-02] |
| Do not deny services for voluntary SSN refusal | [RULE-03] |
| Inform individuals of disclosure requirements | [RULE-04] |
| Communicate legal authority for SSN solicitation | [RULE-04] |
| Inform individuals of intended SSN uses | [RULE-04] |