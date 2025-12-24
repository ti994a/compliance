# AU-6.8: Full Text Analysis of Privileged Commands

**Family:** Audit and Accountability  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Perform a full text analysis of logged privileged commands in a physically distinct component or subsystem of the system, or other system that is dedicated to that analysis.

## Implementation Guidance
Full text analysis of privileged commands requires a distinct environment for the analysis of audit record information related to privileged users without compromising such information on the system where the users have elevated privileges, including the capability to execute privileged commands. Full text analysis refers to analysis that considers the full text of privileged commands (i.e., commands and parameters) as opposed to analysis that considers only the name of the command. Full text analysis includes the use of pattern matching and heuristics.

## Assessment Objectives
a full text analysis of logged privileged commands in a physically distinct component or subsystem of the system or other system that is dedicated to that analysis is performed.

## Assessment Methods
Audit and accountability policy  procedures addressing audit review, analysis, and reporting  system design documentation  system configuration settings and associated documentation  text analysis tools and techniques  text analysis documentation of audited privileged commands  system security plan  privacy plan  other relevant documents or records Organizational personnel with audit review, analysis, and reporting responsibilities  organizational personnel with information security and privacy responsibilities Mechanisms implementing the capability to perform a full text analysis of audited privilege commands

## Related Controls
- au-3
- au-9
- au-11
- au-12

---
*NIST SP 800-53 Rev 5 Control*
