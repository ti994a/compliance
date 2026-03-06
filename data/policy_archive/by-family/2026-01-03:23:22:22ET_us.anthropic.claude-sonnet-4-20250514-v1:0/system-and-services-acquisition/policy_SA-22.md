```markdown
# POLICY: SA-22: Unsupported System Components

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SA-22 |
| NIST Control | SA-22: Unsupported System Components |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | unsupported components, vendor support, patches, firmware updates, alternative support, in-house support |

## 1. POLICY STATEMENT
System components MUST be replaced when vendor support ends, or alternative support sources MUST be established with appropriate risk mitigation. Unsupported components SHALL NOT remain in production without documented justification and compensating controls.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All IT Systems | YES | Including cloud, on-premises, and hybrid |
| Software Applications | YES | Commercial and custom applications |
| Hardware Components | YES | Servers, network devices, endpoints |
| Firmware | YES | All embedded system firmware |
| Third-party Services | YES | SaaS, PaaS, and vendor-managed services |
| Development/Test Systems | CONDITIONAL | If connected to production networks |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| System Owners | • Monitor vendor support lifecycle<br>• Request replacement or alternative support<br>• Document business justification for exceptions |
| IT Operations | • Track support end-dates<br>• Execute component replacements<br>• Implement compensating controls |
| Security Team | • Assess risks of unsupported components<br>• Approve alternative support arrangements<br>• Monitor for security patches |
| Procurement | • Source replacement components<br>• Negotiate alternative support contracts<br>• Manage vendor relationships |

## 4. RULES

[RULE-01] System components MUST be replaced within 90 days of vendor end-of-support unless alternative support is established.
[VALIDATION] IF support_end_date < (current_date - 90_days) AND replacement_status != "completed" AND alternative_support != "approved" THEN violation

[RULE-02] Alternative support sources MUST be documented and approved by the security team before support end-date.
[VALIDATION] IF alternative_support = TRUE AND (documentation != "complete" OR security_approval != "approved") THEN violation

[RULE-03] Unsupported components with alternative support MUST have compensating controls implemented based on risk assessment.
[VALIDATION] IF component_status = "unsupported" AND alternative_support = TRUE AND compensating_controls != "implemented" THEN violation

[RULE-04] Critical mission systems MAY continue using unsupported components only with CISO approval and enhanced monitoring.
[VALIDATION] IF system_criticality = "mission_critical" AND component_status = "unsupported" AND ciso_approval != "granted" THEN critical_violation

[RULE-05] Unsupported components SHALL NOT be connected to public networks without network isolation controls.
[VALIDATION] IF component_status = "unsupported" AND network_exposure = "public" AND isolation_controls != "implemented" THEN critical_violation

[RULE-06] Component support status MUST be reviewed quarterly and tracked in the asset inventory.
[VALIDATION] IF last_support_review > 90_days OR asset_inventory_updated != TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Component Lifecycle Tracking - Monitor vendor support timelines and end-of-life announcements
- [PROC-02] Risk Assessment for Unsupported Components - Evaluate security and operational risks
- [PROC-03] Alternative Support Evaluation - Assess in-house or third-party support options
- [PROC-04] Component Replacement Planning - Develop migration timelines and resource requirements
- [PROC-05] Compensating Controls Implementation - Deploy additional security measures for retained components

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Major vendor announcements, security incidents involving unsupported components, regulatory changes

## 7. SCENARIO PATTERNS

[SCENARIO-01: Standard Component End-of-Support]
IF vendor_support_end_date < current_date
AND replacement_completed = FALSE
AND alternative_support = FALSE
AND days_past_support > 90
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Critical System with Alternative Support]
IF system_criticality = "mission_critical"
AND component_status = "unsupported"
AND alternative_support = "in-house"
AND compensating_controls = "implemented"
AND ciso_approval = "granted"
THEN compliance = TRUE

[SCENARIO-03: Unsupported Component on Public Network]
IF component_status = "unsupported"
AND network_connectivity = "internet_facing"
AND network_isolation = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Approved Exception with Monitoring]
IF component_status = "unsupported"
AND business_justification = "documented"
AND security_approval = "granted"
AND enhanced_monitoring = "active"
AND compensating_controls = "implemented"
THEN compliance = TRUE

[SCENARIO-05: Overdue Support Status Review]
IF last_support_review > 90_days
AND component_count > 0
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Replace unsupported components when support unavailable | [RULE-01] |
| Provide alternative support sources for continued use | [RULE-02], [RULE-03] |
| Document and approve alternative support arrangements | [RULE-02], [RULE-04] |
| Implement risk mitigation for unsupported components | [RULE-03], [RULE-05] |
| Maintain current inventory of component support status | [RULE-06] |
```