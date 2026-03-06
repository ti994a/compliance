# POLICY: SC-32(1): Separate Physical Domains for Privileged Functions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-32-1 |
| NIST Control | SC-32(1): Separate Physical Domains for Privileged Functions |
| Version | 1.0 |
| Owner | Infrastructure Security Manager |
| Keywords | privileged functions, physical domains, partitioning, separation, single point of failure, denial of service |

## 1. POLICY STATEMENT
Privileged functions SHALL be partitioned into separate physical domains to prevent single points of failure and limit the impact of domain compromise or denial of service. Physical separation MUST be implemented to ensure that compromise of one domain does not directly affect privileged functions operating in other domains.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Privileged system functions | YES | All functions requiring elevated access |
| Administrative systems | YES | Domain controllers, identity management |
| Critical infrastructure | YES | Network management, security tools |
| Standard user workstations | NO | Unless hosting privileged functions |
| Cloud privileged services | YES | Virtual separation with physical isolation |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Infrastructure Security Manager | • Define physical domain separation requirements<br>• Approve domain architecture designs<br>• Monitor compliance with separation standards |
| System Architects | • Design physical domain partitioning<br>• Document domain boundaries and isolation<br>• Ensure no single points of failure |
| Data Center Operations | • Implement physical separation controls<br>• Maintain domain isolation integrity<br>• Report domain boundary violations |

## 4. RULES
[RULE-01] Privileged functions MUST be distributed across a minimum of two separate physical domains with no shared physical infrastructure components.
[VALIDATION] IF privileged_function_count > 0 AND unique_physical_domains < 2 THEN violation

[RULE-02] Each physical domain hosting privileged functions MUST have independent power, network, and environmental systems to prevent cascading failures.
[VALIDATION] IF shared_infrastructure_components > 0 AND domain_type = "privileged" THEN violation

[RULE-03] Physical domain boundaries MUST be documented with clear identification of all privileged functions and their assigned domains.
[VALIDATION] IF privileged_function_domain_mapping = "undefined" OR documentation_current = FALSE THEN violation

[RULE-04] No single physical domain SHALL contain more than 70% of critical privileged functions to ensure operational resilience.
[VALIDATION] IF (privileged_functions_in_domain / total_privileged_functions) > 0.70 THEN violation

[RULE-05] Physical domain separation MUST be maintained during system maintenance, with procedures to prevent temporary consolidation of privileged functions.
[VALIDATION] IF maintenance_mode = TRUE AND privileged_functions_consolidated = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Physical Domain Assessment - Annual review of privileged function distribution
- [PROC-02] Domain Isolation Verification - Quarterly validation of physical separation
- [PROC-03] Privileged Function Mapping - Continuous inventory of functions and domains
- [PROC-04] Domain Failure Response - Incident response for domain compromise or outage

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Infrastructure changes, privileged function additions, domain compromises, significant outages

## 7. SCENARIO PATTERNS
[SCENARIO-01: Single Domain Concentration]
IF privileged_functions_in_single_domain > 70%
AND total_privileged_functions > 5
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Shared Infrastructure Dependencies]
IF physical_domain_count >= 2
AND shared_power_systems = TRUE
AND privileged_functions_present = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Undocumented Domain Mapping]
IF privileged_functions_identified = TRUE
AND domain_assignment_documented = FALSE
AND last_documentation_update > 90_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Maintenance Consolidation]
IF maintenance_window = TRUE
AND privileged_functions_moved_to_single_domain = TRUE
AND temporary_consolidation_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Adequate Distribution]
IF privileged_functions_distributed_across >= 2_domains
AND no_shared_critical_infrastructure = TRUE
AND domain_mapping_current = TRUE
AND max_domain_concentration <= 70%
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Privileged functions are partitioned into separate physical domains | RULE-01, RULE-04 |
| Physical independence prevents single points of failure | RULE-02 |
| Domain separation is documented and maintained | RULE-03 |
| Separation integrity during operations and maintenance | RULE-05 |