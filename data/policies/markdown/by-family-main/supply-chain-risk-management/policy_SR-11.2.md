# POLICY: SR-11.2: Configuration Control for Component Service and Repair

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-11.2 |
| NIST Control | SR-11.2: Configuration Control for Component Service and Repair |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | configuration control, component service, repair, supply chain, maintenance |

## 1. POLICY STATEMENT
The organization must maintain strict configuration control over system components during service and repair activities to prevent unauthorized modifications and ensure integrity upon return to service. All components requiring service or repair must follow documented configuration management procedures throughout the entire maintenance lifecycle.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical system components | YES | All components supporting critical business functions |
| Security-relevant components | YES | Components with security functions or containing sensitive data |
| Network infrastructure | YES | Routers, switches, firewalls, and security appliances |
| End-user devices | CONDITIONAL | Only devices processing regulated data |
| Third-party components | YES | Components serviced by external vendors |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Configuration Manager | • Maintain component inventory and configuration baselines<br>• Approve service/repair activities<br>• Verify configuration integrity upon return |
| IT Operations Manager | • Coordinate component service scheduling<br>• Implement secure handling procedures<br>• Document component chain of custody |
| Security Officer | • Define security requirements for service activities<br>• Monitor compliance with configuration controls<br>• Assess risks of component modifications |

## 4. RULES
[RULE-01] Organizations MUST maintain a documented inventory of all system components requiring configuration control during service and repair activities.
[VALIDATION] IF component_requires_service = TRUE AND inventory_documented = FALSE THEN violation

[RULE-02] Configuration baselines MUST be captured and stored securely before any component is sent for service or repair.
[VALIDATION] IF component_status = "awaiting_service" AND baseline_captured = FALSE THEN violation

[RULE-03] Components awaiting service or repair MUST be stored in a secure, controlled environment with documented chain of custody.
[VALIDATION] IF component_status = "awaiting_service" AND secure_storage = FALSE THEN violation

[RULE-04] All service and repair activities MUST be performed by authorized personnel or vendors with appropriate security clearances and agreements.
[VALIDATION] IF service_provider_authorized = FALSE OR security_agreement_signed = FALSE THEN critical_violation

[RULE-05] Serviced or repaired components MUST undergo configuration verification against approved baselines before return to service.
[VALIDATION] IF component_status = "awaiting_return" AND configuration_verified = FALSE THEN violation

[RULE-06] Any unauthorized configuration changes discovered during verification MUST be documented and remediated before component deployment.
[VALIDATION] IF unauthorized_changes_detected = TRUE AND remediation_completed = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Service Authorization - Process for approving and documenting service requests
- [PROC-02] Configuration Baseline Management - Procedures for capturing and storing component configurations
- [PROC-03] Secure Component Handling - Chain of custody and storage requirements
- [PROC-04] Post-Service Verification - Configuration validation and integrity checking procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving serviced components, vendor changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Network Device Repair]
IF component_type = "network_device"
AND service_location = "external_vendor"
AND baseline_captured = TRUE
AND vendor_authorized = TRUE
THEN compliance = TRUE

[SCENARIO-02: Unauthorized Configuration Change]
IF component_status = "returned_from_service"
AND configuration_verified = TRUE
AND unauthorized_changes_detected = TRUE
AND remediation_completed = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Missing Chain of Custody]
IF component_status = "awaiting_service"
AND custody_documentation = FALSE
AND secure_storage = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Unverified Component Return]
IF component_status = "awaiting_return"
AND service_completed = TRUE
AND configuration_verified = FALSE
AND deployment_attempted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Emergency Repair Bypass]
IF service_urgency = "emergency"
AND baseline_captured = FALSE
AND business_justification_documented = TRUE
AND compensating_controls_implemented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Configuration control over components awaiting service maintained | [RULE-02], [RULE-03] |
| Configuration control over serviced components awaiting return maintained | [RULE-05], [RULE-06] |
| System components requiring configuration control defined | [RULE-01] |
| Service and repair authorization controls | [RULE-04] |