```markdown
# POLICY: SI-4.24: Indicators of Compromise

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-4.24 |
| NIST Control | SI-4.24: Indicators of Compromise |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | indicators of compromise, IOC, threat intelligence, forensic artifacts, malware signatures, cybersecurity |

## 1. POLICY STATEMENT
The organization SHALL establish processes to discover, collect, and distribute indicators of compromise (IOCs) from defined sources to designated personnel and roles. IOCs include forensic artifacts, malware signatures, network indicators, and other threat intelligence that enable rapid identification and response to security incidents across organizational systems.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Including cloud, hybrid, and on-premises |
| Third-party managed services | YES | Must provide IOC integration capabilities |
| Development/test environments | YES | Critical for supply chain security |
| Mobile devices | CONDITIONAL | If accessing organizational data |
| Contractor systems | CONDITIONAL | If processing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center (SOC) | • Monitor IOC feeds continuously<br>• Validate and correlate IOCs<br>• Distribute actionable IOCs to response teams |
| Incident Response Team | • Analyze IOCs during investigations<br>• Generate new IOCs from incidents<br>• Update IOC databases with findings |
| System Administrators | • Implement IOC-based detection rules<br>• Monitor systems for IOC matches<br>• Report IOC detections to SOC |

## 4. RULES
[RULE-01] The organization MUST maintain relationships with at least three external IOC sources including government cooperatives (US-CERT, FBI) and commercial threat intelligence providers.
[VALIDATION] IF external_IOC_sources < 3 OR government_sources = FALSE THEN violation

[RULE-02] IOCs MUST be collected from external sources within 2 hours of availability and processed within 4 hours of collection.
[VALIDATION] IF (collection_time - source_publish_time) > 2_hours OR (processing_time - collection_time) > 4_hours THEN violation

[RULE-03] High-confidence IOCs MUST be distributed to SOC analysts within 1 hour and to system administrators within 4 hours of validation.
[VALIDATION] IF IOC_confidence = "high" AND (SOC_distribution_time > 1_hour OR sysadmin_distribution_time > 4_hours) THEN violation

[RULE-04] All organizational systems MUST be configured to automatically ingest and apply IOCs for detection within 24 hours of distribution.
[VALIDATION] IF IOC_application_time > 24_hours OR automated_ingestion = FALSE THEN violation

[RULE-05] IOCs generated from internal incidents MUST be shared with external cooperatives within 72 hours unless classified or containing PII.
[VALIDATION] IF internal_IOC = TRUE AND sharing_time > 72_hours AND classification = "unclassified" AND PII_present = FALSE THEN violation

[RULE-06] IOC effectiveness MUST be measured monthly with at least 85% of high-confidence IOCs producing actionable detections within 30 days.
[VALIDATION] IF monthly_IOC_effectiveness < 0.85 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] IOC Source Management - Establish and maintain relationships with threat intelligence providers
- [PROC-02] IOC Collection and Validation - Automated collection with analyst validation workflows
- [PROC-03] IOC Distribution - Role-based distribution with urgency classifications
- [PROC-04] IOC Integration - Technical implementation across security tools and systems
- [PROC-05] IOC Effectiveness Analysis - Monthly review of IOC detection rates and false positives

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major security incidents, new threat intelligence sources, regulatory changes, technology platform changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical IOC Distribution Delay]
IF IOC_severity = "critical"
AND distribution_time > 1_hour
AND business_hours = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Government IOC Sources]
IF government_IOC_sources = 0
AND commercial_sources >= 3
AND total_sources >= 3
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Automated IOC Integration Failure]
IF IOC_distribution_complete = TRUE
AND automated_application = FALSE
AND manual_override_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Internal IOC Sharing Restriction]
IF IOC_source = "internal_incident"
AND classification = "unclassified"
AND PII_present = FALSE
AND external_sharing = FALSE
AND sharing_time > 72_hours
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: IOC Effectiveness Below Threshold]
IF monthly_detection_rate < 0.85
AND high_confidence_IOCs > 100
AND reporting_period = "current_month"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| IOC sources are defined and maintained | [RULE-01] |
| IOCs are discovered from defined sources | [RULE-02] |
| IOCs are collected systematically | [RULE-02] |
| IOCs are distributed to designated personnel | [RULE-03] |
| IOC processes are automated and measured | [RULE-04], [RULE-06] |
| Internal IOCs are shared externally | [RULE-05] |
```