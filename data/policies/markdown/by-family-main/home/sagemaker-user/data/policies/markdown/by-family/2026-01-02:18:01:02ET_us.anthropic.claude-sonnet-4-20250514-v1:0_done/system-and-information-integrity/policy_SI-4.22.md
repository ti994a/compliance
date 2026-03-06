# POLICY: SI-4.22: Unauthorized Network Services

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.22 |
| NIST Control | SI-4.22: Unauthorized Network Services |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | network services, unauthorized services, service monitoring, network detection, service approval |

## 1. POLICY STATEMENT
The organization SHALL implement continuous monitoring to detect unauthorized or unapproved network services and initiate audit processes when such services are identified. All network services MUST be properly authorized through established approval processes before deployment.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All network services | YES | Including SOA, microservices, APIs |
| Cloud services | YES | Both public and private cloud |
| Third-party services | YES | Requires vendor validation |
| Development environments | YES | Including test and staging |
| Legacy systems | YES | Gradual compliance required |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Deploy detection tools<br>• Monitor for unauthorized services<br>• Investigate detected violations |
| Service Owners | • Obtain proper authorization<br>• Maintain service documentation<br>• Report service changes |
| IT Operations | • Implement monitoring controls<br>• Generate audit logs<br>• Respond to alerts |

## 4. RULES

[RULE-01] All network services MUST be authorized through the formal service approval process before deployment to production environments.
[VALIDATION] IF service_deployed = TRUE AND authorization_status != "approved" THEN violation

[RULE-02] Network monitoring tools MUST be configured to detect unauthorized services within 15 minutes of service activation.
[VALIDATION] IF detection_time > 15_minutes AND service_unauthorized = TRUE THEN violation

[RULE-03] Audit processes MUST be initiated within 1 hour of detecting unauthorized network services.
[VALIDATION] IF unauthorized_service_detected = TRUE AND audit_initiated_time > 1_hour THEN violation

[RULE-04] Service-oriented architecture components SHALL NOT be deployed without organizational verification and validation.
[VALIDATION] IF service_type = "SOA" AND (verification_status != "complete" OR validation_status != "complete") THEN critical_violation

[RULE-05] Network service inventory MUST be updated within 24 hours of any authorized service deployment or decommissioning.
[VALIDATION] IF service_change_date + 24_hours < current_time AND inventory_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Network Service Authorization - Formal approval workflow for new services
- [PROC-02] Continuous Service Monitoring - Automated detection and alerting procedures
- [PROC-03] Unauthorized Service Response - Incident response for detected violations
- [PROC-04] Service Inventory Management - Maintaining accurate service catalogs

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, architecture changes, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unauthorized Microservice Deployment]
IF service_type = "microservice"
AND deployment_environment = "production"
AND authorization_status = "pending"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unvalidated Third-Party Service]
IF service_provider = "external"
AND validation_completed = FALSE
AND service_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Shadow IT Service Discovery]
IF service_discovered_by = "monitoring_tool"
AND service_in_inventory = FALSE
AND detection_to_audit_time <= 1_hour
THEN compliance = TRUE

[SCENARIO-04: Legacy Service Without Documentation]
IF service_age > 2_years
AND authorization_documentation = "missing"
AND remediation_plan_exists = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Development Service in Production]
IF service_classification = "development"
AND network_segment = "production"
AND business_justification = "none"
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Network services authorization/approval processes defined | RULE-01 |
| Unauthorized network services are detected | RULE-02 |
| Audit initiated when unauthorized services detected | RULE-03 |
| SOA services properly verified and validated | RULE-04 |
| Service inventory maintained | RULE-05 |