```markdown
POLICY: SI-7.17: Runtime Application Self-protection

METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SI-7.17 |
| NIST Control | SI-7.17: Runtime Application Self-protection |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | runtime protection, application security, exploit prevention, vulnerability detection, instrumentation |

1. POLICY STATEMENT
All applications in production environments MUST implement runtime application self-protection (RASP) controls to detect and block exploitation of software vulnerabilities during execution. RASP solutions SHALL operate with contextual awareness to monitor application inputs and prevent malicious exploitation attempts in real-time.

2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Production Applications | YES | All customer-facing and internal applications |
| Development Applications | CONDITIONAL | Required for applications handling sensitive data |
| Third-party Applications | YES | Where technically feasible and supported |
| Legacy Applications | CONDITIONAL | Risk-based implementation required |
| Cloud Applications | YES | Including containerized and serverless |

3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Application Security Team | • Define RASP implementation standards<br>• Evaluate and approve RASP solutions<br>• Monitor RASP effectiveness and coverage |
| Development Teams | • Integrate RASP controls into applications<br>• Configure application-specific protection rules<br>• Respond to RASP alerts and incidents |
| Security Operations Center | • Monitor RASP alerts and events<br>• Investigate potential exploitation attempts<br>• Coordinate incident response for blocked attacks |

4. RULES
[RULE-01] All in-scope applications MUST implement RASP controls that monitor runtime execution and block exploitation attempts.
[VALIDATION] IF application_in_scope = TRUE AND rasp_implemented = FALSE THEN violation

[RULE-02] RASP solutions MUST operate in protection mode for production applications, not monitor-only mode.
[VALIDATION] IF environment = "production" AND rasp_mode = "monitor" THEN violation

[RULE-03] RASP controls MUST be configured to detect and block at minimum: injection attacks, deserialization exploits, and remote code execution attempts.
[VALIDATION] IF rasp_coverage NOT includes ["injection", "deserialization", "rce"] THEN violation

[RULE-04] RASP alerts indicating blocked exploitation attempts MUST be investigated within 4 hours during business hours and 8 hours during off-hours.
[VALIDATION] IF rasp_alert_type = "blocked_exploit" AND response_time > defined_sla THEN violation

[RULE-05] Applications with RASP protection MUST maintain performance impact below 10% baseline response time.
[VALIDATION] IF performance_impact > 10_percent THEN configuration_review_required

[RULE-06] RASP configurations and rules MUST be reviewed and updated quarterly or when new vulnerability classes are identified.
[VALIDATION] IF last_rasp_review > 90_days THEN review_required

5. REQUIRED PROCEDURES
- [PROC-01] RASP Implementation Standard - Technical requirements and deployment guidelines
- [PROC-02] RASP Alert Response - Investigation and escalation procedures for protection events
- [PROC-03] RASP Performance Monitoring - Baseline establishment and impact assessment
- [PROC-04] RASP Rule Management - Configuration update and testing procedures

6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: New vulnerability classes, major application changes, RASP technology updates

7. SCENARIO PATTERNS
[SCENARIO-01: Production Application Without RASP]
IF application_environment = "production"
AND handles_sensitive_data = TRUE
AND rasp_implemented = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: RASP in Monitor Mode Only]
IF application_environment = "production"
AND rasp_implemented = TRUE
AND rasp_mode = "monitor"
AND protection_mode_available = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Delayed Response to Blocked Exploit]
IF rasp_alert_type = "blocked_exploit"
AND business_hours = TRUE
AND response_time > 4_hours
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Excessive Performance Impact]
IF rasp_implemented = TRUE
AND performance_impact > 10_percent
AND no_remediation_plan = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-05: Compliant RASP Implementation]
IF rasp_implemented = TRUE
AND rasp_mode = "protection"
AND coverage_adequate = TRUE
AND performance_impact <= 10_percent
THEN compliance = TRUE

8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Controls implemented for application self-protection at runtime are defined | [RULE-01], [RULE-03] |
| Controls are implemented for application self-protection at runtime | [RULE-01], [RULE-02] |
| Runtime instrumentation detects exploitation attempts | [RULE-03], [RULE-04] |
| Protection measures block malicious inputs | [RULE-02], [RULE-03] |
```