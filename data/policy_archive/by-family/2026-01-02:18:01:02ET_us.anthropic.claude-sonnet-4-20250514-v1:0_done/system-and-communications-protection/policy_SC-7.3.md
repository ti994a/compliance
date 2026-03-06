# POLICY: SC-7.3: Access Points

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.3 |
| NIST Control | SC-7.3: Access Points |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | external connections, network access points, boundary protection, TIC, network monitoring |

## 1. POLICY STATEMENT
The organization SHALL limit the number of external network connections to information systems to facilitate effective monitoring and control of network traffic. All external network connections MUST be documented, approved, and regularly reviewed to ensure minimal attack surface and compliance with federal guidelines.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Systems | YES | All systems processing organizational data |
| Development Systems | YES | If accessible from external networks |
| Test Systems | YES | If connected to external networks |
| Contractor Systems | YES | If integrated with organizational networks |
| Personal Devices | CONDITIONAL | Only if granted network access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Maintain inventory of external connections<br>• Monitor connection usage and traffic<br>• Implement technical controls for connection limiting |
| System Administrators | • Request approval for new external connections<br>• Document business justification for connections<br>• Implement approved connection configurations |
| CISO Office | • Approve external connection requests<br>• Define maximum connection thresholds<br>• Review connection inventory quarterly |

## 4. RULES

[RULE-01] Organizations MUST maintain a documented inventory of all external network connections including connection type, business justification, and responsible system owner.
[VALIDATION] IF external_connection_exists = TRUE AND inventory_documented = FALSE THEN violation

[RULE-02] The total number of external network connections per system SHALL NOT exceed the approved threshold defined in the system security plan.
[VALIDATION] IF connection_count > approved_threshold THEN violation

[RULE-03] New external network connections MUST receive written approval from the CISO or designated authority before implementation.
[VALIDATION] IF connection_date > policy_effective_date AND ciso_approval = FALSE THEN violation

[RULE-04] All external network connections MUST be reviewed quarterly to validate continued business need and security posture.
[VALIDATION] IF last_review_date > 90_days AND connection_active = TRUE THEN violation

[RULE-05] Legacy connections during technology transitions (e.g., IPv4 to IPv6) MUST have documented migration timelines not exceeding 12 months.
[VALIDATION] IF transition_connection = TRUE AND migration_timeline > 365_days THEN violation

[RULE-06] External connections MUST implement monitoring capabilities to track inbound and outbound traffic patterns.
[VALIDATION] IF external_connection = TRUE AND monitoring_enabled = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Connection Request Process - Formal approval workflow for new connections
- [PROC-02] Connection Inventory Management - Quarterly review and validation procedures
- [PROC-03] Traffic Monitoring Implementation - Technical controls for connection monitoring
- [PROC-04] Connection Decommissioning - Process for removing unnecessary connections

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Security incidents involving external connections, major network architecture changes, regulatory requirement updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unauthorized External Connection]
IF external_connection_detected = TRUE
AND connection_in_inventory = FALSE  
AND discovery_method = "security_scan"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Exceeded Connection Threshold]
IF system_connection_count = 15
AND approved_threshold = 10
AND business_justification = "valid"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Legacy Connection Overdue]
IF connection_type = "IPv4_transition"
AND implementation_date = "2023-01-01"
AND current_date = "2024-02-01"
AND migration_complete = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Approved Connection with Monitoring]
IF external_connection = TRUE
AND ciso_approval = TRUE
AND monitoring_enabled = TRUE
AND quarterly_review_current = TRUE
THEN compliance = TRUE

[SCENARIO-05: Emergency Connection Grace Period]
IF connection_type = "emergency"
AND implementation_date < 72_hours_ago
AND approval_pending = TRUE
AND business_justification = "documented"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| External network connections are limited | [RULE-01], [RULE-02] |
| Connection monitoring is implemented | [RULE-06] |
| Approval process is enforced | [RULE-03] |
| Regular reviews are conducted | [RULE-04] |
| Transition connections are managed | [RULE-05] |