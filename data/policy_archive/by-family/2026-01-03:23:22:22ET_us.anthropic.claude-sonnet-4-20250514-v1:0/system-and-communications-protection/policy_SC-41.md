# POLICY: SC-41: Port and I/O Device Access

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-41 |
| NIST Control | SC-41: Port and I/O Device Access |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | ports, USB, I/O devices, physical security, data exfiltration, malicious code |

## 1. POLICY STATEMENT
The organization SHALL physically disable or remove specified connection ports and input/output devices on designated systems to prevent unauthorized data exfiltration and malicious code introduction. Physical disabling or removal is required over software-based controls for enhanced security assurance.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production systems | YES | All systems processing sensitive data |
| Development systems | CONDITIONAL | Only those with access to production data |
| Test/staging systems | CONDITIONAL | Based on data classification |
| Employee workstations | CONDITIONAL | Role-based requirements apply |
| Contractor devices | YES | All contractor-managed devices |
| Kiosks/public terminals | YES | All public-facing systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve port/device restriction policies<br>• Define system categorization for restrictions<br>• Oversee compliance monitoring |
| IT Security Team | • Maintain inventory of restricted ports/devices<br>• Perform physical modifications<br>• Conduct compliance assessments |
| System Administrators | • Implement port/device restrictions<br>• Document system configurations<br>• Report compliance status |

## 4. RULES
[RULE-01] High-impact systems MUST have all USB ports, optical drives, and external storage connection ports physically disabled or removed.
[VALIDATION] IF system_impact_level = "high" AND (usb_ports_active = TRUE OR optical_drives_active = TRUE OR external_storage_ports_active = TRUE) THEN violation

[RULE-02] Moderate-impact systems MUST have USB ports physically disabled unless a documented business exception exists and compensating controls are implemented.
[VALIDATION] IF system_impact_level = "moderate" AND usb_ports_active = TRUE AND (business_exception = FALSE OR compensating_controls = FALSE) THEN violation

[RULE-03] Systems processing PCI-DSS data MUST have all removable media ports and wireless communication ports physically disabled.
[VALIDATION] IF pci_data_processing = TRUE AND (removable_media_ports_active = TRUE OR wireless_ports_active = TRUE) THEN violation

[RULE-04] Physical modifications to disable ports MUST be documented in the system security plan within 5 business days of implementation.
[VALIDATION] IF port_modification_date IS NOT NULL AND documentation_date > (port_modification_date + 5_business_days) THEN violation

[RULE-05] Quarterly assessments MUST verify the continued physical disabling of required ports and devices.
[VALIDATION] IF last_assessment_date < (current_date - 90_days) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Port and Device Assessment - Quarterly verification of physical restrictions
- [PROC-02] Physical Modification Process - Standardized method for disabling/removing ports
- [PROC-03] Exception Management - Process for documenting and approving business exceptions
- [PROC-04] Compensating Controls - Implementation when physical restriction not feasible

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents involving removable media, changes to data classification, new system deployments

## 7. SCENARIO PATTERNS
[SCENARIO-01: High-Impact System USB Access]
IF system_impact_level = "high"
AND usb_ports_physically_present = TRUE
AND usb_ports_functional = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: PCI System with CD Drive]
IF pci_data_processing = TRUE
AND optical_drive_present = TRUE
AND optical_drive_functional = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Moderate System with Exception]
IF system_impact_level = "moderate"
AND usb_ports_active = TRUE
AND business_exception_approved = TRUE
AND compensating_controls_implemented = TRUE
THEN compliance = TRUE

[SCENARIO-04: Undocumented Port Modification]
IF port_modification_completed = TRUE
AND system_security_plan_updated = FALSE
AND days_since_modification > 5
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Overdue Assessment]
IF last_port_assessment_date < (current_date - 90_days)
AND system_in_scope = TRUE
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Connection ports or I/O devices are defined for restriction | [RULE-01], [RULE-02], [RULE-03] |
| Ports/devices are physically disabled or removed on designated systems | [RULE-01], [RULE-02], [RULE-03] |
| Modifications are properly documented | [RULE-04] |
| Ongoing verification of restrictions | [RULE-05] |