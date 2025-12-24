# SI-2: Flaw Remediation

**Family:** System and Information Integrity  
**Class:** SP800-53  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Identify, report, and correct system flaws; Test software and firmware updates related to flaw remediation for effectiveness and potential side effects before installation; Install security-relevant software and firmware updates within time period within which to install security-relevant software updates after the release of the updates is defined; of the release of the updates; and Incorporate flaw remediation into the organizational configuration management process.

## Implementation Guidance
The need to remediate system flaws applies to all types of software and firmware. Organizations identify systems affected by software flaws, including potential vulnerabilities resulting from those flaws, and report this information to designated organizational personnel with information security and privacy responsibilities. Organizations consider establishing a controlled patching environment for mission-critical systems. Security-relevant updates include patches, service packs, and malicious code signatures. Organizations also address flaws discovered during assessments, continuous monitoring, incident response activities, and system error handling. By incorporating flaw remediation into configuration management processes, required remediation actions can be tracked and verified.  Organization-defined time periods for updating security-relevant software and firmware may vary based on a variety of risk factors, including the security category of the system, the criticality of the update (i.e., severity of the vulnerability related to the discovered flaw), the organizational risk tolerance, the mission supported by the system, or the threat environment. Some types of flaw remediation may require more testing than other types. Organizations determine the type of testing needed for the specific type of flaw remediation activity under consideration and the types of changes that are to be configuration-managed. Flaw remediation testing addresses both effectiveness of addressing security issues and for potential side effects on functionality, system and system component performance and operations. When implementing remediation activities, organizations consider the order and timing of updates to validate correct execution within the system environment, and to support system and component availability needs (i.e., implementing a staggered deployment strategy). In some situations, organizations may determine that the testing of software or firmware updates is not necessary or practical, such as when implementing simple malicious code signature updates. In testing decisions, organizations consider whether security-relevant software or firmware updates are obtained from authorized sources with appropriate digital signatures.  When implementing remediation activities, organizations consider the order and timing of updates to validate correct execution within the system environment, and to support system and component availability needs (i.e., implementing a staggered deployment strategy). Organizations verify that software and firmware updates come from authorized sources prior to downloading.

## Assessment Objectives
system flaws are identified; system flaws are reported; system flaws are corrected; software updates related to flaw remediation are tested for effectiveness before installation; software updates related to flaw remediation are tested for potential side effects before installation; firmware updates related to flaw remediation are tested for effectiveness before installation; firmware updates related to flaw remediation are tested for potential side effects before installation; security-relevant software updates are installed within time period within which to install security-relevant software updates after the release of the updates is defined; of the release of the updates; security-relevant firmware updates are installed within time period within which to install security-relevant software updates after the release of the updates is defined; of the release of the updates; flaw remediation is incorporated into the organizational configuration management process.

## Assessment Methods
System and information integrity policy  system and information integrity procedures  procedures addressing flaw remediation  procedures addressing configuration management  list of flaws and vulnerabilities potentially affecting the system  list of recent security flaw remediation actions performed on the system (e.g., list of installed patches, service packs, hot fixes, and other software updates to correct system flaws)  test results from the installation of software and firmware updates to correct system flaws  installation/change control records for security-relevant software and firmware updates  system security plan  privacy plan  other relevant documents or records System/network administrators  organizational personnel with information security and privacy responsibilities  organizational personnel responsible for installing, configuring, and/or maintaining the system  organizational personnel responsible for flaw remediation  organizational personnel with configuration management responsibilities Organizational processes for identifying, reporting, and correcting system flaws  organizational process for installing software and firmware updates  mechanisms supporting and/or implementing the reporting and correcting of system flaws  mechanisms supporting and/or implementing testing software and firmware updates

## Related Controls
- ca-5
- cm-3
- cm-4
- cm-5
- cm-6
- cm-8
- ma-2
- ra-5
- sa-8
- sa-10
- sa-11
- si-3
- si-5
- si-7
- si-11

---
*NIST SP 800-53 Rev 5 Control*
