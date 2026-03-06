# POLICY: SR-4.3: Validate as Genuine and Not Altered

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-4.3 |
| NIST Control | SR-4.3: Validate as Genuine and Not Altered |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | supply chain, validation, authenticity, tampering, counterfeit, hardware verification |

## 1. POLICY STATEMENT
All systems and system components received by the organization MUST be validated as genuine and unaltered before deployment or integration into production environments. The organization SHALL employ technical and procedural controls to detect counterfeit, tampered, or altered components throughout the supply chain process.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Hardware components | YES | All servers, network equipment, storage devices |
| Software packages | YES | Commercial and open-source software |
| Firmware | YES | BIOS, embedded system firmware |
| Third-party services | CONDITIONAL | When physical components are involved |
| Cloud services | NO | Covered under separate cloud security policies |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Manager | • Define validation requirements for suppliers<br>• Maintain approved supplier list<br>• Coordinate component verification processes |
| Security Team | • Implement technical validation controls<br>• Perform forensic analysis of suspect components<br>• Train personnel on tampering detection |
| Procurement Team | • Verify supplier authenticity<br>• Document chain of custody<br>• Report suspicious deliveries |

## 4. RULES
[RULE-01] All system components MUST undergo authenticity validation using at least two independent verification methods before acceptance.
[VALIDATION] IF component_received = TRUE AND verification_methods < 2 THEN violation

[RULE-02] Hardware components SHALL be inspected for visible tampering indicators including packaging inconsistencies, broken seals, and incorrect labeling within 24 hours of receipt.
[VALIDATION] IF hardware_received = TRUE AND visual_inspection_time > 24_hours THEN violation

[RULE-03] Cryptographic hash verification or digital signature validation MUST be performed on all software components and firmware updates.
[VALIDATION] IF software_component = TRUE AND (hash_verified = FALSE OR signature_verified = FALSE) THEN critical_violation

[RULE-04] Components suspected of tampering or counterfeiting MUST be immediately quarantined and SHALL NOT be deployed to production environments.
[VALIDATION] IF tampering_suspected = TRUE AND quarantine_status = FALSE THEN critical_violation

[RULE-05] Suppliers MUST provide certificates of authenticity and chain of custody documentation for all critical system components.
[VALIDATION] IF component_criticality = "high" AND (authenticity_certificate = FALSE OR custody_documentation = FALSE) THEN violation

[RULE-06] Personnel involved in component receipt and validation MUST complete anti-counterfeiting training annually.
[VALIDATION] IF role_involves_validation = TRUE AND training_completion_date < (current_date - 365_days) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Authentication Protocol - Technical validation methods and acceptance criteria
- [PROC-02] Supplier Verification Process - Supplier authenticity and trustworthiness assessment
- [PROC-03] Incident Response for Counterfeit Detection - Actions when tampering is suspected
- [PROC-04] Chain of Custody Documentation - Tracking component provenance and handling

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving counterfeit components, new supplier onboarding, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Hardware Delivery Inspection]
IF hardware_component = TRUE
AND visual_inspection_completed = FALSE
AND acceptance_time > 24_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Software Without Verification]
IF software_package = TRUE
AND hash_verification = FALSE
AND digital_signature_check = FALSE
AND deployment_status = "production"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Suspected Counterfeit Component]
IF tampering_indicators_present = TRUE
AND quarantine_action = FALSE
AND time_since_detection < 1_hour
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Missing Supplier Documentation]
IF component_criticality = "high"
AND supplier_certificate = FALSE
AND procurement_approved = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Untrained Validation Personnel]
IF personnel_role = "component_validator"
AND last_training_date < (current_date - 365_days)
AND validation_activities_performed = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Controls to validate genuineness are defined | [RULE-01], [RULE-03] |
| Controls to validate genuineness are employed | [RULE-01], [RULE-02] |
| Controls to validate non-alteration are defined | [RULE-03], [RULE-04] |
| Controls to validate non-alteration are employed | [RULE-02], [RULE-03] |