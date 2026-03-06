# POLICY: SC-7.22: Separate Subnets for Connecting to Different Security Domains

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.22 |
| NIST Control | SC-7.22: Separate Subnets for Connecting to Different Security Domains |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | network segmentation, subnets, security domains, network addresses, boundary protection |

## 1. POLICY STATEMENT
The organization SHALL implement separate network addresses and subnets to connect to systems operating in different security domains. Network segmentation MUST provide appropriate protection levels based on information security categories and classification levels.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Networks | YES | All networks handling regulated data |
| Development Networks | YES | When connecting to production domains |
| Cloud Infrastructure | YES | Multi-tenant and hybrid environments |
| Partner Networks | YES | External connections to different domains |
| Guest Networks | CONDITIONAL | Only if accessing internal resources |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Design and implement subnet segmentation<br>• Monitor cross-domain connections<br>• Validate network address separation |
| System Administrators | • Configure systems within assigned subnets<br>• Maintain subnet boundary controls<br>• Report cross-domain connection requests |
| Security Architecture Team | • Define security domain classifications<br>• Approve network segmentation designs<br>• Review subnet allocation requests |

## 4. RULES
[RULE-01] Systems in different security domains MUST be assigned to separate network subnets with distinct network address ranges.
[VALIDATION] IF system_domain_A != system_domain_B AND subnet_A = subnet_B THEN violation

[RULE-02] Network connections between different security domains MUST traverse controlled boundary protection mechanisms.
[VALIDATION] IF cross_domain_connection = TRUE AND boundary_control = FALSE THEN critical_violation

[RULE-03] Subnet allocation MUST align with data classification levels, with higher classification systems using more restrictive network segments.
[VALIDATION] IF data_classification = "restricted" AND subnet_type != "high_security" THEN violation

[RULE-04] Network address assignments MUST be documented and maintained in the network inventory with security domain mappings.
[VALIDATION] IF network_address_assigned = TRUE AND domain_mapping_documented = FALSE THEN violation

[RULE-05] Cross-domain network traffic MUST be logged and monitored for unauthorized connections.
[VALIDATION] IF cross_domain_traffic = TRUE AND logging_enabled = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Network Segmentation Design - Define subnet architecture based on security domains
- [PROC-02] Subnet Allocation Process - Assign network addresses according to security requirements
- [PROC-03] Cross-Domain Connection Review - Evaluate and approve inter-domain network connections
- [PROC-04] Network Inventory Management - Maintain current mapping of subnets to security domains

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New security domains, network architecture changes, security incidents involving cross-domain access

## 7. SCENARIO PATTERNS
[SCENARIO-01: Production-Development Connection]
IF source_domain = "production"
AND destination_domain = "development"
AND same_subnet = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Proper Domain Segmentation]
IF system_classification = "restricted"
AND subnet_type = "high_security"
AND boundary_controls = "enabled"
THEN compliance = TRUE

[SCENARIO-03: Undocumented Cross-Domain Traffic]
IF cross_domain_connection = TRUE
AND connection_documented = FALSE
AND monitoring_enabled = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Guest Network Isolation]
IF network_type = "guest"
AND internal_subnet_access = TRUE
AND security_controls = "standard"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Cloud Multi-Tenant Separation]
IF deployment_model = "cloud"
AND tenant_domains_different = TRUE
AND network_isolation = "logical_only"
AND data_classification = "restricted"
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Separate network addresses implemented for different security domains | [RULE-01] |
| Cross-domain connections properly controlled | [RULE-02] |
| Network segmentation aligned with classification levels | [RULE-03] |
| Network address assignments documented | [RULE-04] |
| Cross-domain traffic monitored | [RULE-05] |