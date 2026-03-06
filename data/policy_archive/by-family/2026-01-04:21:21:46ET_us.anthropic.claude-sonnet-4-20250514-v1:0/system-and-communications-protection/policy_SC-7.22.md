# POLICY: SC-7.22: Separate Subnets for Connecting to Different Security Domains

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.22 |
| NIST Control | SC-7.22: Separate Subnets for Connecting to Different Security Domains |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | network segmentation, subnets, security domains, network architecture, boundary protection |

## 1. POLICY STATEMENT
Systems connecting to different security domains MUST use separate network addresses and subnets to provide appropriate protection levels. Network segmentation SHALL be implemented based on data classification and security categorization to prevent unauthorized cross-domain access.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing classified/sensitive data |
| Development Systems | YES | When connecting to production domains |
| Cloud Infrastructure | YES | Multi-tenant and hybrid cloud environments |
| Network Equipment | YES | Routers, switches, firewalls managing domain connections |
| Third-party Connections | YES | External partner/vendor system connections |
| Administrative Networks | YES | Management interfaces crossing security domains |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Design and implement subnet segmentation architecture<br>• Configure network access controls between domains<br>• Monitor cross-domain traffic patterns |
| System Administrators | • Implement system-level network configurations<br>• Maintain accurate network documentation<br>• Report segmentation violations |
| Security Architecture Team | • Define security domain boundaries<br>• Approve network segmentation designs<br>• Review cross-domain connection requests |

## 4. RULES
[RULE-01] Systems in different security domains MUST use separate network address ranges with no overlapping IP spaces.
[VALIDATION] IF system_domain_A != system_domain_B AND network_range_overlap = TRUE THEN violation

[RULE-02] Cross-domain connections MUST traverse dedicated network segments with appropriate security controls.
[VALIDATION] IF cross_domain_connection = TRUE AND dedicated_segment = FALSE THEN violation

[RULE-03] Network segmentation design MUST be documented and approved before implementation.
[VALIDATION] IF segmentation_implemented = TRUE AND (documentation_exists = FALSE OR approval_status != "approved") THEN violation

[RULE-04] Security domain classifications MUST align with data classification levels and system categorization.
[VALIDATION] IF data_classification != domain_security_level THEN violation

[RULE-05] Subnet configurations MUST be reviewed and validated quarterly for compliance with segmentation requirements.
[VALIDATION] IF last_review_date > 90_days AND review_status != "compliant" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Network Domain Classification - Classify systems into appropriate security domains based on data sensitivity
- [PROC-02] Subnet Design and Implementation - Design and deploy network segmentation architecture
- [PROC-03] Cross-Domain Connection Approval - Review and approve requests for cross-domain connectivity
- [PROC-04] Segmentation Compliance Monitoring - Monitor and validate ongoing compliance with segmentation requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, architecture changes, new domain creation, compliance audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Production-Development Connection]
IF system_type = "production"
AND connection_target = "development"
AND separate_subnet = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Multi-Classification Environment]
IF data_classification_A = "confidential"
AND data_classification_B = "public"
AND shared_network_segment = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Cloud Multi-Tenancy]
IF deployment_type = "cloud"
AND tenant_security_domains > 1
AND network_isolation = "logical_only"
AND separate_subnets = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Third-Party Integration]
IF connection_type = "third_party"
AND security_domain = "internal"
AND dedicated_subnet = TRUE
AND access_controls = "implemented"
THEN compliance = TRUE

[SCENARIO-05: Administrative Access]
IF access_type = "administrative"
AND target_domains = "multiple"
AND management_subnet = "shared"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Separate network addresses implemented for different security domains | [RULE-01], [RULE-02] |
| Network segmentation aligns with security categorization | [RULE-04] |
| Cross-domain connections properly controlled | [RULE-02], [RULE-03] |
| Segmentation design documented and approved | [RULE-03] |
| Ongoing compliance validation | [RULE-05] |