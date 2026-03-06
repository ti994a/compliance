```markdown
# POLICY: PS-3.4: Citizenship Requirements

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_PS-3.4 |
| NIST Control | PS-3.4: Citizenship Requirements |
| Version | 1.0 |
| Owner | Chief Security Officer |
| Keywords | citizenship, personnel screening, access control, information types, verification |

## 1. POLICY STATEMENT
The organization MUST verify that individuals accessing systems processing, storing, or transmitting classified or controlled information meet defined citizenship requirements. Citizenship verification SHALL be completed before granting system access and documented in personnel records.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Federal employees | YES | All levels requiring system access |
| Contractors | YES | When accessing controlled information |
| Temporary personnel | YES | Including interns and consultants |
| Visitors | CONDITIONAL | Only if granted system access |
| Public cloud systems | YES | When processing controlled information |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Security Officer | • Define citizenship requirements per information type<br>• Maintain approved citizenship verification procedures<br>• Conduct periodic compliance reviews |
| HR Personnel | • Verify citizenship documentation<br>• Maintain personnel screening records<br>• Report citizenship status changes |
| System Owners | • Identify information types requiring citizenship verification<br>• Ensure access controls enforce citizenship requirements<br>• Document system-specific requirements |

## 4. RULES
[RULE-01] Organizations MUST define specific citizenship requirements for each information type processed, stored, or transmitted by their systems.
[VALIDATION] IF information_type = "classified" AND citizenship_requirements = "undefined" THEN critical_violation

[RULE-02] Citizenship verification MUST be completed and documented before granting initial system access to individuals.
[VALIDATION] IF system_access_granted = TRUE AND citizenship_verified = FALSE THEN critical_violation

[RULE-03] Citizenship documentation MUST be verified through primary source documents (passport, birth certificate, naturalization certificate).
[VALIDATION] IF citizenship_verification_method != "primary_source" THEN violation

[RULE-04] Personnel records MUST maintain current citizenship verification status and documentation for all individuals with system access.
[VALIDATION] IF system_access = TRUE AND citizenship_record_current = FALSE THEN violation

[RULE-05] Access controls MUST enforce citizenship requirements automatically where technically feasible.
[VALIDATION] IF citizenship_enforcement = "manual_only" AND technical_controls_available = TRUE THEN moderate_violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Citizenship Verification Process - Standard procedures for verifying and documenting citizenship status
- [PROC-02] Information Type Classification - Process for identifying information requiring citizenship verification
- [PROC-03] Access Control Configuration - Technical implementation of citizenship-based access controls
- [PROC-04] Periodic Review Process - Regular validation of citizenship requirements and compliance

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Every 6 months
- Triggering events: Changes in information classification, new regulatory requirements, security incidents involving citizenship violations

## 7. SCENARIO PATTERNS
[SCENARIO-01: Contractor Access to Classified System]
IF user_type = "contractor"
AND information_type = "classified"
AND citizenship_verified = FALSE
AND access_granted = TRUE
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Dual Citizen Access Review]
IF citizenship_status = "dual_citizen"
AND information_type = "export_controlled"
AND additional_screening_completed = TRUE
AND access_approved_by_security_officer = TRUE
THEN compliance = TRUE

[SCENARIO-03: Expired Citizenship Documentation]
IF citizenship_verification_date < (current_date - 3_years)
AND system_access = "active"
AND reverification_initiated = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Foreign National Emergency Access]
IF user_citizenship = "foreign_national"
AND information_type = "controlled_unclassified"
AND emergency_access = TRUE
AND temporary_authorization_documented = TRUE
AND access_duration <= 72_hours
THEN compliance = TRUE

[SCENARIO-05: Automated Citizenship Enforcement]
IF information_classification = "secret"
AND citizenship_requirements = "us_citizen_only"
AND access_control_enforces_citizenship = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Define citizenship requirements for information types | RULE-01 |
| Verify citizenship before access | RULE-02 |
| Use primary source documentation | RULE-03 |
| Maintain current records | RULE-04 |
| Implement technical controls | RULE-05 |
```