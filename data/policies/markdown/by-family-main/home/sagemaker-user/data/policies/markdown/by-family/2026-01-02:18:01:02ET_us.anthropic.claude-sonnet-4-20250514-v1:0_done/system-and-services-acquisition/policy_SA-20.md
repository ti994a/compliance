# POLICY: SA-20: Customized Development of Critical Components

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-20 |
| NIST Control | SA-20: Customized Development of Critical Components |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | custom development, critical components, reimplementation, supply chain, trusted components |

## 1. POLICY STATEMENT
The organization SHALL identify critical system components that cannot be adequately trusted due to specific threats and vulnerabilities, and either reimplement or custom develop these components to achieve higher assurance levels. When reimplementation or custom development is not feasible, additional compensating controls MUST be implemented to mitigate associated risks.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical System Components | YES | Hardware, software, firmware identified as high-risk |
| Commercial Off-the-Shelf Software | CONDITIONAL | Only when identified as critical and untrusted |
| Third-party Components | CONDITIONAL | When no trusted alternatives exist |
| Internal Applications | YES | Custom-developed mission-critical applications |
| Cloud Services | CONDITIONAL | When providing critical infrastructure functions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve critical component designations<br>• Oversee risk assessments for untrusted components<br>• Authorize compensating controls |
| System Architects | • Identify critical system components<br>• Design reimplementation specifications<br>• Evaluate alternative sourcing options |
| Development Teams | • Execute custom development of critical components<br>• Implement secure coding practices<br>• Maintain development documentation |
| Supply Chain Manager | • Assess component trustworthiness<br>• Identify alternative sourcing options<br>• Maintain supplier risk assessments |

## 4. RULES

[RULE-01] Organizations MUST maintain a documented inventory of critical system components with trustworthiness assessments updated at least annually.
[VALIDATION] IF critical_component_inventory_exists = FALSE OR last_updated > 365_days THEN violation

[RULE-02] Critical components identified as untrusted MUST be reimplemented, custom developed, or protected with documented compensating controls within 180 days of identification.
[VALIDATION] IF component_trust_level = "untrusted" AND (reimplemented = FALSE AND custom_developed = FALSE AND compensating_controls = FALSE) AND days_since_identification > 180 THEN violation

[RULE-03] Custom development of critical components MUST follow secure development lifecycle practices including threat modeling, secure coding standards, and security testing.
[VALIDATION] IF custom_development = TRUE AND (threat_model = FALSE OR secure_coding_review = FALSE OR security_testing = FALSE) THEN violation

[RULE-04] When reimplementation or custom development is not feasible, organizations MUST implement enhanced auditing, access restrictions, and file protection controls.
[VALIDATION] IF reimplementation = FALSE AND custom_development = FALSE AND (enhanced_auditing = FALSE OR access_restrictions = FALSE OR file_protection = FALSE) THEN violation

[RULE-05] All decisions regarding critical component trust assessments and mitigation approaches MUST be documented and approved by the CISO.
[VALIDATION] IF critical_component_decision_documented = FALSE OR ciso_approval = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Critical Component Identification - Process for identifying and assessing trustworthiness of system components
- [PROC-02] Custom Development Standards - Secure development lifecycle requirements for critical components
- [PROC-03] Compensating Controls Implementation - Alternative controls when custom development is not feasible
- [PROC-04] Supply Chain Risk Assessment - Evaluation of component suppliers and alternatives

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: New critical system deployment, supply chain incidents, threat intelligence updates, regulatory changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Untrusted Component with No Mitigation]
IF component_criticality = "high"
AND trust_assessment = "untrusted"
AND reimplemented = FALSE
AND custom_developed = FALSE
AND compensating_controls = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Custom Development Without Security Controls]
IF custom_development = TRUE
AND component_criticality = "high"
AND (threat_modeling = FALSE OR security_testing = FALSE)
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Compensating Controls for Untrusted Component]
IF component_trust_level = "untrusted"
AND reimplementation = FALSE
AND custom_development = FALSE
AND enhanced_auditing = TRUE
AND access_restrictions = TRUE
AND file_protection = TRUE
AND ciso_approval = TRUE
THEN compliance = TRUE

[SCENARIO-04: Outdated Trust Assessment]
IF critical_component_inventory = TRUE
AND last_trust_assessment > 365_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Critical Component Custom Development]
IF component_criticality = "high"
AND trust_assessment = "untrusted"
AND custom_developed = TRUE
AND secure_sdlc_followed = TRUE
AND security_testing_completed = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Critical system components reimplemented or custom-developed are defined | [RULE-01] |
| Critical components are reimplemented or custom-developed | [RULE-02], [RULE-03] |
| Alternative controls implemented when custom development not feasible | [RULE-04] |
| Decisions documented and approved | [RULE-05] |