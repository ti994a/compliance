# SA-8.14: Least Privilege

**Family:** System and Services Acquisition  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Implement the security design principle of least privilege in systems or system components that implement the security design principle of least privilege are defined;.

## Implementation Guidance
The principle of least privilege states that each system component is allocated sufficient privileges to accomplish its specified functions but no more. Applying the principle of least privilege limits the scope of the component’s actions, which has two desirable effects: the security impact of a failure, corruption, or misuse of the component will have a minimized security impact, and the security analysis of the component will be simplified. Least privilege is a pervasive principle that is reflected in all aspects of the secure system design. Interfaces used to invoke component capability are available to only certain subsets of the user population, and component design supports a sufficiently fine granularity of privilege decomposition. For example, in the case of an audit mechanism, there may be an interface for the audit manager, who configures the audit settings; an interface for the audit operator, who ensures that audit data is safely collected and stored; and, finally, yet another interface for the audit reviewer, who only has need to view the audit data that has been collected but no need to perform operations on that data.  In addition to its manifestations at the system interface, least privilege can be used as a guiding principle for the internal structure of the system itself. One aspect of internal least privilege is to construct modules so that only the elements encapsulated by the module are directly operated on by the functions within the module. Elements external to a module that may be affected by the module’s operation are indirectly accessed through interaction (e.g., via a function call) with the module that contains those elements. Another aspect of internal least privilege is that the scope of a given module or component includes only those system elements that are necessary for its functionality and that the access modes for the elements (e.g., read, write) are minimal.

## Assessment Objectives
systems or system components that implement the security design principle of least privilege are defined; implement the security design principle of least privilege.

## Assessment Methods
System and services acquisition policy  procedures addressing the security design principle of least privilege used in the specification, design, development, implementation, and modification of the system  system design documentation  security and privacy requirements and specifications for the system  system security and privacy architecture  system security plan  other relevant documents or records Organizational personnel with the responsibility for determining system security and privacy requirements  organizational personnel with system specification, design, development, implementation, and modification responsibilities  system developers  organizational personnel with information security responsibilities Organizational processes for applying the security design principle of least privilege in system specification, design, development, implementation, and modification  mechanisms supporting the application of the security design principle of least privilege in system specification, design, development, implementation, and modification

## Related Controls
- ac-6
- cm-7

---
*NIST SP 800-53 Rev 5 Control*
