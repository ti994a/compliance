# POLICY: MA-5.4: Foreign Nationals

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_MA-5.4 |
| NIST Control | MA-5.4: Foreign Nationals |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | foreign nationals, classified systems, maintenance, security clearances, memoranda of agreements |

## 1. POLICY STATEMENT
Foreign nationals may only conduct maintenance and diagnostic activities on classified systems when systems are jointly owned and operated by the United States and foreign allied governments, or owned and operated solely by foreign allied governments. All approvals, consents, and operational conditions for foreign national maintenance activities MUST be fully documented within Memoranda of Agreements.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Classified Information Systems | YES | All systems processing classified information |
| Foreign National Personnel | YES | Non-U.S. citizens performing maintenance |
| Maintenance Contractors | YES | When employing foreign nationals |
| Unclassified Systems | NO | Policy applies only to classified systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Security Manager | • Verify system ownership requirements<br>• Validate foreign national clearances<br>• Ensure MOA compliance |
| Personnel Security Office | • Conduct additional vetting of foreign nationals<br>• Verify security clearance validity<br>• Monitor clearance status |
| Legal Compliance Team | • Review and approve Memoranda of Agreements<br>• Ensure international agreement compliance<br>• Document operational conditions |

## 4. RULES
[RULE-01] Foreign nationals MUST possess appropriate security clearances before conducting maintenance or diagnostic activities on classified systems.
[VALIDATION] IF personnel_nationality != "US" AND system_classification != "unclassified" AND security_clearance = NULL THEN violation

[RULE-02] Foreign nationals SHALL only perform maintenance on classified systems that are jointly owned and operated by the US and foreign allied governments OR owned and operated solely by foreign allied governments.
[VALIDATION] IF personnel_nationality != "US" AND system_ownership != "joint_allied" AND system_ownership != "foreign_allied_only" THEN critical_violation

[RULE-03] All approvals for foreign national maintenance activities MUST be documented within executed Memoranda of Agreements.
[VALIDATION] IF foreign_national_maintenance = TRUE AND moa_approval_documented = FALSE THEN violation

[RULE-04] All consents for foreign national maintenance activities MUST be documented within executed Memoranda of Agreements.
[VALIDATION] IF foreign_national_maintenance = TRUE AND moa_consent_documented = FALSE THEN violation

[RULE-05] Detailed operational conditions for foreign national maintenance activities MUST be documented within executed Memoranda of Agreements.
[VALIDATION] IF foreign_national_maintenance = TRUE AND moa_operational_conditions_documented = FALSE THEN violation

[RULE-06] Additional vetting MUST be completed for foreign nationals before granting access to classified systems for maintenance purposes.
[VALIDATION] IF personnel_nationality != "US" AND additional_vetting_completed = FALSE AND classified_system_access = TRUE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Foreign National Vetting - Additional security screening beyond standard clearance requirements
- [PROC-02] MOA Documentation Review - Verification of complete approval, consent, and operational condition documentation
- [PROC-03] System Ownership Verification - Validation of joint or foreign allied government ownership status
- [PROC-04] Clearance Validation - Confirmation of appropriate security clearance levels for foreign nationals

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Changes to international agreements, security incidents involving foreign nationals, changes to system ownership

## 7. SCENARIO PATTERNS
[SCENARIO-01: Foreign National on US-Only System]
IF personnel_nationality = "foreign_allied"
AND system_ownership = "us_only"
AND maintenance_request = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Proper Joint System Maintenance]
IF personnel_nationality = "foreign_allied"
AND system_ownership = "joint_allied"
AND security_clearance = "valid"
AND moa_documented = TRUE
THEN compliance = TRUE

[SCENARIO-03: Missing MOA Documentation]
IF personnel_nationality = "foreign_allied"
AND system_ownership = "joint_allied"
AND security_clearance = "valid"
AND moa_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Inadequate Clearance Level]
IF personnel_nationality = "foreign_allied"
AND system_classification = "top_secret"
AND security_clearance = "secret"
AND maintenance_access = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Missing Additional Vetting]
IF personnel_nationality = "foreign_allied"
AND security_clearance = "valid"
AND additional_vetting = "incomplete"
AND classified_system_access = "requested"
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Foreign nationals with appropriate clearances used only on joint/allied systems | [RULE-01], [RULE-02] |
| Approvals documented in MOAs | [RULE-03] |
| Consents documented in MOAs | [RULE-04] |
| Operational conditions documented in MOAs | [RULE-05] |
| Additional vetting requirements | [RULE-06] |