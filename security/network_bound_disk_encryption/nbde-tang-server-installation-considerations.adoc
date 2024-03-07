:_mod-docs-content-type: ASSEMBLY
// CNF-2127 assembly
[id="nbde-tang-server-installation-considerations"]
= Tang server installation considerations
include::_attributes/common-attributes.adoc[]
:context: nbde-implementation

toc::[]

Network-Bound Disk Encryption (NBDE) must be enabled when a cluster node is installed. However, you can change the disk encryption policy at any time after it was initialized at installation.

include::modules/nbde-installation-scenarios.adoc[leveloffset=+1]

[id="nbde-installing-a-tang-server_{context}"]
== Installing a Tang server

To deploy one or more Tang servers, you can choose from the following options depending on your scenario:

. xref:../../security/nbde_tang_server_operator/nbde-tang-server-operator-configuring-managing.adoc#deploying-nbde-tang-server_configuring-and-managing-nbde-tang-server-operator[Deploying a Tang server using the NBDE Tang Server Operator]
. link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption_security-hardening#deploying-a-tang-server-with-selinux-in-enforcing-mode_configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption[Deploying a Tang server with SELinux in enforcing mode on RHEL systems]
. link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption_security-hardening#configuring-automated-unlocking-using-a-tang-key-in-the-web-console_configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption[Configuring a Tang server in the RHEL web console]
. link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption_security-hardening#proc_deploying-tang-as-a-container_configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption[Deploying Tang as a container]
. link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption_security-hardening#using-the-nbde_server-system-role-for-setting-up-multiple-tang-servers_configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption[Using the nbde_server System Role for setting up multiple Tang servers]

include::modules/nbde-compute-requirements.adoc[leveloffset=+2]

include::modules/nbde-automatic-start-at-boot.adoc[leveloffset=+2]

include::modules/nbde-http-versus-https.adoc[leveloffset=+2]

[role="_additional-resources"]
.Additional resources
* https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/configuring-automated-unlocking-of-encrypted-volumes-using-policy-based-decryption_security-hardening[Configuring automated unlocking of encrypted volumes using policy-based decryption] in the link:https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/security_hardening/index[RHEL 8 Security hardening] document
* https://catalog.redhat.com/software/containers/detail/5fbc405674aa0cc23b445f8f?container-tabs=overview&gti-tabs=registry-tokens[Official Tang server container]
* xref:../../installing/install_config/installing-customizing.adoc#installation-special-config-storage_installing-customizing[Encrypting and mirroring disks during installation]
