:_mod-docs-content-type: ASSEMBLY
[id="configuring-a-custom-pki"]
= Configuring a custom PKI
include::_attributes/common-attributes.adoc[]
:context: configuring-a-custom-pki

toc::[]

Some platform components, such as the web console, use Routes for communication and
must trust other components' certificates to interact with them. If
you are using a custom public key infrastructure (PKI), you must configure it so
its privately signed CA certificates are recognized across the cluster.

You can leverage the Proxy API to add cluster-wide trusted CA certificates. You
must do this either during installation or at runtime.

* During _installation_, xref:../networking/configuring-a-custom-pki.adoc#installation-configure-proxy_{context}[configure the cluster-wide proxy]. You must define your
privately signed CA certificates in the `install-config.yaml` file's
`additionalTrustBundle` setting.
+
The installation program generates a ConfigMap that is named `user-ca-bundle`
that contains the additional CA certificates you defined. The Cluster Network
Operator then creates a `trusted-ca-bundle` ConfigMap that merges these CA
certificates with the {op-system-first} trust bundle; this ConfigMap is
referenced in the Proxy object's `trustedCA` field.

* At _runtime_, xref:../networking/configuring-a-custom-pki.adoc#nw-proxy-configure-object_{context}[modify the default Proxy object to include your privately signed CA certificates] (part of cluster's proxy enablement workflow). This involves
creating a ConfigMap that contains the privately signed CA certificates that
should be trusted by the cluster, and then modifying the proxy resource with the
`trustedCA` referencing the privately signed certificates' ConfigMap.

[NOTE]
====
The installer configuration's `additionalTrustBundle` field and the proxy
resource's `trustedCA` field are used to manage the cluster-wide trust bundle;
`additionalTrustBundle` is used at install time and the proxy's `trustedCA` is
used at runtime.

The `trustedCA` field is a reference to a `ConfigMap` containing the custom
certificate and key pair used by the cluster component.
====

include::modules/installation-configure-proxy.adoc[leveloffset=+1]

include::modules/nw-proxy-configure-object.adoc[leveloffset=+1]

include::modules/certificate-injection-using-operators.adoc[leveloffset=+1]
