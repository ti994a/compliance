# POLICY: AC-16.5: Attribute Displays on Objects to Be Output

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-16.5 |
| NIST Control | AC-16.5: Attribute Displays on Objects to Be Output |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | attribute display, output devices, human-readable, security attributes, privacy attributes, dissemination markings |

## 1. POLICY STATEMENT
All systems MUST display security and privacy attributes in human-readable form on objects transmitted to output devices to identify special dissemination, handling, or distribution instructions. Standard naming conventions MUST be used for all displayed attributes to ensure consistent interpretation across the organization.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All systems processing classified or sensitive data |
| Output Devices | YES | Printers, displays, mobile devices, tablets |
| Data Objects | CONDITIONAL | Only those requiring special handling instructions |
| Public Systems | NO | Systems processing only public information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owners | • Implement attribute display requirements<br>• Ensure output devices comply with display standards<br>• Validate attribute visibility on all outputs |
| Data Stewards | • Define security and privacy attributes for data objects<br>• Establish handling and dissemination instructions<br>• Review attribute accuracy and completeness |
| Security Engineers | • Configure systems to display required attributes<br>• Implement standard naming conventions<br>• Test attribute display functionality |

## 4. RULES
[RULE-01] Systems MUST display security attributes in human-readable form on all objects transmitted to output devices that contain classified or sensitive information.
[VALIDATION] IF object_sensitivity > "public" AND output_device_transmission = TRUE AND security_attributes_displayed = FALSE THEN violation

[RULE-02] Systems MUST display privacy attributes in human-readable form on all objects containing personally identifiable information (PII) transmitted to output devices.
[VALIDATION] IF contains_pii = TRUE AND output_device_transmission = TRUE AND privacy_attributes_displayed = FALSE THEN violation

[RULE-03] All displayed security and privacy attributes MUST use organization-approved standard naming conventions and formatting.
[VALIDATION] IF attributes_displayed = TRUE AND standard_naming_convention = FALSE THEN violation

[RULE-04] Attribute displays MUST include dissemination, handling, and distribution instructions when applicable to the data classification.
[VALIDATION] IF data_classification >= "restricted" AND handling_instructions_displayed = FALSE THEN violation

[RULE-05] Output devices MUST be configured to display full attribute values when unmasked by authorized users to prevent unauthorized exposure.
[VALIDATION] IF user_authorized = TRUE AND attribute_masking = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Attribute Definition Process - Establish and maintain security and privacy attributes for data objects
- [PROC-02] Output Device Configuration - Configure all output devices to display required attributes
- [PROC-03] Naming Convention Management - Maintain standard naming conventions for attribute display
- [PROC-04] Display Testing - Validate attribute visibility and readability on output devices

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New output device deployment, data classification changes, security incidents involving attribute display

## 7. SCENARIO PATTERNS
[SCENARIO-01: Classified Document Printing]
IF document_classification = "confidential"
AND output_device = "printer"
AND security_attributes_visible = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: PII Display on Mobile Device]
IF data_contains_pii = TRUE
AND output_device = "mobile_tablet"
AND privacy_attributes_displayed = TRUE
AND standard_naming_used = TRUE
THEN compliance = TRUE

[SCENARIO-03: Non-Standard Attribute Format]
IF attributes_displayed = TRUE
AND naming_convention = "custom_format"
AND approved_standard = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Public Information Output]
IF data_classification = "public"
AND special_handling_required = FALSE
AND attribute_display = "not_required"
THEN compliance = TRUE

[SCENARIO-05: Masked Attributes for Unauthorized User]
IF user_clearance_level < data_classification_level
AND attribute_masking = TRUE
AND shoulder_surfing_risk = "high"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Security attributes displayed in human-readable form | [RULE-01] |
| Privacy attributes displayed in human-readable form | [RULE-02] |
| Standard naming conventions used | [RULE-03] |
| Dissemination instructions displayed | [RULE-04] |
| Proper attribute masking controls | [RULE-05] |