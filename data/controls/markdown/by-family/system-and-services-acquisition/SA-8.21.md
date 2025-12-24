# SA-8.21: Self-analysis

**Family:** System and Services Acquisition  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Implement the security design principle of self-analysis in systems or system components that implement the security design principle of self-analysis are defined;.

## Implementation Guidance
The principle of self-analysis states that a system component is able to assess its internal state and functionality to a limited extent at various stages of execution, and that this self-analysis capability is commensurate with the level of trustworthiness invested in the system. At the system level, self-analysis can be achieved through hierarchical assessments of trustworthiness established in a bottom-up fashion. In this approach, the lower-level components check for data integrity and correct functionality (to a limited extent) of higher-level components. For example, trusted boot sequences involve a trusted lower-level component that attests to the trustworthiness of the next higher-level components so that a transitive chain of trust can be established. At the root, a component attests to itself, which usually involves an axiomatic or environmentally enforced assumption about its integrity. Results of the self-analyses can be used to guard against externally induced errors, internal malfunction, or transient errors. By following this principle, some simple malfunctions or errors can be detected without allowing the effects of the error or malfunction to propagate outside of the component. Further, the self-test can be used to attest to the configuration of the component, detecting any potential conflicts in configuration with respect to the expected configuration.

## Assessment Objectives
systems or system components that implement the security design principle of self-analysis are defined; implement the security design principle of self-analysis.

## Assessment Methods
System and services acquisition policy  procedures addressing the security design principle of self-analysis used in the specification, design, development, implementation, and modification of the system  system design documentation  security and privacy requirements and specifications for the system  system security and privacy architecture  system security plan  other relevant documents or records Organizational personnel with the responsibility for determining system security and privacy requirements  organizational personnel with system specification, design, development, implementation, and modification responsibilities  system developers  organizational personnel with information security responsibilities Organizational processes for applying the security design principle of self-analysis in system specification, design, development, implementation, and modification  mechanisms supporting the application of the security design principle of self-analysis in system specification, design, development, implementation, and modification

## Related Controls
- ca-7

---
*NIST SP 800-53 Rev 5 Control*
