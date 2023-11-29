// Module included in the following assemblies:
//
// * virt/virtual_machines/virt-exporting-vms.adoc

:_mod-docs-content-type: PROCEDURE
[id="virt-accessing-exported-vm-manifests_{context}"]
= Accessing exported virtual machine manifests

After you export a virtual machine (VM) or snapshot, you can get the `VirtualMachine` manifest and related information from the export server.

.Prerequisites

* You exported a virtual machine or VM snapshot by creating a `VirtualMachineExport` custom resource (CR).
+
[NOTE]
====
`VirtualMachineExport` objects that have the `spec.source.kind: PersistentVolumeClaim` parameter do not generate virtual machine manifests.
====

.Procedure

. To access the manifests, you must first copy the certificates from the source cluster to the target cluster.

.. Log in to the source cluster.

.. Save the certificates to the `cacert.crt` file by running the following command:
+
[source,terminal]
----
$ oc get vmexport <export_name> -o jsonpath={.status.links.external.cert} > cacert.crt <1>
----
<1> Replace `<export_name>` with the `metadata.name` value from the `VirtualMachineExport` object.

.. Copy the `cacert.crt` file to the target cluster.

. Decode the token in the source cluster and save it to the `token_decode` file by running the following command:
+
[source,terminal]
----
$ oc get secret export-token-<export_name> -o jsonpath={.data.token} | base64 --decode > token_decode <1>
----
<1> Replace `<export_name>` with the `metadata.name` value from the `VirtualMachineExport` object.

. Copy the `token_decode` file to the target cluster.

. Get the `VirtualMachineExport` custom resource by running the following command:
+
[source,terminal]
----
$ oc get vmexport <export_name> -o yaml
----

. Review the `status.links` stanza, which is divided into `external` and `internal` sections. Note the `manifests.url` fields within each section:
+
.Example output

[source,yaml]
----
apiVersion: export.kubevirt.io/v1alpha1
kind: VirtualMachineExport
metadata:
  name: example-export
spec:
  source:
    apiGroup: "kubevirt.io"
    kind: VirtualMachine
    name: example-vm
  tokenSecretRef: example-token
status:
#...
  links:
    external:
#...
      manifests:
      - type: all
        url: https://vmexport-proxy.test.net/api/export.kubevirt.io/v1alpha1/namespaces/example/virtualmachineexports/example-export/external/manifests/all <1>
      - type: auth-header-secret
        url: https://vmexport-proxy.test.net/api/export.kubevirt.io/v1alpha1/namespaces/example/virtualmachineexports/example-export/external/manifests/secret <2>
    internal:
#...
      manifests:
      - type: all
        url: https://virt-export-export-pvc.default.svc/internal/manifests/all <3>
      - type: auth-header-secret
        url: https://virt-export-export-pvc.default.svc/internal/manifests/secret
  phase: Ready
  serviceName: virt-export-example-export
----
<1> Contains the `VirtualMachine` manifest, `DataVolume` manifest, if present, and a `ConfigMap` manifest that contains the public certificate for the external URL's ingress or route.
<2> Contains a secret containing a header that is compatible with Containerized Data Importer (CDI). The header contains a text version of the export token.
<3> Contains the `VirtualMachine` manifest, `DataVolume` manifest, if present, and a `ConfigMap` manifest that contains the certificate for the internal URL's export server.

. Log in to the target cluster.

. Get the `Secret` manifest by running the following command:
+
[source,terminal]
----
$ curl --cacert cacert.crt <secret_manifest_url> -H \ <1>
"x-kubevirt-export-token:token_decode" -H \ <2>
"Accept:application/yaml"
----
<1> Replace `<secret_manifest_url>` with an `auth-header-secret` URL from the `VirtualMachineExport` YAML output.
<2> Reference the `token_decode` file that you created earlier.
+
For example:
+
[source,terminal]
----
$ curl --cacert cacert.crt https://vmexport-proxy.test.net/api/export.kubevirt.io/v1alpha1/namespaces/example/virtualmachineexports/example-export/external/manifests/secret -H "x-kubevirt-export-token:token_decode" -H "Accept:application/yaml"
----

. Get the manifests of `type: all`, such as the `ConfigMap` and `VirtualMachine` manifests, by running the following command:
+
[source,terminal]
----
$ curl --cacert cacert.crt <all_manifest_url> -H \ <1>
"x-kubevirt-export-token:token_decode" -H \ <2>
"Accept:application/yaml"
----
<1> Replace `<all_manifest_url>` with a URL from the `VirtualMachineExport` YAML output.
<2> Reference the `token_decode` file that you created earlier.
+
For example:
+
[source,terminal]
----
$ curl --cacert cacert.crt https://vmexport-proxy.test.net/api/export.kubevirt.io/v1alpha1/namespaces/example/virtualmachineexports/example-export/external/manifests/all -H "x-kubevirt-export-token:token_decode" -H "Accept:application/yaml"
----

.Next steps

* You can now create the `ConfigMap` and `VirtualMachine` objects on the target cluster by using the exported manifests.