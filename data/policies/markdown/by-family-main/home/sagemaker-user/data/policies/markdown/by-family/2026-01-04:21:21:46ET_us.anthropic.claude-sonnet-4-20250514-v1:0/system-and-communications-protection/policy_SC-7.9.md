# POLICY: SC-7.9: Restrict Threatening Outgoing Communications Traffic

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.9 |
| NIST Control | SC-7.9: Restrict Threatening Outgoing Communications Traffic |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | extrusion detection, outgoing traffic, threat detection, malicious communications, traffic blocking |

## 1. POLICY STATEMENT
The organization SHALL implement extrusion detection capabilities to identify, block, and audit outgoing communications traffic that poses threats to external systems. All threatening outbound traffic MUST be denied at managed network interfaces with complete audit logging of associated internal users.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Network Infrastructure | YES | All managed network interfaces and gateways |
| Cloud Environments | YES | Hybrid cloud egress points and connections |
| Remote Workers | YES | VPN and direct internet connections |
| Partner Networks | YES | B2B connections and extranets |
| Guest Networks | YES | Visitor and contractor network access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Deploy and maintain extrusion detection systems<br>• Configure threat detection rules and criteria<br>• Monitor and respond to blocked traffic alerts |
| SOC Analysts | • Analyze blocked traffic incidents<br>• Investigate user activities associated with threats<br>• Escalate confirmed malicious activity |
| Network Operations | • Maintain network infrastructure supporting detection<br>• Ensure proper routing of traffic through inspection points<br>• Coordinate with security during incident response |

## 4. RULES
[RULE-01] All outgoing communications traffic MUST be inspected for threats at managed network interfaces before egress to external systems.
[VALIDATION] IF traffic_direction = "outbound" AND inspection_performed = FALSE THEN violation

[RULE-02] Traffic identified as threatening MUST be immediately denied and blocked from reaching external systems.
[VALIDATION] IF threat_detected = TRUE AND traffic_blocked = FALSE THEN critical_violation

[RULE-03] The identity of internal users associated with denied communications MUST be logged and audited within 5 minutes of the blocking action.
[VALIDATION] IF traffic_blocked = TRUE AND user_audit_logged = FALSE AND time_elapsed > 5_minutes THEN violation

[RULE-04] Extrusion detection systems MUST monitor for denial-of-service attack patterns, spoofed source addresses, and malicious code in outbound traffic.
[VALIDATION] IF detection_capability NOT IN ["dos_detection", "spoofing_detection", "malware_detection"] THEN violation

[RULE-05] Threat detection criteria MUST be reviewed and updated at least quarterly based on current threat intelligence.
[VALIDATION] IF threat_criteria_last_updated > 90_days THEN violation

[RULE-06] Blocked traffic incidents MUST be investigated within 4 hours for high-severity threats and 24 hours for medium-severity threats.
[VALIDATION] IF threat_severity = "high" AND investigation_time > 4_hours THEN violation
[VALIDATION] IF threat_severity = "medium" AND investigation_time > 24_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Extrusion Detection Configuration - Deploy and configure traffic inspection systems at all egress points
- [PROC-02] Threat Criteria Management - Establish and maintain criteria for identifying threatening outbound communications
- [PROC-03] Traffic Blocking Response - Immediate blocking and logging procedures for identified threats
- [PROC-04] User Investigation Process - Procedures for investigating users associated with blocked traffic
- [PROC-05] Threat Intelligence Integration - Regular updates to detection rules based on threat feeds

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving outbound threats, changes to network architecture, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: DDoS Traffic Detection]
IF outbound_traffic_volume > normal_baseline * 10
AND destination_diversity < 5_unique_hosts
AND traffic_blocked = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Malware Command and Control]
IF outbound_connection_matches_ioc = TRUE
AND traffic_inspection_enabled = TRUE
AND traffic_blocked = TRUE
AND user_identity_logged = TRUE
THEN compliance = TRUE

[SCENARIO-03: Spoofed Source Address]
IF source_ip NOT IN internal_ip_ranges
AND traffic_direction = "outbound"
AND traffic_blocked = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Unmonitored Egress Point]
IF network_interface = "egress"
AND extrusion_detection_enabled = FALSE
AND external_connectivity = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Delayed User Audit]
IF threatening_traffic_blocked = TRUE
AND user_audit_completion_time > 5_minutes
AND incident_severity = "high"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Outgoing communications traffic posing a threat to external systems is detected | [RULE-01], [RULE-04] |
| Outgoing communications traffic posing a threat to external systems is denied | [RULE-02] |
| The identity of internal users associated with denied communications is audited | [RULE-03], [RULE-06] |