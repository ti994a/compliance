# SA-8.20: Secure Metadata Management

**Family:** System and Services Acquisition  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Implement the security design principle of secure metadata management in systems or system components that implement the security design principle of secure metadata management are defined;.

## Implementation Guidance
The principle of secure metadata management states that metadata are "first class" objects with respect to security policy when the policy requires either complete protection of information or that the security subsystem be self-protecting. The principle of secure metadata management is driven by the recognition that a system, subsystem, or component cannot achieve self-protection unless it protects the data it relies on for correct execution. Data is generally not interpreted by the system that stores it. It may have semantic value (i.e., it comprises information) to users and programs that process the data. In contrast, metadata is information about data, such as a file name or the date when the file was created. Metadata is bound to the target data that it describes in a way that the system can interpret, but it need not be stored inside of or proximate to its target data. There may be metadata whose target is itself metadata (e.g., the classification level or impact level of a file name), including self-referential metadata.  The apparent secondary nature of metadata can lead to neglect of its legitimate need for protection, resulting in a violation of the security policy that includes the exfiltration of information. A particular concern associated with insufficient protections for metadata is associated with multilevel secure (MLS) systems. MLS systems mediate access by a subject to an object based on relative sensitivity levels. It follows that all subjects and objects in the scope of control of the MLS system are either directly labeled or indirectly attributed with sensitivity levels. The corollary of labeled metadata for MLS systems states that objects containing metadata are labeled. As with protection needs assessments for data, attention is given to ensure that the confidentiality and integrity protections are individually assessed, specified, and allocated to metadata, as would be done for mission, business, and system data.

## Assessment Objectives
systems or system components that implement the security design principle of secure metadata management are defined; implement the security design principle of secure metadata management.

## Assessment Methods
System and services acquisition policy  procedures addressing the security design principle of metadata management used in the specification, design, development, implementation, and modification of the system  system design documentation  security and privacy requirements and specifications for the system  system security and privacy architecture  system security plan  other relevant documents or records Organizational personnel with the responsibility for determining system security and privacy requirements  organizational personnel with system specification, design, development, implementation, and modification responsibilities  system developers  organizational personnel with information security responsibilities Organizational processes for applying the security design principle of metadata management in system specification, design, development, implementation, and modification  mechanisms supporting the application of the security design principle of metadata management in system specification, design, development, implementation, and modification

## Related Controls


---
*NIST SP 800-53 Rev 5 Control*
