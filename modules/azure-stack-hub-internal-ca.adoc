// Module included in the following assemblies:
//
// *installing/installing_azure_stack_hub/installing-azure-stack-hub-default.adoc

:_mod-docs-content-type: PROCEDURE
[id="internal-certificate-authority_{context}"]
= Configuring the cluster to use an internal CA

If the Azure Stack Hub environment is using an internal Certificate Authority (CA), update the `cluster-proxy-01-config.yaml file` to configure the cluster to use the internal CA.

.Prerequisites

* Create the `install-config.yaml` file and specify the certificate trust bundle in `.pem` format.
* Create the cluster manifests.

.Procedure

. From the directory in which the installation program creates files, go to the `manifests` directory.
. Add `user-ca-bundle` to  the `spec.trustedCA.name` field.
+
.Example `cluster-proxy-01-config.yaml` file
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Proxy
metadata:
  creationTimestamp: null
  name: cluster
spec:
  trustedCA:
    name: user-ca-bundle
status: {}
----
. Optional: Back up the `manifests/ cluster-proxy-01-config.yaml` file. The installation program consumes the `manifests/` directory when you deploy the cluster.
