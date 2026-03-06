# POLICY: CP-7.6: Inability to Return to Primary Site

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CP-7.6 |
| NIST Control | CP-7.6: Inability to Return to Primary Site |
| Version | 1.0 |
| Owner | Business Continuity Manager |
| Keywords | contingency planning, primary site, alternate processing, site recovery, disaster recovery |

## 1. POLICY STATEMENT
The organization SHALL plan and prepare for circumstances that preclude returning to the primary processing site. Contingency plans MUST include provisions for permanent relocation to alternate processing sites when the primary site cannot be restored.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Critical business systems | YES | All systems supporting essential functions |
| Primary data centers | YES | Physical and cloud-based primary facilities |
| Alternate processing sites | YES | All designated backup facilities |
| Emergency response teams | YES | Personnel responsible for site recovery decisions |
| Non-critical development systems | CONDITIONAL | If supporting critical business functions |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Business Continuity Manager | • Develop permanent relocation procedures<br>• Coordinate site assessment activities<br>• Maintain alternate site readiness |
| IT Operations Manager | • Execute technical migration procedures<br>• Validate alternate site capabilities<br>• Coordinate data recovery operations |
| Facilities Manager | • Assess primary site damage and recovery feasibility<br>• Coordinate with insurance and construction vendors<br>• Manage physical infrastructure requirements |

## 4. RULES
[RULE-01] Organizations MUST maintain documented procedures for assessing primary site recoverability within 72 hours of a disaster event.
[VALIDATION] IF disaster_declared = TRUE AND site_assessment_completed = FALSE AND elapsed_time > 72_hours THEN violation

[RULE-02] Alternate processing sites MUST be capable of supporting permanent operations for a minimum of 12 months without dependency on the primary site.
[VALIDATION] IF alternate_site_capacity < 12_months AND primary_site_available = FALSE THEN critical_violation

[RULE-03] Decision criteria for permanent relocation MUST be documented and include cost-benefit analysis thresholds exceeding $1M or 6-month recovery timeframes.
[VALIDATION] IF relocation_decision_made = TRUE AND (cost_analysis_completed = FALSE OR criteria_documented = FALSE) THEN violation

[RULE-04] Permanent relocation procedures MUST be tested annually through tabletop exercises involving executive leadership.
[VALIDATION] IF current_date - last_relocation_test > 365_days THEN violation

[RULE-05] Data migration and system reconfiguration procedures for permanent relocation MUST be completed within 30 days of relocation decision.
[VALIDATION] IF relocation_approved = TRUE AND migration_time > 30_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Site Damage Assessment - Systematic evaluation of primary site recoverability
- [PROC-02] Permanent Relocation Decision Matrix - Criteria-based decision framework
- [PROC-03] Alternate Site Activation for Permanent Operations - Technical migration procedures
- [PROC-04] Stakeholder Communication During Permanent Relocation - Internal and external notification processes

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major disaster events, facility lease changes, significant infrastructure modifications

## 7. SCENARIO PATTERNS
[SCENARIO-01: Hurricane Facility Destruction]
IF primary_site_damage > 75_percent
AND estimated_rebuild_time > 6_months
AND alternate_site_available = TRUE
THEN permanent_relocation_required = TRUE
compliance = PASS if procedures_followed = TRUE

[SCENARIO-02: Flood with Extended Recovery]
IF primary_site_flooded = TRUE
AND recovery_cost > 1_million_USD
AND business_interruption > 90_days
AND relocation_decision_delayed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Earthquake with Zoning Changes]
IF primary_site_damaged = TRUE
AND local_zoning_prohibits_rebuild = TRUE
AND alternate_site_activation_time > 30_days
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Successful Permanent Migration]
IF site_assessment_completed_within_72hrs = TRUE
AND relocation_decision_documented = TRUE
AND migration_completed_within_30days = TRUE
THEN compliance = TRUE

[SCENARIO-05: Inadequate Alternate Site Capacity]
IF primary_site_unavailable = TRUE
AND alternate_site_capacity < 12_months
AND permanent_operations_required = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Circumstances that preclude returning to primary site are planned for | RULE-01, RULE-03 |
| Circumstances that preclude returning to primary site are prepared for | RULE-02, RULE-04, RULE-05 |