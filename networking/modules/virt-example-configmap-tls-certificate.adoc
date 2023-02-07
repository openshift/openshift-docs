// Module included in the following assemblies:
//
// * virt/virtual_machines/importing_vms/virt-tls-certificates-for-dv-imports.adoc

[id="virt-example-configmap-tls-certificate_{context}"]
= Example: Config map created from a TLS certificate

The following example is of a config map created from `ca.pem` TLS certificate. 

[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: tls-certs
data:
  ca.pem: |
    -----BEGIN CERTIFICATE-----
    ... <base64 encoded cert> ...
    -----END CERTIFICATE-----
----
