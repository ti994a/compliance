# POLICY: CP-8.3: Separation of Primary and Alternate Providers

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CP-8.3 |
| NIST Control | CP-8.3: Separation of Primary and Alternate Providers |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | telecommunications, alternate providers, separation, contingency planning, disaster recovery, service continuity |

## 1. POLICY STATEMENT
The organization MUST obtain alternate telecommunications services from providers that are separated from primary service providers to reduce susceptibility to the same threats. Provider separation MUST minimize shared infrastructure and achieve sufficient geographic separation to ensure service continuity during disruptions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All critical information systems | YES | Systems requiring continuous operations |
| Primary telecommunications services | YES | All production network services |
| Alternate telecommunications services | YES | All backup/failover network services |
| Emergency communications systems | YES | Crisis communication infrastructure |
| Development/test environments | CONDITIONAL | If supporting critical business functions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Infrastructure Manager | • Evaluate and select separated telecommunications providers<br>• Maintain provider separation documentation<br>• Coordinate with vendors on geographic separation requirements |
| Business Continuity Manager | • Assess threat susceptibility across providers<br>• Validate separation effectiveness during testing<br>• Document risk assessments for provider selection |
| Procurement Manager | • Negotiate contracts ensuring provider independence<br>• Verify provider infrastructure separation claims<br>• Maintain vendor relationship documentation |

## 4. RULES
[RULE-01] Primary and alternate telecommunications providers MUST be separate legal entities with independent infrastructure ownership.
[VALIDATION] IF primary_provider = alternate_provider OR shared_infrastructure_percentage > 25% THEN violation

[RULE-02] Geographic separation between primary and alternate provider infrastructure MUST exceed 50 miles for critical services.
[VALIDATION] IF geographic_distance < 50_miles AND service_criticality = "high" THEN violation

[RULE-03] Shared infrastructure dependencies between providers MUST NOT exceed 25% of the total service path.
[VALIDATION] IF shared_infrastructure_percentage > 25% THEN violation

[RULE-04] Provider separation assessment MUST be conducted annually and documented with threat analysis.
[VALIDATION] IF last_assessment_date > 365_days_ago THEN violation

[RULE-05] Alternate provider capabilities MUST support minimum 80% of primary service capacity within 4 hours of activation.
[VALIDATION] IF alternate_capacity < 80% OR activation_time > 4_hours THEN violation

[RULE-06] Provider independence verification MUST include infrastructure ownership, routing paths, and facility locations.
[VALIDATION] IF verification_components < ["ownership", "routing", "facilities"] THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Provider Separation Assessment - Annual evaluation of telecommunications provider independence and threat susceptibility
- [PROC-02] Geographic Separation Verification - Validation of physical separation distances and routing diversity
- [PROC-03] Shared Infrastructure Analysis - Assessment of common dependencies between primary and alternate providers
- [PROC-04] Provider Failover Testing - Quarterly testing of alternate provider activation and capacity verification

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 6 months
- Triggering events: Provider changes, major service outages, infrastructure modifications, risk assessment updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Same Corporate Parent]
IF primary_provider_parent_company = alternate_provider_parent_company
AND corporate_separation_verified = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Insufficient Geographic Separation]
IF service_criticality = "high"
AND geographic_distance < 50_miles
AND risk_assessment_approved_exception = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Excessive Shared Infrastructure]
IF shared_fiber_infrastructure > 25%
AND alternative_routing_available = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Outdated Separation Assessment]
IF last_provider_assessment > 365_days
AND provider_changes_occurred = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Adequate Provider Separation]
IF primary_provider ≠ alternate_provider
AND geographic_distance >= 50_miles
AND shared_infrastructure_percentage <= 25%
AND annual_assessment_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Alternate telecommunications services from separated providers obtained | RULE-01, RULE-02 |
| Reduced susceptibility to same threats achieved | RULE-03, RULE-06 |
| Provider separation adequately documented and assessed | RULE-04 |
| Service continuity capabilities maintained | RULE-05 |