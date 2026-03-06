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
The organization MUST implement separate network addresses and subnets to connect to systems in different security domains. Network segmentation SHALL ensure appropriate isolation between systems containing information with different security categories or classification levels.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All network infrastructure | YES | Including routers, switches, firewalls |
| Cloud networks (AWS VPCs, Azure VNets) | YES | Must follow same segmentation rules |
| System connections between domains | YES | Cross-domain connections require separate addressing |
| Development/Test networks | YES | Must be segmented from production |
| Guest/Public networks | YES | Must be isolated from internal domains |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Design and implement network segmentation architecture<br>• Monitor cross-domain connections<br>• Validate subnet isolation controls |
| System Administrators | • Configure systems with appropriate network addresses<br>• Ensure compliance with domain-specific addressing schemes<br>• Document network configurations |
| Security Architecture Team | • Define security domain classifications<br>• Approve network segmentation designs<br>• Review cross-domain connection requests |

## 4. RULES
[RULE-01] Systems in different security domains MUST be assigned separate network address ranges with no overlapping IP space.
[VALIDATION] IF system1_domain ≠ system2_domain AND network_overlap(system1_subnet, system2_subnet) = TRUE THEN violation

[RULE-02] Cross-domain connections MUST traverse dedicated network segments with appropriate security controls and monitoring.
[VALIDATION] IF connection_crosses_domains = TRUE AND dedicated_segment = FALSE THEN violation

[RULE-03] Network address assignments MUST align with the system's security classification and domain designation.
[VALIDATION] IF system_classification ≠ subnet_classification THEN violation

[RULE-04] Production systems MUST be on separate subnets from development and test environments.
[VALIDATION] IF system_env = "production" AND connected_system_env ∈ ["development", "test"] AND same_subnet = TRUE THEN violation

[RULE-05] Guest and public-facing networks MUST be isolated on separate subnets with no direct access to internal domains.
[VALIDATION] IF network_type = "guest" AND direct_access_to_internal = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Network Segmentation Design - Define subnet architecture based on security domains
- [PROC-02] IP Address Management - Assign and track network addresses by security domain
- [PROC-03] Cross-Domain Connection Approval - Review and approve connections between security domains
- [PROC-04] Network Configuration Review - Validate segmentation implementation and controls

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New security domain creation, network architecture changes, security incidents involving cross-domain access

## 7. SCENARIO PATTERNS
[SCENARIO-01: Production-Development Connection]
IF system1_environment = "production"
AND system2_environment = "development"
AND same_subnet = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Cross-Classification Access]
IF system1_classification = "confidential"
AND system2_classification = "public"
AND network_separation = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Guest Network Isolation]
IF network_type = "guest"
AND internal_network_access = TRUE
AND dedicated_segment = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Cloud Environment Segmentation]
IF deployment_type = "cloud"
AND security_domain_1 ≠ security_domain_2
AND vpc_separation = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Domain Segmentation]
IF system1_domain ≠ system2_domain
AND separate_subnets = TRUE
AND appropriate_controls = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Separate network addresses implemented for different security domains | RULE-01, RULE-03 |
| Cross-domain connections properly controlled | RULE-02 |
| Production environment isolation | RULE-04 |
| Guest network segregation | RULE-05 |