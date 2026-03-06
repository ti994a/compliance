# POLICY: SC-7.28: Connections to Public Networks

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.28 |
| NIST Control | SC-7.28: Connections to Public Networks |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | public network, direct connection, network isolation, boundary protection, internet access |

## 1. POLICY STATEMENT
Systems designated as prohibited from public network access SHALL NOT have direct physical or virtual connections to public networks including the Internet and organizational extranets with public access. All network connections for restricted systems MUST be routed through approved security boundary controls.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Classified Systems | YES | All systems processing classified data |
| High-Value Assets | YES | Systems identified as critical infrastructure |
| Development Systems | CONDITIONAL | Only if containing production data |
| Test/Sandbox Systems | CONDITIONAL | Only if processing sensitive data |
| Employee Workstations | NO | Standard business workstations excluded |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Maintain inventory of restricted systems<br>• Monitor network connections<br>• Implement technical controls |
| System Owners | • Request system classification<br>• Document business justification<br>• Ensure compliance implementation |
| Security Architecture Team | • Design compliant network topologies<br>• Review connection requests<br>• Define approved connection methods |

## 4. RULES
[RULE-01] Systems classified as public-network-prohibited MUST NOT have direct physical network connections to public networks.
[VALIDATION] IF system_classification = "public_network_prohibited" AND direct_physical_connection = TRUE AND destination_network = "public" THEN critical_violation

[RULE-02] Systems classified as public-network-prohibited MUST NOT have direct virtual network connections to public networks.
[VALIDATION] IF system_classification = "public_network_prohibited" AND direct_virtual_connection = TRUE AND destination_network = "public" THEN critical_violation

[RULE-03] All restricted systems requiring external connectivity MUST route traffic through approved security boundary controls.
[VALIDATION] IF system_classification = "public_network_prohibited" AND external_connectivity_required = TRUE AND approved_boundary_control = FALSE THEN violation

[RULE-04] System classification determinations MUST be documented and approved by the Security Architecture Team within 30 days of system deployment.
[VALIDATION] IF system_deployed = TRUE AND classification_documented = FALSE AND days_since_deployment > 30 THEN violation

[RULE-05] Network connection changes for restricted systems MUST be pre-approved through the change management process.
[VALIDATION] IF system_classification = "public_network_prohibited" AND network_change = TRUE AND change_approved = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Classification Procedure - Process for determining and documenting system public network restrictions
- [PROC-02] Network Connection Review Procedure - Regular assessment of system network connections
- [PROC-03] Boundary Control Implementation Procedure - Configuration and maintenance of approved security controls
- [PROC-04] Exception Management Procedure - Process for handling temporary or emergency connection needs

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving restricted systems, major network architecture changes, new system classifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Classified System Internet Connection]
IF system_classification = "public_network_prohibited"
AND internet_connection = "direct"
AND connection_type = "physical"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: High-Value Asset with Approved Gateway]
IF system_classification = "public_network_prohibited"
AND external_connectivity = TRUE
AND connection_method = "approved_security_gateway"
AND gateway_approved = TRUE
THEN compliance = TRUE

[SCENARIO-03: Development System with Production Data]
IF system_type = "development"
AND contains_production_data = TRUE
AND public_network_connection = TRUE
AND classification_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Emergency Connection Without Approval]
IF system_classification = "public_network_prohibited"
AND emergency_connection = TRUE
AND connection_duration > 24_hours
AND emergency_approval_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Virtual Network Segmentation]
IF system_classification = "public_network_prohibited"
AND connection_type = "virtual"
AND network_segmentation = "logical_only"
AND physical_separation = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Direct connection prohibition for restricted systems | [RULE-01], [RULE-02] |
| Approved boundary control implementation | [RULE-03] |
| System classification documentation | [RULE-04] |
| Change management for network connections | [RULE-05] |