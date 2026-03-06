# POLICY: AC-20: Use of External Systems

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-20 |
| NIST Control | AC-20: Use of External Systems |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | external systems, third-party access, remote access, trust relationships, terms and conditions |

## 1. POLICY STATEMENT
The organization establishes terms and conditions for external system usage that are consistent with trust relationships and organizational security requirements. External systems may be used to access organizational systems or process organizational information only under approved conditions with appropriate security controls.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All organizational systems | YES | Applies to all systems accessed from external sources |
| External systems accessing org data | YES | Including contractor, partner, and personal systems |
| Public-facing system interfaces | NO | Covered under separate access controls |
| Federal systems under direct control | NO | Not considered external systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve external system usage policies<br>• Define prohibited external system types<br>• Establish trust relationship criteria |
| System Owners | • Implement external access controls<br>• Monitor external system connections<br>• Maintain approved external system inventory |
| Legal/Compliance | • Review terms and conditions agreements<br>• Ensure regulatory compliance<br>• Approve third-party access agreements |

## 4. RULES
[RULE-01] Organizations MUST establish written terms and conditions for external system usage that address application types, data categories, and security requirements.
[VALIDATION] IF external_system_access = TRUE AND written_terms_conditions = FALSE THEN violation

[RULE-02] External systems SHALL NOT process, store, or transmit organizational data above the approved security categorization level defined in the terms and conditions.
[VALIDATION] IF data_classification > approved_max_classification AND external_system = TRUE THEN critical_violation

[RULE-03] Prohibited external system types as defined by the organization MUST NOT be used to access organizational systems or data.
[VALIDATION] IF external_system_type IN prohibited_types_list THEN critical_violation

[RULE-04] Terms and conditions MUST be consistent with established trust relationships and organizational security policies.
[VALIDATION] IF trust_relationship_level < required_trust_level AND external_access = TRUE THEN violation

[RULE-05] Organizations MUST maintain an inventory of approved external systems and their associated access permissions.
[VALIDATION] IF external_system_documented = FALSE AND active_access = TRUE THEN violation

[RULE-06] External system access agreements MUST be reviewed and reauthorized at least annually or when trust relationships change.
[VALIDATION] IF last_review_date > 365_days OR trust_relationship_changed = TRUE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] External System Risk Assessment - Evaluate security posture before approval
- [PROC-02] Terms and Conditions Development - Create specific usage agreements
- [PROC-03] Trust Relationship Evaluation - Assess organizational relationships
- [PROC-04] External System Monitoring - Track usage and compliance
- [PROC-05] Incident Response for External Systems - Handle security events

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Annually or upon significant changes
- Triggering events: New external partnerships, security incidents, regulatory changes, technology changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: Contractor Personal Device]
IF user_type = "contractor"
AND device_ownership = "personal"
AND terms_conditions_signed = FALSE
AND organizational_data_access = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-02: Partner System Data Processing]
IF external_org_type = "business_partner"
AND data_classification = "confidential"
AND approved_max_classification = "internal"
AND processing_active = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Prohibited System Type Usage]
IF external_system_type = "public_cloud_unapproved"
AND system_type IN prohibited_list
AND organizational_access = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-04: Expired Agreement Usage]
IF external_system_agreement_date < (current_date - 365_days)
AND active_access = TRUE
AND reauthorization_completed = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Appropriate External Access]
IF terms_conditions_current = TRUE
AND data_classification <= approved_max_classification
AND external_system_type NOT IN prohibited_list
AND trust_relationship = "established"
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Establish terms and conditions for external system access | RULE-01, RULE-04 |
| Allow authorized access from external systems per agreements | RULE-01, RULE-05 |
| Control processing/storage of org data on external systems | RULE-02, RULE-03 |
| Define and prohibit unauthorized external system types | RULE-03 |
| Maintain consistency with trust relationships | RULE-04, RULE-06 |