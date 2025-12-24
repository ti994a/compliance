# AC-2: Account Management

**Family:** Access Control  
**Class:** SP800-53  
**Keywords:** Assessment, assessment plan, assurance, availability, computer security, confidentiality, control, control assessment, cybersecurity, FISMA, information security, information system, integrity, personally identifiable information, OSCAL, Open Security Controls Assessment Language, Privacy Act, privacy controls, privacy functions, privacy requirements, Risk Management Framework, security controls, security functions, security requirements, system, system security

## Control Statement
Define and document the types of accounts allowed and specifically prohibited for use within the system; Assign account managers; Require prerequisites and criteria for group and role membership are defined; for group and role membership; Specify: Authorized users of the system; Group and role membership; and Access authorizations (i.e., privileges) and attributes (as required) for each account are defined; for each account; Require approvals by personnel or roles required to approve requests to create accounts for requests to create accounts; Create, enable, modify, disable, and remove accounts in accordance with policy, procedures, prerequisites, and criteria for account creation, enabling, modification, disabling, and removal are defined;; Monitor the use of accounts; Notify account managers and personnel or roles notified within: time period within which to notify account managers when accounts are no longer required is defined; when accounts are no longer required; time period within which to notify account managers when users are terminated or transferred is defined; when users are terminated or transferred; and time period within which to notify account managers when system usage or the need to know changes for an individual is defined; when system usage or need-to-know changes for an individual; Authorize access to the system based on: A valid access authorization; Intended system usage; and attributes needed to authorize system access (as required) are defined;; Review accounts for compliance with account management requirements the frequency of account review is defined;; Establish and implement a process for changing shared or group account authenticators (if deployed) when individuals are removed from the group; and Align account management processes with personnel termination and transfer processes.

## Implementation Guidance
Examples of system account types include individual, shared, group, system, guest, anonymous, emergency, developer, temporary, and service. Identification of authorized system users and the specification of access privileges reflect the requirements in other controls in the security plan. Users requiring administrative privileges on system accounts receive additional scrutiny by organizational personnel responsible for approving such accounts and privileged access, including system owner, mission or business owner, senior agency information security officer, or senior agency official for privacy. Types of accounts that organizations may wish to prohibit due to increased risk include shared, group, emergency, anonymous, temporary, and guest accounts.  Where access involves personally identifiable information, security programs collaborate with the senior agency official for privacy to establish the specific conditions for group and role membership; specify authorized users, group and role membership, and access authorizations for each account; and create, adjust, or remove system accounts in accordance with organizational policies. Policies can include such information as account expiration dates or other factors that trigger the disabling of accounts. Organizations may choose to define access privileges or other attributes by account, type of account, or a combination of the two. Examples of other attributes required for authorizing access include restrictions on time of day, day of week, and point of origin. In defining other system account attributes, organizations consider system-related requirements and mission/business requirements. Failure to consider these factors could affect system availability.  Temporary and emergency accounts are intended for short-term use. Organizations establish temporary accounts as part of normal account activation procedures when there is a need for short-term accounts without the demand for immediacy in account activation. Organizations establish emergency accounts in response to crisis situations and with the need for rapid account activation. Therefore, emergency account activation may bypass normal account authorization processes. Emergency and temporary accounts are not to be confused with infrequently used accounts, including local logon accounts used for special tasks or when network resources are unavailable (may also be known as accounts of last resort). Such accounts remain available and are not subject to automatic disabling or removal dates. Conditions for disabling or deactivating accounts include when shared/group, emergency, or temporary accounts are no longer required and when individuals are transferred or terminated. Changing shared/group authenticators when members leave the group is intended to ensure that former group members do not retain access to the shared or group account. Some types of system accounts may require specialized training.

## Assessment Objectives
account types allowed for use within the system are defined and documented; account types specifically prohibited for use within the system are defined and documented; account managers are assigned; prerequisites and criteria for group and role membership are defined; for group and role membership are required; authorized users of the system are specified; group and role membership are specified; access authorizations (i.e., privileges) are specified for each account; attributes (as required) for each account are defined; are specified for each account; approvals are required by personnel or roles required to approve requests to create accounts for requests to create accounts; accounts are created in accordance with policy, procedures, prerequisites, and criteria for account creation, enabling, modification, disabling, and removal are defined;; accounts are enabled in accordance with policy, procedures, prerequisites, and criteria for account creation, enabling, modification, disabling, and removal are defined;; accounts are modified in accordance with policy, procedures, prerequisites, and criteria for account creation, enabling, modification, disabling, and removal are defined;; accounts are disabled in accordance with policy, procedures, prerequisites, and criteria for account creation, enabling, modification, disabling, and removal are defined;; accounts are removed in accordance with policy, procedures, prerequisites, and criteria for account creation, enabling, modification, disabling, and removal are defined;; the use of accounts is monitored;  account managers and personnel or roles notified are notified within time period within which to notify account managers when accounts are no longer required is defined; when accounts are no longer required; account managers and personnel or roles notified are notified within time period within which to notify account managers when users are terminated or transferred is defined; when users are terminated or transferred; account managers and personnel or roles notified are notified within time period within which to notify account managers when system usage or the need to know changes for an individual is defined; when system usage or the need to know changes for an individual; access to the system is authorized based on a valid access authorization; access to the system is authorized based on intended system usage; access to the system is authorized based on attributes needed to authorize system access (as required) are defined;; accounts are reviewed for compliance with account management requirements the frequency of account review is defined;; a process is established for changing shared or group account authenticators (if deployed) when individuals are removed from the group; a process is implemented for changing shared or group account authenticators (if deployed) when individuals are removed from the group; account management processes are aligned with personnel termination processes; account management processes are aligned with personnel transfer processes.

## Assessment Methods
Access control policy  personnel termination policy and procedure  personnel transfer policy and procedure  procedures for addressing account management  system design documentation  system configuration settings and associated documentation  list of active system accounts along with the name of the individual associated with each account  list of recently disabled system accounts and the name of the individual associated with each account  list of conditions for group and role membership  notifications of recent transfers, separations, or terminations of employees  access authorization records  account management compliance reviews  system monitoring records  system audit records  system security plan  privacy plan  other relevant documents or records Organizational personnel with account management responsibilities  system/network administrators  organizational personnel with information security with information security and privacy responsibilities Organizational processes for account management on the system  mechanisms for implementing account management

## Related Controls
- ac-3
- ac-5
- ac-6
- ac-17
- ac-18
- ac-20
- ac-24
- au-2
- au-12
- cm-5
- ia-2
- ia-4
- ia-5
- ia-8
- ma-3
- ma-5
- pe-2
- pl-4
- ps-2
- ps-4
- ps-5
- ps-7
- pt-2
- pt-3
- sc-7
- sc-12
- sc-13
- sc-37

---
*NIST SP 800-53 Rev 5 Control*
