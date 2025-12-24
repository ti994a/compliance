# SC-7.7: Split Tunneling for Remote Devices

**Family:** System and Communications Protection  
**Class:** SP800-53-enhancement  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Prevent split tunneling for remote devices connecting to organizational systems unless the split tunnel is securely provisioned using safeguards to securely provision split tunneling are defined;.

## Implementation Guidance
Split tunneling is the process of allowing a remote user or device to establish a non-remote connection with a system and simultaneously communicate via some other connection to a resource in an external network. This method of network access enables a user to access remote devices and simultaneously, access uncontrolled networks. Split tunneling might be desirable by remote users to communicate with local system resources, such as printers or file servers. However, split tunneling can facilitate unauthorized external connections, making the system vulnerable to attack and to exfiltration of organizational information. Split tunneling can be prevented by disabling configuration settings that allow such capability in remote devices and by preventing those configuration settings from being configurable by users. Prevention can also be achieved by the detection of split tunneling (or of configuration settings that allow split tunneling) in the remote device, and by prohibiting the connection if the remote device is using split tunneling. A virtual private network (VPN) can be used to securely provision a split tunnel. A securely provisioned VPN includes locking connectivity to exclusive, managed, and named environments, or to a specific set of pre-approved addresses, without user control.

## Assessment Objectives
split tunneling is prevented for remote devices connecting to organizational systems unless the split tunnel is securely provisioned using safeguards to securely provision split tunneling are defined;.

## Assessment Methods
System and communications protection policy  procedures addressing boundary protection  system design documentation  system hardware and software  system architecture  system configuration settings and associated documentation  system audit records  system security plan  other relevant documents or records System/network administrators  organizational personnel with information security responsibilities  system developer  organizational personnel with boundary protection responsibilities Mechanisms implementing boundary protection capabilities  mechanisms supporting/restricting non-remote connections

## Related Controls


---
*NIST SP 800-53 Rev 5 Control*
