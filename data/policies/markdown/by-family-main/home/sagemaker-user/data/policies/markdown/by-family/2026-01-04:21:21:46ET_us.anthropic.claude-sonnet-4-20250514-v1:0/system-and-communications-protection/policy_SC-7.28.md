# POLICY: SC-7.28: Connections to Public Networks

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SC-7.28 |
| NIST Control | SC-7.28: Connections to Public Networks |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | public networks, direct connection, network isolation, boundary protection, internet access |

## 1. POLICY STATEMENT
Systems designated as prohibited from public network access SHALL NOT have direct physical or virtual connections to public networks including the Internet and organizational extranets with public access. All network connections for designated systems MUST be routed through approved security controls and boundary protection mechanisms.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Classified systems | YES | All systems processing classified information |
| High-impact systems | YES | Systems with FIPS 199 High confidentiality rating |
| Financial systems | YES | SOX-regulated financial reporting systems |
| Development systems | CONDITIONAL | Only if containing production data |
| Test environments | CONDITIONAL | Only if containing sensitive data |
| Public-facing systems | NO | Systems designed for public access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owner | • Identify systems requiring public network isolation<br>• Maintain system classification documentation<br>• Approve network architecture changes |
| Network Administrator | • Implement physical and logical network isolation<br>• Monitor network connections and configurations<br>• Document network topology and connection points |
| Security Engineer | • Design secure network architectures<br>• Validate isolation controls<br>• Perform compliance assessments |

## 4. RULES
[RULE-01] Systems classified as prohibited from public network access MUST NOT have direct physical connections to public networks.
[VALIDATION] IF system_classification = "no_public_access" AND direct_physical_connection = TRUE THEN critical_violation

[RULE-02] Systems classified as prohibited from public network access MUST NOT have direct virtual connections to public networks including VPNs, tunnels, or bridge connections.
[VALIDATION] IF system_classification = "no_public_access" AND direct_virtual_connection = TRUE THEN critical_violation

[RULE-03] Network administrators MUST document and maintain an approved list of systems prohibited from public network connections.
[VALIDATION] IF prohibited_systems_list = NULL OR last_updated > 90_days THEN violation

[RULE-04] All network connections for prohibited systems MUST be routed through approved boundary protection devices with documented security controls.
[VALIDATION] IF system_classification = "no_public_access" AND boundary_protection = FALSE THEN critical_violation

[RULE-05] Network topology diagrams MUST be updated within 30 days of any connection changes to prohibited systems.
[VALIDATION] IF connection_change_date > (topology_update_date + 30_days) THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Classification Procedure - Process for identifying and documenting systems requiring public network isolation
- [PROC-02] Network Architecture Review - Regular assessment of network connections and isolation controls
- [PROC-03] Connection Change Management - Approval process for any network modifications affecting prohibited systems
- [PROC-04] Compliance Monitoring - Continuous monitoring of network connections and boundary controls

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, system reclassification, network architecture changes, regulatory updates

## 7. SCENARIO PATTERNS
[SCENARIO-01: Classified System Internet Connection]
IF system_classification = "classified"
AND internet_connection = "direct"
AND boundary_protection = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Financial System with VPN Access]
IF system_type = "financial_reporting"
AND vpn_connection = TRUE
AND vpn_destination = "public_internet"
AND security_controls_documented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Development System with Production Data]
IF system_environment = "development"
AND contains_production_data = TRUE
AND public_network_access = TRUE
AND data_sensitivity = "high"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Properly Isolated High-Impact System]
IF system_classification = "high_impact"
AND direct_public_connection = FALSE
AND boundary_protection = TRUE
AND isolation_documented = TRUE
THEN compliance = TRUE

[SCENARIO-05: Emergency Internet Access]
IF system_classification = "no_public_access"
AND emergency_connection = TRUE
AND emergency_approval = FALSE
AND connection_duration > 24_hours
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Direct connection prohibition for designated systems | RULE-01, RULE-02 |
| System identification and documentation | RULE-03 |
| Boundary protection implementation | RULE-04 |
| Network topology maintenance | RULE-05 |