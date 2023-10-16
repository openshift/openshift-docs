// Module included in the following assemblies:
//
// * security/container_security/security-hardening.adoc

[id="security-hardening-what_{context}"]

= Choosing what to harden in {op-system}
ifdef::openshift-origin[]
The link:https://docs.fedoraproject.org/en-US/Fedora/19/html/Security_Guide/chap-Security_Guide-Basic_Hardening.html[{op-system-base} Security Hardening] guide describes how you should approach security for any
{op-system-base} system.
endif::[]
ifdef::openshift-enterprise,openshift-webscale,openshift-aro[]
The link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/security_hardening/index#scanning-container-and-container-images-for-vulnerabilities_scanning-the-system-for-security-compliance-and-vulnerabilities[{op-system-base} 8 Security Hardening] guide describes how you should approach security for any
{op-system-base} system.
endif::[]

Use this guide to learn how to approach cryptography, evaluate
vulnerabilities, and assess threats to various services.
Likewise, you can learn how to scan for compliance standards, check file
integrity, perform auditing, and encrypt storage devices.

With the knowledge of what features you want to harden, you can then
decide how to harden them in {op-system}.
