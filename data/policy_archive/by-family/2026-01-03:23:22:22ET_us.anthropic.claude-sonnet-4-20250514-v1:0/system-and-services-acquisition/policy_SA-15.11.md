# POLICY: SA-15.11: Archive System or Component

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-15.11 |
| NIST Control | SA-15.11: Archive System or Component |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | archive, developer, system component, security review, privacy review, evidence, baseline |

## 1. POLICY STATEMENT
Developers of systems or system components must archive deliverables with supporting evidence from final security and privacy reviews. This ensures availability of configuration baselines and supporting documentation for future system modifications and compliance validation.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All systems and components developed internally |
| External Vendors/Contractors | YES | Systems and components procured from third parties |
| COTS Products | CONDITIONAL | When customization or integration requires security/privacy review |
| Open Source Components | CONDITIONAL | When modified or integrated into critical systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Developers | • Archive all required artifacts and evidence<br>• Maintain archive integrity and accessibility<br>• Provide archive contents upon request |
| CISO Office | • Define archival requirements and standards<br>• Validate archive completeness<br>• Approve archive retention schedules |
| Procurement Team | • Include archival requirements in contracts<br>• Verify vendor compliance with archival obligations<br>• Manage archive handover processes |

## 4. RULES
[RULE-01] Developers MUST archive the final system or component deliverable together with all evidence supporting the final security and privacy review before release or delivery.
[VALIDATION] IF system_released = TRUE AND archive_created = FALSE THEN critical_violation

[RULE-02] Archives MUST include hardware specifications, source code, object code, and all relevant development documentation that establishes a configuration baseline.
[VALIDATION] IF archive_missing_baseline_components = TRUE THEN violation

[RULE-03] Archive creation MUST be completed within 5 business days of final security and privacy review approval.
[VALIDATION] IF days_since_review_approval > 5 AND archive_status != "complete" THEN violation

[RULE-04] Archives MUST be stored in a secure, accessible location with appropriate access controls and backup procedures for a minimum of 7 years or system lifecycle plus 3 years, whichever is longer.
[VALIDATION] IF archive_age > retention_period AND archive_status = "active" THEN review_required

[RULE-05] Third-party developers MUST provide archives in formats specified in acquisition contracts and compatible with organizational standards.
[VALIDATION] IF vendor_archive_format NOT IN approved_formats THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Archive Creation - Process for developers to create compliant archives
- [PROC-02] Archive Validation - Verification of archive completeness and format compliance
- [PROC-03] Archive Storage and Access - Secure storage and controlled access procedures
- [PROC-04] Vendor Archive Requirements - Contract language and validation for third-party archives

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: System modifications, vendor changes, regulatory updates, archive access incidents

## 7. SCENARIO PATTERNS
[SCENARIO-01: Internal Development Release]
IF development_type = "internal"
AND security_review_status = "approved"
AND privacy_review_status = "approved"
AND archive_created = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Vendor Deliverable Archive]
IF vendor_type = "third_party"
AND contract_includes_archive_requirements = TRUE
AND archive_received = FALSE
AND system_delivered = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Archive Content Validation]
IF archive_exists = TRUE
AND source_code_included = FALSE
AND system_type = "custom_developed"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Archive Retention Compliance]
IF archive_age > 7_years
AND system_status = "decommissioned"
AND retention_extension_approved = FALSE
THEN compliance = TRUE
action_required = "Archive disposal authorized"

[SCENARIO-05: COTS Product Archive]
IF product_type = "COTS"
AND customization_level = "significant"
AND security_review_conducted = TRUE
AND vendor_archive_provided = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer required to archive system/component with security and privacy review evidence | [RULE-01] |
| Archive includes configuration baseline components | [RULE-02] |
| Timely archive creation | [RULE-03] |
| Secure archive storage and retention | [RULE-04] |
| Third-party archive format compliance | [RULE-05] |