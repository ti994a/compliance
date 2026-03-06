# POLICY: IR-4.8: Correlation with External Organizations

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IR-4.8 |
| NIST Control | IR-4.8: Correlation with External Organizations |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | incident response, external coordination, information sharing, cross-organization, incident correlation |

## 1. POLICY STATEMENT
The organization SHALL coordinate incident response activities with defined external organizations to correlate and share incident information. This coordination enables cross-organizational incident awareness and more effective incident responses through leveraged intelligence and collaborative response capabilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Security Operations Center | YES | Primary coordination responsibility |
| Incident Response Team | YES | Execute coordination activities |
| Business Partners | CONDITIONAL | When formal agreements exist |
| Vendors/Suppliers | CONDITIONAL | For incidents affecting shared systems |
| Government Agencies | CONDITIONAL | Per regulatory requirements |
| Industry Partners | CONDITIONAL | When mutual benefit agreements exist |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve external organization coordination agreements<br>• Define incident sharing criteria and boundaries<br>• Oversee compliance with sharing policies |
| Incident Response Manager | • Maintain list of external coordination partners<br>• Execute incident information sharing procedures<br>• Coordinate cross-organizational incident activities |
| SOC Manager | • Implement technical correlation capabilities<br>• Monitor shared incident feeds<br>• Escalate coordination needs to IR team |

## 4. RULES
[RULE-01] The organization MUST maintain a documented list of external organizations authorized for incident information coordination and sharing.
[VALIDATION] IF external_org_list EXISTS AND documented = TRUE AND current_date - last_updated <= 365_days THEN compliant

[RULE-02] Incident information sharing with external organizations MUST be governed by formal agreements that define scope, methods, and protection requirements.
[VALIDATION] IF incident_shared = TRUE AND formal_agreement = FALSE THEN violation

[RULE-03] Shared incident information MUST be classified and marked according to organizational data classification standards before transmission.
[VALIDATION] IF incident_info_shared = TRUE AND classification_marking = NULL THEN violation

[RULE-04] Cross-organizational incident correlation activities MUST be documented and maintained for audit purposes for minimum 3 years.
[VALIDATION] IF correlation_activity = TRUE AND documentation_retained < 3_years THEN violation

[RULE-05] External incident information sharing MUST NOT include sensitive organizational data unless explicitly authorized by data owner and covered by agreement.
[VALIDATION] IF shared_data_contains_sensitive = TRUE AND (data_owner_approval = FALSE OR agreement_covers_sensitive = FALSE) THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External Organization Coordination Setup - Establish and maintain partnerships for incident coordination
- [PROC-02] Incident Information Sharing - Process for sharing incident details with external partners
- [PROC-03] Cross-Organization Correlation - Analyze and correlate incident data across organizational boundaries
- [PROC-04] Agreement Management - Maintain and review external coordination agreements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major incident involving external coordination, new partnership agreements, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Authorized Partner Sharing]
IF incident_severity >= "High"
AND external_org IN approved_coordination_list
AND formal_agreement = TRUE
AND data_classified = TRUE
THEN compliance = TRUE

[SCENARIO-02: Unauthorized Information Sharing]
IF incident_info_shared = TRUE
AND external_org NOT IN approved_coordination_list
AND formal_agreement = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Sensitive Data Exposure]
IF shared_incident_data CONTAINS sensitive_data
AND data_owner_approval = FALSE
AND external_org_clearance < required_level
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Missing Documentation]
IF cross_org_correlation_performed = TRUE
AND incident_date > 90_days_ago
AND correlation_documentation = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Expired Agreement Usage]
IF incident_shared_with_external_org = TRUE
AND coordination_agreement_status = "expired"
AND current_date > agreement_expiry_date
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Coordination with defined external organizations | [RULE-01], [RULE-02] |
| Incident information correlation and sharing | [RULE-03], [RULE-04] |
| Cross-organization incident awareness | [RULE-01], [RULE-04] |
| Effective incident response coordination | [RULE-02], [RULE-05] |