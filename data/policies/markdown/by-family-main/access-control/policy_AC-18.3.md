# POLICY: AC-18.3: Disable Wireless Networking

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-18.3 |
| NIST Control | AC-18.3: Disable Wireless Networking |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | wireless, networking, embedded, disable, deployment, issuance |

## 1. POLICY STATEMENT
All wireless networking capabilities embedded within system components MUST be disabled prior to issuance and deployment when not intended for organizational use. This requirement applies to reduce attack surface and prevent unauthorized wireless access vectors.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT equipment with embedded wireless | YES | Includes laptops, desktops, servers, IoT devices |
| Network infrastructure devices | YES | Routers, switches, access points with unused wireless |
| Mobile devices | CONDITIONAL | Only if wireless features not required for business function |
| Guest/visitor devices | NO | Managed through separate guest access policies |
| Personal devices (BYOD) | NO | Covered under separate BYOD policies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Asset Management | • Inventory all devices with wireless capabilities<br>• Coordinate wireless capability assessment<br>• Track deployment status and configurations |
| System Administrators | • Disable unused wireless capabilities before deployment<br>• Document wireless configuration decisions<br>• Maintain configuration baselines |
| Security Team | • Define wireless usage requirements<br>• Validate wireless disablement procedures<br>• Monitor compliance through audits |

## 4. RULES

[RULE-01] System components with embedded wireless networking capabilities MUST have unused wireless features disabled prior to organizational issuance and deployment.
[VALIDATION] IF device_has_wireless = TRUE AND wireless_required = FALSE AND wireless_disabled = FALSE THEN violation

[RULE-02] Wireless capability assessment MUST be completed and documented for all system components during the procurement and deployment process.
[VALIDATION] IF deployment_status = "pending" AND wireless_assessment_completed = FALSE THEN violation

[RULE-03] Exceptions for enabling wireless capabilities MUST be documented with business justification and approved by the Information System Security Officer.
[VALIDATION] IF wireless_enabled = TRUE AND (business_justification = NULL OR isso_approval = FALSE) THEN violation

[RULE-04] Deployed systems MUST be audited quarterly to verify wireless capabilities remain properly configured according to organizational requirements.
[VALIDATION] IF last_wireless_audit > 90_days THEN violation

[RULE-05] System configuration baselines MUST specify the required state (enabled/disabled) for all wireless networking capabilities.
[VALIDATION] IF system_baseline_exists = FALSE OR wireless_config_specified = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Wireless Capability Assessment - Systematic evaluation of wireless features during asset intake
- [PROC-02] Wireless Disablement Process - Technical procedures for disabling wireless on various device types  
- [PROC-03] Configuration Baseline Management - Maintenance of approved wireless configuration standards
- [PROC-04] Quarterly Wireless Audit - Verification of ongoing compliance with wireless policies

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: New device types, security incidents involving wireless, regulatory changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Standard Laptop Deployment]
IF device_type = "laptop"
AND wireless_capability = TRUE
AND business_use_case = "office_work_only"
AND wireless_disabled = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Server with Unused Wireless]
IF device_type = "server"
AND embedded_wireless = TRUE
AND wireless_business_need = FALSE
AND wireless_disabled = TRUE
AND baseline_documented = TRUE
THEN compliance = TRUE

[SCENARIO-03: IoT Device Deployment]
IF device_type = "IoT"
AND wireless_capability = TRUE
AND deployment_approved = TRUE
AND wireless_assessment = NULL
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Approved Wireless Exception]
IF wireless_enabled = TRUE
AND business_justification = "documented"
AND isso_approval = TRUE
AND security_controls_implemented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Missing Configuration Baseline]
IF system_deployed = TRUE
AND wireless_capability = TRUE
AND configuration_baseline = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Wireless networking capabilities are disabled when not intended for use prior to issuance and deployment | RULE-01, RULE-02, RULE-05 |
| Proper documentation and approval process for wireless exceptions | RULE-03 |
| Ongoing verification of wireless configuration compliance | RULE-04 |