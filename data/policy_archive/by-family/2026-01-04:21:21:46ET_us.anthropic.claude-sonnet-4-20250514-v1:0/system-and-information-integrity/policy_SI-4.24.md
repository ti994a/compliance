# POLICY: SI-4.24: Indicators of Compromise

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.24 |
| NIST Control | SI-4.24: Indicators of Compromise |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | indicators of compromise, IOC, threat intelligence, forensic artifacts, malware signatures, network monitoring |

## 1. POLICY STATEMENT
The organization MUST establish capabilities to discover, collect, and distribute indicators of compromise (IOCs) from defined sources to designated personnel and roles. IOCs SHALL be rapidly distributed to reduce organizational exposure to known threats and vulnerabilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Production, development, and test environments |
| Cloud infrastructure | YES | Hybrid and multi-cloud deployments |
| Network infrastructure | YES | Internal and DMZ networks |
| Endpoint devices | YES | Corporate-managed devices |
| Third-party systems | CONDITIONAL | When processing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) | • Monitor IOC feeds and sources<br>• Validate and analyze IOCs<br>• Distribute IOCs to relevant teams |
| Incident Response Team | • Collect IOCs during incident investigation<br>• Share IOCs with external partners<br>• Update IOC databases |
| System Administrators | • Implement IOC-based detection rules<br>• Monitor systems for IOC matches<br>• Report IOC discoveries |

## 4. RULES

[RULE-01] The organization MUST define and maintain a list of approved IOC sources including government and industry threat intelligence feeds.
[VALIDATION] IF ioc_sources_list = NULL OR last_updated > 90_days THEN violation

[RULE-02] IOC collection processes MUST be automated where technically feasible and SHALL operate continuously during business hours at minimum.
[VALIDATION] IF ioc_collection_automated = FALSE AND manual_collection_frequency < daily THEN violation

[RULE-03] Critical IOCs MUST be distributed to designated personnel within 4 hours of discovery, and standard IOCs within 24 hours.
[VALIDATION] IF ioc_criticality = "critical" AND distribution_time > 4_hours THEN critical_violation
[VALIDATION] IF ioc_criticality = "standard" AND distribution_time > 24_hours THEN violation

[RULE-04] All discovered IOCs MUST be logged with source, timestamp, distribution list, and validation status.
[VALIDATION] IF ioc_logged = FALSE OR missing_required_fields = TRUE THEN violation

[RULE-05] IOC sources MUST be reviewed quarterly for relevance and effectiveness, with inactive sources removed.
[VALIDATION] IF source_review_date < current_date - 90_days THEN violation

[RULE-06] Personnel receiving IOCs MUST acknowledge receipt and confirm implementation within defined timeframes.
[VALIDATION] IF ioc_acknowledgment = NULL AND distribution_date < current_date - 48_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] IOC Source Management - Define, evaluate, and maintain threat intelligence sources
- [PROC-02] IOC Collection and Validation - Automated and manual collection processes
- [PROC-03] IOC Distribution and Communication - Dissemination to appropriate personnel
- [PROC-04] IOC Implementation Tracking - Monitor deployment of IOC-based detections

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, new threat intelligence sources, regulatory changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Critical IOC Distribution Delay]
IF ioc_criticality = "critical"
AND discovery_timestamp < current_time - 6_hours
AND distribution_complete = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Unvalidated IOC Source]
IF ioc_source NOT IN approved_sources_list
AND ioc_distributed = TRUE
AND source_validation = "pending"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Missing IOC Acknowledgment]
IF ioc_distributed = TRUE
AND distribution_date < current_date - 48_hours
AND recipient_acknowledgment = NULL
AND follow_up_attempted = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Automated IOC Collection Failure]
IF ioc_collection_method = "automated"
AND last_successful_collection > 24_hours
AND manual_backup_initiated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: IOC Implementation Tracking]
IF ioc_distributed = TRUE
AND implementation_required = TRUE
AND implementation_status = "unknown"
AND distribution_date < current_date - 72_hours
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| IOC sources are defined | [RULE-01] |
| IOCs are discovered | [RULE-02] |
| IOCs are collected | [RULE-02], [RULE-04] |
| IOCs are distributed to designated personnel | [RULE-03], [RULE-06] |