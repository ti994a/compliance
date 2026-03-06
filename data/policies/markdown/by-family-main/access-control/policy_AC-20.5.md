# POLICY: AC-20.5: Portable Storage Devices — Prohibited Use

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-20.5 |
| NIST Control | AC-20.5: Portable Storage Devices — Prohibited Use |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | portable storage, external systems, USB devices, removable media, access control |

## 1. POLICY STATEMENT
Organization-controlled portable storage devices SHALL NOT be used by authorized personnel on external systems outside the organization's control. This prohibition applies to all removable media including USB drives, external hard drives, SD cards, and similar devices owned or managed by the organization.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Includes full-time, part-time, temporary |
| Contractors | YES | When using organization-controlled devices |
| Third-party vendors | YES | When accessing organization systems |
| Organization-owned portable storage | YES | All removable media devices |
| Personal portable storage | NO | Covered under separate policies |
| Cloud storage services | NO | Covered under AC-20 base control |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Team | • Implement technical controls to prevent unauthorized use<br>• Monitor compliance through audit logs<br>• Investigate policy violations |
| System Administrators | • Configure endpoint protection to block external use<br>• Maintain device inventory and tracking<br>• Report policy violations |
| Employees/Users | • Comply with portable storage restrictions<br>• Report lost or stolen organization devices<br>• Request exceptions through proper channels |

## 4. RULES
[RULE-01] Organization-controlled portable storage devices MUST NOT be connected to or used with external systems not owned or controlled by the organization.
[VALIDATION] IF device_owner = "organization" AND connected_system = "external" THEN violation

[RULE-02] Technical controls MUST be implemented to prevent organization-controlled portable storage devices from functioning on external systems.
[VALIDATION] IF technical_controls_implemented = FALSE THEN violation

[RULE-03] Users MUST immediately report any loss, theft, or unauthorized use of organization-controlled portable storage devices.
[VALIDATION] IF incident_occurred = TRUE AND report_time > 24_hours THEN violation

[RULE-04] Exceptions to this policy MUST be documented, approved by CISO, and include compensating controls.
[VALIDATION] IF exception_granted = TRUE AND (documentation = FALSE OR ciso_approval = FALSE) THEN violation

[RULE-05] All organization-controlled portable storage devices MUST be inventoried and tracked throughout their lifecycle.
[VALIDATION] IF device_in_inventory = FALSE AND device_age > 30_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Portable Storage Device Inventory Management - Maintain comprehensive tracking of all organization-controlled removable media
- [PROC-02] Technical Control Implementation - Deploy endpoint protection to prevent external system usage
- [PROC-03] Incident Response for Lost/Stolen Devices - Process for reporting and responding to device security incidents
- [PROC-04] Exception Request and Approval - Formal process for requesting policy exceptions with risk assessment

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving portable storage, changes to external system access requirements, new device technologies

## 7. SCENARIO PATTERNS
[SCENARIO-01: Employee Uses Company USB on Home Computer]
IF device_owner = "organization"
AND connected_system = "personal_home_computer"
AND technical_controls_bypassed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Contractor Connects Company Drive to Client System]
IF user_type = "contractor"
AND device_owner = "organization" 
AND connected_system = "client_external_system"
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Approved Exception with Compensating Controls]
IF device_owner = "organization"
AND connected_system = "external"
AND exception_approved = TRUE
AND compensating_controls_active = TRUE
AND ciso_approval = TRUE
THEN compliance = TRUE

[SCENARIO-04: Lost Organization USB Device]
IF device_owner = "organization"
AND device_status = "lost"
AND incident_reported = TRUE
AND report_time <= 24_hours
THEN compliance = TRUE

[SCENARIO-05: Technical Control Failure]
IF technical_controls_implemented = TRUE
AND control_bypass_possible = TRUE
AND monitoring_alerts_configured = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Prohibit use of organization-controlled portable storage devices on external systems | [RULE-01] |
| Implement technical enforcement methods | [RULE-02] |
| Maintain device accountability | [RULE-05] |
| Document and approve exceptions | [RULE-04] |
| Incident reporting for device compromise | [RULE-03] |