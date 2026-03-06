# POLICY: SC-7.3: Access Points

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.3 |
| NIST Control | SC-7.3: Access Points |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | external connections, network access points, boundary protection, connection limits, network monitoring |

## 1. POLICY STATEMENT
The organization SHALL limit the number of external network connections to information systems to facilitate effective monitoring and reduce attack surface. All external network connections MUST be documented, approved, and regularly reviewed for necessity and security compliance.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing organizational data |
| Development Systems | YES | If connected to external networks |
| Test/Staging Systems | YES | If connected to external networks |
| Isolated Lab Systems | NO | Systems with no external connectivity |
| Third-party SaaS | CONDITIONAL | If direct network integration required |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Maintain external connection inventory<br>• Review and approve new external connections<br>• Monitor connection usage and security |
| System Administrators | • Document system external connections<br>• Implement approved connection configurations<br>• Report unauthorized connections |
| CISO | • Approve external connection limits policy<br>• Review high-risk external connections<br>• Ensure compliance monitoring |

## 4. RULES
[RULE-01] Each information system MUST have a documented maximum limit for external network connections based on business requirements and risk assessment.
[VALIDATION] IF system_external_connections > documented_limit THEN violation

[RULE-02] All external network connections MUST be documented in the enterprise connection inventory within 24 hours of establishment.
[VALIDATION] IF connection_established = TRUE AND inventory_updated = FALSE AND hours_elapsed > 24 THEN violation

[RULE-03] External network connections SHALL NOT exceed the approved maximum limit without written exception approval from the CISO.
[VALIDATION] IF current_connections > approved_limit AND ciso_exception = FALSE THEN critical_violation

[RULE-04] External connection inventory MUST be reviewed quarterly to validate necessity and remove unused connections.
[VALIDATION] IF last_inventory_review > 90_days THEN violation

[RULE-05] Unauthorized external network connections MUST be disconnected within 2 hours of discovery.
[VALIDATION] IF connection_authorized = FALSE AND discovery_time > 2_hours AND status = "active" THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Connection Request Process - Standardized approval workflow for new external connections
- [PROC-02] Connection Inventory Management - Quarterly review and validation of all external connections
- [PROC-03] Unauthorized Connection Response - Incident response for discovery of unauthorized connections
- [PROC-04] Connection Monitoring - Continuous monitoring of external connection usage and security

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents involving external connections, major network architecture changes, regulatory requirement updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Excessive Production Connections]
IF system_type = "production"
AND external_connections = 8
AND approved_limit = 5
AND ciso_exception = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Undocumented Development Connection]
IF system_type = "development"
AND external_connection_active = TRUE
AND inventory_documented = FALSE
AND connection_age = 48_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Approved Exception Scenario]
IF external_connections = 6
AND approved_limit = 4
AND ciso_exception = TRUE
AND exception_valid = TRUE
THEN compliance = TRUE

[SCENARIO-04: Stale Inventory Review]
IF last_quarterly_review = 120_days_ago
AND external_connections > 0
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Unauthorized Connection Discovery]
IF connection_authorized = FALSE
AND discovery_timestamp = 3_hours_ago
AND connection_status = "active"
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Number of external network connections is limited | [RULE-01], [RULE-03] |
| External connections are documented and tracked | [RULE-02], [RULE-04] |
| Unauthorized connections are promptly addressed | [RULE-05] |
| Connection limits are enforced through approval process | [RULE-03] |