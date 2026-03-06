# POLICY: CM-8.4: Accountability Information

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-8.4 |
| NIST Control | CM-8.4: Accountability Information |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | component inventory, accountability, administrator identification, system components, configuration management |

## 1. POLICY STATEMENT
All system components in the organization's inventory MUST include identification by name of individuals responsible and accountable for administering those components. This accountability information enables rapid response to security incidents and ensures proper component administration.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Information Systems | YES | All production, development, and test systems |
| Network Components | YES | Routers, switches, firewalls, load balancers |
| Cloud Resources | YES | IaaS, PaaS, and SaaS components |
| Physical Hardware | YES | Servers, workstations, mobile devices |
| Software Components | YES | Applications, operating systems, middleware |
| Third-party Components | YES | Vendor-managed components with identified liaison |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Maintain accurate component inventory records<br>• Update administrator assignments within 24 hours of changes<br>• Ensure contact information remains current |
| Component Owners | • Accept formal accountability for assigned components<br>• Respond to security incidents involving their components<br>• Coordinate maintenance and updates |
| Configuration Management Team | • Validate inventory completeness and accuracy<br>• Audit administrator assignments quarterly<br>• Maintain centralized inventory database |

## 4. RULES

[RULE-01] Every system component in the inventory MUST have at least one named individual identified as responsible and accountable for its administration.
[VALIDATION] IF component_exists = TRUE AND administrator_name = NULL THEN violation

[RULE-02] Administrator identification MUST include full name, employee ID, contact information, and role/title.
[VALIDATION] IF administrator_record_complete = FALSE THEN violation

[RULE-03] Component inventory records MUST be updated within 24 hours when administrator assignments change.
[VALIDATION] IF administrator_change_date > 0 AND inventory_update_time > 24_hours THEN violation

[RULE-04] Each component MUST have a primary administrator and MAY have secondary administrators for redundancy.
[VALIDATION] IF primary_administrator = NULL THEN violation

[RULE-05] Administrator contact information MUST be validated and updated at least quarterly.
[VALIDATION] IF last_contact_validation > 90_days THEN violation

[RULE-06] Shared service components MUST identify a single accountable administrator even when multiple individuals have administrative access.
[VALIDATION] IF component_type = "shared" AND accountable_administrator_count != 1 THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Registration - Process for adding new components with administrator assignment
- [PROC-02] Administrator Assignment - Formal process for assigning and documenting component responsibility
- [PROC-03] Contact Validation - Quarterly verification of administrator contact information
- [PROC-04] Inventory Audit - Monthly review of component-administrator mappings for completeness

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving unidentified components, organizational restructuring, major system deployments

## 7. SCENARIO PATTERNS

[SCENARIO-01: New Component Without Administrator]
IF component_added = TRUE
AND deployment_date <= current_date
AND administrator_assigned = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Outdated Contact Information]
IF administrator_contact_last_verified > 90_days
AND component_status = "active"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Administrator Transfer Without Update]
IF administrator_employment_status = "terminated"
AND component_assignment_active = TRUE
AND replacement_assigned = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Shared Component with Multiple Accountable Parties]
IF component_type = "shared_service"
AND accountable_administrator_count > 1
AND primary_designee = NULL
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Emergency Component Deployment]
IF component_deployment_type = "emergency"
AND deployment_time < 4_hours
AND temporary_administrator_assigned = TRUE
THEN compliance = TRUE
note = "Permanent assignment required within 72 hours"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Individuals responsible for administering system components are identified by name | RULE-01, RULE-02 |
| Component inventory includes accountability information | RULE-01, RULE-04 |
| Administrator identification enables contact for required actions | RULE-02, RULE-05 |
| Accountability assignments are current and accurate | RULE-03, RULE-05 |