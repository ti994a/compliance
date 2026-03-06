```markdown
# POLICY: SR-4(4): Supply Chain Integrity — Pedigree

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-4-4 |
| NIST Control | SR-4(4): Supply Chain Integrity — Pedigree |
| Version | 1.0 |
| Owner | Chief Supply Chain Officer |
| Keywords | supply chain, pedigree, provenance, component integrity, SWID tags, bill of materials |

## 1. POLICY STATEMENT
The organization MUST employ controls to validate the internal composition and provenance of critical or mission-essential technologies, products, and services to ensure system and component integrity. All critical system components MUST have documented pedigree information including material composition, software composition, and evidentiary artifacts that validate supplier claims about internal composition and provenance.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical/Mission-Essential Systems | YES | All systems classified as critical or mission-essential |
| Commercial Off-the-Shelf (COTS) Products | YES | When used in critical systems |
| Custom Developed Software | YES | All internally developed software for critical systems |
| Third-Party Software Components | YES | Including open-source and proprietary components |
| Microelectronics/Hardware Components | YES | For critical system hardware |
| Non-Critical Systems | CONDITIONAL | Only if handling sensitive data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Risk Manager | • Define pedigree validation controls<br>• Oversee pedigree analysis methods<br>• Maintain supplier pedigree requirements |
| System Owners | • Identify critical/mission-essential components<br>• Ensure pedigree documentation is current<br>• Validate component integrity |
| Procurement Team | • Require pedigree documentation from suppliers<br>• Validate evidentiary artifacts<br>• Maintain bill of materials |

## 4. RULES
[RULE-01] Critical and mission-essential system components MUST have documented pedigree information including internal composition and provenance validation.
[VALIDATION] IF component_criticality = "critical" OR component_criticality = "mission-essential" AND pedigree_documented = FALSE THEN violation

[RULE-02] Software components MUST include Software Identification (SWID) tags and component inventory documentation for version tracking and composition validation.
[VALIDATION] IF component_type = "software" AND (swid_tags_present = FALSE OR component_inventory = FALSE) THEN violation

[RULE-03] Hardware components MUST include manufacturer declarations of platform attributes, serial numbers, hardware inventory, and cryptographic measurements bound to hardware.
[VALIDATION] IF component_type = "hardware" AND (platform_attributes = FALSE OR hardware_inventory = FALSE OR crypto_measurements = FALSE) THEN violation

[RULE-04] Pedigree validation analysis MUST be conducted before system integration and annually thereafter for all critical components.
[VALIDATION] IF pedigree_analysis_date < (current_date - 365_days) OR integration_pedigree_check = FALSE THEN violation

[RULE-05] Evidentiary artifacts from suppliers MUST be validated against independent sources or through cryptographic verification methods.
[VALIDATION] IF evidentiary_artifacts_validated = FALSE OR validation_method = "none" THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Pedigree Documentation Collection - Process for obtaining and validating supplier pedigree information
- [PROC-02] Component Composition Analysis - Technical analysis of internal component composition
- [PROC-03] Provenance Validation - Verification of component origin and supply chain path
- [PROC-04] Evidentiary Artifact Management - Collection, validation, and maintenance of pedigree evidence

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New critical system deployment, supply chain incident, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Software Pedigree]
IF component_type = "software"
AND system_criticality = "critical"
AND swid_tags_present = FALSE
AND component_inventory = "incomplete"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Hardware Without Cryptographic Binding]
IF component_type = "hardware"
AND crypto_measurements = FALSE
AND hardware_inventory = "present"
AND system_criticality = "mission-essential"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Outdated Pedigree Analysis]
IF pedigree_analysis_date < (current_date - 400_days)
AND component_criticality = "critical"
AND system_status = "operational"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unvalidated Supplier Claims]
IF evidentiary_artifacts_present = TRUE
AND supplier_claims_validated = FALSE
AND validation_method = "none"
AND component_criticality = "mission-essential"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Complete Pedigree Documentation]
IF pedigree_documented = TRUE
AND evidentiary_artifacts_validated = TRUE
AND pedigree_analysis_date > (current_date - 300_days)
AND (swid_tags_present = TRUE OR component_type != "software")
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Controls employed to ensure system/component integrity are defined | RULE-01, RULE-04 |
| Controls are employed to ensure system/component integrity | RULE-02, RULE-03, RULE-05 |
| Analysis method to validate composition and provenance is defined | RULE-04 |
| Analysis is conducted to ensure system/component integrity | RULE-04, RULE-05 |
```