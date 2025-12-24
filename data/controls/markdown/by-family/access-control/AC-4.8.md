# AC-4.8: Security and Privacy Policy Filters

**Family:** Access Control  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Enforce information flow control using organization-defined security or privacy policy filters as a basis for flow control decisions for organization-defined information flows ; and block data after a filter processing failure in accordance with organization-defined security or privacy policy.

## Implementation Guidance
Organization-defined security or privacy policy filters can address data structures and content. For example, security or privacy policy filters for data structures can check for maximum file lengths, maximum field sizes, and data/file types (for structured and unstructured data). Security or privacy policy filters for data content can check for specific words, enumerated values or data value ranges, and hidden content. Structured data permits the interpretation of data content by applications. Unstructured data refers to digital information without a data structure or with a data structure that does not facilitate the development of rule sets to address the impact or classification level of the information conveyed by the data or the flow enforcement decisions. Unstructured data consists of bitmap objects that are inherently non-language-based (i.e., image, video, or audio files) and textual objects that are based on written or printed languages. Organizations can implement more than one security or privacy policy filter to meet information flow control objectives.

## Assessment Objectives
information flow control is enforced using security policy filters used as a basis for enforcing information flow control are defined; as a basis for flow control decisions for information flows for which information flow control is enforced by security filters are defined;; information flow control is enforced using privacy policy filters used as a basis for enforcing information flow control are defined; as a basis for flow control decisions for information flows for which information flow control is enforced by privacy filters are defined;; block data after a filter processing failure in accordance with security policy identifying actions taken after a filter processing failure are defined;;  block data after a filter processing failure in accordance with privacy policy identifying actions taken after a filter processing failure are defined;.

## Assessment Methods
Access control policy  information flow control policies  procedures addressing information flow enforcement  system design documentation  system configuration settings and associated documentation  list of security policy filters regulating flow control decisions  list of privacy policy filters regulating flow control decisions  system audit records  system security plan  privacy plan  other relevant documents or records System/network administrators  organizational personnel with information security and privacy responsibilities  system developers Mechanisms implementing information flow enforcement policy  security and privacy policy filters

## Related Controls


---
*NIST SP 800-53 Rev 5 Control*
