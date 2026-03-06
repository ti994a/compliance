# POLICY: IA-5.17: Presentation Attack Detection for Biometric Authenticators

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_IA-5.17 |
| NIST Control | IA-5.17: Presentation Attack Detection for Biometric Authenticators |
| Version | 1.0 |
| Owner | Chief Information Security Officer |
| Keywords | biometric, authentication, presentation attack, liveness detection, spoofing |

## 1. POLICY STATEMENT
All biometric authentication systems MUST implement presentation attack detection mechanisms to prevent spoofing attacks using fake biometric artifacts. These mechanisms SHALL include liveness detection capabilities to verify the authenticity of biometric samples during authentication processes.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| Biometric authentication systems | YES | All systems using fingerprint, facial, iris, or voice recognition |
| Mobile device biometric unlock | YES | Corporate-managed devices with biometric capabilities |
| Physical access control systems | YES | Biometric door locks and facility access points |
| Legacy authentication systems | NO | Systems using only passwords or tokens |
| Third-party biometric services | YES | When integrated with corporate systems |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| CISO | • Approve biometric system implementations<br>• Ensure policy compliance across organization<br>• Review presentation attack incidents |
| Identity and Access Management Team | • Configure presentation attack detection settings<br>• Monitor biometric authentication failures<br>• Maintain biometric system security baselines |
| System Administrators | • Deploy and maintain biometric systems<br>• Implement liveness detection mechanisms<br>• Report presentation attack attempts |

## 4. RULES
[RULE-01] All biometric authentication systems MUST implement presentation attack detection mechanisms before deployment to production environments.
[VALIDATION] IF biometric_system = "deployed" AND presentation_attack_detection = FALSE THEN critical_violation

[RULE-02] Liveness detection capabilities SHALL be enabled and configured to detect spoofing attempts using photographs, videos, silicone molds, or other artificial artifacts.
[VALIDATION] IF liveness_detection_enabled = FALSE AND biometric_type IN ["facial", "fingerprint", "iris"] THEN violation

[RULE-03] Presentation attack detection systems MUST log all suspected spoofing attempts and generate security alerts for investigation within 15 minutes.
[VALIDATION] IF suspected_attack_detected = TRUE AND alert_generated = FALSE THEN violation
[VALIDATION] IF suspected_attack_detected = TRUE AND alert_time > 15_minutes THEN violation

[RULE-04] Biometric systems SHALL reject authentication attempts when presentation attack detection mechanisms identify potential spoofing with confidence scores below the established threshold.
[VALIDATION] IF spoofing_confidence_score < threshold AND authentication_granted = TRUE THEN critical_violation

[RULE-05] Presentation attack detection mechanisms MUST be tested quarterly using known spoofing techniques to validate effectiveness.
[VALIDATION] IF last_spoofing_test > 90_days THEN violation

## 5. REQUIRED PROCEDURES
- [PROC-01] Biometric System Assessment - Evaluate presentation attack detection capabilities before procurement
- [PROC-02] Liveness Detection Configuration - Configure and tune detection sensitivity settings
- [PROC-03] Spoofing Incident Response - Investigate and respond to presentation attack attempts
- [PROC-04] Quarterly Security Testing - Test systems against known presentation attack methods

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Security incidents, new biometric technologies, failed spoofing tests

## 7. SCENARIO PATTERNS
[SCENARIO-01: Facial Recognition Without Liveness Detection]
IF biometric_type = "facial_recognition"
AND liveness_detection = FALSE
AND system_status = "production"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-02: Delayed Spoofing Alert]
IF presentation_attack_detected = TRUE
AND alert_generation_time = 25_minutes
AND system_operational = TRUE
THEN compliance = FALSE
violation_severity = "Moderate"

[SCENARIO-03: Overdue Spoofing Test]
IF last_presentation_attack_test > 95_days
AND biometric_system_active = TRUE
AND no_approved_exception = TRUE
THEN compliance = FALSE
violation_severity = "Low"

[SCENARIO-04: Authentication Despite Detection]
IF spoofing_confidence_score = 0.2
AND detection_threshold = 0.7
AND authentication_result = "SUCCESS"
THEN compliance = FALSE
violation_severity = "Critical"

[SCENARIO-05: Compliant Mobile Device Implementation]
IF device_type = "corporate_mobile"
AND biometric_type = "fingerprint"
AND liveness_detection = TRUE
AND presentation_attack_detection = TRUE
THEN compliance = TRUE

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Presentation attack detection mechanisms are employed for biometric-based authentication | RULE-01, RULE-02 |
| Detection mechanisms prevent spoofing attacks | RULE-04 |
| Security monitoring and alerting | RULE-03 |
| Regular effectiveness validation | RULE-05 |