# SI-3.8: Detect Unauthorized Commands

**Family:** System and Information Integrity  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Detect the following unauthorized operating system commands through the kernel application programming interface on unauthorized operating system commands detected are defined;: system hardware components for which unauthorized operating system commands are detected through the kernel application programming interface are defined; ; and issue a warning.

## Implementation Guidance
Detecting unauthorized commands can be applied to critical interfaces other than kernel-based interfaces, including interfaces with virtual machines and privileged applications. Unauthorized operating system commands include commands for kernel functions from system processes that are not trusted to initiate such commands as well as commands for kernel functions that are suspicious even though commands of that type are reasonable for processes to initiate. Organizations can define the malicious commands to be detected by a combination of command types, command classes, or specific instances of commands. Organizations can also define hardware components by component type, component, component location in the network, or a combination thereof. Organizations may select different actions for different types, classes, or instances of malicious commands.

## Assessment Objectives
system hardware components for which unauthorized operating system commands are detected through the kernel application programming interface are defined; are detected through the kernel application programming interface on unauthorized operating system commands detected are defined;; issue a warning is/are performed.

## Assessment Methods
System and information integrity policy  system and information integrity procedures  procedures addressing malicious code protection  system design documentation  malicious code protection mechanisms  warning messages sent upon the detection of unauthorized operating system command execution  system configuration settings and associated documentation  system audit records  system security plan  other relevant documents or records System/network administrators  organizational personnel with information security responsibilities  system developers  organizational personnel installing, configuring, and/or maintaining the system  organizational personnel responsible for malicious code protection Mechanisms supporting and/or implementing malicious code protection capabilities  mechanisms supporting and/or implementing the detection of unauthorized operating system commands through the kernel application programming interface

## Related Controls
- au-2
- au-6
- au-12

---
*NIST SP 800-53 Rev 5 Control*
