# POLICY: MP-6.3: Nondestructive Techniques

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MP-6.3 |
| NIST Control | MP-6.3: Nondestructive Techniques |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | portable storage, sanitization, nondestructive, USB devices, malware prevention |

## 1. POLICY STATEMENT
All portable storage devices MUST undergo nondestructive sanitization before connection to organizational systems under defined risk circumstances. This policy ensures malicious code cannot be introduced through removable media while preserving device functionality and data integrity.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All portable storage devices | YES | External drives, USB devices, optical media, flash memory |
| Employee-owned devices | YES | When connecting to organizational systems |
| Vendor/contractor devices | YES | All third-party portable storage devices |
| Internal data transfers | CONDITIONAL | Only under defined high-risk circumstances |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Team | • Define sanitization circumstances<br>• Maintain sanitization tools and procedures<br>• Monitor compliance and violations |
| System Administrators | • Implement technical controls<br>• Perform sanitization procedures<br>• Document sanitization activities |
| End Users | • Request sanitization when required<br>• Report unsanitized device connections<br>• Comply with connection restrictions |

## 4. RULES
[RULE-01] Portable storage devices MUST undergo nondestructive sanitization prior to system connection when obtained from untrusted sources, purchased from new vendors, or when chain of custody cannot be verified.
[VALIDATION] IF device_source = "untrusted" OR chain_of_custody = "unverified" AND sanitization_performed = FALSE THEN violation

[RULE-02] Organizations MUST define and document specific circumstances requiring portable storage device sanitization within their security policies.
[VALIDATION] IF sanitization_circumstances = "undefined" OR documentation_status = "missing" THEN policy_violation

[RULE-03] Sanitization procedures MUST use nondestructive techniques that preserve device functionality and legitimate data while removing potential malicious code.
[VALIDATION] IF sanitization_method = "destructive" OR device_functionality = "impaired" THEN procedure_violation

[RULE-04] All sanitization activities MUST be documented with device identification, sanitization method, date/time, and responsible personnel.
[VALIDATION] IF sanitization_performed = TRUE AND documentation_complete = FALSE THEN documentation_violation

[RULE-05] Systems MUST technically enforce sanitization requirements through endpoint controls that prevent connection of unsanitized devices when circumstances warrant.
[VALIDATION] IF technical_enforcement = FALSE AND risk_circumstances = TRUE THEN control_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Device Risk Assessment - Evaluate portable storage devices for sanitization requirements
- [PROC-02] Nondestructive Sanitization - Apply approved sanitization techniques to portable devices
- [PROC-03] Sanitization Documentation - Record all sanitization activities and outcomes
- [PROC-04] Exception Handling - Process requests for sanitization exemptions with risk justification

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving portable media, new device types, sanitization tool updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Vendor USB Drive]
IF device_type = "USB_drive"
AND vendor_status = "new"
AND sanitization_performed = FALSE
AND connection_attempted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Employee Personal Device]
IF device_ownership = "personal"
AND connection_location = "corporate_network"
AND chain_of_custody = "unverified"
AND sanitization_bypass = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Internal Device Transfer]
IF device_source = "internal"
AND chain_of_custody = "verified"
AND risk_assessment = "low"
AND sanitization_required = FALSE
THEN compliance = TRUE

[SCENARIO-04: Contractor Equipment]
IF user_type = "contractor"
AND device_source = "external"
AND sanitization_documented = TRUE
AND technical_scan_passed = TRUE
THEN compliance = TRUE

[SCENARIO-05: Emergency Access Override]
IF business_justification = "emergency"
AND sanitization_bypassed = TRUE
AND compensating_controls = FALSE
AND approval_documented = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Apply nondestructive sanitization techniques to portable storage devices | [RULE-01], [RULE-03] |
| Define circumstances requiring sanitization | [RULE-02] |
| Sanitize devices prior to system connection | [RULE-01], [RULE-05] |
| Document sanitization activities | [RULE-04] |
| Implement technical enforcement controls | [RULE-05] |