// Module included in the following assemblies:
//
// * post_installation_configuration/machine-configuration-tasks.adoc

:_mod-docs-content-type: PROCEDURE
[id="checking-mco-status-certs_{context}"]
= Viewing and interacting with certificates

The following certificates are handled in the cluster by the Machine Config Controller (MCC) and can be found in the `ControllerConfig` resource:

* `/etc/kubernetes/kubelet-ca.crt`
* `/etc/kubernetes/static-pod-resources/configmaps/cloud-config/ca-bundle.pem`
* `/etc/pki/ca-trust/source/anchors/openshift-config-user-ca-bundle.crt`

The MCC also handles the image registry certificates and its associated user bundle certificate.

You can get information about the listed certificates, including the underyling bundle the certificate comes from, and the signing and subject data.

.Procedure

* Get detailed certificate information by running the following command:
+
[source,terminal]
----
$ oc get controllerconfig/machine-config-controller -o yaml | yq -y '.status.controllerCertificates'
----
+
.Example output
+
[source,text]
----
"controllerCertificates": [
                   {
                       "bundleFile": "KubeAPIServerServingCAData",
                       "signer": "<signer_data1>",
                       "subject": "CN=openshift-kube-apiserver-operator_node-system-admin-signer@168909215"
                   },
                   {
                       "bundleFile": "RootCAData",
                       "signer": "<signer_data2>",
                       "subject": "CN=root-ca,OU=openshift"
                   }
                ]
----

* Get a simpler version of the information found in the ControllerConfig by checking the machine config pool status using the following command:
+
[source,terminal]
----
$ oc get mcp master -o yaml | yq -y '.status.certExpirys'
----
+
.Example output
+
[source,text]
----
status:
  certExpirys:
  - bundle: KubeAPIServerServingCAData
    subject: CN=admin-kubeconfig-signer,OU=openshift
  - bundle: KubeAPIServerServingCAData
    subject: CN=kube-csr-signer_@1689585558
  - bundle: KubeAPIServerServingCAData
    subject: CN=kubelet-signer,OU=openshift
  - bundle: KubeAPIServerServingCAData
    subject: CN=kube-apiserver-to-kubelet-signer,OU=openshift
  - bundle: KubeAPIServerServingCAData
    subject: CN=kube-control-plane-signer,OU=openshift
----
+
This method is meant for {product-title} applications that already consume machine config pool information.

* Check which image registry certificates are on the nodes by looking at the contents of the `/etc/docker/cert.d` directory:
+
[source,terminal]
----
# ls /etc/docker/certs.d
----
+
.Example output
[source,text]
----
image-registry.openshift-image-registry.svc.cluster.local:5000 image-registry.openshift-image-registry.svc:5000
----
