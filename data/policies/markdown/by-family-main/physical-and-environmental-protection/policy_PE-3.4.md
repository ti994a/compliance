# POLICY: PE-3.4: Lockable Casings

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PE-3.4 |
| NIST Control | PE-3.4: Lockable Casings |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | lockable casings, physical protection, unauthorized access, portable devices, theft prevention |

## 1. POLICY STATEMENT
The organization SHALL use lockable physical casings to protect designated system components from unauthorized physical access and theft. All portable devices and critical system components identified as requiring enhanced physical protection MUST be secured using approved lockable casings when not under direct supervision.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Portable computing devices | YES | Laptops, tablets, smartphones used for business |
| Server equipment | CONDITIONAL | Only those in non-secured areas |
| Network infrastructure | CONDITIONAL | Equipment outside data centers |
| Personal devices | CONDITIONAL | Only if accessing company data |
| Data center equipment | NO | Already in secured facility |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Manager | • Define components requiring lockable casings<br>• Approve casing standards and vendors<br>• Monitor compliance with casing requirements |
| Facilities Manager | • Procure and maintain lockable casings<br>• Install permanent casing solutions<br>• Coordinate with security for access controls |
| Asset Managers | • Track casing assignments and locations<br>• Ensure proper casing deployment<br>• Report missing or damaged casings |

## 4. RULES
[RULE-01] All portable devices containing sensitive data MUST be secured in approved lockable casings when unattended in public or semi-public areas.
[VALIDATION] IF device_type = "portable" AND data_classification >= "sensitive" AND location_type IN ["public", "semi-public"] AND supervised = FALSE AND lockable_casing = FALSE THEN violation

[RULE-02] System components in unsecured areas MUST be protected by lockable physical casings that meet organizational security standards.
[VALIDATION] IF component_location = "unsecured_area" AND lockable_casing = FALSE THEN violation

[RULE-03] Lockable casings SHALL be constructed of materials that provide adequate protection against forced entry for a minimum of 15 minutes.
[VALIDATION] IF casing_resistance_time < 15_minutes THEN violation

[RULE-04] Keys or access codes for lockable casings MUST be managed through the organization's key management system and limited to authorized personnel only.
[VALIDATION] IF casing_access_method NOT IN approved_key_management_system THEN violation

[RULE-05] Lockable casings MUST be inspected monthly for physical integrity and proper locking mechanisms.
[VALIDATION] IF last_inspection_date > 30_days_ago THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Casing Assessment Procedure - Identify and classify components requiring lockable casings
- [PROC-02] Casing Procurement Procedure - Standards for selecting and purchasing approved lockable casings
- [PROC-03] Key Management Procedure - Distribution and control of casing access credentials
- [PROC-04] Inspection and Maintenance Procedure - Regular verification of casing integrity and functionality

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving physical theft, changes in facility security posture, introduction of new portable device types

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unattended Laptop in Conference Room]
IF device_type = "laptop"
AND data_classification = "confidential"
AND location = "conference_room"
AND attendees_present = FALSE
AND lockable_casing = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Server in Temporary Location]
IF component_type = "server"
AND location_security_level = "temporary"
AND lockable_casing = TRUE
AND casing_approved = TRUE
THEN compliance = TRUE

[SCENARIO-03: Mobile Device with Expired Casing Inspection]
IF device_type = "mobile"
AND lockable_casing = TRUE
AND last_inspection > 35_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Approved Casing with Proper Key Management]
IF lockable_casing = TRUE
AND casing_meets_standards = TRUE
AND key_management = "centralized"
AND authorized_access_only = TRUE
THEN compliance = TRUE

[SCENARIO-05: Damaged Casing Still in Use]
IF lockable_casing = TRUE
AND casing_integrity = "compromised"
AND replacement_pending = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Lockable physical casings protect system components from unauthorized access | [RULE-01], [RULE-02] |
| Casings provide adequate physical protection | [RULE-03] |
| Access to casings is properly controlled | [RULE-04] |
| Casing effectiveness is regularly verified | [RULE-05] |