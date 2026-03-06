# POLICY: SC-7.29: Separate Subnets to Isolate Functions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.29 |
| NIST Control | SC-7.29: Separate Subnets to Isolate Functions |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | network segmentation, subnet isolation, critical systems, physical separation, network architecture |

## 1. POLICY STATEMENT
The organization MUST implement physically separate subnetworks to isolate critical system components and functions from non-critical components. Physical separation of network segments reduces the risk of catastrophic system compromise by preventing lateral movement between critical and non-critical functions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical system components | YES | As defined in criticality analysis |
| Production networks | YES | All production environments |
| Development/test networks | CONDITIONAL | Only if processing critical data |
| Guest networks | NO | Already isolated by design |
| Management networks | YES | Critical infrastructure function |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Define critical system components requiring isolation<br>• Design physically separate subnet architecture<br>• Implement and maintain network segmentation controls |
| System Administrators | • Configure subnet isolation according to approved designs<br>• Monitor network traffic between segments<br>• Maintain documentation of network topology |
| Security Architecture Team | • Conduct criticality analysis of system components<br>• Review and approve network segmentation designs<br>• Validate isolation effectiveness through testing |

## 4. RULES
[RULE-01] Critical system components and functions MUST be isolated using physically separate subnetworks with no direct network connectivity to non-critical components.
[VALIDATION] IF critical_component = TRUE AND physical_separation = FALSE THEN violation

[RULE-02] Organizations MUST maintain a documented criticality analysis that defines which system components and functions require physical subnet isolation.
[VALIDATION] IF criticality_analysis_exists = FALSE OR last_update > 12_months THEN violation

[RULE-03] Cross-subnet communication between critical and non-critical components MUST traverse approved security controls including firewalls, proxies, or air-gapped transfer mechanisms.
[VALIDATION] IF direct_connectivity = TRUE AND approved_controls = FALSE THEN critical_violation

[RULE-04] Physical network infrastructure supporting critical subnets MUST use dedicated hardware components that do not serve non-critical functions.
[VALIDATION] IF shared_infrastructure = TRUE AND component_criticality = "critical" THEN violation

[RULE-05] Network topology documentation MUST be updated within 30 days of any changes to critical subnet isolation architecture.
[VALIDATION] IF topology_change_date - documentation_update_date > 30_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Criticality Analysis - Annual assessment to identify components requiring isolation
- [PROC-02] Network Segmentation Design - Architecture review process for subnet isolation
- [PROC-03] Isolation Testing - Quarterly validation of physical separation effectiveness
- [PROC-04] Emergency Bridge Procedures - Controlled temporary connectivity for critical incidents

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annual
- Procedure review frequency: Semi-annual
- Triggering events: Security incidents involving lateral movement, major system changes, criticality analysis updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Database on Shared Infrastructure]
IF system_criticality = "critical"
AND physical_infrastructure = "shared"
AND isolation_mechanism = "VLAN_only"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Approved Air-Gapped Transfer]
IF source_subnet = "critical"
AND destination_subnet = "non_critical"
AND transfer_method = "air_gapped"
AND approval_documented = TRUE
THEN compliance = TRUE

[SCENARIO-03: Outdated Criticality Analysis]
IF criticality_analysis_date < current_date - 365_days
AND critical_components_defined = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Emergency Direct Connection]
IF connection_type = "direct"
AND justification = "emergency"
AND approval_level = "CISO"
AND duration > 72_hours
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Command and Control Isolation]
IF function_type = "command_control"
AND entertainment_network_access = TRUE
AND physical_separation = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Subnetworks are separated physically to isolate critical system components | [RULE-01], [RULE-04] |
| Critical system components and functions are defined | [RULE-02] |
| Physical separation reduces catastrophic breach risk | [RULE-03], [RULE-04] |
| Isolation architecture is documented and maintained | [RULE-05] |