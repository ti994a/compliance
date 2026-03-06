# POLICY: SR-10: Inspection of Systems or Components

## METADATA
| Field | Value |
|-------|-------|
| Policy ID | POL_SR-10 |
| NIST Control | SR-10: Inspection of Systems or Components |
| Version | 1.0 |
| Owner | Chief Supply Chain Officer |
| Keywords | inspection, tampering, supply chain, components, random inspection |

## 1. POLICY STATEMENT
The organization SHALL conduct random inspections of designated systems and system components to detect physical and logical tampering. Inspections MUST be performed on systems or components that have been outside organizational control or present elevated supply chain risks.

## 2. SCOPE
| Entity | In Scope | Notes |
|--------|----------|-------|
| IT Systems | YES | All production and non-production systems |
| Network Components | YES | Routers, switches, firewalls, security appliances |
| Hardware Components | YES | Servers, workstations, mobile devices |
| Third-party Components | YES | Vendor-supplied hardware and software |
| Cloud Services | CONDITIONAL | When organization has inspection access |

## 3. KEY ROLES
| Role | Key Responsibilities |
|------|---------------------|
| Supply Chain Risk Manager | • Define inspection requirements and schedules<br>• Oversee inspection program execution<br>• Maintain inspection documentation |
| IT Security Team | • Conduct technical inspections<br>• Analyze inspection results<br>• Report tampering indicators |
| Procurement Team | • Identify high-risk acquisitions<br>• Coordinate vendor inspections<br>• Maintain supplier risk profiles |

## 4. RULES

**[RULE-01]** Organizations MUST define specific systems and system components that require inspection based on risk assessment and supply chain analysis.
**[VALIDATION]** IF inspection_requirements_defined = FALSE THEN violation

**[RULE-02]** Random inspections MUST be conducted on defined systems and components with frequency determined by risk level but not less than annually for high-risk components.
**[VALIDATION]** IF component_risk = "high" AND last_inspection > 365_days THEN violation

**[RULE-03]** Inspections MUST be performed when components return from high-risk locations, change suppliers, or show packaging anomalies.
**[VALIDATION]** IF (high_risk_travel = TRUE OR supplier_change = TRUE OR packaging_anomaly = TRUE) AND inspection_completed = FALSE THEN violation

**[RULE-04]** Inspection procedures MUST include both physical examination for tampering evidence and logical analysis for unauthorized modifications.
**[VALIDATION]** IF inspection_type NOT IN ["physical", "logical"] OR inspection_scope = "incomplete" THEN violation

**[RULE-05]** All inspection activities MUST be documented with findings, methodology, and follow-up actions within 48 hours of completion.
**[VALIDATION]** IF inspection_completed = TRUE AND documentation_time > 48_hours THEN violation

**[RULE-06]** Components showing evidence of tampering MUST be immediately quarantined and subject to detailed forensic analysis.
**[VALIDATION]** IF tampering_detected = TRUE AND quarantine_status = FALSE THEN critical_violation

## 5. REQUIRED PROCEDURES
- **[PROC-01]** Component Risk Assessment - Classify components requiring inspection based on criticality and supply chain risk
- **[PROC-02]** Random Inspection Scheduling - Generate unpredictable inspection schedules using approved randomization methods
- **[PROC-03]** Physical Tampering Detection - Examine components for physical evidence of unauthorized access or modification
- **[PROC-04]** Logical Integrity Verification - Validate software, firmware, and configuration integrity using cryptographic methods
- **[PROC-05]** Incident Response for Tampering - Respond to confirmed or suspected tampering incidents

## 6. REVIEW REQUIREMENTS
- Policy review frequency: Annually
- Procedure review frequency: Semi-annually
- Triggering events: Supply chain incidents, new threat intelligence, regulatory changes, significant vendor changes

## 7. SCENARIO PATTERNS

**[SCENARIO-01: High-Risk Component Inspection]**
IF component_risk_level = "high"
AND last_inspection_date > 365_days
AND inspection_scheduled = FALSE
THEN compliance = FALSE
violation_severity = "Moderate"

**[SCENARIO-02: Post-Travel Inspection]**
IF component_travel_location = "high_risk_country"
AND return_date < current_date
AND post_travel_inspection = FALSE
AND days_since_return > 5
THEN compliance = FALSE
violation_severity = "High"

**[SCENARIO-03: Tampering Detection Response]**
IF inspection_result = "tampering_detected"
AND quarantine_initiated = TRUE
AND forensic_analysis_started = TRUE
AND incident_reported = TRUE
THEN compliance = TRUE

**[SCENARIO-04: Vendor Change Inspection]**
IF supplier_changed = TRUE
AND component_received = TRUE
AND pre_deployment_inspection = FALSE
THEN compliance = FALSE
violation_severity = "High"

**[SCENARIO-05: Documentation Compliance]**
IF inspection_completed = TRUE
AND inspection_date = "2024-01-15"
AND documentation_date > "2024-01-17"
THEN compliance = FALSE
violation_severity = "Low"

## 8. COMPLIANCE MAPPING
| Requirement | Rule Reference |
|-------------|---------------|
| Systems or system components that require inspection are defined | RULE-01 |
| Components are inspected at random to detect tampering | RULE-02, RULE-03 |
| Inspection addresses physical and logical tampering | RULE-04 |
| Inspections documented and tracked | RULE-05 |
| Tampering incidents properly handled | RULE-06 |