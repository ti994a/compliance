# AC-4.1: Object Security and Privacy Attributes

**Family:** Access Control  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Use organization-defined security and privacy attributes associated with organization-defined information, source, and destination objects to enforce information flow control policies as a basis for enforcement of flow control decisions are defined; as a basis for flow control decisions.

## Implementation Guidance
Information flow enforcement mechanisms compare security and privacy attributes associated with information (i.e., data content and structure) and source and destination objects and respond appropriately when the enforcement mechanisms encounter information flows not explicitly allowed by information flow policies. For example, an information object labeled Secret would be allowed to flow to a destination object labeled Secret, but an information object labeled Top Secret would not be allowed to flow to a destination object labeled Secret. A dataset of personally identifiable information may be tagged with restrictions against combining with other types of datasets and, thus, would not be allowed to flow to the restricted dataset. Security and privacy attributes can also include source and destination addresses employed in traffic filter firewalls. Flow enforcement using explicit security or privacy attributes can be used, for example, to control the release of certain types of information.

## Assessment Objectives
security attributes associated with information, source, and destination objects are defined; associated with information objects associated with information security attributes are defined;, source objects associated with information security attributes are defined; , and destination objects associated with information security attributes are defined; are used to enforce information flow control policies as a basis for enforcement of flow control decisions are defined; as a basis for flow control decisions; privacy attributes associated with information, source, and destination objects are defined; associated with information objects associated with privacy attributes are defined;, source objects associated with privacy attributes are defined; , and destination objects associated with privacy attributes are defined; are used to enforce information flow control policies as a basis for enforcement of flow control decisions are defined; as a basis for flow control decisions.

## Assessment Methods
Access control policy  information flow control policies  procedures addressing information flow enforcement  system design documentation  system configuration settings and associated documentation  list of security and privacy attributes and associated source and destination objects  system audit records  system security plan  privacy plan  other relevant documents or records System/network administrators  organizational personnel with information security responsibilities  organizational personnel with privacy responsibilities  system developers Mechanisms implementing information flow enforcement policy

## Related Controls


---
*NIST SP 800-53 Rev 5 Control*
