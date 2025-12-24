# SC-3: Security Function Isolation

**Family:** System and Communications Protection  
**Class:** SP800-53  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Isolate security functions from nonsecurity functions.

## Implementation Guidance
Security functions are isolated from nonsecurity functions by means of an isolation boundary implemented within a system via partitions and domains. The isolation boundary controls access to and protects the integrity of the hardware, software, and firmware that perform system security functions. Systems implement code separation in many ways, such as through the provision of security kernels via processor rings or processor modes. For non-kernel code, security function isolation is often achieved through file system protections that protect the code on disk and address space protections that protect executing code. Systems can restrict access to security functions using access control mechanisms and by implementing least privilege capabilities. While the ideal is for all code within the defined security function isolation boundary to only contain security-relevant code, it is sometimes necessary to include nonsecurity functions as an exception. The isolation of security functions from nonsecurity functions can be achieved by applying the systems security engineering design principles in [SA-8](#sa-8) , including [SA-8(1)](#sa-8.1), [SA-8(3)](#sa-8.3), [SA-8(4)](#sa-8.4), [SA-8(10)](#sa-8.10), [SA-8(12)](#sa-8.12), [SA-8(13)](#sa-8.13), [SA-8(14)](#sa-8.14) , and [SA-8(18)](#sa-8.18).

## Assessment Objectives
security functions are isolated from non-security functions.

## Assessment Methods
System and communications protection policy  procedures addressing security function isolation  list of security functions to be isolated from non-security functions  system design documentation  system configuration settings and associated documentation  system audit records  system security plan  other relevant documents or records System/network administrators  organizational personnel with information security responsibilities  system developer Separation of security functions from non-security functions within the system

## Related Controls
- ac-3
- ac-6
- ac-25
- cm-2
- cm-4
- sa-4
- sa-5
- sa-8
- sa-15
- sa-17
- sc-2
- sc-7
- sc-32
- sc-39
- si-16

---
*NIST SP 800-53 Rev 5 Control*
