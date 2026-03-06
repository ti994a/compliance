# POLICY: IA-3.3: Dynamic Address Allocation

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-3.3 |
| NIST Control | IA-3.3: Dynamic Address Allocation |
| Version | 1.0 |
| Owner | Network Security Manager |
| Keywords | DHCP, dynamic addressing, lease management, network audit, device identification |

## 1. POLICY STATEMENT
All systems using dynamic address allocation must standardize lease information and duration according to organizational requirements and maintain audit logs of all address assignments. This policy ensures consistent network addressing practices and enables security monitoring of device network access.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| DHCP Servers | YES | All organizational DHCP infrastructure |
| Network Devices | YES | Devices receiving dynamic IP addresses |
| Cloud Infrastructure | YES | Auto-scaling and dynamic provisioning systems |
| Guest Networks | YES | Visitor and temporary access networks |
| IoT Devices | YES | Internet of Things devices with dynamic addressing |
| Static IP Systems | NO | Systems with permanently assigned addresses |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Manager | • Define lease information standards<br>• Approve lease duration policies<br>• Review audit compliance |
| Network Administrators | • Configure DHCP servers per standards<br>• Monitor lease assignments<br>• Maintain audit logging |
| Security Operations Center | • Monitor lease assignment anomalies<br>• Investigate unauthorized device connections<br>• Escalate compliance violations |

## 4. RULES
[RULE-01] DHCP servers MUST implement standardized lease information including hostname format, domain suffix, DNS server assignments, and gateway configurations as defined in the Network Configuration Standard.
[VALIDATION] IF dhcp_server_config != standard_lease_template THEN violation

[RULE-02] Dynamic address lease duration MUST NOT exceed 24 hours for guest networks, 7 days for employee devices, and 1 hour for IoT devices.
[VALIDATION] IF network_type = "guest" AND lease_duration > 24_hours THEN violation
[VALIDATION] IF network_type = "employee" AND lease_duration > 7_days THEN violation
[VALIDATION] IF network_type = "iot" AND lease_duration > 1_hour THEN violation

[RULE-03] All DHCP servers MUST log lease assignments including timestamp, MAC address, assigned IP, hostname, and lease duration to centralized SIEM within 5 minutes of assignment.
[VALIDATION] IF dhcp_log_delay > 5_minutes THEN violation

[RULE-04] DHCP lease information MUST include device classification tags based on MAC address OUI and connection patterns for security monitoring purposes.
[VALIDATION] IF lease_assignment = TRUE AND device_classification = NULL THEN violation

[RULE-05] Lease renewal activities MUST be audited with the same detail requirements as initial lease assignments.
[VALIDATION] IF lease_renewal = TRUE AND audit_log_created = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] DHCP Server Configuration - Standardized deployment and configuration of DHCP infrastructure
- [PROC-02] Lease Duration Management - Process for setting appropriate lease times based on device and network type
- [PROC-03] Dynamic Address Audit Review - Monthly review of lease assignment logs and anomaly investigation
- [PROC-04] Incident Response for Unauthorized Devices - Response procedures for unknown devices obtaining network addresses

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Network security incidents, infrastructure changes, regulatory updates, audit findings

## 7. SCENARIO PATTERNS
[SCENARIO-01: Guest Network Lease Violation]
IF network_segment = "guest"
AND dhcp_lease_duration > 24_hours
AND exception_approved = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: Missing Audit Logs]
IF dhcp_lease_assigned = TRUE
AND audit_log_generated = FALSE
AND time_since_assignment > 5_minutes
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Unauthorized Device Connection]
IF mac_address NOT IN approved_device_list
AND device_classification = "unknown"
AND lease_granted = TRUE
AND investigation_initiated = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: IoT Device Lease Duration]
IF device_type = "iot"
AND lease_duration > 1_hour
AND business_justification = FALSE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Compliant Employee Device]
IF network_type = "employee"
AND lease_duration <= 7_days
AND audit_log_complete = TRUE
AND device_classification = "corporate_managed"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Standardized lease information for dynamic addresses | [RULE-01] |
| Standardized lease duration for dynamic addresses | [RULE-02] |
| Audit of lease information when assigned | [RULE-03], [RULE-05] |
| Device identification through lease management | [RULE-04] |