# POLICY: AC-2.8: Dynamic Account Management

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_AC-2.8 |
| NIST Control | AC-2.8: Dynamic Account Management |
| Version | 1.0 |
| Owner | Identity and Access Management Team |
| Keywords | dynamic accounts, provisioning, runtime creation, trust relationships, automated management |

## 1. POLICY STATEMENT
The organization SHALL implement automated mechanisms to dynamically create, activate, manage, and deactivate system accounts at runtime for previously unknown entities. All dynamic account operations MUST follow established trust relationships and business rules with validated authorities.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All information systems | YES | Including cloud, on-premises, and hybrid |
| Dynamic provisioning systems | YES | IAM platforms, SAML/OIDC providers |
| Service accounts | YES | When dynamically provisioned |
| Emergency access accounts | NO | Covered under separate procedures |
| Shared accounts | NO | Dynamic creation prohibited |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IAM Team | • Configure dynamic provisioning rules<br>• Monitor automated account operations<br>• Maintain trust relationships with authorities |
| System Administrators | • Implement technical controls for dynamic management<br>• Configure business rules and validation logic<br>• Ensure proper deactivation mechanisms |
| Security Operations | • Monitor dynamic account activities<br>• Investigate anomalous provisioning events<br>• Validate compliance with authorization policies |

## 4. RULES
[RULE-01] Dynamic account creation MUST only occur through pre-approved automated provisioning systems with established trust relationships.
[VALIDATION] IF account_creation_method != "approved_dynamic_system" AND account_type = "dynamic" THEN violation

[RULE-02] All dynamically created accounts MUST be validated against authoritative identity sources before activation.
[VALIDATION] IF dynamic_account_created = TRUE AND identity_validation = FALSE THEN critical_violation

[RULE-03] Dynamic accounts MUST be automatically deactivated within 8 hours of the triggering condition being removed or expired.
[VALIDATION] IF trigger_condition_removed = TRUE AND deactivation_time > 8_hours THEN violation

[RULE-04] Business rules for dynamic account management MUST be documented and approved by the data owner before implementation.
[VALIDATION] IF dynamic_provisioning_enabled = TRUE AND business_rules_approved = FALSE THEN violation

[RULE-05] Dynamic account activities MUST be logged with sufficient detail to support audit and forensic analysis.
[VALIDATION] IF dynamic_account_operation = TRUE AND audit_log_created = FALSE THEN violation

[RULE-06] Trust relationships with external authorities MUST be reviewed and validated at least quarterly.
[VALIDATION] IF trust_relationship_last_review > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Dynamic Account Provisioning - Automated creation and activation of accounts based on validated requests
- [PROC-02] Trust Relationship Management - Establishment and maintenance of relationships with authoritative sources
- [PROC-03] Business Rule Configuration - Definition and implementation of dynamic account management rules
- [PROC-04] Dynamic Account Monitoring - Real-time oversight of automated account operations
- [PROC-05] Emergency Deprovisioning - Rapid deactivation of dynamic accounts when required

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving dynamic accounts, changes to trust relationships, new provisioning systems

## 7. SCENARIO PATTERNS
[SCENARIO-01: Valid Dynamic Provisioning]
IF provisioning_system = "approved"
AND identity_validated = TRUE
AND business_rules_met = TRUE
AND trust_relationship_valid = TRUE
THEN compliance = TRUE

[SCENARIO-02: Unauthorized Dynamic Creation]
IF account_created_dynamically = TRUE
AND provisioning_system = "unapproved"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-03: Delayed Deactivation]
IF dynamic_account_active = TRUE
AND trigger_condition_expired = TRUE
AND hours_since_expiration > 8
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Missing Identity Validation]
IF dynamic_account_activated = TRUE
AND authoritative_source_check = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-05: Stale Trust Relationship]
IF dynamic_provisioning_enabled = TRUE
AND trust_relationship_review_date < (current_date - 90_days)
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Dynamic accounts are defined and created dynamically | [RULE-01], [RULE-02] |
| Dynamic accounts are activated dynamically | [RULE-02], [RULE-04] |
| Dynamic accounts are managed dynamically | [RULE-04], [RULE-05] |
| Dynamic accounts are deactivated dynamically | [RULE-03] |