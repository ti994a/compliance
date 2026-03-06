# POLICY: SR-11.2: Configuration Control for Component Service and Repair

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-11.2 |
| NIST Control | SR-11.2: Configuration Control for Component Service and Repair |
| Version | 1.0 |
| Owner | Supply Chain Risk Manager |
| Keywords | configuration control, component service, repair, maintenance, supply chain, system components |

## 1. POLICY STATEMENT
The organization SHALL maintain strict configuration control over system components during service and repair activities to prevent unauthorized modifications and ensure secure return to service. All components requiring service or repair MUST be tracked and controlled throughout the maintenance lifecycle to preserve system integrity and security posture.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical system components | YES | Hardware, software, firmware components |
| Third-party service providers | YES | External repair and maintenance vendors |
| Internal maintenance teams | YES | IT staff performing component service |
| Development/test components | CONDITIONAL | Only if containing production data |
| End-user devices | CONDITIONAL | Only if accessing critical systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Risk Manager | • Define components requiring configuration control<br>• Oversee service provider agreements<br>• Monitor compliance with control procedures |
| Configuration Manager | • Maintain component inventory and status<br>• Implement configuration control procedures<br>• Validate component integrity before return to service |
| Maintenance Coordinator | • Coordinate service and repair activities<br>• Ensure proper handoff procedures<br>• Document all maintenance actions |

## 4. RULES
[RULE-01] Organizations MUST define and document all system components that require configuration control during service and repair activities.
[VALIDATION] IF component_criticality >= "moderate" AND configuration_control_defined = FALSE THEN violation

[RULE-02] Components awaiting service or repair MUST be placed under configuration control within 4 hours of being designated for maintenance.
[VALIDATION] IF component_status = "awaiting_service" AND config_control_time > 4_hours THEN violation

[RULE-03] All serviced or repaired components MUST remain under configuration control until successfully returned to operational service.
[VALIDATION] IF component_status = "awaiting_return" AND config_control_active = FALSE THEN violation

[RULE-04] Configuration baselines MUST be captured before components are released for service or repair.
[VALIDATION] IF component_released = TRUE AND baseline_captured = FALSE THEN critical_violation

[RULE-05] Components returning from service MUST undergo integrity verification against original configuration baselines before being returned to service.
[VALIDATION] IF component_status = "return_ready" AND integrity_verified = FALSE THEN violation

[RULE-06] Service providers MUST acknowledge configuration control requirements in writing before receiving components.
[VALIDATION] IF provider_acknowledgment = FALSE AND component_transferred = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Configuration Control - Define and implement configuration control processes
- [PROC-02] Service Provider Management - Establish and manage third-party service relationships
- [PROC-03] Baseline Capture and Verification - Document and validate component configurations
- [PROC-04] Chain of Custody - Maintain custody records throughout service lifecycle

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving serviced components, new service providers, major system changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical Server Repair]
IF component_type = "critical_server"
AND service_location = "external"
AND configuration_control_active = TRUE
AND baseline_captured = TRUE
THEN compliance = TRUE

[SCENARIO-02: Uncontrolled Component Service]
IF component_criticality = "high"
AND service_status = "in_progress"
AND configuration_control_active = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Baseline Documentation]
IF component_released_for_service = TRUE
AND baseline_documentation = FALSE
AND component_criticality >= "moderate"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Unauthorized Component Return]
IF component_status = "returned_from_service"
AND integrity_verification = FALSE
AND operational_deployment = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Compliant Third-Party Service]
IF service_provider = "external"
AND provider_acknowledgment = TRUE
AND chain_of_custody_maintained = TRUE
AND configuration_control_active = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Configuration control over components awaiting service is maintained | RULE-02, RULE-04 |
| Configuration control over serviced components awaiting return is maintained | RULE-03, RULE-05 |
| System components requiring configuration control are defined | RULE-01 |
| Service provider configuration control acknowledgment | RULE-06 |