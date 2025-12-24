# CM-7.5: Authorized Software — Allow-by-exception

**Family:** Configuration Management  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Identify software programs authorized to execute on the system are defined;; Employ a deny-all, permit-by-exception policy to allow the execution of authorized software programs on the system; and Review and update the list of authorized software programs frequency at which to review and update the list of authorized software programs is defined;.

## Implementation Guidance
Authorized software programs can be limited to specific versions or from a specific source. To facilitate a comprehensive authorized software process and increase the strength of protection for attacks that bypass application level authorized software, software programs may be decomposed into and monitored at different levels of detail. These levels include applications, application programming interfaces, application modules, scripts, system processes, system services, kernel functions, registries, drivers, and dynamic link libraries. The concept of permitting the execution of authorized software may also be applied to user actions, system ports and protocols, IP addresses/ranges, websites, and MAC addresses. Organizations consider verifying the integrity of authorized software programs using digital signatures, cryptographic checksums, or hash functions. Verification of authorized software can occur either prior to execution or at system startup. The identification of authorized URLs for websites is addressed in [CA-3(5)](#ca-3.5) and [SC-7](#sc-7).

## Assessment Objectives
software programs authorized to execute on the system are defined; are identified; a deny-all, permit-by-exception policy to allow the execution of authorized software programs on the system is employed; the list of authorized software programs is reviewed and updated frequency at which to review and update the list of authorized software programs is defined;.

## Assessment Methods
Configuration management policy  procedures addressing least functionality in the system  configuration management plan  system design documentation  system configuration settings and associated documentation  list of software programs authorized to execute on the system  system component inventory  common secure configuration checklists  review and update records associated with list of authorized software programs  change control records  system audit records  system security plan  other relevant documents or records Organizational personnel with responsibilities for identifying software authorized to execute on the system  organizational personnel with information security responsibilities  system/network administrators Organizational process for identifying, reviewing, and updating programs authorized to execute on the system  organizational process for implementing authorized software policy  mechanisms supporting and/or implementing authorized software policy

## Related Controls
- cm-2
- cm-6
- cm-8
- cm-10
- pl-9
- pm-5
- sa-10
- sc-34
- si-7

---
*NIST SP 800-53 Rev 5 Control*
