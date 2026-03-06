# POLICY: CM-10: Software Usage Restrictions

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-10 |
| NIST Control | CM-10: Software Usage Restrictions |
| Version | 1.0 |
| Owner | Chief Information Officer |
| Keywords | software licensing, copyright compliance, peer-to-peer, license tracking, contract agreements |

## 1. POLICY STATEMENT
The organization must use all software and documentation in accordance with contract agreements and copyright laws, track quantity-licensed software to prevent unauthorized copying and distribution, and control peer-to-peer file sharing to prevent copyright violations. All software usage must be monitored, documented, and compliant with licensing terms.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Includes full-time, part-time, contractors |
| All computing systems | YES | Corporate, cloud, and hybrid infrastructure |
| All software installations | YES | Commercial, open source, and custom software |
| Mobile devices | YES | Company-owned and BYOD devices |
| Third-party vendors | CONDITIONAL | When accessing company systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Asset Manager | • Maintain software inventory and license database<br>• Track license compliance and usage metrics<br>• Coordinate license renewals and procurement |
| System Administrators | • Implement software installation controls<br>• Monitor for unauthorized software<br>• Report license violations |
| Legal/Compliance Team | • Review software agreements and licensing terms<br>• Provide guidance on copyright compliance<br>• Handle license violation incidents |

## 4. RULES
[RULE-01] All software installations MUST be authorized through the IT asset management system and comply with applicable license agreements and copyright laws.
[VALIDATION] IF software_installed = TRUE AND authorization_documented = FALSE THEN violation

[RULE-02] Organizations MUST maintain an automated software inventory system that tracks all installed software and associated license compliance status.
[VALIDATION] IF software_inventory_automated = FALSE OR inventory_current = FALSE THEN violation

[RULE-03] Quantity-licensed software usage MUST be monitored to ensure installed instances do not exceed licensed quantities, with compliance checks performed monthly.
[VALIDATION] IF installed_instances > licensed_quantity THEN critical_violation

[RULE-04] Peer-to-peer file sharing applications MUST be blocked on corporate networks unless explicitly approved and documented for legitimate business purposes.
[VALIDATION] IF p2p_detected = TRUE AND business_justification_approved = FALSE THEN violation

[RULE-05] Software license violations MUST be remediated within 48 hours of detection for standard violations and within 24 hours for critical over-licensing situations.
[VALIDATION] IF violation_detected = TRUE AND remediation_time > 48_hours THEN escalation_required

[RULE-06] All software procurement MUST include legal review of licensing terms and integration with the software asset management database.
[VALIDATION] IF software_procured = TRUE AND legal_review_completed = FALSE THEN procurement_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Software Installation Authorization - Formal approval process for all software installations
- [PROC-02] License Compliance Monitoring - Monthly automated scanning and compliance reporting
- [PROC-03] P2P Technology Assessment - Quarterly review of peer-to-peer applications and controls
- [PROC-04] Software Audit Response - Process for addressing license compliance findings
- [PROC-05] Vendor License Management - Procedures for managing enterprise software agreements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Software audit findings, new licensing models, regulatory changes, significant infrastructure changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unauthorized Software Installation]
IF software_installed = TRUE
AND approval_documented = FALSE
AND discovery_method = "automated_scan"
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-02: License Over-Usage]
IF software_type = "quantity_licensed"
AND current_installations > licensed_quantity
AND duration > 30_days
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Approved P2P Usage]
IF p2p_application_detected = TRUE
AND business_justification = "approved"
AND monitoring_enabled = TRUE
AND usage_documented = TRUE
THEN compliance = TRUE

[SCENARIO-04: Unlicensed Software Discovery]
IF software_commercial = TRUE
AND license_valid = FALSE
AND installation_date > 90_days_ago
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Mobile Device Software Compliance]
IF device_type = "mobile"
AND corporate_managed = TRUE
AND unauthorized_apps_installed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Software used per contract agreements and copyright laws | [RULE-01], [RULE-06] |
| Quantity license usage tracked and controlled | [RULE-02], [RULE-03] |
| P2P file sharing controlled and documented | [RULE-04] |
| Software license compliance monitoring | [RULE-02], [RULE-05] |
| Documentation of software usage restrictions | [RULE-01], [RULE-04] |