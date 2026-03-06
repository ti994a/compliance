# POLICY: SA-9.8: Processing and Storage Location — U.S. Jurisdiction

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-9.8 |
| NIST Control | SA-9.8: Processing and Storage Location — U.S. Jurisdiction |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | data processing, data storage, U.S. jurisdiction, geographic restrictions, external providers, cloud services |

## 1. POLICY STATEMENT
All information processing and data storage activities SHALL be restricted to facilities physically located within the legal jurisdictional boundary of the United States. This requirement applies to all organizational data, systems, and services including those provided by external service providers.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational data | YES | Including backup and archived data |
| Cloud service providers | YES | Must certify U.S. jurisdiction compliance |
| External service providers | YES | Contractual requirements mandatory |
| Development/test environments | YES | No exception for non-production data |
| Mobile device data | CONDITIONAL | When containing organizational information |
| Third-party integrations | YES | API and data exchange partners |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Information Security Officer | • Establish jurisdiction verification procedures<br>• Approve exceptions for critical business needs<br>• Monitor compliance across all service providers |
| Procurement Team | • Include jurisdiction requirements in all contracts<br>• Verify provider certifications before engagement<br>• Maintain documentation of provider locations |
| System Owners | • Validate processing/storage locations for their systems<br>• Report jurisdiction compliance status quarterly<br>• Implement technical controls to enforce restrictions |

## 4. RULES
[RULE-01] All information processing activities MUST occur within facilities located in the United States and its territories.
[VALIDATION] IF processing_location NOT IN ["US", "US_territories"] THEN critical_violation

[RULE-02] All data storage, including primary, backup, and archival storage, MUST be physically located within U.S. jurisdiction.
[VALIDATION] IF storage_location NOT IN ["US", "US_territories"] THEN critical_violation

[RULE-03] External service providers MUST provide written certification of U.S. jurisdiction compliance before contract execution.
[VALIDATION] IF provider_certification = FALSE OR certification_date > contract_date THEN violation

[RULE-04] Cloud service agreements MUST include contractual guarantees that data will not be processed or stored outside U.S. jurisdiction.
[VALIDATION] IF contract_includes_jurisdiction_clause = FALSE THEN violation

[RULE-05] Data replication or synchronization to locations outside U.S. jurisdiction is PROHIBITED without CISO written exception.
[VALIDATION] IF replication_location NOT IN ["US", "US_territories"] AND exception_approved = FALSE THEN critical_violation

[RULE-06] Service providers MUST notify the organization within 24 hours of any changes to processing or storage locations.
[VALIDATION] IF location_change_occurred = TRUE AND notification_time > 24_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Jurisdiction Verification Process - Validate and document geographic locations of all processing and storage
- [PROC-02] Provider Assessment Procedure - Evaluate external providers for jurisdiction compliance
- [PROC-03] Contract Review Process - Ensure all agreements include appropriate jurisdiction clauses
- [PROC-04] Exception Management Process - Handle requests for jurisdiction exceptions with proper approvals

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: New service provider engagements, contract renewals, regulatory changes, security incidents involving jurisdiction

## 7. SCENARIO PATTERNS
[SCENARIO-01: Cloud Provider Selection]
IF cloud_provider_location = "non-US"
AND data_classification = "organizational"
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Backup Storage Location]
IF backup_storage_location = "Canada"
AND data_type = "organizational"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Development Environment]
IF environment_type = "development"
AND processing_location = "US"
AND storage_location = "US"
THEN compliance = TRUE

[SCENARIO-04: Emergency Data Recovery]
IF incident_type = "disaster_recovery"
AND temporary_location = "non-US"
AND duration > 72_hours
AND exception_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Third-Party Integration]
IF integration_type = "API"
AND partner_processing_location = "US"
AND contract_includes_jurisdiction_clause = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Geographic location of information processing is restricted to U.S. facilities | [RULE-01] |
| Geographic location of data storage is restricted to U.S. facilities | [RULE-02] |
| External providers comply with jurisdiction restrictions | [RULE-03], [RULE-04] |
| Monitoring and notification of location changes | [RULE-06] |