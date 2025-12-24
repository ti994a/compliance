# AU-5: Response to Audit Logging Process Failures

**Family:** Audit and Accountability  
**Class:** SP800-53  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Alert personnel or roles receiving audit logging process failure alerts are defined; within time period for personnel or roles receiving audit logging process failure alerts is defined; in the event of an audit logging process failure; and Take the following additional actions: additional actions taken in the event of an audit logging process failure are defined;.

## Implementation Guidance
Audit logging process failures include software and hardware errors, failures in audit log capturing mechanisms, and reaching or exceeding audit log storage capacity. Organization-defined actions include overwriting oldest audit records, shutting down the system, and stopping the generation of audit records. Organizations may choose to define additional actions for audit logging process failures based on the type of failure, the location of the failure, the severity of the failure, or a combination of such factors. When the audit logging process failure is related to storage, the response is carried out for the audit log storage repository (i.e., the distinct system component where the audit logs are stored), the system on which the audit logs reside, the total audit log storage capacity of the organization (i.e., all audit log storage repositories combined), or all three. Organizations may decide to take no additional actions after alerting designated roles or personnel.

## Assessment Objectives
personnel or roles receiving audit logging process failure alerts are defined; are alerted in the event of an audit logging process failure within time period for personnel or roles receiving audit logging process failure alerts is defined;; additional actions taken in the event of an audit logging process failure are defined; are taken in the event of an audit logging process failure.

## Assessment Methods
Audit and accountability policy  procedures addressing response to audit processing failures  system design documentation  system security plan  privacy plan  system configuration settings and associated documentation  list of personnel to be notified in case of an audit processing failure  system audit records  other relevant documents or records Organizational personnel with audit and accountability responsibilities  organizational personnel with information security and privacy responsibilities  system/network administrators  system developers Mechanisms implementing system response to audit processing failures

## Related Controls
- au-2
- au-4
- au-7
- au-9
- au-11
- au-12
- au-14
- si-4
- si-12

---
*NIST SP 800-53 Rev 5 Control*
