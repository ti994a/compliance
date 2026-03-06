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
The organization SHALL establish and maintain a Public Key Infrastructure (PKI) certificate management program that ensures all public key certificates are issued under defined certificate policies or obtained from approved service providers. Only approved trust anchors SHALL be included in organizational trust stores and certificate stores.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal PKI Systems | YES | All organizational certificate authorities |
| External Certificate Providers | YES | Must be pre-approved vendors |
| Application Certificate Stores | YES | Including time services and internal apps |
| User Workstations | YES | Managed trust stores only |
| Mobile Devices | YES | Enterprise-managed devices |
| Third-party Systems | CONDITIONAL | Only if integrated with org PKI |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| PKI Administrator | • Maintain certificate policies<br>• Manage internal certificate authorities<br>• Approve trust anchor additions/removals |
| Security Operations | • Monitor certificate compliance<br>• Validate service provider approvals<br>• Audit trust store configurations |
| System Administrators | • Implement trust store configurations<br>• Request certificates per policy<br>• Report certificate violations |

## 4. RULES

[RULE-01] All public key certificates MUST be issued under a documented certificate policy that defines issuance criteria, validation procedures, and lifecycle management requirements.
[VALIDATION] IF certificate_issued = TRUE AND certificate_policy_documented = FALSE THEN violation

[RULE-02] Public key certificates obtained from external sources MUST be from service providers approved by the organization's PKI governance board.
[VALIDATION] IF certificate_source = "external" AND provider_approved = FALSE THEN violation

[RULE-03] Trust stores and certificate stores managed by the organization MUST contain only trust anchors that have been explicitly approved through the formal trust anchor approval process.
[VALIDATION] IF trust_anchor_in_store = TRUE AND approval_status != "approved" THEN violation

[RULE-04] Certificate policies MUST be reviewed and updated annually or when significant changes occur to cryptographic standards or organizational requirements.
[VALIDATION] IF last_policy_review > 365_days AND no_triggering_event = TRUE THEN violation

[RULE-05] All trust anchor additions, modifications, or removals MUST be documented with business justification and approved by the PKI Administrator.
[VALIDATION] IF trust_anchor_change = TRUE AND (documentation = FALSE OR approval = FALSE) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Certificate Policy Development - Establish and maintain comprehensive certificate policies
- [PROC-02] Service Provider Evaluation - Assess and approve external certificate service providers  
- [PROC-03] Trust Anchor Management - Control addition/removal of trust anchors in organizational stores
- [PROC-04] Certificate Lifecycle Management - Manage certificate issuance, renewal, and revocation
- [PROC-05] Trust Store Auditing - Regular verification of trust store contents

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Changes to cryptographic standards, new compliance requirements, security incidents involving PKI

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unauthorized Trust Anchor]
IF trust_anchor_present = TRUE
AND approval_documentation = FALSE
AND discovery_method = "audit"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: External Certificate from Unapproved Provider]
IF certificate_source = "external"
AND provider_approval_status = "pending"
AND certificate_deployed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing Certificate Policy]
IF internal_ca_active = TRUE
AND certificate_policy_exists = FALSE
AND certificates_issued > 0
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Outdated Certificate Policy]
IF certificate_policy_last_review > 365_days
AND crypto_standards_updated = TRUE
AND policy_review_triggered = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Approved PKI Configuration]
IF certificate_policy_documented = TRUE
AND all_providers_approved = TRUE
AND trust_anchors_approved = TRUE
AND annual_review_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Public key certificates issued under defined certificate policy | [RULE-01] |
| Public key certificates obtained from approved service provider | [RULE-02] |
| Only approved trust anchors in organizational trust stores | [RULE-03] |