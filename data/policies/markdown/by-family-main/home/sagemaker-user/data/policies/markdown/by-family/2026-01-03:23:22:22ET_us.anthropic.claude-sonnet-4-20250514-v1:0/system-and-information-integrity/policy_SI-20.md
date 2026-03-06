# POLICY: SI-20: Tainting

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-20 |
| NIST Control | SI-20: Tainting |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | tainting, data exfiltration, insider threats, deception, canary tokens, steganography |

## 1. POLICY STATEMENT
The organization SHALL embed data or capabilities in designated systems and system components to detect unauthorized exfiltration or improper removal of organizational data. Tainting mechanisms must provide alerting capabilities when organizational data is accessed or transmitted by unauthorized entities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production systems containing sensitive data | YES | All systems processing PII, financial, or classified data |
| Development/test environments | CONDITIONAL | Only if containing production data copies |
| Cloud storage repositories | YES | All cloud-based data repositories |
| Database systems | YES | Customer, employee, and financial databases |
| File shares and document repositories | YES | Shared drives containing sensitive documents |
| Mobile devices with organizational data | YES | Company-issued and BYOD devices |
| Backup systems | YES | All backup repositories and archives |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Protection Officer | • Define data classification requiring tainting<br>• Approve tainting methodologies<br>• Monitor tainting effectiveness |
| Security Engineering Team | • Implement tainting mechanisms<br>• Configure detection and alerting systems<br>• Maintain tainting infrastructure |
| SOC Analysts | • Monitor tainting alerts<br>• Investigate potential data exfiltration events<br>• Coordinate incident response activities |
| System Administrators | • Deploy tainting capabilities on assigned systems<br>• Ensure tainting mechanisms remain operational<br>• Report tainting system failures |

## 4. RULES
[RULE-01] Systems containing sensitive data (Confidential or above) MUST implement at least one form of data tainting mechanism.
[VALIDATION] IF data_classification >= "Confidential" AND tainting_enabled = FALSE THEN violation

[RULE-02] Passive tainting mechanisms MUST be deployed in all customer databases and include false but realistic data entries.
[VALIDATION] IF system_type = "customer_database" AND passive_tainting_deployed = FALSE THEN violation

[RULE-03] Active tainting mechanisms MUST be implemented for systems containing PII or financial data and SHALL provide real-time alerting capabilities.
[VALIDATION] IF (data_type = "PII" OR data_type = "financial") AND active_tainting_enabled = FALSE THEN violation

[RULE-04] Tainting alerts MUST be investigated within 4 hours of detection during business hours and within 12 hours outside business hours.
[VALIDATION] IF tainting_alert_triggered = TRUE AND investigation_start_time > 4_hours_business OR > 12_hours_non_business THEN violation

[RULE-05] Steganographic tainting MUST be applied to documents classified as Confidential or above before storage in shared repositories.
[VALIDATION] IF document_classification >= "Confidential" AND shared_storage = TRUE AND steganographic_tainting = FALSE THEN violation

[RULE-06] Tainting mechanisms MUST NOT interfere with normal business operations or system performance by more than 5%.
[VALIDATION] IF tainting_performance_impact > 5_percent THEN violation

[RULE-07] All tainting implementations MUST be documented and reviewed quarterly for effectiveness.
[VALIDATION] IF tainting_review_date > 90_days_ago THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Tainting Implementation - Standardized deployment of tainting mechanisms across system types
- [PROC-02] Alert Response - Investigation and response procedures for tainting alerts
- [PROC-03] Effectiveness Assessment - Quarterly review and testing of tainting capabilities
- [PROC-04] False Positive Management - Process for handling and reducing false tainting alerts

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Data breach incidents, new system deployments, regulatory changes, technology updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Customer Database Access]
IF system_type = "customer_database"
AND external_email_received_at_canary_address = TRUE
AND source_verification = "unauthorized"
THEN compliance = TRUE (detection working)
violation_severity = "Critical_Alert"

[SCENARIO-02: Missing Tainting on Sensitive System]
IF data_classification = "Confidential"
AND system_deployed_date < 30_days_ago
AND tainting_mechanism_deployed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Delayed Alert Investigation]
IF tainting_alert_triggered = TRUE
AND business_hours = TRUE
AND investigation_start_time = 6_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Active Tainting Call-Home]
IF active_tainting_triggered = TRUE
AND location_data_captured = TRUE
AND incident_response_initiated = TRUE
THEN compliance = TRUE (successful detection)
violation_severity = "Critical_Alert"

[SCENARIO-05: Performance Impact Violation]
IF tainting_enabled = TRUE
AND system_performance_degradation = 8_percent
AND business_operations_affected = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Embed data or capabilities in defined systems | [RULE-01], [RULE-02], [RULE-03] |
| Determine if organizational data has been exfiltrated | [RULE-04], [RULE-07] |
| Implement detection mechanisms | [RULE-02], [RULE-03], [RULE-05] |
| Maintain operational effectiveness | [RULE-06], [RULE-07] |