```markdown
# POLICY: CM-11: User-installed Software

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_CM-11 |
| NIST Control | CM-11: User-installed Software |
| Version | 1.0 |
| Owner | IT Security Manager |
| Keywords | software installation, user privileges, policy enforcement, monitoring, configuration management |

## 1. POLICY STATEMENT
This policy establishes governance for user-installed software on organizational systems through defined policies, enforcement methods, and compliance monitoring. Users may only install software in accordance with approved policies and through authorized methods.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All employees | YES | Includes full-time, part-time, contractors |
| Workstations | YES | Company-owned and BYOD devices accessing corporate resources |
| Servers | YES | Production, development, and test environments |
| Mobile devices | YES | Corporate-managed and BYOD with corporate access |
| Guest users | CONDITIONAL | Only on designated guest networks/systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| IT Security Manager | • Define software installation policies<br>• Approve enforcement methods<br>• Review compliance reports |
| System Administrators | • Implement technical controls<br>• Configure monitoring systems<br>• Generate compliance reports |
| End Users | • Follow software installation policies<br>• Request approval for non-standard software<br>• Report policy violations |

## 4. RULES
[RULE-01] Organizations MUST establish written policies that explicitly define permitted and prohibited software installations by users.
[VALIDATION] IF software_installation_policy_exists = FALSE THEN critical_violation

[RULE-02] Permitted software installations MUST be limited to organization-approved app stores, security patches, and pre-authorized applications.
[VALIDATION] IF software_source NOT IN approved_sources AND installation_attempted = TRUE THEN violation

[RULE-03] Users MUST NOT install software with unknown pedigree, open source software without approval, or applications from unauthorized sources.
[VALIDATION] IF software_pedigree = "unknown" OR software_source = "unauthorized" THEN violation

[RULE-04] Software installation policies MUST be enforced through automated technical controls and procedural methods.
[VALIDATION] IF enforcement_methods_count < 1 THEN critical_violation

[RULE-05] Organizations MUST monitor compliance with software installation policies at least monthly.
[VALIDATION] IF last_compliance_review > 30_days THEN violation

[RULE-06] All software installation attempts MUST be logged and reviewed for policy compliance.
[VALIDATION] IF installation_logging_enabled = FALSE THEN violation

[RULE-07] Users requiring non-standard software MUST obtain written approval before installation.
[VALIDATION] IF software_category = "non_standard" AND approval_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Software Installation Policy Definition - Annual review and update of permitted/prohibited software lists
- [PROC-02] User Software Request Process - Approval workflow for non-standard software installations  
- [PROC-03] Automated Enforcement Configuration - Technical controls implementation and maintenance
- [PROC-04] Compliance Monitoring - Monthly review of installation logs and policy violations
- [PROC-05] Violation Response - Incident handling for unauthorized software installations

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually  
- Triggering events: Security incidents, new software categories, regulatory changes, technology refresh

## 7. SCENARIO PATTERNS
[SCENARIO-01: Approved Software Installation]
IF software_source = "approved_app_store"
AND user_has_permission = TRUE
AND software_category = "business_approved"
THEN compliance = TRUE

[SCENARIO-02: Unauthorized Software Source]
IF software_source = "internet_download" 
AND source NOT IN approved_sources
AND installation_completed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Missing Installation Approval]
IF software_category = "development_tool"
AND approval_documented = FALSE
AND installation_attempted = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Security Patch Installation]
IF software_type = "security_patch"
AND vendor = "approved_vendor"
AND patch_source = "official_vendor_site"
THEN compliance = TRUE

[SCENARIO-05: Monitoring Compliance Gap]
IF last_compliance_review > 30_days
AND monitoring_system_active = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Policies governing software installation are defined | [RULE-01] |
| Software installation policies are established | [RULE-01], [RULE-02], [RULE-03] |
| Software installation policies are enforced | [RULE-04], [RULE-06] |
| Policy compliance is monitored | [RULE-05], [RULE-06] |
| Enforcement methods are defined | [RULE-04] |
| Monitoring frequency is defined | [RULE-05] |
```