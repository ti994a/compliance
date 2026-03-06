# POLICY: SI-4.24: Indicators of Compromise

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.24 |
| NIST Control | SI-4.24: Indicators of Compromise |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | indicators of compromise, IOC, threat intelligence, forensic artifacts, malware signatures, cybersecurity monitoring |

## 1. POLICY STATEMENT
The organization SHALL establish processes to discover, collect, and distribute indicators of compromise (IOCs) from defined sources to designated personnel and roles. IOCs MUST be rapidly distributed to reduce organizational vulnerability to known exploits and attacks.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT Systems | YES | Including cloud, hybrid, and on-premises |
| Network Infrastructure | YES | Routers, switches, firewalls, IDS/IPS |
| Security Operations Center | YES | Primary IOC processing entity |
| Incident Response Team | YES | IOC consumers and contributors |
| Third-party Managed Services | CONDITIONAL | When handling organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| SOC Manager | • Establish IOC collection processes<br>• Define IOC distribution lists<br>• Ensure 24/7 IOC monitoring capability |
| Threat Intelligence Analyst | • Source and validate IOCs from external feeds<br>• Analyze IOC relevance and priority<br>• Maintain IOC database and signatures |
| Security Engineers | • Implement IOC detection rules<br>• Configure automated IOC ingestion<br>• Validate IOC detection accuracy |

## 4. RULES
[RULE-01] The organization MUST maintain relationships with at least three (3) external IOC sources including government cooperatives, commercial threat feeds, and industry sharing groups.
[VALIDATION] IF ioc_sources_count < 3 OR government_source = FALSE THEN violation

[RULE-02] IOCs MUST be collected from defined sources within 4 hours of availability and processed for organizational relevance within 8 hours.
[VALIDATION] IF ioc_collection_time > 4_hours OR ioc_processing_time > 8_hours THEN violation

[RULE-03] High-priority IOCs MUST be distributed to SOC personnel within 1 hour and to all designated roles within 4 hours of validation.
[VALIDATION] IF ioc_priority = "high" AND soc_distribution_time > 1_hour THEN critical_violation
[VALIDATION] IF ioc_priority = "high" AND full_distribution_time > 4_hours THEN violation

[RULE-04] IOC detection signatures MUST be implemented in security monitoring tools within 24 hours for high-priority IOCs and within 72 hours for standard IOCs.
[VALIDATION] IF ioc_priority = "high" AND signature_deployment_time > 24_hours THEN critical_violation
[VALIDATION] IF ioc_priority = "standard" AND signature_deployment_time > 72_hours THEN violation

[RULE-05] IOC sources MUST be validated for authenticity and organizational systems MUST maintain logs of all IOC processing activities for audit purposes.
[VALIDATION] IF ioc_source_validation = FALSE OR ioc_processing_logs = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] IOC Source Management - Establish and maintain relationships with external IOC providers
- [PROC-02] IOC Collection and Validation - Automated ingestion and manual validation processes
- [PROC-03] IOC Distribution Protocol - Standardized distribution to personnel and systems
- [PROC-04] IOC Signature Deployment - Implementation in security monitoring infrastructure
- [PROC-05] IOC Effectiveness Review - Periodic assessment of IOC detection accuracy

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, new threat intelligence sources, changes to monitoring infrastructure

## 7. SCENARIO PATTERNS
[SCENARIO-01: External IOC Feed Integration]
IF ioc_source = "external_feed"
AND source_validation = TRUE
AND collection_automated = TRUE
AND distribution_time <= 4_hours
THEN compliance = TRUE

[SCENARIO-02: Manual IOC Processing Delay]
IF ioc_priority = "high"
AND processing_method = "manual"
AND processing_time > 8_hours
AND no_exception_documented = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: IOC Distribution Failure]
IF ioc_received = TRUE
AND soc_notified = FALSE
AND time_elapsed > 1_hour
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Incomplete IOC Implementation]
IF ioc_validated = TRUE
AND signature_created = TRUE
AND deployment_status = "pending"
AND time_elapsed > 72_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: IOC Source Authentication]
IF ioc_source_type = "government_cooperative"
AND authentication_verified = FALSE
AND ioc_deployed = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| IOC sources are defined and maintained | [RULE-01] |
| IOCs are discovered from defined sources | [RULE-02] |
| IOCs are collected within required timeframes | [RULE-02] |
| IOCs are distributed to designated personnel | [RULE-03] |
| IOC processing activities are logged | [RULE-05] |