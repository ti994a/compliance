```markdown
# POLICY: AC-3.15: Discretionary and Mandatory Access Control

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-3.15 |
| NIST Control | AC-3.15: Discretionary and Mandatory Access Control |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | mandatory access control, discretionary access control, MAC, DAC, subjects, objects, dual enforcement |

## 1. POLICY STATEMENT
The organization SHALL simultaneously enforce both mandatory access control (MAC) and discretionary access control (DAC) policies over defined sets of subjects and objects. This dual enforcement provides additional protection against unauthorized code execution and prevents single points of compromise from affecting the entire system.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Classified and sensitive systems require MAC |
| Cloud infrastructure | YES | Both hybrid and public cloud components |
| Database systems | YES | Especially systems handling regulated data |
| Development environments | CONDITIONAL | When processing production-like data |
| Third-party SaaS | CONDITIONAL | When containing sensitive organizational data |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Administrators | • Configure and maintain MAC/DAC enforcement mechanisms<br>• Monitor access control violations<br>• Implement security labels and classifications |
| Security Engineers | • Design dual access control architectures<br>• Define subject and object classifications<br>• Validate policy enforcement effectiveness |
| Data Owners | • Define sensitivity classifications for data objects<br>• Approve discretionary access permissions<br>• Review access control policy compliance |

## 4. RULES
[RULE-01] Systems processing classified or sensitive data MUST implement both mandatory access control and discretionary access control policies simultaneously.
[VALIDATION] IF system_sensitivity_level IN ["classified", "sensitive", "regulated"] AND (mac_enabled = FALSE OR dac_enabled = FALSE) THEN critical_violation

[RULE-02] Mandatory access control policies MUST be defined for all covered subjects and objects with appropriate security classifications.
[VALIDATION] IF subject_or_object IN covered_entities AND mac_classification = NULL THEN violation

[RULE-03] Discretionary access control policies MUST be defined and enforced for all covered subjects and objects as specified in the organizational policy.
[VALIDATION] IF subject_or_object IN covered_entities AND dac_permissions = NULL THEN violation

[RULE-04] Access control enforcement mechanisms MUST prevent subjects from bypassing either mandatory or discretionary access controls.
[VALIDATION] IF bypass_attempt_detected = TRUE AND enforcement_prevented_bypass = FALSE THEN critical_violation

[RULE-05] Security labels and classifications MUST be consistently applied and maintained across all system components implementing dual access controls.
[VALIDATION] IF security_label_consistency_check = FALSE THEN violation

[RULE-06] Access control violations MUST be logged and monitored for both MAC and DAC policy enforcement.
[VALIDATION] IF access_violation_occurred = TRUE AND violation_logged = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] MAC/DAC Policy Definition - Establish and document mandatory and discretionary access control policies
- [PROC-02] Security Classification Management - Assign and maintain security labels for subjects and objects
- [PROC-03] Dual Access Control Implementation - Configure systems to enforce both MAC and DAC simultaneously
- [PROC-04] Access Control Monitoring - Monitor and respond to policy violations
- [PROC-05] Policy Effectiveness Review - Regularly assess dual access control implementation

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, system architecture changes, regulatory updates, classification changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Classified System Without MAC]
IF system_classification = "classified"
AND mac_policy_enforced = FALSE
AND dac_policy_enforced = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Incomplete Policy Coverage]
IF covered_subjects_defined = TRUE
AND covered_objects_defined = FALSE
AND dual_enforcement_required = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Successful Dual Enforcement]
IF mac_policy_defined = TRUE
AND dac_policy_defined = TRUE
AND both_policies_enforced = TRUE
AND subjects_and_objects_covered = TRUE
THEN compliance = TRUE

[SCENARIO-04: Access Control Bypass]
IF user_attempted_privilege_escalation = TRUE
AND mac_enforcement_bypassed = TRUE
AND incident_logged = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Inconsistent Security Labels]
IF security_labels_applied = TRUE
AND label_consistency_across_components = FALSE
AND dual_enforcement_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Mandatory access control policy defined for subjects | [RULE-02] |
| Mandatory access control policy enforced for subjects | [RULE-01] |
| Mandatory access control policy defined for objects | [RULE-02] |
| Mandatory access control policy enforced for objects | [RULE-01] |
| Discretionary access control policy defined for subjects | [RULE-03] |
| Discretionary access control policy enforced for subjects | [RULE-01] |
| Discretionary access control policy defined for objects | [RULE-03] |
| Discretionary access control policy enforced for objects | [RULE-01] |
```