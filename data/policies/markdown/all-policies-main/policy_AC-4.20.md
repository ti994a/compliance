# POLICY: AC-4.20: Approved Solutions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-4.20 |
| NIST Control | AC-4.20: Approved Solutions |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | cross-domain, information flow, approved solutions, security domains, NSA, NCDSMO |

## 1. POLICY STATEMENT
The organization SHALL employ only approved solutions in approved configurations to control information flow across security domains. All cross-domain information transfers MUST utilize solutions that have been formally approved and configured according to established security requirements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Systems handling cross-domain transfers |
| Cross-Domain Solutions | YES | Hardware and software solutions |
| Network Infrastructure | YES | Components facilitating cross-domain flow |
| Cloud Services | YES | Multi-tenant and hybrid deployments |
| Third-Party Solutions | YES | Must meet approval requirements |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve cross-domain solution policies<br>• Maintain approved solutions list<br>• Coordinate with NSA NCDSMO |
| System Administrators | • Implement approved configurations<br>• Monitor cross-domain transfers<br>• Maintain configuration baselines |
| Security Engineers | • Evaluate cross-domain solutions<br>• Validate approved configurations<br>• Document security domain boundaries |

## 4. RULES
[RULE-01] Organizations MUST maintain a documented list of approved cross-domain solutions and their approved configurations.
[VALIDATION] IF cross_domain_solution_deployed = TRUE AND solution_on_approved_list = FALSE THEN critical_violation

[RULE-02] All cross-domain information flow MUST utilize only approved solutions in their approved configurations.
[VALIDATION] IF information_crosses_security_domains = TRUE AND solution_approved = FALSE THEN critical_violation

[RULE-03] Cross-domain solutions MUST be configured according to approved baseline configurations with no unauthorized modifications.
[VALIDATION] IF solution_configuration != approved_baseline AND unauthorized_modification = TRUE THEN violation

[RULE-04] Organizations MUST define security domains and document information flow requirements between domains.
[VALIDATION] IF security_domains_defined = FALSE OR flow_requirements_documented = FALSE THEN violation

[RULE-05] NSA NCDSMO approved solutions SHALL be prioritized for cross-domain information flow control when available.
[VALIDATION] IF ncdsmo_solution_available = TRUE AND alternative_solution_used = TRUE AND justification_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Cross-Domain Solution Approval Process - Evaluation and approval of solutions for cross-domain use
- [PROC-02] Configuration Management - Maintenance of approved baseline configurations
- [PROC-03] Security Domain Definition - Documentation of security boundaries and flow requirements
- [PROC-04] NCDSMO Coordination - Regular review of NSA approved solutions list

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New cross-domain requirements, solution updates, security incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unapproved Cross-Domain Solution]
IF information_flow_crosses_domains = TRUE
AND solution_on_approved_list = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Modified Approved Configuration]
IF approved_solution_deployed = TRUE
AND configuration_matches_baseline = FALSE
AND change_authorized = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Security Domain Definition]
IF cross_domain_transfer_required = TRUE
AND security_domains_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: NCDSMO Solution Available But Not Used]
IF ncdsmo_approved_solution_exists = TRUE
AND alternative_solution_used = TRUE
AND business_justification_documented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Proper Approved Solution Implementation]
IF solution_on_approved_list = TRUE
AND configuration_matches_baseline = TRUE
AND security_domains_defined = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Solutions in approved configurations defined | [RULE-01], [RULE-04] |
| Approved solutions employed for cross-domain flow | [RULE-02], [RULE-03] |
| Information flow control across security domains | [RULE-02], [RULE-05] |