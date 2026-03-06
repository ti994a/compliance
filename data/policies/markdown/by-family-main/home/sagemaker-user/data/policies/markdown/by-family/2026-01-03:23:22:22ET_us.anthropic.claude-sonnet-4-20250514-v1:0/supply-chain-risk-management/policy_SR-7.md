# POLICY: SR-7: Supply Chain Operations Security

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-7 |
| NIST Control | SR-7: Supply Chain Operations Security |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | supply chain, OPSEC, operations security, supplier information, critical information, safeguards |

## 1. POLICY STATEMENT
The organization SHALL employ Operations Security (OPSEC) controls to protect supply chain-related information for systems, system components, and system services. OPSEC controls MUST include identification of critical information, analysis of observable actions, implementation of safeguards, and consideration of information aggregation risks.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud and hybrid systems |
| System components | YES | Hardware, software, firmware |
| System services | YES | Including third-party services |
| Suppliers and vendors | YES | All tiers of supply chain |
| Acquisition personnel | YES | Staff involved in procurement |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define OPSEC control requirements<br>• Approve supply chain OPSEC procedures<br>• Oversee implementation of safeguards |
| Supply Chain Risk Manager | • Implement OPSEC controls in supplier relationships<br>• Monitor supplier compliance with OPSEC requirements<br>• Coordinate with OPSEC personnel |
| Acquisition Manager | • Apply OPSEC controls in procurement processes<br>• Protect sensitive information during acquisitions<br>• Implement information withholding procedures |
| OPSEC Officer | • Conduct critical information analysis<br>• Develop and maintain OPSEC safeguards<br>• Train personnel on OPSEC requirements |

## 4. RULES
[RULE-01] Organizations MUST define specific OPSEC controls to protect supply chain-related information for each system, system component, and system service.
[VALIDATION] IF system_documented = TRUE AND opsec_controls_defined = FALSE THEN violation

[RULE-02] Critical supply chain information MUST be identified and classified including user identities, supplier identities, security requirements, configurations, processes, and design specifications.
[VALIDATION] IF critical_info_inventory = FALSE OR classification_applied = FALSE THEN violation

[RULE-03] Organizations MUST analyze friendly actions and activities to identify observable indicators that could be exploited by adversaries within the supply chain context.
[VALIDATION] IF threat_analysis_completed = FALSE OR analysis_age > 12_months THEN violation

[RULE-04] Safeguards and countermeasures MUST be implemented to eliminate or reduce supply chain OPSEC vulnerabilities to acceptable risk levels.
[VALIDATION] IF identified_vulnerabilities > 0 AND safeguards_implemented = FALSE THEN violation

[RULE-05] Organizations MUST consider information aggregation risks when sharing information across the supply chain and implement controls to prevent harmful data correlation.
[VALIDATION] IF aggregation_risk_assessment = FALSE OR controls_for_aggregation = FALSE THEN violation

[RULE-06] Mission or business information MAY be withheld from suppliers when necessary to maintain operational security, with documented justification.
[VALIDATION] IF information_withheld = TRUE AND justification_documented = FALSE THEN violation

[RULE-07] Organizations MAY use intermediaries to obscure end users or specific uses of systems, components, or services when operationally required.
[VALIDATION] IF intermediary_used = TRUE AND security_controls_applied = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Critical Information Identification - Systematic process to identify and classify supply chain sensitive information
- [PROC-02] Supplier OPSEC Assessment - Evaluation of supplier OPSEC capabilities and requirements
- [PROC-03] Information Sharing Controls - Procedures for controlling information disclosure to suppliers
- [PROC-04] Aggregation Risk Analysis - Process to assess risks from information correlation across suppliers
- [PROC-05] OPSEC Safeguard Implementation - Deployment and maintenance of OPSEC countermeasures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or upon significant supply chain changes
- Triggering events: New supplier onboarding, security incidents, regulatory changes, major system acquisitions

## 7. SCENARIO PATTERNS
[SCENARIO-01: Unprotected Critical Information Sharing]
IF critical_supply_chain_info_shared = TRUE
AND opsec_controls_applied = FALSE
AND supplier_access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Inadequate Aggregation Risk Assessment]
IF multiple_suppliers_engaged = TRUE
AND shared_information_overlaps = TRUE
AND aggregation_risk_assessed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Proper Use of Intermediary]
IF sensitive_acquisition = TRUE
AND intermediary_used = TRUE
AND end_user_obscured = TRUE
AND security_controls_maintained = TRUE
THEN compliance = TRUE

[SCENARIO-04: Missing Threat Analysis]
IF supply_chain_established = TRUE
AND threat_analysis_age > 12_months
AND new_suppliers_added = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Documented Information Withholding]
IF mission_critical_info_withheld = TRUE
AND business_justification_documented = TRUE
AND alternative_verification_method_established = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| OPSEC controls defined for supply chain protection | [RULE-01] |
| OPSEC controls employed to protect supply chain information | [RULE-02], [RULE-04] |
| Critical information identification and analysis | [RULE-02], [RULE-03] |
| Safeguard implementation and risk reduction | [RULE-04] |
| Information aggregation risk consideration | [RULE-05] |