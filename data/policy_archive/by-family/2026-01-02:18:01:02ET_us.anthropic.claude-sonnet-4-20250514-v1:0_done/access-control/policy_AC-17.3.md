# POLICY: AC-17.3: Managed Access Control Points

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-17.3 |
| NIST Control | AC-17.3: Managed Access Control Points |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | remote access, network access control, TIC, trusted internet connections, managed endpoints |

## 1. POLICY STATEMENT
All remote access to organizational systems MUST be routed through authorized and managed network access control points. Organizations SHALL implement centralized access control mechanisms to reduce attack surfaces and maintain visibility over remote connections.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All remote users | YES | Employees, contractors, partners |
| VPN connections | YES | All remote network access |
| Cloud services | YES | When accessing internal systems |
| Emergency access | CONDITIONAL | Must use alternate managed control points |
| Physical office access | NO | Covered under physical security controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Maintain authorized access control points<br>• Monitor routing compliance<br>• Configure access control mechanisms |
| System Administrators | • Implement routing configurations<br>• Maintain system documentation<br>• Report unauthorized access attempts |
| Security Operations Center | • Monitor remote access patterns<br>• Investigate routing violations<br>• Maintain access logs |

## 4. RULES
[RULE-01] All remote access connections MUST be routed through pre-authorized and managed network access control points only.
[VALIDATION] IF remote_connection = TRUE AND access_point NOT IN authorized_control_points THEN violation

[RULE-02] Organizations SHALL maintain a documented list of all authorized network access control points with designated owners.
[VALIDATION] IF access_control_point EXISTS AND documented = FALSE THEN violation

[RULE-03] Unauthorized network access control points MUST be blocked and reported within 4 hours of detection.
[VALIDATION] IF unauthorized_access_point_detected = TRUE AND response_time > 4_hours THEN violation

[RULE-04] Remote access routing configurations MUST be reviewed and validated quarterly.
[VALIDATION] IF last_routing_review > 90_days THEN violation

[RULE-05] Emergency access procedures MUST specify alternate managed control points and require security approval within 24 hours.
[VALIDATION] IF emergency_access = TRUE AND approval_time > 24_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Network Access Control Point Authorization - Process for approving and documenting authorized control points
- [PROC-02] Remote Access Routing Validation - Quarterly verification of routing configurations
- [PROC-03] Unauthorized Access Point Response - Incident response for detecting bypass attempts
- [PROC-04] Emergency Access Management - Procedures for emergency access through alternate control points

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving access bypass, infrastructure changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Direct Internet Access Bypass]
IF remote_user = TRUE
AND connection_path = "direct_internet"
AND authorized_control_point = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Approved VPN Gateway Usage]
IF remote_user = TRUE
AND connection_path = "corporate_vpn"
AND vpn_gateway IN authorized_control_points
AND routing_validated = TRUE
THEN compliance = TRUE

[SCENARIO-03: Unauthorized Personal VPN]
IF employee_connection = TRUE
AND connection_method = "personal_vpn"
AND corporate_traffic = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Cloud Service Access Routing]
IF cloud_service_access = TRUE
AND access_point = "managed_cloud_gateway"
AND gateway_authorized = TRUE
THEN compliance = TRUE

[SCENARIO-05: Emergency Access Scenario]
IF emergency_access = TRUE
AND alternate_control_point = "approved_emergency_gateway"
AND security_approval < 24_hours
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Remote accesses routed through authorized control points | RULE-01, RULE-02 |
| Managed network access control implementation | RULE-03, RULE-04 |
| Emergency access management | RULE-05 |
| Documentation and validation requirements | RULE-02, RULE-04 |