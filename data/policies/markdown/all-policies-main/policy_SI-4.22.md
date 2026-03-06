# POLICY: SI-4.22: Unauthorized Network Services

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.22 |
| NIST Control | SI-4.22: Unauthorized Network Services |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | network services, unauthorized services, service detection, network monitoring, service authorization |

## 1. POLICY STATEMENT
The organization must continuously monitor and detect network services that have not been authorized through established approval processes. All unauthorized network services must be audited and remediated immediately upon detection.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Network Infrastructure | YES | Including cloud, on-premises, and hybrid environments |
| Third-party Network Services | YES | Services accessed through organizational networks |
| Development/Test Networks | YES | Must follow same authorization requirements |
| Guest Networks | CONDITIONAL | Only if connected to corporate infrastructure |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Deploy and maintain network service detection tools<br>• Monitor for unauthorized services<br>• Investigate security alerts<br>• Maintain service authorization database |
| System Administrators | • Report discovered network services<br>• Implement remediation actions<br>• Maintain current service inventories |
| Service Owners | • Submit authorization requests for new services<br>• Maintain service documentation<br>• Ensure compliance with approval processes |

## 4. RULES
[RULE-01] All network services operating within organizational infrastructure MUST be authorized through the formal service approval process before deployment.
[VALIDATION] IF service_status = "active" AND authorization_status = "pending" OR authorization_status = "denied" THEN violation

[RULE-02] Network monitoring systems MUST scan for unauthorized services at least every 24 hours across all network segments.
[VALIDATION] IF last_scan_time > 24_hours THEN violation

[RULE-03] Unauthorized network services MUST be documented and audited within 4 hours of detection.
[VALIDATION] IF unauthorized_service_detected = TRUE AND audit_initiated_time > 4_hours THEN violation

[RULE-04] Critical unauthorized services MUST be disabled within 2 hours of detection, non-critical services within 24 hours.
[VALIDATION] IF service_criticality = "high" AND unauthorized = TRUE AND disable_time > 2_hours THEN critical_violation
[VALIDATION] IF service_criticality = "low" AND unauthorized = TRUE AND disable_time > 24_hours THEN violation

[RULE-05] Service authorization database MUST be updated within 1 hour of any service approval or denial decision.
[VALIDATION] IF approval_decision_time + 1_hour < current_time AND database_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Network Service Authorization - Formal process for requesting and approving new network services
- [PROC-02] Unauthorized Service Detection - Automated scanning and manual verification procedures
- [PROC-03] Incident Response for Unauthorized Services - Response procedures including containment and remediation
- [PROC-04] Service Inventory Management - Maintaining accurate records of authorized services

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving unauthorized services, infrastructure changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Web Service Discovery]
IF service_type = "web_service"
AND authorization_status = "none"
AND detection_time < 4_hours_ago
AND audit_initiated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Approved Service with Expired Authorization]
IF service_status = "active"
AND authorization_expiry_date < current_date
AND renewal_request = "not_submitted"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Critical Unauthorized Service Response]
IF service_criticality = "critical"
AND authorization_status = "unauthorized"
AND detection_time > 2_hours_ago
AND service_status = "active"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Compliant Service Detection Process]
IF monitoring_scan_frequency <= 24_hours
AND unauthorized_service_detected = TRUE
AND audit_initiated_time <= 4_hours
AND remediation_plan = "documented"
THEN compliance = TRUE

[SCENARIO-05: Development Network Unauthorized Service]
IF network_segment = "development"
AND service_authorization = "production_only"
AND service_status = "active"
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Network services authorization detection | RULE-01, RULE-02 |
| Audit initiation upon detection | RULE-03 |
| Authorization/approval process definition | RULE-01, RULE-05 |
| Continuous monitoring implementation | RULE-02 |
| Unauthorized service remediation | RULE-04 |