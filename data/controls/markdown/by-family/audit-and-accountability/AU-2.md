# AU-2: Event Logging

**Family:** Audit and Accountability  
**Class:** SP800-53  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Identify the types of events that the system is capable of logging in support of the audit function: the event types that the system is capable of logging in support of the audit function are defined;; Coordinate the event logging function with other organizational entities requiring audit-related information to guide and inform the selection criteria for events to be logged; Specify the following event types for logging within the system: organization-defined event types (subset of the event types defined in [AU-2a.](#au-2_smt.a)) along with the frequency of (or situation requiring) logging for each identified event type; Provide a rationale for why the event types selected for logging are deemed to be adequate to support after-the-fact investigations of incidents; and Review and update the event types selected for logging the frequency of event types selected for logging are reviewed and updated;.

## Implementation Guidance
An event is an observable occurrence in a system. The types of events that require logging are those events that are significant and relevant to the security of systems and the privacy of individuals. Event logging also supports specific monitoring and auditing needs. Event types include password changes, failed logons or failed accesses related to systems, security or privacy attribute changes, administrative privilege usage, PIV credential usage, data action changes, query parameters, or external credential usage. In determining the set of event types that require logging, organizations consider the monitoring and auditing appropriate for each of the controls to be implemented. For completeness, event logging includes all protocols that are operational and supported by the system.  To balance monitoring and auditing requirements with other system needs, event logging requires identifying the subset of event types that are logged at a given point in time. For example, organizations may determine that systems need the capability to log every file access successful and unsuccessful, but not activate that capability except for specific circumstances due to the potential burden on system performance. The types of events that organizations desire to be logged may change. Reviewing and updating the set of logged events is necessary to help ensure that the events remain relevant and continue to support the needs of the organization. Organizations consider how the types of logging events can reveal information about individuals that may give rise to privacy risk and how best to mitigate such risks. For example, there is the potential to reveal personally identifiable information in the audit trail, especially if the logging event is based on patterns or time of usage.  Event logging requirements, including the need to log specific event types, may be referenced in other controls and control enhancements. These include [AC-2(4)](#ac-2.4), [AC-3(10)](#ac-3.10), [AC-6(9)](#ac-6.9), [AC-17(1)](#ac-17.1), [CM-3f](#cm-3_smt.f), [CM-5(1)](#cm-5.1), [IA-3(3)(b)](#ia-3.3_smt.b), [MA-4(1)](#ma-4.1), [MP-4(2)](#mp-4.2), [PE-3](#pe-3), [PM-21](#pm-21), [PT-7](#pt-7), [RA-8](#ra-8), [SC-7(9)](#sc-7.9), [SC-7(15)](#sc-7.15), [SI-3(8)](#si-3.8), [SI-4(22)](#si-4.22), [SI-7(8)](#si-7.8) , and [SI-10(1)](#si-10.1) . Organizations include event types that are required by applicable laws, executive orders, directives, policies, regulations, standards, and guidelines. Audit records can be generated at various levels, including at the packet level as information traverses the network. Selecting the appropriate level of event logging is an important part of a monitoring and auditing capability and can identify the root causes of problems. When defining event types, organizations consider the logging necessary to cover related event types, such as the steps in distributed, transaction-based processes and the actions that occur in service-oriented architectures.

## Assessment Objectives
the event types that the system is capable of logging in support of the audit function are defined; that the system is capable of logging are identified in support of the audit logging function; the event logging function is coordinated with other organizational entities requiring audit-related information to guide and inform the selection criteria for events to be logged; the event types (subset of AU-02_ODP[01]) for logging within the system are defined; are specified for logging within the system; the specified event types are logged within the system the frequency or situation requiring logging for each specified event type is defined;; a rationale is provided for why the event types selected for logging are deemed to be adequate to support after-the-fact investigations of incidents; the event types selected for logging are reviewed and updated the frequency of event types selected for logging are reviewed and updated;.

## Assessment Methods
Audit and accountability policy  procedures addressing auditable events  system security plan  privacy plan  system design documentation  system configuration settings and associated documentation  system audit records  system auditable events  other relevant documents or records Organizational personnel with audit and accountability responsibilities  organizational personnel with information security and privacy responsibilities  system/network administrators Mechanisms implementing system auditing

## Related Controls
- ac-2
- ac-3
- ac-6
- ac-7
- ac-8
- ac-16
- ac-17
- au-3
- au-4
- au-5
- au-6
- au-7
- au-11
- au-12
- cm-3
- cm-5
- cm-6
- cm-13
- ia-3
- ma-4
- mp-4
- pe-3
- pm-21
- pt-2
- pt-7
- ra-8
- sa-8
- sc-7
- sc-18
- si-3
- si-4
- si-7
- si-10
- si-11

---
*NIST SP 800-53 Rev 5 Control*
