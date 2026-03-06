# POLICY: SR-7: Supply Chain Operations Security

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-7 |
| NIST Control | SR-7: Supply Chain Operations Security |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | supply chain, OPSEC, operations security, supplier information, procurement, vendor management |

## 1. POLICY STATEMENT
The organization SHALL implement Operations Security (OPSEC) controls to protect supply chain-related information throughout the acquisition lifecycle. Supply chain OPSEC controls MUST be defined, documented, and employed to safeguard critical information from potential adversaries who may exploit supply chain vulnerabilities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT systems | YES | Including cloud, on-premises, and hybrid |
| System components | YES | Hardware, software, firmware |
| System services | YES | Managed services, SaaS, consulting |
| Suppliers/Vendors | YES | All tiers of supply chain |
| Procurement staff | YES | All acquisition personnel |
| Business units | YES | When engaging suppliers |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define OPSEC control requirements<br>• Approve supply chain OPSEC procedures<br>• Monitor compliance with OPSEC controls |
| Procurement Manager | • Implement OPSEC controls in acquisition processes<br>• Train staff on supply chain OPSEC requirements<br>• Maintain supplier OPSEC documentation |
| Supply Chain Risk Manager | • Assess OPSEC risks in supplier relationships<br>• Monitor supply chain information exposure<br>• Coordinate OPSEC incident response |

## 4. RULES

[RULE-01] Organizations MUST define and document specific OPSEC controls for protecting supply chain-related information including user identities, system uses, supplier identities, security requirements, configurations, and testing results.
[VALIDATION] IF supply_chain_engagement = TRUE AND opsec_controls_documented = FALSE THEN violation

[RULE-02] Critical supply chain information SHALL NOT be disclosed to suppliers unless operationally necessary and approved through the risk assessment process.
[VALIDATION] IF critical_info_disclosed = TRUE AND risk_assessment_approved = FALSE THEN critical_violation

[RULE-03] Organizations MUST use intermediaries or indirect procurement methods when direct supplier engagement would expose sensitive mission or business information.
[VALIDATION] IF mission_critical_system = TRUE AND direct_supplier_contact = TRUE AND intermediary_justified = FALSE THEN violation

[RULE-04] Supply chain OPSEC controls MUST be implemented before engaging with potential suppliers and maintained throughout the supplier relationship lifecycle.
[VALIDATION] IF supplier_engagement_started = TRUE AND opsec_controls_implemented = FALSE THEN critical_violation

[RULE-05] Aggregated supply chain information that could expose users, uses, or operational patterns MUST be protected through compartmentalization and need-to-know principles.
[VALIDATION] IF aggregated_info_accessible = TRUE AND compartmentalization = FALSE THEN violation

[RULE-06] Supply chain OPSEC procedures MUST include safeguards to eliminate or reduce exploitable vulnerabilities to an acceptable risk level as defined by organizational risk tolerance.
[VALIDATION] IF opsec_procedures_exist = TRUE AND risk_level > acceptable_threshold THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Supply Chain OPSEC Assessment - Identify and classify supply chain information requiring protection
- [PROC-02] Supplier Information Disclosure Control - Manage what information is shared with suppliers
- [PROC-03] Intermediary Procurement Process - Use third parties to obscure end users when necessary
- [PROC-04] Supply Chain Information Monitoring - Detect and respond to information exposure incidents
- [PROC-05] OPSEC Training and Awareness - Educate personnel on supply chain OPSEC requirements

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New supplier onboarding, supply chain incidents, regulatory changes, major system acquisitions

## 7. SCENARIO PATTERNS

[SCENARIO-01: Direct Supplier Engagement for Classified System]
IF system_classification = "classified"
AND supplier_contact_method = "direct"
AND intermediary_used = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Excessive Information Sharing in RFP]
IF rfp_contains_critical_info = TRUE
AND business_justification = FALSE
AND opsec_review_completed = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Proper Use of Intermediary]
IF sensitive_procurement = TRUE
AND intermediary_used = TRUE
AND end_user_identity_protected = TRUE
THEN compliance = TRUE

[SCENARIO-04: Aggregated Data Exposure]
IF multiple_supplier_data_combined = TRUE
AND operational_patterns_revealed = TRUE
AND access_controls_implemented = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Undocumented OPSEC Controls]
IF supplier_engagement_active = TRUE
AND opsec_controls_defined = FALSE
AND supply_chain_info_shared = TRUE
THEN compliance = FALSE
violation_severity = "High"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| OPSEC controls are defined | RULE-01 |
| OPSEC controls are employed to protect supply chain information | RULE-02, RULE-04, RULE-06 |
| Critical information protection | RULE-02, RULE-05 |
| Intermediary usage when appropriate | RULE-03 |
| Lifecycle implementation | RULE-04 |
| Risk-based safeguards | RULE-06 |