# SA-8.22: Accountability and Traceability

**Family:** System and Services Acquisition  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Implement the security design principle of accountability and traceability in organization-defined systems or system components.

## Implementation Guidance
The principle of accountability and traceability states that it is possible to trace security-relevant actions (i.e., subject-object interactions) to the entity on whose behalf the action is being taken. The principle of accountability and traceability requires a trustworthy infrastructure that can record details about actions that affect system security (e.g., an audit subsystem). To record the details about actions, the system is able to uniquely identify the entity on whose behalf the action is being carried out and also record the relevant sequence of actions that are carried out. The accountability policy also requires that audit trail itself be protected from unauthorized access and modification. The principle of least privilege assists in tracing the actions to particular entities, as it increases the granularity of accountability. Associating specific actions with system entities, and ultimately with users, and making the audit trail secure against unauthorized access and modifications provide non-repudiation because once an action is recorded, it is not possible to change the audit trail. Another important function that accountability and traceability serves is in the routine and forensic analysis of events associated with the violation of security policy. Analysis of audit logs may provide additional information that may be helpful in determining the path or component that allowed the violation of the security policy and the actions of individuals associated with the violation of the security policy.

## Assessment Objectives
systems or system components that implement the security design principle of accountability are defined; implement the security design principle of accountability; systems or system components that implement the security design principle of traceability are defined; implement the security design principle of traceability.

## Assessment Methods
System and services acquisition policy  audit and accountability policy  access control policy  procedures addressing least privilege  procedures addressing auditable events  identification and authentication policy  procedures addressing user identification and authentication  procedures addressing the security design principle of accountability and traceability used in the specification, design, development, implementation, and modification of the system  system design documentation  system audit records  system auditable events  system configuration settings and associated documentation  security and privacy requirements and specifications for the system  system security and privacy architecture  system security plan  other relevant documents or records Organizational personnel with the responsibility for determining system security and privacy requirements  organizational personnel with audit and accountability responsibilities  organizational personnel with system specification, design, development, implementation, and modification responsibilities  system developers  organizational personnel with information security responsibilities Organizational processes for applying the security design principle of accountability and traceability in system specification, design, development, implementation, and modification  mechanisms supporting the application of the security design principle of accountability and traceability in system specification, design, development, implementation, and modification  mechanisms implementing information system auditing  mechanisms implementing least privilege functions

## Related Controls
- ac-6
- au-2
- au-3
- au-6
- au-9
- au-10
- au-12
- ia-2
- ir-4

---
*NIST SP 800-53 Rev 5 Control*
