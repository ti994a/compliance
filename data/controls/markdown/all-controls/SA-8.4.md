# SA-8.4: Partially Ordered Dependencies

**Family:** System and Services Acquisition  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Implement the security design principle of partially ordered dependencies in systems or system components that implement the security design principle of partially ordered dependencies are defined;.

## Implementation Guidance
The principle of partially ordered dependencies states that the synchronization, calling, and other dependencies in the system are partially ordered. A fundamental concept in system design is layering, whereby the system is organized into well-defined, functionally related modules or components. The layers are linearly ordered with respect to inter-layer dependencies, such that higher layers are dependent on lower layers. While providing functionality to higher layers, some layers can be self-contained and not dependent on lower layers. While a partial ordering of all functions in a given system may not be possible, if circular dependencies are constrained to occur within layers, the inherent problems of circularity can be more easily managed. Partially ordered dependencies and system layering contribute significantly to the simplicity and coherency of the system design. Partially ordered dependencies also facilitate system testing and analysis.

## Assessment Objectives
systems or system components that implement the security design principle of partially ordered dependencies are defined; implement the security design principle of partially ordered dependencies.

## Assessment Methods
System and services acquisition policy  procedures addressing the security design principle of partially ordered dependencies used in the specification, design, development, implementation, and modification of the system  system design documentation  security and privacy requirements and specifications for the system  system security and privacy architecture  system security plan  other relevant documents or records Organizational personnel with the responsibility for determining system security and privacy requirements  organizational personnel with system specification, design, development, implementation, and modification responsibilities  system developers  organizational personnel with information security responsibilities Organizational processes for applying the security design principle of partially ordered dependencies in system specification, design, development, implementation, and modification  mechanisms supporting the application of the security design principle of partially ordered dependencies in system specification, design, development, implementation, and modification

## Related Controls


---
*NIST SP 800-53 Rev 5 Control*
