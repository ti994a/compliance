# POLICY: SC-17: Public Key Infrastructure Certificates

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-17 |
| NIST Control | SC-17: Public Key Infrastructure Certificates |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | PKI, certificates, trust anchors, certificate authority, cryptographic systems |

## 1. POLICY STATEMENT
The organization SHALL establish and maintain a comprehensive public key infrastructure certificate management program that ensures all PKI certificates are issued under defined certificate policies or obtained from approved service providers. Only approved trust anchors SHALL be included in organizational trust stores and certificate stores.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Including cloud and hybrid infrastructure |
| External-facing certificates | YES | Certificates with external visibility |
| Internal operational certificates | YES | Application-specific and time services |
| Third-party service providers | CONDITIONAL | Only approved PKI service providers |
| Employee personal devices | CONDITIONAL | Only when accessing organizational resources |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| PKI Administrator | • Manage certificate lifecycle<br>• Maintain trust stores<br>• Validate certificate policies<br>• Monitor certificate expiration |
| Security Team | • Approve trust anchors<br>• Review certificate policies<br>• Conduct compliance assessments<br>• Manage service provider approvals |
| System Administrators | • Implement PKI certificates<br>• Configure trust stores<br>• Report certificate issues<br>• Maintain certificate inventories |

## 4. RULES
[RULE-01] All public key certificates MUST be issued under a documented certificate policy that defines issuance, validation, and revocation procedures.
[VALIDATION] IF certificate_issued = TRUE AND certificate_policy_documented = FALSE THEN violation

[RULE-02] Public key certificates MAY be obtained from approved service providers only if the provider appears on the organizational approved vendor list.
[VALIDATION] IF certificate_source = "external_provider" AND provider_approved = FALSE THEN violation

[RULE-03] Trust stores and certificate stores MUST contain only approved trust anchors as defined in the organizational trust anchor registry.
[VALIDATION] IF trust_anchor IN trust_store AND trust_anchor_approved = FALSE THEN critical_violation

[RULE-04] Certificate policies MUST be reviewed and updated at least annually or when significant changes occur to PKI infrastructure.
[VALIDATION] IF certificate_policy_last_review > 365_days THEN violation

[RULE-05] All PKI certificates MUST be inventoried and tracked through their complete lifecycle from issuance to expiration or revocation.
[VALIDATION] IF certificate_in_production = TRUE AND certificate_in_inventory = FALSE THEN violation

[RULE-06] Certificate expiration monitoring MUST provide alerts at 90, 30, and 7 days before expiration for all certificates.
[VALIDATION] IF certificate_expires_in <= 90_days AND alert_sent = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Certificate Policy Development - Establish comprehensive policies for PKI certificate lifecycle management
- [PROC-02] Trust Anchor Management - Define processes for approving, implementing, and removing trust anchors
- [PROC-03] Service Provider Evaluation - Assess and approve external PKI service providers
- [PROC-04] Certificate Inventory Management - Maintain complete inventory of all organizational certificates
- [PROC-05] Certificate Renewal Process - Ensure timely renewal of certificates before expiration

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: PKI infrastructure changes, security incidents involving certificates, regulatory requirement changes, service provider changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unapproved Trust Anchor]
IF trust_anchor_added_to_store = TRUE
AND trust_anchor_in_approved_registry = FALSE
AND business_justification_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: External Certificate Provider]
IF certificate_obtained_from_external = TRUE
AND provider_on_approved_list = TRUE
AND certificate_policy_compliant = TRUE
THEN compliance = TRUE

[SCENARIO-03: Expired Certificate in Production]
IF certificate_status = "expired"
AND certificate_in_production_use = TRUE
AND expiration_date < current_date
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Missing Certificate Policy]
IF certificate_issued = TRUE
AND certificate_type = "organizational"
AND certificate_policy_exists = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Untracked Certificate Discovery]
IF certificate_discovered_in_scan = TRUE
AND certificate_in_inventory = FALSE
AND certificate_age > 30_days
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Public key certificates issued under defined certificate policy | [RULE-01] |
| Public key certificates obtained from approved service provider | [RULE-02] |
| Only approved trust anchors in trust stores | [RULE-03] |
| Certificate policy documentation and maintenance | [RULE-04] |
| Complete certificate lifecycle management | [RULE-05] |