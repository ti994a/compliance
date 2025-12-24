# SI-3: Malicious Code Protection

**Family:** System and Information Integrity  
**Class:** SP800-53  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Implement signature-based malicious code protection mechanisms at system entry and exit points to detect and eradicate malicious code; Automatically update malicious code protection mechanisms as new releases are available in accordance with organizational configuration management policy and procedures; Configure malicious code protection mechanisms to: Perform periodic scans of the system the frequency at which malicious code protection mechanisms perform scans is defined; and real-time scans of files from external sources at endpoint as the files are downloaded, opened, or executed in accordance with organizational policy; and block malicious code ; and send alert to personnel or roles alerted when malicious code is detected in response to malicious code detection; and Address the receipt of false positives during malicious code detection and eradication and the resulting potential impact on the availability of the system.

## Implementation Guidance
System entry and exit points include firewalls, remote access servers, workstations, electronic mail servers, web servers, proxy servers, notebook computers, and mobile devices. Malicious code includes viruses, worms, Trojan horses, and spyware. Malicious code can also be encoded in various formats contained within compressed or hidden files or hidden in files using techniques such as steganography. Malicious code can be inserted into systems in a variety of ways, including by electronic mail, the world-wide web, and portable storage devices. Malicious code insertions occur through the exploitation of system vulnerabilities. A variety of technologies and methods exist to limit or eliminate the effects of malicious code.  Malicious code protection mechanisms include both signature- and nonsignature-based technologies. Nonsignature-based detection mechanisms include artificial intelligence techniques that use heuristics to detect, analyze, and describe the characteristics or behavior of malicious code and to provide controls against such code for which signatures do not yet exist or for which existing signatures may not be effective. Malicious code for which active signatures do not yet exist or may be ineffective includes polymorphic malicious code (i.e., code that changes signatures when it replicates). Nonsignature-based mechanisms also include reputation-based technologies. In addition to the above technologies, pervasive configuration management, comprehensive software integrity controls, and anti-exploitation software may be effective in preventing the execution of unauthorized code. Malicious code may be present in commercial off-the-shelf software as well as custom-built software and could include logic bombs, backdoors, and other types of attacks that could affect organizational mission and business functions.  In situations where malicious code cannot be detected by detection methods or technologies, organizations rely on other types of controls, including secure coding practices, configuration management and control, trusted procurement processes, and monitoring practices to ensure that software does not perform functions other than the functions intended. Organizations may determine that, in response to the detection of malicious code, different actions may be warranted. For example, organizations can define actions in response to malicious code detection during periodic scans, the detection of malicious downloads, or the detection of maliciousness when attempting to open or execute files.

## Assessment Objectives
signature-based malicious code protection mechanisms are implemented at system entry and exit points to detect malicious code; signature-based malicious code protection mechanisms are implemented at system entry and exit points to eradicate malicious code; malicious code protection mechanisms are updated automatically as new releases are available in accordance with organizational configuration management policy and procedures; malicious code protection mechanisms are configured to perform periodic scans of the system the frequency at which malicious code protection mechanisms perform scans is defined;; malicious code protection mechanisms are configured to perform real-time scans of files from external sources at endpoint as the files are downloaded, opened, or executed in accordance with organizational policy; malicious code protection mechanisms are configured to block malicious code in response to malicious code detection; malicious code protection mechanisms are configured to send alerts to personnel or roles alerted when malicious code is detected in response to malicious code detection; the receipt of false positives during malicious code detection and eradication and the resulting potential impact on the availability of the system are addressed.

## Assessment Methods
System and information integrity policy  system and information integrity procedures  configuration management policy and procedures  procedures addressing malicious code protection  malicious code protection mechanisms  records of malicious code protection updates  system design documentation  system configuration settings and associated documentation  scan results from malicious code protection mechanisms  record of actions initiated by malicious code protection mechanisms in response to malicious code detection  system audit records  system security plan  other relevant documents or records System/network administrators  organizational personnel with information security responsibilities  organizational personnel installing, configuring, and/or maintaining the system  organizational personnel responsible for malicious code protection  organizational personnel with configuration management responsibilities Organizational processes for employing, updating, and configuring malicious code protection mechanisms  organizational processes for addressing false positives and resulting potential impacts  mechanisms supporting and/or implementing, employing, updating, and configuring malicious code protection mechanisms  mechanisms supporting and/or implementing malicious code scanning and subsequent actions

## Related Controls
- ac-4
- ac-19
- cm-3
- cm-8
- ir-4
- ma-3
- ma-4
- pl-9
- ra-5
- sc-7
- sc-23
- sc-26
- sc-28
- sc-44
- si-2
- si-4
- si-7
- si-8
- si-15

---
*NIST SP 800-53 Rev 5 Control*
