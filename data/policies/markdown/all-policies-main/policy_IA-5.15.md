# POLICY: IA-5.15: GSA-approved Products and Services

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-5.15 |
| NIST Control | IA-5.15: GSA-approved Products and Services |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | GSA-approved, FICAM, identity management, credential management, access management, approved products list |

## 1. POLICY STATEMENT
The organization SHALL use only General Services Administration (GSA)-approved products and services for all identity, credential, and access management functions. All ICAM solutions MUST be selected from the GSA Approved Products List and comply with Federal Identity, Credential, and Access Management (FICAM) policies.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal systems | YES | All systems processing federal data |
| FedRAMP systems | YES | Required for FedRAMP compliance |
| Commercial systems | CONDITIONAL | If processing federal data or under federal contract |
| Development environments | YES | Must use approved ICAM for federal development |
| Third-party integrations | YES | ICAM components must be GSA-approved |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Maintain GSA Approved Products List access<br>• Approve ICAM architecture decisions<br>• Ensure policy compliance monitoring |
| IT Procurement | • Verify GSA approval status before purchase<br>• Maintain vendor compliance documentation<br>• Coordinate with GSA for product verification |
| System Architects | • Design ICAM solutions using only approved products<br>• Document GSA approval status in system designs<br>• Validate FICAM compliance patterns |

## 4. RULES
[RULE-01] All identity management products MUST be selected exclusively from the current GSA Approved Products List.
[VALIDATION] IF product_category = "identity_management" AND gsa_approved_status != "approved" THEN critical_violation

[RULE-02] All credential management services MUST have valid GSA approval and active listing status.
[VALIDATION] IF service_type = "credential_management" AND (gsa_approval_date = null OR listing_status != "active") THEN critical_violation

[RULE-03] Access management solutions MUST comply with FICAM implementation patterns and maintain GSA approval.
[VALIDATION] IF solution_type = "access_management" AND (ficam_compliant != true OR gsa_approved != true) THEN critical_violation

[RULE-04] Procurement teams MUST verify GSA approval status within 30 days before any ICAM product purchase.
[VALIDATION] IF purchase_category = "ICAM" AND gsa_verification_date > (purchase_date - 30_days) THEN compliant ELSE violation

[RULE-05] Existing non-GSA-approved ICAM products MUST be replaced within 12 months of policy effective date.
[VALIDATION] IF deployment_date < policy_effective_date AND gsa_approved != true AND current_date > (policy_effective_date + 365_days) THEN critical_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] GSA Approval Verification - Validate product approval status before procurement
- [PROC-02] FICAM Compliance Assessment - Evaluate solutions against FICAM patterns
- [PROC-03] Approved Products List Monitoring - Regular review of GSA list updates
- [PROC-04] Legacy System Remediation - Plan for replacing non-approved products

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: GSA Approved Products List updates, new FICAM guidance, system architecture changes

## 7. SCENARIO PATTERNS
[SCENARIO-01: New Identity Provider Selection]
IF system_type = "identity_provider"
AND procurement_phase = "vendor_selection"
AND vendor_gsa_status != "approved"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Legacy System Assessment]
IF system_deployment_date < "2024-01-01"
AND icam_components_present = TRUE
AND gsa_approval_verified = FALSE
AND remediation_plan_exists = FALSE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Third-party Integration]
IF integration_type = "ICAM"
AND third_party_solution = TRUE
AND gsa_approved_status = "approved"
AND ficam_compliance_verified = TRUE
THEN compliance = TRUE

[SCENARIO-04: Emergency ICAM Deployment]
IF deployment_urgency = "emergency"
AND gsa_approved_status = "pending"
AND temporary_authorization_exists = FALSE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Multi-vendor ICAM Solution]
IF solution_architecture = "multi_vendor"
AND all_components_gsa_approved = TRUE
AND ficam_pattern_compliance = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Only GSA-approved products used for identity management | [RULE-01] |
| Only GSA-approved services used for credential management | [RULE-02] |
| Only GSA-approved solutions used for access management | [RULE-03] |
| Procurement verification process implemented | [RULE-04] |
| Legacy system remediation completed | [RULE-05] |