```markdown
# POLICY: AC-16: Security and Privacy Attributes

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-16 |
| NIST Control | AC-16: Security and Privacy Attributes |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | security attributes, privacy attributes, data labeling, information classification, attribute binding, data retention, PII processing |

## 1. POLICY STATEMENT
The organization SHALL implement security and privacy attribute systems to associate, maintain, and enforce metadata-based access controls and information flow policies for data in storage, processing, and transmission. All information assets MUST be properly labeled with appropriate security and privacy attributes to enable automated policy enforcement and compliance monitoring.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All Information Systems | YES | Including cloud, on-premises, and hybrid |
| Data in Storage | YES | Databases, file systems, archives |
| Data in Transit | YES | Network communications, APIs |
| Data in Processing | YES | Memory, temporary files, caches |
| Third-party Systems | CONDITIONAL | When processing organizational data |
| Personal Devices | CONDITIONAL | When accessing organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Data Owners | • Define security and privacy attribute requirements<br>• Approve attribute schemas and values<br>• Review attribute applicability quarterly |
| System Administrators | • Implement attribute binding mechanisms<br>• Configure automated labeling systems<br>• Monitor attribute integrity and changes |
| Security Team | • Audit attribute changes and violations<br>• Define permitted attribute values and ranges<br>• Validate attribute enforcement mechanisms |

## 4. RULES

[RULE-01] All information systems MUST implement automated mechanisms to associate organization-defined security and privacy attributes with data objects during creation, modification, and transmission.
[VALIDATION] IF system_processes_data = TRUE AND attribute_binding_mechanism = FALSE THEN critical_violation

[RULE-02] Security attributes SHALL include at minimum: data classification level, access authorization requirements, retention period, and high-value asset designation.
[VALIDATION] IF data_object EXISTS AND (classification = NULL OR access_auth = NULL OR retention = NULL) THEN violation

[RULE-03] Privacy attributes for PII SHALL include processing purpose, legal basis, individual consent status, and data subject rights applicability.
[VALIDATION] IF contains_pii = TRUE AND (purpose = NULL OR legal_basis = NULL OR consent_status = NULL) THEN violation

[RULE-04] Attribute associations MUST be cryptographically bound to information objects and retained throughout the data lifecycle including backup and archival.
[VALIDATION] IF attribute_binding_strength < "cryptographic" OR backup_retains_attributes = FALSE THEN violation

[RULE-05] All changes to security and privacy attributes MUST be logged with timestamp, user identity, old value, new value, and justification.
[VALIDATION] IF attribute_change_logged = FALSE OR log_missing_required_fields = TRUE THEN violation

[RULE-06] Permitted attribute values and ranges MUST be formally defined and approved by data owners before system implementation.
[VALIDATION] IF attribute_schema_approved = FALSE OR implementation_before_approval = TRUE THEN violation

[RULE-07] Security and privacy attributes MUST be reviewed for continued applicability quarterly or when triggered by system changes, regulatory updates, or data incidents.
[VALIDATION] IF last_review_date > 90_days AND no_triggering_event = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Attribute Schema Management - Define, approve, and maintain security and privacy attribute taxonomies
- [PROC-02] Automated Labeling Implementation - Deploy and configure systems for automatic attribute assignment
- [PROC-03] Attribute Audit and Monitoring - Monitor attribute changes and validate enforcement effectiveness
- [PROC-04] Quarterly Attribute Review - Assess attribute applicability and update schemas as needed

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Regulatory changes, major system updates, data breaches, merger/acquisition

## 7. SCENARIO PATTERNS

[SCENARIO-01: Unclassified Data Processing]
IF data_classification = "confidential"
AND system_clearance_level = "public"
AND override_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: PII Without Privacy Attributes]
IF data_contains_pii = TRUE
AND privacy_attributes_present = FALSE
AND system_processes_pii = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Attribute Change Without Audit]
IF attribute_value_changed = TRUE
AND change_audit_log_exists = FALSE
AND change_date < 24_hours_ago
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Backup Without Attributes]
IF data_backed_up = TRUE
AND backup_contains_attributes = FALSE
AND original_data_has_attributes = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Expired Attribute Review]
IF last_attribute_review > 90_days
AND no_system_changes = TRUE
AND no_regulatory_changes = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Associate security attributes with information | RULE-01, RULE-02 |
| Associate privacy attributes with information | RULE-01, RULE-03 |
| Retain attribute associations | RULE-04 |
| Establish permitted attributes for systems | RULE-06 |
| Determine permitted attribute values/ranges | RULE-06 |
| Audit changes to attributes | RULE-05 |
| Review attributes for applicability | RULE-07 |
```