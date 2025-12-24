# AC-4.26: Audit Filtering Actions

**Family:** Access Control  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
When transferring information between different security domains, record and audit content filtering actions and results for the information being filtered.

## Implementation Guidance
Content filtering is the process of inspecting information as it traverses a cross-domain solution and determines if the information meets a predefined policy. Content filtering actions and the results of filtering actions are recorded for individual messages to ensure that the correct filter actions were applied. Content filter reports are used to assist in troubleshooting actions by, for example, determining why message content was modified and/or why it failed the filtering process. Audit events are defined in [AU-2](#au-2) . Audit records are generated in [AU-12](#au-12).

## Assessment Objectives
when transferring information between different security domains, content-filtering actions are recorded and audited; when transferring information between different security domains, results for the information being filtered are recorded and audited.

## Assessment Methods
Information flow enforcement policy  procedures addressing information flow enforcement  system design documentation  system configuration settings and associated documentation  system audit records  system security plan  other relevant documents or records Organizational personnel with information flow enforcement responsibilities  system/network administrators  organizational personnel with information security responsibilities Mechanisms implementing information flow enforcement functions  mechanisms implementing content filtering  mechanisms recording and auditing content filtering

## Related Controls
- au-2
- au-3
- au-12

---
*NIST SP 800-53 Rev 5 Control*
