# POLICY: SI-4.22: Unauthorized Network Services

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.22 |
| NIST Control | SI-4.22: Unauthorized Network Services |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | network services, unauthorized services, service detection, network monitoring, service authorization, rogue services |

## 1. POLICY STATEMENT
The organization SHALL detect network services that have not been authorized through established approval processes and initiate audit activities when such services are identified. All network services must be properly authorized before deployment and continuously monitored for compliance.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Networks | YES | All production network segments |
| Development Networks | YES | Including test and staging environments |
| Cloud Services | YES | All cloud-hosted network services |
| Third-party Services | YES | Services accessed through organizational networks |
| IoT Devices | YES | Network-enabled devices and services |
| Guest Networks | CONDITIONAL | If they can access internal resources |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Deploy and maintain network service detection tools<br>• Monitor for unauthorized services<br>• Investigate detected unauthorized services |
| System Administrators | • Ensure all deployed services are properly authorized<br>• Report unauthorized service discoveries<br>• Implement service remediation actions |
| Security Operations Center | • Monitor detection alerts 24/7<br>• Initiate incident response for critical violations<br>• Maintain audit logs of detection events |

## 4. RULES
[RULE-01] All network services MUST be authorized through the formal service approval process before deployment to any organizational network.
[VALIDATION] IF service_deployed = TRUE AND authorization_status = "pending" OR "denied" OR "none" THEN violation

[RULE-02] Network service detection tools MUST be deployed on all network segments and configured to identify unauthorized services within 15 minutes of service activation.
[VALIDATION] IF detection_tool_coverage < 100% OR detection_time > 15_minutes THEN violation

[RULE-03] When unauthorized network services are detected, audit activities MUST be initiated within 1 hour of detection.
[VALIDATION] IF unauthorized_service_detected = TRUE AND audit_initiation_time > 1_hour THEN violation

[RULE-04] Unauthorized network services MUST be disabled or blocked within 4 hours of detection unless a documented exception is approved by the CISO.
[VALIDATION] IF service_status = "unauthorized" AND remediation_time > 4_hours AND ciso_exception = FALSE THEN violation

[RULE-05] Detection systems MUST maintain logs of all network service discovery activities for a minimum of 12 months.
[VALIDATION] IF log_retention_period < 12_months THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Network Service Authorization - Formal process for approving network services
- [PROC-02] Unauthorized Service Detection - Automated scanning and identification procedures
- [PROC-03] Service Audit Initiation - Steps for beginning audit activities upon detection
- [PROC-04] Service Remediation - Process for disabling or removing unauthorized services
- [PROC-05] Exception Handling - Procedures for managing temporary service exceptions

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving unauthorized services, major network changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Rogue Web Service]
IF service_type = "web_service"
AND authorization_status = "none"
AND network_location = "production"
AND detection_time > 15_minutes
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Approved Service Wrong Network]
IF service_type = "database"
AND authorization_status = "approved"
AND authorized_network = "development"
AND deployed_network = "production"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Delayed Audit Response]
IF unauthorized_service_detected = TRUE
AND detection_timestamp = "2024-01-15 10:00"
AND audit_initiation_timestamp = "2024-01-15 12:30"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Authorized Service with Monitoring]
IF service_type = "API_gateway"
AND authorization_status = "approved"
AND detection_coverage = TRUE
AND audit_logs_current = TRUE
THEN compliance = TRUE

[SCENARIO-05: Emergency Service Exception]
IF service_status = "unauthorized"
AND business_impact = "critical"
AND ciso_exception = TRUE
AND remediation_plan_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Network services authorization processes defined | [RULE-01] |
| Unauthorized network services detected | [RULE-02] |
| Audit initiated when unauthorized services detected | [RULE-03] |
| Service remediation procedures implemented | [RULE-04] |
| Detection activities logged and retained | [RULE-05] |