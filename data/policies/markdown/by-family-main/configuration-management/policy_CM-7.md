# POLICY: CM-7: Least Functionality

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-7 |
| NIST Control | CM-7: Least Functionality |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | least functionality, mission-essential, prohibited services, restricted ports, system hardening |

## 1. POLICY STATEMENT
All information systems SHALL be configured to provide only mission-essential capabilities required for business operations. Organizations MUST prohibit or restrict the use of non-essential functions, ports, protocols, software, and services to minimize attack surface and security risks.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All production information systems |
| Development Systems | YES | When processing production data |
| Test Systems | CONDITIONAL | When connected to production networks |
| Personal Devices | YES | When accessing corporate resources |
| Third-party Systems | YES | When integrated with corporate systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure systems per approved baselines<br>• Disable unnecessary services and ports<br>• Document approved exceptions |
| Security Team | • Define prohibited/restricted functions<br>• Review system configurations<br>• Monitor for unauthorized services |
| System Owners | • Define mission-essential capabilities<br>• Approve configuration baselines<br>• Maintain capability inventories |

## 4. RULES

[RULE-01] Systems MUST be configured using approved secure configuration baselines that define only mission-essential capabilities.
[VALIDATION] IF system_baseline ≠ approved_baseline THEN violation

[RULE-02] Prohibited functions, ports, protocols, software, and services MUST be documented in an organizational restriction list and updated annually.
[VALIDATION] IF restriction_list_age > 365_days THEN violation

[RULE-03] Systems MUST NOT run services, protocols, or software identified on the organizational prohibition list.
[VALIDATION] IF prohibited_service = active AND exception_approved = FALSE THEN critical_violation

[RULE-04] Restricted capabilities MAY only be enabled with documented business justification and security approval.
[VALIDATION] IF restricted_capability = enabled AND (business_justification = NULL OR security_approval = NULL) THEN violation

[RULE-05] System capability inventories MUST be maintained and reviewed quarterly to identify unauthorized functions.
[VALIDATION] IF capability_inventory_age > 90_days THEN violation

[RULE-06] Network scanning MUST be performed monthly to detect unauthorized services and open ports.
[VALIDATION] IF last_network_scan > 30_days THEN violation

[RULE-07] Unused physical and logical ports MUST be disabled or physically secured.
[VALIDATION] IF port_status = unused AND port_state = enabled THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Hardening Procedure - Standardized process for implementing secure baselines
- [PROC-02] Service Exception Management - Process for requesting and approving restricted capabilities
- [PROC-03] Network Scanning Procedure - Regular scanning for unauthorized services and ports
- [PROC-04] Capability Inventory Management - Quarterly review of system functions and services

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents, system changes, new threat intelligence, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unauthorized Service Discovery]
IF network_scan_results = "unauthorized_service_detected"
AND service_type ∈ prohibited_list
AND exception_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Legacy System Exception]
IF system_type = "legacy"
AND restricted_protocol = enabled
AND business_justification = documented
AND security_approval = current
AND compensating_controls = implemented
THEN compliance = TRUE

[SCENARIO-03: Development System Exposure]
IF system_environment = "development"
AND network_connection = "production"
AND unnecessary_services > 0
AND hardening_applied = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Quarterly Review Overdue]
IF capability_inventory_last_review > 90_days
AND system_criticality = "high"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Emergency Service Activation]
IF restricted_service = enabled
AND activation_reason = "emergency"
AND temporary_approval = documented
AND review_scheduled ≤ 72_hours
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Mission-essential capabilities defined | [RULE-01], [RULE-05] |
| Prohibited functions restricted | [RULE-02], [RULE-03] |
| Prohibited ports restricted | [RULE-02], [RULE-03], [RULE-07] |
| Prohibited protocols restricted | [RULE-02], [RULE-03] |
| Prohibited software restricted | [RULE-02], [RULE-03] |
| Prohibited services restricted | [RULE-02], [RULE-03] |