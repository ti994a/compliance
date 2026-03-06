# POLICY: SR-4.4: Supply Chain Integrity — Pedigree

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-4.4 |
| NIST Control | SR-4.4: Supply Chain Integrity — Pedigree |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | supply chain, pedigree, provenance, composition, integrity, validation, critical systems, mission-essential |

## 1. POLICY STATEMENT
The organization SHALL employ controls to ensure system and component integrity by validating the internal composition and provenance of critical or mission-essential technologies, products, and services. All critical systems and components MUST have documented pedigree information that validates their internal composition and supply chain provenance.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical Systems | YES | All systems classified as critical or mission-essential |
| Standard Systems | CONDITIONAL | When containing critical components |
| Third-party Components | YES | All components in critical systems |
| Software Components | YES | Including open-source and proprietary code |
| Hardware Components | YES | Including microelectronics and firmware |
| Cloud Services | YES | When supporting critical operations |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Risk Manager | • Define pedigree validation requirements<br>• Oversee supplier pedigree documentation<br>• Maintain component inventory and provenance records |
| System Owners | • Identify critical system components<br>• Ensure pedigree validation for system components<br>• Maintain system component inventories |
| Procurement Team | • Require pedigree documentation in contracts<br>• Validate supplier pedigree capabilities<br>• Collect and verify evidentiary artifacts |

## 4. RULES

[RULE-01] Critical and mission-essential systems MUST have documented controls to ensure integrity of all system components.
[VALIDATION] IF system_criticality IN ["critical", "mission-essential"] AND integrity_controls_documented = FALSE THEN violation

[RULE-02] Organizations MUST conduct pedigree analysis to validate internal composition and provenance of critical technologies, products, and services.
[VALIDATION] IF component_criticality = "critical" AND pedigree_analysis_conducted = FALSE THEN violation

[RULE-03] Suppliers of critical components MUST provide evidentiary artifacts including SWID tags, component inventories, platform attribute declarations, and hardware-bound measurements.
[VALIDATION] IF component_criticality = "critical" AND evidentiary_artifacts_provided = FALSE THEN violation

[RULE-04] Software components MUST include composition documentation of open-source and proprietary code with version information.
[VALIDATION] IF component_type = "software" AND composition_documented = FALSE THEN violation

[RULE-05] Hardware components MUST include material composition documentation and hardware-bound measurements such as firmware hashes.
[VALIDATION] IF component_type = "hardware" AND material_composition_documented = FALSE THEN violation

[RULE-06] Pedigree validation MUST be performed before integration of critical components into production systems.
[VALIDATION] IF component_criticality = "critical" AND pedigree_validated = FALSE AND integration_status = "production" THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Pedigree Validation Process - Defines methodology for validating component composition and provenance
- [PROC-02] Supplier Pedigree Requirements - Establishes mandatory pedigree documentation requirements for suppliers
- [PROC-03] Component Inventory Management - Maintains comprehensive inventory of critical system components
- [PROC-04] Evidentiary Artifact Collection - Processes for collecting and validating supplier-provided evidence

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New critical system deployment, supplier changes, security incidents involving supply chain

## 7. SCENARIO PATTERNS

[SCENARIO-01: Critical Component Missing Pedigree]
IF component_criticality = "critical"
AND pedigree_documentation = "missing"
AND system_status = "production"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Software Without Composition Details]
IF component_type = "software"
AND open_source_inventory = "missing"
AND version_tracking = "incomplete"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Hardware Without Material Composition]
IF component_type = "hardware"
AND material_composition = "undocumented"
AND firmware_hash_verified = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Supplier Lacks Evidentiary Artifacts]
IF supplier_category = "critical_component_provider"
AND swid_tags_provided = FALSE
AND platform_attributes_declared = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Complete Pedigree Documentation]
IF component_criticality = "critical"
AND pedigree_analysis_complete = TRUE
AND evidentiary_artifacts_validated = TRUE
AND integrity_controls_implemented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Controls to ensure system and component integrity are defined | [RULE-01] |
| Controls are employed to ensure system and component integrity | [RULE-01], [RULE-06] |
| Analysis method to validate internal composition and provenance is defined | [RULE-02] |
| Analysis is conducted to ensure system and component integrity | [RULE-02], [RULE-06] |
| Software composition validation | [RULE-04] |
| Hardware composition validation | [RULE-05] |
| Evidentiary artifact collection | [RULE-03] |