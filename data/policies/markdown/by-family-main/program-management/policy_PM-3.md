```markdown
POLICY: PM-3: Information Security and Privacy Resources

METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PM-3 |
| NIST Control | PM-3: Information Security and Privacy Resources |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | capital planning, investment requests, security resources, privacy resources, budget allocation, resource documentation |

1. POLICY STATEMENT
The organization must include information security and privacy program resources in all capital planning and investment requests with documented exceptions. Required documentation must comply with applicable laws and regulations, and approved resources must be made available for expenditure as planned.

2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| IT Capital Projects | YES | All projects requiring capital investment |
| Security Programs | YES | Both information security and privacy programs |
| Investment Review Board | YES | Oversight and approval responsibilities |
| Business Units | YES | When submitting capital planning requests |
| Third-party Services | CONDITIONAL | When requiring security/privacy resources |

3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Chief Information Security Officer | • Ensure security resources included in capital planning<br>• Review and approve security resource requirements<br>• Document exceptions to resource inclusion |
| Chief Privacy Officer | • Ensure privacy resources included in capital planning<br>• Review and approve privacy resource requirements<br>• Document exceptions to privacy inclusion |
| Investment Review Board | • Oversee security and privacy aspects of capital planning<br>• Approve resource allocations<br>• Ensure compliance with regulatory requirements |
| Project Managers | • Include security/privacy resources in project requests<br>• Prepare compliant documentation<br>• Coordinate with security and privacy teams |

4. RULES
[RULE-01] All capital planning and investment requests MUST include resources needed for information security program implementation.
[VALIDATION] IF capital_request_submitted = TRUE AND security_resources_included = FALSE AND documented_exception = FALSE THEN violation

[RULE-02] All capital planning and investment requests MUST include resources needed for privacy program implementation.
[VALIDATION] IF capital_request_submitted = TRUE AND privacy_resources_included = FALSE AND documented_exception = FALSE THEN violation

[RULE-03] Documentation for capital planning requests MUST be prepared in accordance with applicable laws, executive orders, directives, policies, regulations, and standards.
[VALIDATION] IF documentation_prepared = TRUE AND regulatory_compliance_verified = FALSE THEN violation

[RULE-04] All exceptions to security and privacy resource inclusion MUST be documented with business justification and risk assessment.
[VALIDATION] IF resources_excluded = TRUE AND exception_documented = FALSE THEN violation

[RULE-05] Approved information security resources MUST be made available for expenditure within 30 days of budget approval.
[VALIDATION] IF budget_approved = TRUE AND days_since_approval > 30 AND resources_available = FALSE THEN violation

[RULE-06] Approved privacy resources MUST be made available for expenditure within 30 days of budget approval.
[VALIDATION] IF budget_approved = TRUE AND days_since_approval > 30 AND privacy_resources_available = FALSE THEN violation

5. REQUIRED PROCEDURES
- [PROC-01] Capital Planning Resource Assessment - Systematic evaluation of security and privacy resource needs
- [PROC-02] Exception Documentation Process - Standardized process for documenting and approving resource exclusions
- [PROC-03] Regulatory Compliance Review - Verification that documentation meets all applicable requirements
- [PROC-04] Resource Availability Tracking - Monitoring and reporting on approved resource expenditure

6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Regulatory changes, budget cycle changes, organizational restructuring, audit findings

7. SCENARIO PATTERNS
[SCENARIO-01: Missing Security Resources]
IF capital_request_type = "IT_infrastructure"
AND security_resources_included = FALSE
AND documented_exception = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Delayed Resource Availability]
IF budget_approved = TRUE
AND approval_date < (current_date - 45_days)
AND security_resources_available = FALSE
AND privacy_resources_available = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Undocumented Exception]
IF privacy_resources_required = TRUE
AND privacy_resources_included = FALSE
AND exception_documented = FALSE
AND business_justification = NULL
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-04: Compliant Request with Exception]
IF capital_request_submitted = TRUE
AND security_resources_excluded = TRUE
AND documented_exception = TRUE
AND risk_assessment_completed = TRUE
THEN compliance = TRUE

[SCENARIO-05: Non-compliant Documentation]
IF capital_planning_documentation = TRUE
AND regulatory_requirements_met = FALSE
AND sox_compliance = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Security resources included in capital planning | [RULE-01] |
| Privacy resources included in capital planning | [RULE-02] |
| Documentation prepared per regulations | [RULE-03] |
| Exceptions documented | [RULE-04] |
| Security resources made available | [RULE-05] |
| Privacy resources made available | [RULE-06] |
```