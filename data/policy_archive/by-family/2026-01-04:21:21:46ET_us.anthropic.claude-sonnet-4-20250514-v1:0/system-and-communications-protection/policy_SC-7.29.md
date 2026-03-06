# POLICY: SC-7.29: Separate Subnets to Isolate Functions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.29 |
| NIST Control | SC-7.29: Separate Subnets to Isolate Functions |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | network segmentation, physical separation, critical systems, subnetworks, isolation |

## 1. POLICY STATEMENT
The organization SHALL implement physically separate subnetworks to isolate critical system components and functions from non-critical systems. This physical separation reduces the risk of catastrophic system failure due to security breaches or compromises affecting non-critical functions.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical system components | YES | As defined in criticality analysis |
| Production networks | YES | Hosting critical business functions |
| Development/test networks | CONDITIONAL | If processing critical data |
| Administrative networks | YES | Management of critical systems |
| Guest/public networks | NO | Not handling critical functions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Define critical system components requiring isolation<br>• Design physically separate subnet architecture<br>• Monitor compliance with separation requirements |
| System Administrators | • Implement physical network separation<br>• Maintain subnet isolation controls<br>• Document network segmentation configurations |
| Security Architecture Team | • Conduct criticality analysis of system components<br>• Review and approve isolation designs<br>• Validate physical separation effectiveness |

## 4. RULES
[RULE-01] Critical system components and functions MUST be isolated using physically separate subnetworks with no shared physical infrastructure.
[VALIDATION] IF critical_component = TRUE AND physical_separation = FALSE THEN violation

[RULE-02] Organizations MUST maintain a documented criticality analysis identifying all system components requiring physical isolation.
[VALIDATION] IF criticality_analysis_exists = FALSE OR last_review > 12_months THEN violation

[RULE-03] Physical subnet separation MUST include separate network hardware, cabling, and switching infrastructure for critical and non-critical functions.
[VALIDATION] IF shared_physical_infrastructure = TRUE AND component_criticality = "critical" THEN violation

[RULE-04] Cross-subnet communication between critical and non-critical networks MUST be explicitly authorized and documented with security controls.
[VALIDATION] IF cross_subnet_connection = TRUE AND authorization_documented = FALSE THEN violation

[RULE-05] Network configurations implementing physical separation MUST be reviewed and validated annually.
[VALIDATION] IF last_validation > 365_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Criticality Analysis - Annual assessment of system components requiring isolation
- [PROC-02] Physical Network Design - Architecture documentation for separated subnets
- [PROC-03] Separation Validation - Testing and verification of physical isolation controls
- [PROC-04] Exception Management - Process for approved cross-subnet connections

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Major system changes, security incidents affecting critical systems, infrastructure upgrades

## 7. SCENARIO PATTERNS
[SCENARIO-01: Critical System on Shared Infrastructure]
IF system_criticality = "critical"
AND physical_infrastructure = "shared"
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Undocumented Cross-Subnet Connection]
IF connection_type = "cross_subnet"
AND source_criticality = "critical"
AND destination_criticality = "non_critical"
AND authorization_documented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Outdated Criticality Analysis]
IF criticality_analysis_age > 12_months
AND critical_systems_exist = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Proper Physical Separation]
IF system_criticality = "critical"
AND physical_separation = TRUE
AND hardware_dedicated = TRUE
AND validation_current = TRUE
THEN compliance = TRUE

[SCENARIO-05: Emergency Cross-Connection]
IF connection_type = "cross_subnet"
AND emergency_authorization = TRUE
AND temporary_approval_documented = TRUE
AND removal_date_specified = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Physical separation of critical components | RULE-01, RULE-03 |
| Documented criticality analysis | RULE-02 |
| Authorized cross-subnet communications | RULE-04 |
| Regular validation of separation controls | RULE-05 |