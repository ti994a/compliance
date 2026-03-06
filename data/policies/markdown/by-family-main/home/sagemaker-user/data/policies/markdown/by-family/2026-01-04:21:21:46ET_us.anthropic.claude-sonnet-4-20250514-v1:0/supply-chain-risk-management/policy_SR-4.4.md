# POLICY: SR-4.4: Supply Chain Integrity — Pedigree

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-4.4 |
| NIST Control | SR-4.4: Supply Chain Integrity — Pedigree |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | supply chain, pedigree, provenance, integrity, validation, composition, critical systems, mission-essential |

## 1. POLICY STATEMENT
The organization SHALL employ controls to ensure system and component integrity by validating the internal composition and provenance of critical or mission-essential technologies, products, and services. All critical system components MUST have documented pedigree information that validates their authenticity and composition throughout the supply chain lifecycle.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical Information Systems | YES | All systems classified as critical or mission-essential |
| Mission-Essential Technologies | YES | Hardware, software, and firmware components |
| Commercial Off-the-Shelf Products | CONDITIONAL | Only when used in critical systems |
| Development/Test Systems | CONDITIONAL | Only when containing production data |
| Third-Party Services | YES | Cloud services and managed services for critical systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Risk Manager | • Define pedigree validation requirements<br>• Oversee supplier pedigree documentation<br>• Maintain approved supplier registry |
| System Owners | • Identify critical system components requiring pedigree validation<br>• Ensure pedigree documentation is current<br>• Report pedigree validation failures |
| Procurement Team | • Collect pedigree documentation during acquisition<br>• Validate supplier pedigree claims<br>• Maintain component inventory records |

## 4. RULES
[RULE-01] Critical and mission-essential system components MUST have documented pedigree information including internal composition, provenance, and supply chain history.
[VALIDATION] IF component_criticality = "critical" AND pedigree_documented = FALSE THEN violation

[RULE-02] Pedigree validation analysis MUST be conducted using defined methods including software identification tags, hardware component inventory, and cryptographic measurements.
[VALIDATION] IF pedigree_analysis_method = "undefined" OR analysis_conducted = FALSE THEN violation

[RULE-03] Evidentiary artifacts including SWID tags, manufacturer declarations, serial numbers, and firmware hashes MUST be collected and validated for all critical components.
[VALIDATION] IF critical_component = TRUE AND (swid_tags = NULL OR manufacturer_declaration = NULL OR firmware_hash = NULL) THEN violation

[RULE-04] Pedigree information MUST be validated against manufacturer claims and independently verified through trusted sources when available.
[VALIDATION] IF pedigree_validation_status = "unverified" AND component_deployed = TRUE THEN violation

[RULE-05] Changes to critical component composition or provenance MUST trigger re-validation of pedigree information within 30 days.
[VALIDATION] IF component_change_date > 30_days AND pedigree_revalidation = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Pedigree Documentation Collection - Standardized process for gathering component composition and provenance evidence
- [PROC-02] Pedigree Validation Analysis - Technical analysis methods for verifying internal composition claims
- [PROC-03] Supplier Pedigree Assessment - Evaluation of supplier pedigree management capabilities
- [PROC-04] Component Inventory Management - Tracking and maintaining records of critical component pedigree

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Supply chain incidents, new critical system deployments, major component updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Undocumented Critical Component]
IF component_criticality = "critical"
AND pedigree_documentation = "missing"
AND system_status = "production"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Unvalidated Software Component]
IF component_type = "software"
AND swid_tags = "present"
AND validation_status = "pending"
AND deployment_timeframe < 30_days
THEN compliance = TRUE

[SCENARIO-03: Hardware Component Without Manufacturer Declaration]
IF component_type = "hardware"
AND criticality = "mission-essential"
AND manufacturer_declaration = "missing"
AND firmware_hash = "unavailable"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Supplier Pedigree Claims Mismatch]
IF supplier_claim = "documented"
AND independent_verification = "failed"
AND component_status = "deployed"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Legacy System Component Exception]
IF system_age > 5_years
AND pedigree_documentation = "partial"
AND risk_assessment = "completed"
AND compensating_controls = "implemented"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Controls employed to ensure system and component integrity are defined | [RULE-01], [RULE-02] |
| Controls are employed to ensure system and component integrity | [RULE-03], [RULE-04] |
| Analysis method to validate internal composition and provenance is defined | [RULE-02] |
| Analysis is conducted to ensure system and component integrity | [RULE-04], [RULE-05] |