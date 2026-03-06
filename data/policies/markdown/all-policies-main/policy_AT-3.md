# POLICY: AT-3: Role-based Training

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AT-3 |
| NIST Control | AT-3: Role-based Training |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | role-based training, security training, privacy training, personnel, system access, training content |

## 1. POLICY STATEMENT
All personnel with assigned security and privacy roles must complete role-based training before being authorized access to systems or performing assigned duties. Training content must be regularly updated based on defined frequencies and triggering events, including lessons learned from security incidents.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Employees | YES | All personnel with security/privacy roles |
| Contractors | YES | Those providing services with system access |
| Third-party vendors | CONDITIONAL | Only those with assigned security roles |
| Temporary staff | YES | If assigned security/privacy responsibilities |
| All information systems | YES | Including cloud and hybrid infrastructure |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Define training requirements for security roles<br>• Approve role-based training content<br>• Ensure compliance with training requirements |
| Privacy Officer | • Define training requirements for privacy roles<br>• Develop privacy-specific training content<br>• Monitor privacy training compliance |
| HR Department | • Track training completion status<br>• Coordinate training delivery<br>• Maintain training records |
| System Owners | • Identify personnel requiring role-based training<br>• Ensure training completion before access authorization<br>• Report training compliance status |

## 4. RULES
[RULE-01] Personnel with assigned security or privacy roles MUST complete role-based training before being authorized access to systems, information, or performing assigned duties.
[VALIDATION] IF role_assigned = TRUE AND training_completed = FALSE AND access_authorized = TRUE THEN violation

[RULE-02] Role-based training MUST be provided at defined frequencies: annually for standard roles, semi-annually for privileged roles, and quarterly for critical security roles.
[VALIDATION] IF last_training_date + frequency_interval < current_date AND role_active = TRUE THEN violation

[RULE-03] Role-based training MUST be provided when required by system changes that affect security or privacy responsibilities.
[VALIDATION] IF system_change_impact_security = TRUE AND training_updated = FALSE AND days_since_change > 30 THEN violation

[RULE-04] Role-based training content MUST be updated annually and following defined triggering events including security incidents, audit findings, or regulatory changes.
[VALIDATION] IF last_content_update + 365_days < current_date THEN violation

[RULE-05] Lessons learned from internal or external security incidents or breaches MUST be incorporated into role-based training within 90 days of incident closure.
[VALIDATION] IF incident_closed = TRUE AND lessons_learned_available = TRUE AND training_updated = FALSE AND days_since_closure > 90 THEN violation

[RULE-06] Training records MUST be maintained for all personnel with security and privacy roles, including completion dates, content versions, and assessment results.
[VALIDATION] IF role_assigned = TRUE AND training_record_exists = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Role-based Training Assignment - Identify and assign appropriate training based on personnel roles and responsibilities
- [PROC-02] Training Content Development - Create and maintain role-specific security and privacy training materials
- [PROC-03] Training Delivery and Tracking - Deliver training and maintain completion records
- [PROC-04] Training Content Updates - Regular review and update of training materials based on triggers
- [PROC-05] Incident Integration - Process for incorporating lessons learned into training content

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually
- Triggering events: Security incidents, audit findings, regulatory changes, organizational restructuring, technology changes affecting security roles

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Employee Access]
IF employee_status = "new"
AND security_role_assigned = TRUE
AND role_based_training_completed = FALSE
AND system_access_requested = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Training Frequency Violation]
IF role_type = "privileged"
AND last_training_date + 180_days < current_date
AND role_active = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Post-Incident Training Update]
IF security_incident_closed = TRUE
AND lessons_learned_documented = TRUE
AND training_content_updated = FALSE
AND days_since_closure > 90
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: System Change Training]
IF major_system_change = TRUE
AND security_roles_impacted = TRUE
AND updated_training_provided = FALSE
AND days_since_change > 30
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Contractor Training Compliance]
IF user_type = "contractor"
AND security_role_assigned = TRUE
AND role_based_training_completed = TRUE
AND training_current = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Role-based security training provided before access authorization | [RULE-01] |
| Role-based privacy training provided before access authorization | [RULE-01] |
| Training provided at defined frequencies | [RULE-02] |
| Training provided when required by system changes | [RULE-03] |
| Training content updated at defined frequencies | [RULE-04] |
| Training content updated following defined events | [RULE-04] |
| Lessons learned incorporated into training | [RULE-05] |
| Training records maintained | [RULE-06] |