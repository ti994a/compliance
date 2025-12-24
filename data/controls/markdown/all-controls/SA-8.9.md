# SA-8.9: Trusted Components

**Family:** System and Services Acquisition  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Implement the security design principle of trusted components in systems or system components that implement the security design principle of trusted components are defined;.

## Implementation Guidance
The principle of trusted components states that a component is trustworthy to at least a level commensurate with the security dependencies it supports (i.e., how much it is trusted to perform its security functions by other components). This principle enables the composition of components such that trustworthiness is not inadvertently diminished and the trust is not consequently misplaced. Ultimately, this principle demands some metric by which the trust in a component and the trustworthiness of a component can be measured on the same abstract scale. The principle of trusted components is particularly relevant when considering systems and components in which there are complex chains of trust dependencies. A trust dependency is also referred to as a trust relationship and there may be chains of trust relationships.  The principle of trusted components also applies to a compound component that consists of subcomponents (e.g., a subsystem), which may have varying levels of trustworthiness. The conservative assumption is that the trustworthiness of a compound component is that of its least trustworthy subcomponent. It may be possible to provide a security engineering rationale that the trustworthiness of a particular compound component is greater than the conservative assumption. However, any such rationale reflects logical reasoning based on a clear statement of the trustworthiness objectives as well as relevant and credible evidence. The trustworthiness of a compound component is not the same as increased application of defense-in-depth layering within the component or a replication of components. Defense-in-depth techniques do not increase the trustworthiness of the whole above that of the least trustworthy component.

## Assessment Objectives
systems or system components that implement the security design principle of trusted components are defined; implement the security design principle of trusted components.

## Assessment Methods
Supply chain risk management plan  system and services acquisition policy  procedures addressing the security design principle of trusted components used in the specification, design, development, implementation, and modification of the system  system design documentation  security, supply chain risk management, and privacy requirements and specifications for the system  system security and privacy architecture  procedures for determining component assurance  system security plan  other relevant documents or records Organizational personnel with the responsibility for determining system security and privacy requirements  organizational personnel with system specification, design, development, implementation, and modification responsibilities  system developers  organizational personnel with information security responsibilities  organizational personnel with supply chain risk management responsibilities Organizational processes for applying the security design principle of trusted components in system specification, design, development, implementation, and modification  mechanisms supporting the application of the security design principle of trusted components in system specification, design, development, implementation, and modification

## Related Controls


---
*NIST SP 800-53 Rev 5 Control*
