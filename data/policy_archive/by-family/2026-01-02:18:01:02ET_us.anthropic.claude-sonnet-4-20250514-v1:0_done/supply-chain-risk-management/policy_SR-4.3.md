# POLICY: SR-4.3: Validate as Genuine and Not Altered

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-4.3 |
| NIST Control | SR-4.3: Validate as Genuine and Not Altered |
| Version | 1.0 |
| Owner | Supply Chain Risk Manager |
| Keywords | supply chain, validation, genuine, tampering, counterfeit, hardware verification, component integrity |

## 1. POLICY STATEMENT
All systems and system components received by the organization MUST be validated as genuine and unaltered before deployment or integration into production environments. The organization SHALL employ technical and procedural controls to detect counterfeit, tampered, or compromised hardware and software components throughout the supply chain process.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Hardware Components | YES | All servers, network devices, storage systems |
| Software Components | YES | Operating systems, applications, firmware |
| Third-party Suppliers | YES | All vendors providing IT components |
| Internal IT Staff | YES | Personnel handling component receipt/validation |
| Contractors | YES | When handling component procurement/validation |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Risk Manager | • Define validation controls and procedures<br>• Oversee supplier validation processes<br>• Coordinate incident response for suspect components |
| IT Operations Manager | • Implement technical validation controls<br>• Train staff on component inspection procedures<br>• Maintain validation equipment and tools |
| Procurement Manager | • Ensure supplier contracts include validation requirements<br>• Verify supplier authenticity and credentials<br>• Document component chain of custody |

## 4. RULES

[RULE-01] All system components MUST undergo validation using organization-defined technical controls before acceptance into inventory.
[VALIDATION] IF component_received = TRUE AND technical_validation_completed = FALSE THEN violation

[RULE-02] Personnel receiving components MUST inspect packaging for tampering indicators including broken seals, inconsistent labeling, or damaged packaging.
[VALIDATION] IF tampering_indicators_present = TRUE AND inspection_documented = FALSE THEN violation

[RULE-03] Cryptographic hash verification or digital signature validation MUST be performed on all software components and firmware when available from manufacturers.
[VALIDATION] IF software_component = TRUE AND hash_verification_available = TRUE AND verification_performed = FALSE THEN violation

[RULE-04] Suspect or potentially counterfeit components MUST be quarantined immediately and reported to the Supply Chain Risk Manager within 4 hours of discovery.
[VALIDATION] IF component_suspect = TRUE AND quarantine_time > 0_hours THEN violation
[VALIDATION] IF component_suspect = TRUE AND report_time > 4_hours THEN violation

[RULE-05] All validation activities MUST be documented with results retained for minimum 7 years or component lifecycle, whichever is longer.
[VALIDATION] IF validation_performed = TRUE AND documentation_complete = FALSE THEN violation

[RULE-06] Components failing validation MUST NOT be deployed to production environments under any circumstances.
[VALIDATION] IF validation_status = "FAILED" AND production_deployment = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Receipt Inspection - Visual and physical inspection of all incoming components
- [PROC-02] Technical Validation Testing - Cryptographic verification and performance baseline testing
- [PROC-03] Suspect Component Handling - Quarantine and forensic analysis procedures
- [PROC-04] Supplier Validation - Verification of supplier authenticity and supply chain integrity
- [PROC-05] Staff Training - Training personnel to identify counterfeit and tampered components

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving supply chain, new supplier onboarding, regulatory changes, technology refresh cycles

## 7. SCENARIO PATTERNS

[SCENARIO-01: Hardware Component with Broken Seal]
IF component_type = "hardware"
AND packaging_seal = "broken"
AND visual_inspection_documented = TRUE
AND quarantine_initiated = TRUE
THEN compliance = TRUE

[SCENARIO-02: Software Without Hash Verification]
IF component_type = "software"
AND manufacturer_hash_available = TRUE
AND hash_verification_performed = FALSE
AND deployment_attempted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Suspect Component in Production]
IF validation_status = "SUSPECT"
AND component_location = "production"
AND quarantine_initiated = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Delayed Reporting of Counterfeit]
IF counterfeit_detected = TRUE
AND detection_time = "09:00"
AND report_time = "15:00"
AND report_required_by = "13:00"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Proper Validation Process]
IF component_received = TRUE
AND visual_inspection = "PASS"
AND technical_validation = "PASS"
AND documentation_complete = TRUE
AND deployment_authorized = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Controls to validate genuine components are defined | [RULE-01] |
| Controls are employed to validate genuine components | [RULE-01], [RULE-02], [RULE-03] |
| Controls to validate unaltered components are defined | [RULE-03] |
| Controls are employed to validate unaltered components | [RULE-03], [RULE-04], [RULE-06] |