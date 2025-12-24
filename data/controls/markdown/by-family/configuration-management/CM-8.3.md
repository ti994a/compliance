# CM-8.3: Automated Unauthorized Component Detection

**Family:** Configuration Management  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Detect the presence of unauthorized hardware, software, and firmware components within the system using organization-defined automated mechanisms frequency at which automated mechanisms are used to detect the presence of unauthorized system components within the system is defined; ; and Take the following actions when unauthorized components are detected: disable network access by unauthorized components.

## Implementation Guidance
Automated unauthorized component detection is applied in addition to the monitoring for unauthorized remote connections and mobile devices. Monitoring for unauthorized system components may be accomplished on an ongoing basis or by the periodic scanning of systems for that purpose. Automated mechanisms may also be used to prevent the connection of unauthorized components (see [CM-7(9)](#cm-7.9) ). Automated mechanisms can be implemented in systems or in separate system components. When acquiring and implementing automated mechanisms, organizations consider whether such mechanisms depend on the ability of the system component to support an agent or supplicant in order to be detected since some types of components do not have or cannot support agents (e.g., IoT devices, sensors). Isolation can be achieved , for example, by placing unauthorized system components in separate domains or subnets or quarantining such components. This type of component isolation is commonly referred to as "sandboxing."

## Assessment Objectives
the presence of unauthorized hardware within the system is detected using automated mechanisms used to detect the presence of unauthorized hardware within the system are defined; frequency at which automated mechanisms are used to detect the presence of unauthorized system components within the system is defined;; the presence of unauthorized software within the system is detected using automated mechanisms used to detect the presence of unauthorized software within the system are defined; frequency at which automated mechanisms are used to detect the presence of unauthorized system components within the system is defined;; the presence of unauthorized firmware within the system is detected using automated mechanisms used to detect the presence of unauthorized firmware within the system are defined; frequency at which automated mechanisms are used to detect the presence of unauthorized system components within the system is defined;; disable network access by unauthorized components are taken when unauthorized hardware is detected; disable network access by unauthorized components are taken when unauthorized software is detected; disable network access by unauthorized components are taken when unauthorized firmware is detected.

## Assessment Methods
Configuration management policy  procedures addressing system component inventory  configuration management plan  system design documentation  system security plan  system component inventory  change control records  alerts/notifications of unauthorized components within the system  system monitoring records  system maintenance records  system audit records  system security plan  other relevant documents or records Organizational personnel with component inventory management responsibilities  organizational personnel with responsibilities for managing the automated mechanisms implementing unauthorized system component detection  organizational personnel with information security responsibilities  system/network administrators  system developers Organizational processes for detection of unauthorized system components  organizational processes for taking action when unauthorized system components are detected  automated mechanisms supporting and/or implementing the detection of unauthorized system components  automated mechanisms supporting and/or implementing actions taken when unauthorized system components are detected

## Related Controls
- ac-19
- ca-7
- ra-5
- sc-3
- sc-39
- sc-44
- si-3
- si-4
- si-7

---
*NIST SP 800-53 Rev 5 Control*
