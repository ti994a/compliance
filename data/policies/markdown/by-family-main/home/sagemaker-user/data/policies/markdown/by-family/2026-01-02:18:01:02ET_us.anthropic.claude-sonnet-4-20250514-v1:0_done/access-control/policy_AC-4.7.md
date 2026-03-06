# POLICY: AC-4.7: One-way Flow Mechanisms

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-4.7 |
| NIST Control | AC-4.7: One-way Flow Mechanisms |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | one-way flow, data diode, unidirectional gateway, hardware flow control, information flow enforcement |

## 1. POLICY STATEMENT
The organization SHALL enforce one-way information flows through hardware-based flow control mechanisms to prevent unauthorized data export from higher impact domains while permitting controlled data import from lower impact domains. All unidirectional flow mechanisms MUST be implemented using dedicated hardware solutions that physically prevent reverse data flow.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Network segments with different impact levels | YES | Mandatory for HIGH-MODERATE and MODERATE-LOW boundaries |
| Classified/unclassified domain boundaries | YES | Required for all classification level transitions |
| Cloud-to-on-premises data flows | CONDITIONAL | When crossing impact level boundaries |
| Internal network segments (same impact) | NO | Standard network controls apply |
| Development/production environments | YES | When production is higher impact level |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Network Security Team | • Deploy and configure hardware flow control mechanisms<br>• Monitor unidirectional gateway operations<br>• Validate hardware-based enforcement |
| System Administrators | • Implement data flow routing through approved mechanisms<br>• Maintain configuration documentation<br>• Report flow mechanism anomalies |
| Security Architecture Team | • Design network segmentation requiring one-way flows<br>• Approve hardware flow control solutions<br>• Define impact level boundary requirements |

## 4. RULES
[RULE-01] One-way information flows between different impact level domains MUST be enforced through dedicated hardware-based flow control mechanisms (data diodes or unidirectional security gateways).
[VALIDATION] IF source_impact_level > destination_impact_level AND flow_mechanism_type != "hardware_based" THEN critical_violation

[RULE-02] Hardware flow control mechanisms MUST physically prevent reverse data flow and SHALL NOT rely solely on software-based controls.
[VALIDATION] IF flow_control_type = "software_only" OR bidirectional_capability = TRUE THEN violation

[RULE-03] All data transfers through one-way flow mechanisms MUST be logged with source domain, destination domain, data classification, and transfer timestamp.
[VALIDATION] IF one_way_transfer = TRUE AND (source_logged = FALSE OR destination_logged = FALSE OR timestamp_logged = FALSE) THEN violation

[RULE-04] Hardware flow control mechanisms MUST undergo security validation testing every 12 months to verify unidirectional enforcement.
[VALIDATION] IF last_validation_test > 365_days THEN violation

[RULE-05] Data flowing from lower impact to higher impact domains through one-way mechanisms MUST undergo automated security scanning before acceptance.
[VALIDATION] IF flow_direction = "low_to_high" AND security_scan_completed = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Hardware Flow Control Deployment - Standard process for installing and configuring unidirectional gateways
- [PROC-02] One-way Flow Validation Testing - Annual verification of hardware-based flow enforcement
- [PROC-03] Cross-Domain Data Transfer - Approved methods for transferring data through one-way mechanisms
- [PROC-04] Flow Mechanism Monitoring - Continuous monitoring of unidirectional gateway operations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New cross-domain requirements, hardware mechanism failures, security incidents involving unauthorized data export

## 7. SCENARIO PATTERNS
[SCENARIO-01: Classified to Unclassified Data Export]
IF source_classification = "classified"
AND destination_classification = "unclassified"
AND flow_mechanism = "software_firewall"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Production to Development Data Flow]
IF source_environment = "production"
AND destination_environment = "development"
AND production_impact_level > development_impact_level
AND hardware_flow_control = TRUE
AND reverse_flow_blocked = TRUE
THEN compliance = TRUE

[SCENARIO-03: Unvalidated Hardware Flow Control]
IF one_way_mechanism_deployed = TRUE
AND last_validation_date > 365_days
AND current_date > validation_due_date
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Bidirectional Gateway Misconfiguration]
IF gateway_type = "unidirectional"
AND reverse_flow_capability = "enabled"
AND cross_domain_boundary = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Unmonitored Cross-Domain Transfer]
IF data_transfer_occurred = TRUE
AND flow_mechanism = "hardware_data_diode"
AND transfer_logged = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| One-way information flows are enforced through hardware-based flow control mechanisms | [RULE-01], [RULE-02] |
| Hardware mechanisms prevent reverse data flow | [RULE-02] |
| Flow control mechanisms are properly validated | [RULE-04] |
| Cross-domain transfers are monitored and logged | [RULE-03] |
| Data security is maintained during one-way transfers | [RULE-05] |