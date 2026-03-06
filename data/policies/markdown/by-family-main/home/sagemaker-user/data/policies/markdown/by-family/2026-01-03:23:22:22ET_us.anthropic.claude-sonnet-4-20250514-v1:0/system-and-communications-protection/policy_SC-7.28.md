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
Systems designated as prohibited from public network access MUST NOT have direct physical or virtual connections to public networks including the Internet and organizational extranets with public access. All network connections for restricted systems MUST be mediated through approved boundary protection mechanisms.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Classified systems | YES | All systems processing classified information |
| High-impact systems | YES | Systems with FIPS 199 high impact rating |
| PCI-DSS cardholder data environment | YES | Systems storing, processing, or transmitting CHD |
| Development/test systems | CONDITIONAL | Only if containing production data |
| Administrative systems | CONDITIONAL | Based on data classification |
| Public-facing web servers | NO | Designed for public access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Maintain inventory of restricted systems<br>• Monitor network connections for compliance<br>• Implement technical controls preventing direct connections |
| System Administrators | • Configure systems per network isolation requirements<br>• Document network architecture and connections<br>• Report any unauthorized connection attempts |
| Security Architecture Team | • Define system classifications requiring isolation<br>• Design approved connection methods<br>• Review and approve network design changes |

## 4. RULES
[RULE-01] Systems classified as restricted from public network access MUST NOT have direct physical connections to public networks.
[VALIDATION] IF system_classification = "restricted" AND direct_physical_connection = TRUE THEN critical_violation

[RULE-02] Systems classified as restricted from public network access MUST NOT have direct virtual connections to public networks.
[VALIDATION] IF system_classification = "restricted" AND direct_virtual_connection = TRUE THEN critical_violation

[RULE-03] All network connections for restricted systems MUST be mediated through approved boundary protection devices.
[VALIDATION] IF system_classification = "restricted" AND connection_mediated = FALSE THEN violation

[RULE-04] Network architecture documentation MUST accurately reflect all connections for restricted systems.
[VALIDATION] IF system_classification = "restricted" AND documentation_current = FALSE THEN moderate_violation

[RULE-05] Restricted systems MUST be clearly identified and maintained in an authoritative inventory.
[VALIDATION] IF system_classification = "restricted" AND inventory_documented = FALSE THEN moderate_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] System Classification Process - Procedure for identifying and classifying systems requiring public network isolation
- [PROC-02] Network Connection Review - Quarterly review of network connections for restricted systems
- [PROC-03] Boundary Device Management - Configuration and maintenance of approved boundary protection mechanisms
- [PROC-04] Incident Response - Process for responding to unauthorized connection attempts

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents involving restricted systems, network architecture changes, new system deployments

## 7. SCENARIO PATTERNS
[SCENARIO-01: Direct Internet Connection]
IF system_classification = "restricted"
AND internet_connection = "direct"
AND boundary_device = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: VPN Connection to Public Network]
IF system_classification = "restricted"
AND connection_type = "VPN"
AND destination = "public_network"
AND approved_boundary_protection = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Approved Gateway Connection]
IF system_classification = "restricted"
AND connection_mediated = TRUE
AND boundary_device = "approved"
AND security_controls_active = TRUE
THEN compliance = TRUE

[SCENARIO-04: Undocumented System Connection]
IF system_classification = "restricted"
AND network_connection = TRUE
AND documentation_current = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Test System with Production Data]
IF system_type = "development"
AND production_data_present = TRUE
AND public_network_access = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Direct connection prohibition | RULE-01, RULE-02 |
| Mediated connection requirement | RULE-03 |
| System identification and inventory | RULE-05 |
| Documentation accuracy | RULE-04 |