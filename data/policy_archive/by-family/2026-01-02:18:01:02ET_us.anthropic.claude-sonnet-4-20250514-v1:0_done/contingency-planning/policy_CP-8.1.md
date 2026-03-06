# POLICY: CP-8.1: Priority of Service Provisions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CP-8.1 |
| NIST Control | CP-8.1: Priority of Service Provisions |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | telecommunications, priority service, TSP, contingency planning, recovery time objectives, common carrier |

## 1. POLICY STATEMENT
The organization must establish primary and alternate telecommunications service agreements containing priority-of-service provisions aligned with availability requirements and recovery time objectives. For national security emergency preparedness functions using common carrier services, Telecommunications Service Priority (TSP) enrollment is required.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All telecommunications services | YES | Supporting critical business functions |
| National security emergency preparedness systems | YES | TSP enrollment mandatory |
| Non-critical telecommunications | CONDITIONAL | Based on availability requirements |
| Third-party managed services | YES | When using common carriers |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Operations Manager | • Negotiate priority service agreements<br>• Monitor service level compliance<br>• Coordinate TSP enrollment process |
| Business Continuity Manager | • Define availability requirements<br>• Establish recovery time objectives<br>• Validate service priority alignment |
| Procurement Officer | • Execute telecommunications contracts<br>• Ensure priority provisions inclusion<br>• Manage vendor relationships |

## 4. RULES
[RULE-01] Primary telecommunications service agreements MUST contain priority-of-service provisions that align with documented availability requirements and recovery time objectives.
[VALIDATION] IF primary_telecom_agreement EXISTS AND priority_provisions = FALSE THEN violation

[RULE-02] Alternate telecommunications service agreements MUST contain priority-of-service provisions that align with documented availability requirements and recovery time objectives.
[VALIDATION] IF alternate_telecom_agreement EXISTS AND priority_provisions = FALSE THEN violation

[RULE-03] Organizations MUST request Telecommunications Service Priority (TSP) enrollment for all telecommunications services used for national security emergency preparedness when services are provided by common carriers.
[VALIDATION] IF service_type = "national_security_emergency_prep" AND carrier_type = "common_carrier" AND tsp_enrolled = FALSE THEN critical_violation

[RULE-04] Priority-of-service provisions MUST specify response times that meet or exceed established recovery time objectives for each service category.
[VALIDATION] IF priority_response_time > recovery_time_objective THEN violation

[RULE-05] Organizations MUST maintain current documentation of all TSP enrollments and service priority agreements.
[VALIDATION] IF tsp_documentation_age > 365_days OR priority_agreement_documentation = NULL THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Telecommunications Service Priority Enrollment - Process for requesting and maintaining TSP status
- [PROC-02] Priority Service Agreement Review - Annual assessment of service provisions alignment
- [PROC-03] Availability Requirements Documentation - Establishing and updating RTO requirements
- [PROC-04] Service Provider Impact Assessment - Evaluating potential conflicts with other priority customers

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Service provider changes, RTO modifications, new national security designations, service outages exceeding RTO

## 7. SCENARIO PATTERNS
[SCENARIO-01: Missing Primary Service Priority]
IF primary_telecommunications_service EXISTS
AND priority_service_provisions = FALSE
AND availability_requirements = "critical"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: TSP Not Enrolled for NSEP Services]
IF service_function = "national_security_emergency_preparedness"
AND telecommunications_provider = "common_carrier"
AND tsp_enrollment_status = "not_enrolled"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Priority Response Time Exceeds RTO]
IF priority_service_response_time = 8_hours
AND recovery_time_objective = 4_hours
AND service_category = "critical"
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Alternate Service Without Priority]
IF primary_service_priority = TRUE
AND alternate_service_priority = FALSE
AND alternate_service_required = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Outdated TSP Documentation]
IF tsp_enrollment = TRUE
AND last_documentation_update > 365_days
AND service_status = "active"
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Primary telecommunications service agreements contain priority-of-service provisions | [RULE-01] |
| Alternate telecommunications service agreements contain priority-of-service provisions | [RULE-02] |
| TSP requested for national security emergency preparedness services | [RULE-03] |
| Priority provisions align with availability requirements and RTOs | [RULE-04] |
| Current documentation maintained | [RULE-05] |