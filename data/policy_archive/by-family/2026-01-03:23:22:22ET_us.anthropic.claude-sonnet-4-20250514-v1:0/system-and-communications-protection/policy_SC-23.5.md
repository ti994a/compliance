```markdown
# POLICY: SC-23.5: Allowed Certificate Authorities

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-23.5 |
| NIST Control | SC-23.5: Allowed Certificate Authorities |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | certificate authorities, TLS, protected sessions, PKI, SSL, verification |

## 1. POLICY STATEMENT
The organization SHALL only allow the use of pre-approved certificate authorities for verification and establishment of protected sessions. All certificate authorities used for TLS/SSL connections must be explicitly authorized and maintained on an approved list.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Web Applications | YES | All applications using TLS/SSL |
| API Endpoints | YES | Including internal and external APIs |
| Network Infrastructure | YES | Load balancers, proxies, firewalls |
| Third-party Services | CONDITIONAL | Only if establishing protected sessions |
| Development/Test Systems | YES | Must follow same CA restrictions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve certificate authority list<br>• Review CA policy annually<br>• Authorize emergency CA additions |
| PKI Administrator | • Maintain approved CA list<br>• Configure certificate validation<br>• Monitor certificate usage and compliance |
| System Administrators | • Implement CA restrictions in systems<br>• Report unauthorized CA usage<br>• Request CA additions through proper channels |

## 4. RULES
[RULE-01] Systems MUST only accept certificates issued by certificate authorities on the approved CA list for establishing protected sessions.
[VALIDATION] IF certificate_issuer NOT IN approved_ca_list AND session_type = "protected" THEN violation

[RULE-02] The approved certificate authority list MUST be maintained and updated within 30 days of any changes.
[VALIDATION] IF ca_list_last_updated > 30_days AND ca_changes_pending = TRUE THEN violation

[RULE-03] Certificate validation MUST include verification of the complete certificate chain to an approved root CA.
[VALIDATION] IF certificate_chain_validated = FALSE OR root_ca NOT IN approved_ca_list THEN violation

[RULE-04] Systems MUST reject connections using certificates from unauthorized certificate authorities.
[VALIDATION] IF connection_established = TRUE AND certificate_ca NOT IN approved_ca_list THEN critical_violation

[RULE-05] Emergency additions to the approved CA list MUST be documented and reviewed within 7 business days.
[VALIDATION] IF ca_addition_type = "emergency" AND review_completed = FALSE AND days_since_addition > 7 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Certificate Authority Approval Process - Formal process for evaluating and approving new CAs
- [PROC-02] CA List Management - Procedures for maintaining and distributing approved CA list
- [PROC-03] Certificate Validation Configuration - Technical implementation of CA restrictions
- [PROC-04] Unauthorized CA Incident Response - Response procedures for detecting unauthorized CA usage

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving certificates, new regulatory requirements, significant infrastructure changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized CA Certificate]
IF certificate_issuer NOT IN approved_ca_list
AND connection_type = "protected_session"
AND connection_allowed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Self-Signed Certificate in Production]
IF certificate_type = "self_signed"
AND environment = "production"
AND protected_session_required = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Expired CA in Approved List]
IF ca_certificate_status = "expired"
AND ca_in_approved_list = TRUE
AND active_certificates_issued > 0
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Emergency CA Addition]
IF ca_addition_type = "emergency"
AND business_justification_documented = TRUE
AND ciso_approval = TRUE
AND review_scheduled = TRUE
THEN compliance = TRUE
violation_severity = "None"

[SCENARIO-05: Development System Using Public CA]
IF environment = "development"
AND certificate_ca IN approved_ca_list
AND protected_session_established = TRUE
THEN compliance = TRUE
violation_severity = "None"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Only approved CAs allowed for protected sessions | [RULE-01] |
| Certificate chain validation to approved root CA | [RULE-03] |
| Rejection of unauthorized CA certificates | [RULE-04] |
| Maintained list of approved certificate authorities | [RULE-02] |
| Emergency CA addition controls | [RULE-05] |
```