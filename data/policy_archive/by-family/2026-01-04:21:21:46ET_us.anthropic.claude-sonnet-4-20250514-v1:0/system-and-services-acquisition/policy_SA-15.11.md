# POLICY: SA-15.11: Archive System or Component

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-15.11 |
| NIST Control | SA-15.11: Archive System or Component |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | system archival, component archival, developer requirements, security review evidence, privacy review evidence, development artifacts |

## 1. POLICY STATEMENT
Developers of systems or system components must archive the delivered system/component along with all evidence supporting final security and privacy reviews. This archival ensures availability of development artifacts for future system upgrades, modifications, and compliance verification.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Internal Development Teams | YES | All internally developed systems and components |
| External Vendors/Contractors | YES | Systems/components developed under contract |
| COTS Products | CONDITIONAL | Only when customization/integration artifacts exist |
| Cloud Service Providers | YES | Custom configurations and integrations |
| Third-party Integrators | YES | Integration components and customizations |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Developers | • Archive all development artifacts per requirements<br>• Maintain evidence of security and privacy reviews<br>• Ensure archival completeness before delivery |
| CISO Office | • Define archival requirements and standards<br>• Verify archival compliance before system acceptance<br>• Maintain oversight of archival processes |
| Procurement Team | • Include archival requirements in contracts<br>• Verify vendor compliance with archival obligations<br>• Enforce contractual archival deliverables |

## 4. RULES
[RULE-01] Developers MUST archive the complete system or component together with all evidence supporting final security and privacy reviews before release or delivery.
[VALIDATION] IF system_delivered = TRUE AND (security_review_evidence_archived = FALSE OR privacy_review_evidence_archived = FALSE) THEN violation

[RULE-02] Archived materials MUST include hardware specifications, source code, object code, and all relevant development documentation.
[VALIDATION] IF archival_complete = TRUE AND (hardware_specs_missing = TRUE OR source_code_missing = TRUE OR object_code_missing = TRUE OR documentation_missing = TRUE) THEN violation

[RULE-03] Archival MUST occur within 30 days of final security and privacy review completion and before system deployment.
[VALIDATION] IF days_since_review_completion > 30 AND archival_status != "complete" THEN violation

[RULE-04] Archived materials MUST be retained for minimum 7 years or system lifecycle plus 3 years, whichever is longer.
[VALIDATION] IF archive_age > retention_period AND archive_status = "deleted" THEN violation

[RULE-05] All contractual agreements with external developers MUST explicitly require archival deliverables and specify retention requirements.
[VALIDATION] IF contract_type = "external_development" AND archival_requirements_specified = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Archival Process - Standardized process for archiving systems and components with required artifacts
- [PROC-02] Vendor Archival Verification - Process for verifying external vendor compliance with archival requirements
- [PROC-03] Archive Retention Management - Process for managing long-term retention and retrieval of archived materials
- [PROC-04] Contract Review Process - Process ensuring all development contracts include proper archival clauses

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually  
- Triggering events: Major system releases, contract renewals, regulatory changes, archival process failures

## 7. SCENARIO PATTERNS
[SCENARIO-01: Internal Development Completion]
IF development_type = "internal"
AND security_review_status = "complete"
AND privacy_review_status = "complete"
AND archival_status = "pending"
AND days_since_review = 35
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Vendor Delivery Without Archives]
IF vendor_delivery = TRUE
AND system_components_delivered = TRUE
AND security_evidence_archived = FALSE
AND contract_archival_required = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Incomplete Archive Contents]
IF archival_submitted = TRUE
AND source_code_included = TRUE
AND documentation_included = TRUE
AND security_review_evidence = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Premature Archive Deletion]
IF archive_age = 5_years
AND system_lifecycle_remaining = 3_years
AND archive_deletion_requested = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: COTS Integration Archive]
IF product_type = "COTS"
AND customization_performed = TRUE
AND integration_artifacts_archived = TRUE
AND security_review_evidence_archived = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Developer required to archive system/component with security and privacy review evidence | [RULE-01] |
| Retention of key development artifacts for configuration baseline | [RULE-02], [RULE-04] |
| Contractual enforcement of archival requirements | [RULE-05] |
| Timely archival before system release | [RULE-03] |