# AC-3.9: Controlled Release

**Family:** Access Control  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Release information outside of the system only if: The receiving the outside system or system component to which to release information is defined; provides controls provided by the outside system or system component (defined in AC-03(09)_ODP[01]) are defined; ; and controls used to validate appropriateness of information released are defined; are used to validate the appropriateness of the information designated for release.

## Implementation Guidance
Organizations can only directly protect information when it resides within the system. Additional controls may be needed to ensure that organizational information is adequately protected once it is transmitted outside of the system. In situations where the system is unable to determine the adequacy of the protections provided by external entities, as a mitigation measure, organizations procedurally determine whether the external systems are providing adequate controls. The means used to determine the adequacy of controls provided by external systems include conducting periodic assessments (inspections/tests), establishing agreements between the organization and its counterpart organizations, or some other process. The means used by external entities to protect the information received need not be the same as those used by the organization, but the means employed are sufficient to provide consistent adjudication of the security and privacy policy to protect the information and individuals’ privacy.  Controlled release of information requires systems to implement technical or procedural means to validate the information prior to releasing it to external systems. For example, if the system passes information to a system controlled by another organization, technical means are employed to validate that the security and privacy attributes associated with the exported information are appropriate for the receiving system. Alternatively, if the system passes information to a printer in organization-controlled space, procedural means can be employed to ensure that only authorized individuals gain access to the printer.

## Assessment Objectives
information is released outside of the system only if the receiving the outside system or system component to which to release information is defined; provides controls provided by the outside system or system component (defined in AC-03(09)_ODP[01]) are defined;; information is released outside of the system only if controls used to validate appropriateness of information released are defined; are used to validate the appropriateness of the information designated for release.

## Assessment Methods
Access control policy  procedures addressing access enforcement  system design documentation  system configuration settings and associated documentation  list of security and privacy safeguards provided by receiving system or system components  list of security and privacy safeguards validating appropriateness of information designated for release  system audit records  results of period assessments (inspections/tests) of the external system  information sharing agreements  memoranda of understanding  acquisitions/contractual agreements  system security plan  privacy plan  other relevant documents or records Organizational personnel with access enforcement responsibilities  system/network administrators  organizational personnel with information security and privacy responsibilities  organizational personnel with responsibility for acquisitions/contractual agreements  legal counsel  system developers Mechanisms implementing access enforcement functions

## Related Controls
- ca-3
- pt-7
- pt-8
- sa-9
- sc-16

---
*NIST SP 800-53 Rev 5 Control*
