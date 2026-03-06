# POLICY: SR-12: Component Disposal

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-12 |
| NIST Control | SR-12: Component Disposal |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | component disposal, data destruction, supply chain, media sanitization, asset disposal |

## 1. POLICY STATEMENT
All organizational data, documentation, tools, and system components MUST be disposed of using approved sanitization techniques and methods throughout the system development lifecycle. Disposal activities MUST prevent unauthorized access to sensitive information and prevent components from entering unauthorized markets.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Hardware components | YES | Servers, workstations, mobile devices, storage media |
| Software/digital assets | YES | Source code, documentation, cryptographic keys |
| Documentation | YES | Physical and digital system documentation |
| Development artifacts | YES | Prototypes, test systems, research materials |
| Third-party components | YES | Vendor-provided hardware and software |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Asset Management Team | • Maintain inventory of disposable components<br>• Execute approved disposal procedures<br>• Document disposal activities |
| Information Security Team | • Define sanitization requirements<br>• Approve disposal methods<br>• Validate disposal completion |
| Supply Chain Manager | • Oversee vendor disposal activities<br>• Ensure contractual disposal requirements<br>• Monitor gray market prevention |

## 4. RULES
[RULE-01] All system components containing sensitive data MUST be sanitized using NIST SP 800-88 approved methods before disposal.
[VALIDATION] IF component_contains_sensitive_data = TRUE AND sanitization_method NOT IN approved_methods THEN violation

[RULE-02] Cryptographic keys and certificates MUST be securely destroyed and cannot be recovered after component disposal.
[VALIDATION] IF crypto_material_present = TRUE AND destruction_verified = FALSE THEN critical_violation

[RULE-03] Component disposal activities MUST be documented with disposal method, date, responsible party, and verification of completion.
[VALIDATION] IF disposal_completed = TRUE AND (disposal_method = NULL OR disposal_date = NULL OR responsible_party = NULL) THEN violation

[RULE-04] High-value components MUST have witnessed destruction with dual-person control and signed attestation.
[VALIDATION] IF component_value > high_threshold AND witness_count < 2 THEN violation

[RULE-05] Disposal vendors MUST be approved and provide certificates of destruction within 30 days of disposal completion.
[VALIDATION] IF vendor_disposal = TRUE AND (vendor_approved = FALSE OR certificate_received = FALSE OR certificate_days > 30) THEN violation

[RULE-06] Development and prototype systems MUST be disposed of using the same security controls as production systems.
[VALIDATION] IF system_type IN ["development", "prototype"] AND disposal_controls != production_controls THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Asset Sanitization Procedure - NIST SP 800-88 compliant data destruction methods
- [PROC-02] Vendor Disposal Management - Third-party disposal vendor qualification and oversight
- [PROC-03] Disposal Documentation - Recording and tracking of all disposal activities
- [PROC-04] Witnessed Destruction - Dual-person control procedures for high-value assets

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New sanitization technologies, disposal incidents, regulatory changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unwitnessed High-Value Server Disposal]
IF component_type = "server"
AND component_value > $10000
AND witness_count < 2
AND disposal_completed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Missing Crypto Key Destruction]
IF component_contains_crypto = TRUE
AND disposal_method = "physical_destruction"
AND key_destruction_verified = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Vendor Certificate Delay]
IF disposal_vendor_used = TRUE
AND disposal_date < (current_date - 35_days)
AND certificate_of_destruction = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Development System Improper Disposal]
IF system_environment = "development"
AND contains_production_data = TRUE
AND sanitization_level < "purge"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Undocumented Component Disposal]
IF disposal_completed = TRUE
AND disposal_documentation = FALSE
AND component_sensitivity = "confidential"
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Data, documentation, tools, or system components disposed of are defined | RULE-01, RULE-06 |
| Disposal using defined techniques and methods | RULE-01, RULE-02, RULE-04 |
| Documentation of disposal activities | RULE-03, RULE-05 |
| Supply chain protection during disposal | RULE-05, RULE-06 |