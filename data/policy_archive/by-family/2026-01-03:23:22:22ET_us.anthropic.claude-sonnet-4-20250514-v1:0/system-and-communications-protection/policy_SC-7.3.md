# POLICY: SC-7.3: Access Points

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.3 |
| NIST Control | SC-7.3: Access Points |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | network connections, external access, boundary protection, network monitoring, access points |

## 1. POLICY STATEMENT
The organization SHALL limit the number of external network connections to information systems to facilitate effective monitoring and reduce attack surface. All external network connections MUST be documented, approved, and continuously monitored for unauthorized access attempts.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing organizational data |
| Development Systems | YES | If accessible from external networks |
| Test Systems | CONDITIONAL | Only if containing production data |
| Vendor Systems | YES | If directly connected to organizational networks |
| Cloud Services | YES | All external cloud connections |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Maintain inventory of external connections<br>• Monitor connection usage<br>• Approve new external connections |
| System Administrators | • Implement connection limitations<br>• Document system connections<br>• Report unauthorized connections |
| Security Operations Center | • Monitor external connection traffic<br>• Detect anomalous connection patterns<br>• Investigate connection violations |

## 4. RULES
[RULE-01] Organizations MUST maintain a documented inventory of all authorized external network connections with business justification and technical specifications.
[VALIDATION] IF external_connection_exists = TRUE AND inventory_documented = FALSE THEN violation

[RULE-02] External network connections SHALL NOT exceed the approved maximum limit of 10 connections per critical system and 5 connections per non-critical system without CISO approval.
[VALIDATION] IF system_criticality = "critical" AND external_connections > 10 AND ciso_exception = FALSE THEN violation
[VALIDATION] IF system_criticality = "non-critical" AND external_connections > 5 AND ciso_exception = FALSE THEN violation

[RULE-03] All external network connections MUST be reviewed quarterly for continued business necessity and security compliance.
[VALIDATION] IF last_review_date > 90_days AND connection_status = "active" THEN violation

[RULE-04] New external network connections MUST receive security approval before implementation and be documented within 5 business days of activation.
[VALIDATION] IF connection_age > 5_business_days AND security_approval = FALSE THEN violation

[RULE-05] Unused external network connections MUST be decommissioned within 30 days of identification or business need cessation.
[VALIDATION] IF connection_unused_days > 30 AND decommission_status = "pending" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Connection Request Process - Standardized approval workflow for new external connections
- [PROC-02] Connection Inventory Management - Quarterly review and validation of all external connections
- [PROC-03] Connection Monitoring Protocol - Continuous monitoring of external connection traffic and usage
- [PROC-04] Emergency Connection Procedures - Rapid approval process for critical business needs

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving external connections, major infrastructure changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized External Connection]
IF external_connection_detected = TRUE
AND inventory_record = FALSE
AND discovery_method = "automated_scan"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Exceeded Connection Limits]
IF system_type = "critical"
AND active_external_connections = 12
AND ciso_exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Overdue Connection Review]
IF last_connection_review > 120_days
AND connection_status = "active"
AND business_justification = "valid"
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Legacy System Transition]
IF system_migration = "ipv4_to_ipv6"
AND dual_connections = TRUE
AND transition_plan_approved = TRUE
AND timeline_within_limit = TRUE
THEN compliance = TRUE

[SCENARIO-05: Emergency Connection Activation]
IF connection_type = "emergency"
AND business_justification = "critical_incident"
AND temporary_approval = TRUE
AND documentation_pending = TRUE
AND activation_time < 5_business_days
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| External network connections are limited | RULE-02 |
| Connection inventory is maintained | RULE-01 |
| Regular review of connections occurs | RULE-03 |
| New connections receive proper approval | RULE-04 |
| Unused connections are removed | RULE-05 |