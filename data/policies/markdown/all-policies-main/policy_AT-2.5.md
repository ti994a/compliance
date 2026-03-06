# POLICY: AT-2.5: Advanced Persistent Threat

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AT-2.5 |
| NIST Control | AT-2.5: Advanced Persistent Threat |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | advanced persistent threat, APT, literacy training, security awareness, threat detection, social engineering |

## 1. POLICY STATEMENT
The organization SHALL provide comprehensive literacy training on advanced persistent threats (APT) to enable personnel to recognize, understand, and respond appropriately to APT attack vectors. This training is essential for creating a human firewall against sophisticated, targeted cyber attacks that traditional security controls may not detect.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Includes full-time, part-time, and temporary staff |
| Contractors | YES | Those with system access or handling sensitive data |
| Third-party users | CONDITIONAL | Based on access level and data exposure |
| Executives | YES | High-value targets requiring specialized training |
| Remote workers | YES | Enhanced training due to increased risk exposure |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve APT training curriculum and materials<br>• Ensure training aligns with current threat landscape<br>• Monitor training effectiveness metrics |
| Security Awareness Team | • Develop and maintain APT-specific training content<br>• Track training completion and effectiveness<br>• Update materials based on emerging threats |
| HR Department | • Ensure new hire APT training within onboarding<br>• Coordinate training schedules and compliance tracking<br>• Support disciplinary actions for non-compliance |
| Line Managers | • Ensure direct reports complete required training<br>• Reinforce APT awareness in team communications<br>• Report suspected APT activities immediately |

## 4. RULES
[RULE-01] All personnel with system access MUST complete APT literacy training within 30 days of hire or role change.
[VALIDATION] IF employee_start_date + 30_days < current_date AND apt_training_completed = FALSE THEN violation

[RULE-02] APT literacy training MUST be refreshed annually with updated threat intelligence and attack vectors.
[VALIDATION] IF last_apt_training_date + 365_days < current_date THEN violation

[RULE-03] Training content MUST cover website-based attacks, malicious emails, advertisement pop-ups, social engineering, and removable media threats.
[VALIDATION] IF training_modules_covered < required_apt_modules THEN violation

[RULE-04] Personnel in high-risk roles MUST receive enhanced APT training including home/remote work security practices.
[VALIDATION] IF risk_level = "high" AND enhanced_apt_training = FALSE THEN violation

[RULE-05] Training effectiveness MUST be measured through simulated APT scenarios with minimum 80% pass rate.
[VALIDATION] IF simulation_pass_rate < 80% THEN remedial_training_required

[RULE-06] APT training materials MUST be updated within 60 days of significant new threat intelligence or attack patterns.
[VALIDATION] IF threat_intelligence_update_date + 60_days < current_date AND training_materials_updated = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] APT Training Curriculum Development - Define and maintain comprehensive APT literacy training content
- [PROC-02] Training Delivery and Tracking - Manage training schedules, delivery methods, and completion tracking
- [PROC-03] Threat Intelligence Integration - Incorporate current APT tactics into training materials
- [PROC-04] Training Effectiveness Assessment - Conduct simulations and measure training impact
- [PROC-05] Incident Response Integration - Connect APT awareness to incident reporting procedures

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major APT campaigns, successful attacks, regulatory changes, technology shifts

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Employee APT Training]
IF employee_start_date + 30_days < current_date
AND apt_training_completed = FALSE
AND system_access_granted = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Outdated Training Content]
IF major_apt_campaign_identified = TRUE
AND campaign_discovery_date + 60_days < current_date
AND training_materials_updated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Failed Training Assessment]
IF apt_simulation_completed = TRUE
AND simulation_pass_rate < 80%
AND remedial_training_provided = FALSE
AND days_since_failure > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Executive APT Training Exemption]
IF user_role = "executive"
AND apt_training_completed = FALSE
AND training_exemption_documented = TRUE
AND exemption_approved_by_ciso = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Remote Worker Enhanced Training]
IF work_location = "remote"
AND apt_training_completed = TRUE
AND home_security_module_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Literacy training on APT is provided | [RULE-01], [RULE-02] |
| Training covers APT infiltration methods | [RULE-03] |
| Training includes home/remote targeting | [RULE-04] |
| Training effectiveness is measured | [RULE-05] |
| Training content remains current | [RULE-06] |