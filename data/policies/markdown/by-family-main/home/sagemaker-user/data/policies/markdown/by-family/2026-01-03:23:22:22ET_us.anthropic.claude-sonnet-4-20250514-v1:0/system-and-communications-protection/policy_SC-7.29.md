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
The organization MUST implement physically separate subnetworks to isolate critical system components and functions from non-critical systems. Critical system components requiring isolation SHALL be formally defined and documented based on criticality analysis and business impact assessment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Networks | YES | All production environments |
| Development Networks | YES | When hosting critical system components |
| Test Networks | CONDITIONAL | Only if processing production data |
| Guest Networks | NO | Isolated by design |
| Partner Networks | CONDITIONAL | Based on data classification |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Design and implement physical subnet separation<br>• Maintain network segmentation documentation<br>• Monitor cross-subnet traffic |
| System Architects | • Define critical system components requiring isolation<br>• Conduct criticality analysis<br>• Approve network architecture designs |
| Infrastructure Team | • Implement physical network separation<br>• Maintain subnet configurations<br>• Execute network changes |

## 4. RULES

[RULE-01] Critical system components and functions MUST be identified through formal criticality analysis and documented in the system security plan.
[VALIDATION] IF system_component = "critical" AND criticality_analysis_completed = FALSE THEN violation

[RULE-02] Physically separate subnetworks MUST be implemented to isolate each defined critical system component from non-critical components.
[VALIDATION] IF critical_component_isolated = FALSE AND physical_separation = FALSE THEN critical_violation

[RULE-03] Network traffic between critical and non-critical subnets MUST be blocked by default with explicit allow rules only for required business functions.
[VALIDATION] IF default_deny_policy = FALSE OR undocumented_traffic_flows > 0 THEN violation

[RULE-04] Cross-subnet communication rules MUST be documented, approved by system architects, and reviewed quarterly.
[VALIDATION] IF communication_rules_documented = FALSE OR last_review > 90_days THEN violation

[RULE-05] Physical network infrastructure supporting critical subnets MUST be separate from non-critical infrastructure including switches, routers, and cabling.
[VALIDATION] IF shared_physical_infrastructure = TRUE AND system_criticality = "critical" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Criticality Analysis - Systematic evaluation and classification of system components
- [PROC-02] Network Segmentation Design - Architecture review and approval process
- [PROC-03] Subnet Configuration Management - Change control for network isolation settings
- [PROC-04] Cross-Subnet Traffic Monitoring - Continuous monitoring of isolation effectiveness

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, architecture changes, new critical systems deployment

## 7. SCENARIO PATTERNS

[SCENARIO-01: Payment Processing Isolation]
IF system_function = "payment_processing"
AND pci_dss_applicable = TRUE
AND physical_subnet_separation = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Command and Control Separation]
IF system_type = "industrial_control"
AND safety_critical = TRUE
AND shared_network_infrastructure = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Development Environment Access]
IF environment = "development"
AND production_data_present = TRUE
AND subnet_isolation = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Administrative Network Isolation]
IF function = "system_administration"
AND privileged_access = TRUE
AND physical_separation = TRUE
AND documented_criticality = TRUE
THEN compliance = TRUE

[SCENARIO-05: Shared Infrastructure Exception]
IF shared_physical_infrastructure = TRUE
AND formal_risk_acceptance = TRUE
AND compensating_controls = "implemented"
AND system_criticality = "moderate"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Critical components identified and documented | [RULE-01] |
| Physical subnetwork separation implemented | [RULE-02] |
| Cross-subnet traffic controls | [RULE-03] |
| Communication rules documented and reviewed | [RULE-04] |
| Physical infrastructure separation | [RULE-05] |