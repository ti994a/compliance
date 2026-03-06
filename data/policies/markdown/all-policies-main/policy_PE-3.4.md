# POLICY: PE-3.4: Lockable Casings

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-3.4 |
| NIST Control | PE-3.4: Lockable Casings |
| Version | 1.0 |
| Owner | Chief Physical Security Officer |
| Keywords | lockable casings, physical protection, unauthorized access, portable devices, theft prevention |

## 1. POLICY STATEMENT
System components identified as requiring protection from unauthorized physical access MUST be secured using lockable physical casings. This policy applies to portable devices, servers, network equipment, and other critical IT components that are susceptible to theft or unauthorized physical manipulation.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Portable devices (laptops, tablets, smartphones) | YES | Company-owned devices containing sensitive data |
| Server equipment | YES | Servers in non-secure locations or temporary deployments |
| Network infrastructure | YES | Switches, routers, wireless access points in accessible areas |
| Desktop workstations | CONDITIONAL | Only those in high-risk locations or containing sensitive data |
| Personal devices | NO | BYOD devices not subject to physical casing requirements |
| Equipment in secure data centers | NO | Already protected by facility-level controls |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Asset Manager | • Maintain inventory of components requiring lockable casings<br>• Procure appropriate casing solutions<br>• Track casing deployment and compliance |
| Physical Security Officer | • Define risk criteria for casing requirements<br>• Approve casing specifications and vendors<br>• Conduct compliance assessments |
| Department Managers | • Ensure employees comply with casing requirements<br>• Report theft or tampering incidents<br>• Budget for required physical security controls |

## 4. RULES
[RULE-01] System components identified as high-risk or containing sensitive data MUST be protected by lockable physical casings when deployed in non-secure environments.
[VALIDATION] IF component_risk_level = "high" AND environment_security = "non-secure" AND lockable_casing = FALSE THEN violation

[RULE-02] Lockable casings MUST meet minimum security specifications including tamper-evident features and resistance to common bypass tools.
[VALIDATION] IF casing_specifications_approved = FALSE OR tamper_evident = FALSE THEN violation

[RULE-03] Keys or access codes for lockable casings MUST be managed through the organization's key management system and limited to authorized personnel only.
[VALIDATION] IF casing_access_method NOT IN key_management_system OR unauthorized_key_holder = TRUE THEN violation

[RULE-04] Theft or tampering of lockable casings MUST be reported to the security team within 2 hours of discovery.
[VALIDATION] IF incident_type = "casing_theft_tampering" AND report_time > 2_hours THEN violation

[RULE-05] Lockable casing integrity MUST be verified during quarterly physical security inspections.
[VALIDATION] IF last_casing_inspection > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Risk Assessment - Evaluate and classify system components requiring lockable casing protection
- [PROC-02] Casing Procurement and Deployment - Standard process for acquiring and installing approved lockable casings
- [PROC-03] Key Management for Physical Casings - Procedures for issuing, tracking, and revoking casing access
- [PROC-04] Incident Response for Physical Tampering - Response procedures for casing theft or tampering events

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents involving physical theft, changes to risk assessment methodology, new device categories

## 7. SCENARIO PATTERNS
[SCENARIO-01: Laptop in Public Space]
IF device_type = "laptop"
AND location_type = "public_workspace"
AND data_classification = "confidential"
AND lockable_casing = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Server in Branch Office]
IF component_type = "server"
AND facility_security_level = "standard_office"
AND lockable_casing = TRUE
AND casing_approved_specs = TRUE
THEN compliance = TRUE

[SCENARIO-03: Missing Casing Keys]
IF lockable_casing = TRUE
AND key_location = "unknown"
AND key_management_system_tracking = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Quarterly Inspection Overdue]
IF lockable_casing = TRUE
AND last_inspection_date > 90_days
AND inspection_waiver = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Tamper Evidence Found]
IF casing_tamper_evident = TRUE
AND tampering_detected = TRUE
AND incident_reported = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Lockable physical casings protect system components from unauthorized physical access | [RULE-01] |
| Casings meet security specifications and standards | [RULE-02] |
| Access control for casing keys/codes is properly managed | [RULE-03] |
| Incident reporting for physical security breaches | [RULE-04] |
| Regular verification of casing integrity | [RULE-05] |