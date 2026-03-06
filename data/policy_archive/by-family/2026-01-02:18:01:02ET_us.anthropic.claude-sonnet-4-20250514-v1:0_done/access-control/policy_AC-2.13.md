# POLICY: AC-2.13: Disable Accounts for High-risk Individuals

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-2.13 |
| NIST Control | AC-2.13: Disable Accounts for High-risk Individuals |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | account_management, high_risk, disable_accounts, threat_mitigation, insider_threat |

## 1. POLICY STATEMENT
Accounts of individuals who pose significant security or privacy risks to the organization MUST be disabled within defined timeframes upon discovery of such risks. This policy ensures rapid response to insider threats and prevents unauthorized access by high-risk individuals.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All user accounts | YES | Employees, contractors, vendors, partners |
| System accounts | YES | When associated with high-risk individuals |
| Emergency accounts | YES | No exceptions for emergency access |
| Privileged accounts | YES | Higher priority for immediate action |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Operations Center | • Monitor for high-risk indicators<br>• Execute immediate account disabling<br>• Coordinate with incident response team |
| Human Resources | • Report personnel security concerns<br>• Provide termination notifications<br>• Coordinate with legal on employment actions |
| System Administrators | • Implement account disabling procedures<br>• Verify account status across all systems<br>• Document disabling actions |
| Legal Counsel | • Assess legal implications of account actions<br>• Provide guidance on evidence requirements<br>• Coordinate with law enforcement if needed |

## 4. RULES

[RULE-01] Accounts of individuals posing critical security risks MUST be disabled within 1 hour of risk discovery.
[VALIDATION] IF risk_level = "critical" AND discovery_time + 1_hour < current_time AND account_status = "active" THEN critical_violation

[RULE-02] Accounts of individuals posing moderate security risks MUST be disabled within 4 hours of risk discovery.
[VALIDATION] IF risk_level = "moderate" AND discovery_time + 4_hours < current_time AND account_status = "active" THEN major_violation

[RULE-03] All account disabling actions MUST be documented with risk justification and approval from Security Manager or higher authority.
[VALIDATION] IF account_disabled = TRUE AND (documentation_complete = FALSE OR approval_level < "Security_Manager") THEN violation

[RULE-04] Disabled high-risk accounts SHALL NOT be re-enabled without written approval from CISO and completion of risk reassessment.
[VALIDATION] IF previous_risk_disable = TRUE AND account_status = "active" AND (ciso_approval = FALSE OR risk_reassessment = FALSE) THEN critical_violation

[RULE-05] Cross-system account verification MUST be completed within 2 hours of initial account disabling to ensure complete access removal.
[VALIDATION] IF account_disabled = TRUE AND cross_system_verification_time > initial_disable_time + 2_hours THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] High-Risk Individual Identification - Process for detecting and reporting security risks
- [PROC-02] Emergency Account Disabling - Rapid response procedures for immediate threat mitigation
- [PROC-03] Cross-System Account Verification - Comprehensive access removal across all platforms
- [PROC-04] Risk Assessment and Documentation - Evidence collection and justification requirements
- [PROC-05] Account Re-enablement Process - Controlled restoration of access after risk mitigation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving insider threats, changes to risk assessment processes, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Critical Insider Threat]
IF risk_indicators = "malicious_intent"
AND evidence_reliability = "high"
AND account_status = "active"
AND disable_time > discovery_time + 1_hour
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Contractor Under Investigation]
IF user_type = "contractor"
AND investigation_status = "active"
AND risk_level = "moderate"
AND disable_time > discovery_time + 4_hours
THEN compliance = FALSE
violation_severity = "Major"

[SCENARIO-03: Account Re-enabled Without Approval]
IF previous_disable_reason = "high_risk"
AND current_status = "active"
AND ciso_approval = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Incomplete Cross-System Disabling]
IF primary_account = "disabled"
AND secondary_systems_checked = FALSE
AND verification_time > disable_time + 2_hours
THEN compliance = FALSE
violation_severity = "Major"

[SCENARIO-05: Proper High-Risk Response]
IF risk_level = "critical"
AND disable_time <= discovery_time + 1_hour
AND documentation_complete = TRUE
AND cross_system_verification = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Timely disabling of critical risk accounts | RULE-01 |
| Timely disabling of moderate risk accounts | RULE-02 |
| Proper documentation and approval | RULE-03 |
| Controlled re-enablement process | RULE-04 |
| Complete cross-system verification | RULE-05 |