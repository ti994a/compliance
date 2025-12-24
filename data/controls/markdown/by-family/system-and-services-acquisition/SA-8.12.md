# SA-8.12: Hierarchical Protection

**Family:** System and Services Acquisition  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Implement the security design principle of hierarchical protection in systems or system components that implement the security design principle of hierarchical protection are defined;.

## Implementation Guidance
The principle of hierarchical protection states that a component need not be protected from more trustworthy components. In the degenerate case of the most trusted component, it protects itself from all other components. For example, if an operating system kernel is deemed the most trustworthy component in a system, then it protects itself from all untrusted applications it supports, but the applications, conversely, do not need to protect themselves from the kernel. The trustworthiness of users is a consideration for applying the principle of hierarchical protection. A trusted system need not protect itself from an equally trustworthy user, reflecting use of untrusted systems in "system high" environments where users are highly trustworthy and where other protections are put in place to bound and protect the "system high" execution environment.

## Assessment Objectives
systems or system components that implement the security design principle of hierarchical protection are defined; implement the security design principle of hierarchical protection.

## Assessment Methods
System and services acquisition policy  procedures addressing the security design principle of hierarchical protection used in the specification, design, development, implementation, and modification of the system  system design documentation  security and privacy requirements and specifications for the system  system security and privacy architecture  system security plan  other relevant documents or records Organizational personnel with the responsibility for determining system security and privacy requirements  organizational personnel with system specification, design, development, implementation, and modification responsibilities  system developers  organizational personnel with information security responsibilities Organizational processes for applying the security design principle of hierarchical protection in system specification, design, development, implementation, and modification  mechanisms supporting the application of the security design principle of hierarchical protection in system specification, design, development, implementation, and modification

## Related Controls


---
*NIST SP 800-53 Rev 5 Control*
