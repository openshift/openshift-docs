:_mod-docs-content-type: ASSEMBLY
[id="cert-types-machine-config-operator-certificates"]
= Machine Config Operator certificates
include::_attributes/common-attributes.adoc[]
:context: cert-types-machine-config-operator-certificates

toc::[]

== Purpose

This certificate authority is used to secure connections from nodes to Machine Config Server (MCS) during initial provisioning.

There are two certificates:
. A self-signed CA, the MCS CA
. A derived certificate, the MCS cert

=== Provisioning details

{product-title} installations that use {op-system-first} are installed by using Ignition. This process is split into two parts:

. An Ignition config is created that references a URL for the full configuration served by the MCS.
. For user-provisioned infrastucture installation methods, the Ignition config manifests as a `worker.ign` file created by the `openshift-install` command. For installer-provisioned infrastructure installation methods that use the Machine API Operator, this configuration appears as the `worker-user-data` secret.

include::snippets/mcs-endpoint-limitation.adoc[]

.Additional resources

* xref:../../post_installation_configuration/machine-configuration-tasks.adoc#understanding-the-machine-config-operator[Understanding the Machine Config Operator].

* xref:../../networking/openshift_sdn/about-openshift-sdn.adoc#about-openshift-sdn[About the OpenShift SDN network plugin].

=== Provisioning chain of trust

The MCS CA is injected into the Ignition configuration under the `security.tls.certificateAuthorities` configuration field. The MCS then provides the complete configuration using the MCS cert presented by the web server.

The client validates that the MCS cert presented by the server has a chain of trust to an authority it recognizes. In this case, the MCS CA is that authority, and it signs the MCS cert. This ensures that the client is accessing the correct server. The client in this case is Ignition running on a machine in the initramfs.

=== Key material inside a cluster

The MCS CA appears in the cluster as a config map in the `kube-system` namespace, `root-ca` object, with `ca.crt` key.  The private key is not stored in the cluster and is discarded after the installation completes.

The MCS cert appears in the cluster as a secret in the `openshift-machine-config-operator` namespace and `machine-config-server-tls` object with the `tls.crt` and `tls.key` keys.

== Management

At this time, directly modifying either of these certificates is not supported.

== Expiration
The MCS CA is valid for 10 years.

The issued serving certificates are valid for 10 years.

== Customization

You cannot customize the Machine Config Operator certificates.
