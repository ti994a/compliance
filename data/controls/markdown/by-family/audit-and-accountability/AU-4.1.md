# AU-4.1: Transfer to Alternate Storage

**Family:** Audit and Accountability  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Transfer audit logs the frequency of audit logs transferred to a different system, system component, or media other than the system or system component conducting the logging is defined; to a different system, system component, or media other than the system or system component conducting the logging.

## Implementation Guidance
Audit log transfer, also known as off-loading, is a common process in systems with limited audit log storage capacity and thus supports availability of the audit logs. The initial audit log storage is only used in a transitory fashion until the system can communicate with the secondary or alternate system allocated to audit log storage, at which point the audit logs are transferred. Transferring audit logs to alternate storage is similar to [AU-9(2)](#au-9.2) in that audit logs are transferred to a different entity. However, the purpose of selecting [AU-9(2)](#au-9.2) is to protect the confidentiality and integrity of audit records. Organizations can select either control enhancement to obtain the benefit of increased audit log storage capacity and preserving the confidentiality, integrity, and availability of audit records and logs.

## Assessment Objectives
audit logs are transferred the frequency of audit logs transferred to a different system, system component, or media other than the system or system component conducting the logging is defined; to a different system, system component, or media other than the system or system component conducting the logging.

## Assessment Methods
Audit and accountability policy  system security plan  privacy plan  procedures addressing audit storage capacity  procedures addressing transfer of system audit records to secondary or alternate systems  system design documentation  system configuration settings and associated documentation  logs of audit record transfers to secondary or alternate systems  system audit records transferred to secondary or alternate systems  other relevant documents or records Organizational personnel with audit storage capacity planning responsibilities  organizational personnel with information security and privacy responsibilities  system/network administrators Mechanisms supporting the transfer of audit records onto a different system

## Related Controls


---
*NIST SP 800-53 Rev 5 Control*
