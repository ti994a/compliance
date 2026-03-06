```markdown
# POLICY: SC-28.2: Offline Storage

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-28.2 |
| NIST Control | SC-28.2: Offline Storage |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | offline storage, data protection, secure storage, information removal, network isolation |

## 1. POLICY STATEMENT
The organization must identify specific categories of sensitive information that require offline storage and remove such information from online systems to secure offline locations. This control eliminates network-based unauthorized access risks by physically isolating critical data from online environments.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Systems containing sensitive data requiring offline protection |
| Cloud storage services | YES | Including hybrid and multi-cloud environments |
| Backup systems | YES | Both online and offline backup infrastructure |
| Mobile devices | CONDITIONAL | Only when containing designated sensitive information |
| Development/test systems | CONDITIONAL | When containing production-sensitive data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Classification Officer | • Define information categories requiring offline storage<br>• Maintain data classification policies<br>• Review and approve offline storage requirements |
| System Administrators | • Execute offline storage procedures<br>• Verify complete removal from online systems<br>• Maintain offline storage infrastructure |
| Security Operations Team | • Monitor compliance with offline storage requirements<br>• Validate secure offline storage locations<br>• Conduct periodic access reviews |

## 4. RULES
[RULE-01] Organizations MUST define specific categories of information that require removal from online storage and offline storage in secure locations.
[VALIDATION] IF information_categories_defined = FALSE THEN violation

[RULE-02] Designated sensitive information MUST be completely removed from all online storage systems within 30 days of classification or as specified in data handling procedures.
[VALIDATION] IF sensitive_info_online = TRUE AND days_since_classification > 30 THEN violation

[RULE-03] Offline storage locations MUST be physically secured with appropriate environmental controls, access restrictions, and monitoring capabilities.
[VALIDATION] IF offline_location_security_controls < required_baseline THEN violation

[RULE-04] Organizations MUST maintain an inventory of all information moved to offline storage including location, access controls, and retrieval procedures.
[VALIDATION] IF offline_inventory_maintained = FALSE OR inventory_last_updated > 90_days THEN violation

[RULE-05] Access to offline stored information MUST require documented business justification and approval from designated authorities.
[VALIDATION] IF offline_access_request = TRUE AND (business_justification = FALSE OR approval_documented = FALSE) THEN violation

[RULE-06] Verification MUST be performed to ensure complete removal of information from online systems before considering offline storage requirements satisfied.
[VALIDATION] IF removal_verification_completed = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Data Classification and Offline Storage Determination - Process for identifying information requiring offline storage
- [PROC-02] Online to Offline Migration - Secure procedures for moving data from online to offline storage
- [PROC-03] Offline Storage Management - Maintenance and monitoring of secure offline locations
- [PROC-04] Offline Data Retrieval - Controlled process for accessing offline stored information
- [PROC-05] Verification and Validation - Confirming complete removal from online systems

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Data breach incidents, regulatory changes, system architecture changes, merger/acquisition activities

## 7. SCENARIO PATTERNS
[SCENARIO-01: Sensitive Data Discovery]
IF data_classification = "confidential" OR data_classification = "restricted"
AND storage_location = "online"
AND offline_storage_required = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Incomplete Data Removal]
IF migration_to_offline = "completed"
AND online_system_verification = "not_performed"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Unauthorized Offline Access]
IF offline_data_accessed = TRUE
AND business_justification = FALSE
AND management_approval = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Unsecured Offline Location]
IF offline_storage_location = "active"
AND physical_security_controls < baseline_requirements
AND environmental_controls = "inadequate"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Missing Offline Inventory]
IF offline_data_exists = TRUE
AND inventory_maintained = FALSE
AND last_inventory_update > 90_days
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Information categories for offline storage are defined | [RULE-01] |
| Designated information is removed from online storage | [RULE-02], [RULE-06] |
| Information is stored offline in secure locations | [RULE-03] |
| Offline storage inventory and controls are maintained | [RULE-04], [RULE-05] |
```