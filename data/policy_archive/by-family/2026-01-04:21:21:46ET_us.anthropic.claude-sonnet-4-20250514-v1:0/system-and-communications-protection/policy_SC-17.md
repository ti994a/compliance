# POLICY: SC-17: Public Key Infrastructure Certificates

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-17 |
| NIST Control | SC-17: Public Key Infrastructure Certificates |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | PKI, certificates, trust anchors, certificate authority, cryptography |

## 1. POLICY STATEMENT
The organization SHALL establish a defined certificate policy for issuing public key certificates or obtain certificates from approved service providers. Only approved trust anchors SHALL be included in organizational trust stores and certificate stores.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Internal and external PKI certificates |
| Third-party service providers | YES | When providing PKI services |
| Certificate authorities | YES | Internal and external CAs |
| Application-specific certificates | YES | Including time services and internal operations |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| PKI Administrator | • Maintain certificate policies<br>• Manage trust anchor approvals<br>• Oversee certificate lifecycle management |
| Security Team | • Approve service providers<br>• Review trust anchor requests<br>• Monitor certificate compliance |
| System Administrators | • Implement trust store configurations<br>• Report certificate issues<br>• Maintain certificate inventories |

## 4. RULES
[RULE-01] Organizations MUST establish and maintain a documented certificate policy that defines requirements for issuing public key certificates OR obtain certificates from pre-approved service providers.
[VALIDATION] IF certificate_issued = TRUE AND (internal_policy_exists = FALSE AND approved_provider = FALSE) THEN violation

[RULE-02] All public key certificates MUST be issued in accordance with the established certificate policy or obtained from approved service providers only.
[VALIDATION] IF certificate_source NOT IN approved_providers AND policy_compliant = FALSE THEN violation

[RULE-03] Trust stores and certificate stores managed by the organization MUST contain only approved trust anchors.
[VALIDATION] IF trust_anchor IN trust_store AND trust_anchor NOT IN approved_list THEN violation

[RULE-04] Trust anchor approval MUST be documented and reviewed annually or when changes occur.
[VALIDATION] IF trust_anchor_approval_date > 365_days OR approval_documented = FALSE THEN violation

[RULE-05] Certificate service providers MUST be formally approved and reviewed annually for continued compliance.
[VALIDATION] IF provider_approval_date > 365_days OR provider_review_completed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Certificate Policy Management - Define and maintain organizational certificate issuance policies
- [PROC-02] Trust Anchor Approval - Process for evaluating and approving trust anchors
- [PROC-03] Service Provider Evaluation - Assessment and approval of external certificate providers
- [PROC-04] Trust Store Management - Configuration and maintenance of organizational trust stores

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents, provider changes, regulatory updates, technology changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unapproved Certificate Authority]
IF certificate_authority NOT IN approved_ca_list
AND certificates_issued_by_ca > 0
AND organization_managed_system = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Expired Trust Anchor Approval]
IF trust_anchor IN active_trust_store
AND approval_date < (current_date - 365_days)
AND renewal_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Third-Party Provider Without Approval]
IF certificate_source = "external_provider"
AND provider NOT IN approved_provider_list
AND certificate_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Internal Certificate Without Policy]
IF certificate_issued_internally = TRUE
AND certificate_policy_defined = FALSE
AND certificate_active = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Compliant PKI Implementation]
IF (certificate_policy_documented = TRUE OR approved_provider = TRUE)
AND trust_anchors_approved = TRUE
AND trust_store_contains_only_approved = TRUE
THEN compliance = TRUE
violation_severity = "None"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Public key certificates issued under defined policy OR obtained from approved provider | [RULE-01], [RULE-02] |
| Only approved trust anchors in organizational trust stores | [RULE-03], [RULE-04] |
| Service provider approval and oversight | [RULE-05] |