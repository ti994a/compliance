# POLICY: IA-12.5: Address Confirmation

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-12.5 |
| NIST Control | IA-12.5: Address Confirmation |
| Version | 1.0 |
| Owner | Identity and Access Management Team |
| Keywords | address confirmation, out-of-band, registration code, identity proofing, verification |

## 1. POLICY STATEMENT
All user registration processes MUST deliver verification codes through out-of-band channels to confirm the user's address of record before completing identity proofing. Address confirmation prevents adversaries from impersonating legitimate users during the registration process by validating physical or digital addresses from authoritative records.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| All user registration systems | YES | Includes employee, contractor, and customer onboarding |
| Identity proofing processes | YES | All systems requiring identity verification |
| Self-service account creation | YES | Must implement out-of-band confirmation |
| Guest/temporary accounts | CONDITIONAL | Only if requiring formal identity proofing |
| Emergency access procedures | CONDITIONAL | Must document alternative verification methods |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Identity and Access Management Team | • Design and implement out-of-band confirmation processes<br>• Maintain address record validation procedures<br>• Monitor confirmation delivery success rates |
| System Administrators | • Configure systems to enforce out-of-band confirmation<br>• Ensure secure delivery channel implementation<br>• Log all confirmation attempts and outcomes |
| Security Operations | • Monitor for confirmation bypass attempts<br>• Investigate failed confirmation patterns<br>• Validate out-of-band channel security |

## 4. RULES

[RULE-01] Registration codes MUST be delivered through out-of-band channels separate from the primary registration channel.
[VALIDATION] IF registration_code_delivery_channel = primary_registration_channel THEN violation

[RULE-02] User addresses (physical or digital) MUST be obtained from authoritative records and SHALL NOT be self-asserted during registration.
[VALIDATION] IF address_source = "user_provided" AND address_verified_from_records = FALSE THEN violation

[RULE-03] Registration codes MUST expire within 24 hours of generation and SHALL NOT be reusable.
[VALIDATION] IF code_age > 24_hours OR code_usage_count > 1 THEN violation

[RULE-04] Out-of-band confirmation MUST be completed before granting any system access privileges.
[VALIDATION] IF user_access_granted = TRUE AND address_confirmation_status != "completed" THEN critical_violation

[RULE-05] Failed confirmation attempts exceeding 3 tries within 24 hours MUST trigger security review.
[VALIDATION] IF failed_confirmation_attempts > 3 AND timeframe <= 24_hours THEN security_review_required

[RULE-06] Alternative confirmation methods for inaccessible addresses MUST be documented and approved by security team.
[VALIDATION] IF alternative_method_used = TRUE AND security_approval_documented = FALSE THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Out-of-Band Code Generation - Secure generation and delivery of registration codes
- [PROC-02] Address Record Validation - Verification of addresses against authoritative sources
- [PROC-03] Confirmation Failure Investigation - Process for investigating failed confirmation attempts
- [PROC-04] Emergency Confirmation Override - Documented process for emergency access scenarios

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents involving identity fraud, changes to registration systems, regulatory updates

## 7. SCENARIO PATTERNS

[SCENARIO-01: Standard Email Confirmation]
IF registration_channel = "web_portal"
AND confirmation_delivery_channel = "email"
AND email_address_source = "HR_records"
AND code_delivered_within_15_minutes = TRUE
THEN compliance = TRUE

[SCENARIO-02: Self-Asserted Address Usage]
IF address_source = "user_input"
AND address_verification_from_records = FALSE
AND registration_completed = TRUE
THEN compliance = FALSE
violation_severity = "High"

[SCENARIO-03: Same Channel Delivery]
IF registration_channel = "mobile_app"
AND confirmation_delivery_channel = "mobile_app_notification"
AND no_alternative_channel_used = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-04: Expired Code Usage]
IF registration_code_age > 24_hours
AND code_accepted_for_confirmation = TRUE
AND registration_completed = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-05: Emergency Override Process]
IF address_inaccessible = TRUE
AND alternative_method_used = TRUE
AND security_team_approval = TRUE
AND override_documented = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Registration code delivered through out-of-band channel | [RULE-01] |
| User address verification from records | [RULE-02] |
| Address confirmation before access grant | [RULE-04] |
| Secure code lifecycle management | [RULE-03] |
| Failed attempt monitoring | [RULE-05] |