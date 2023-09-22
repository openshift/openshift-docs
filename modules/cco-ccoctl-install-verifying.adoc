// Module included in the following assemblies:
//
// * installing/validating-an-installation.adoc

:_mod-docs-content-type: PROCEDURE
[id="cco-ccoctl-install-verifying_{context}"]
= Clusters that use short-term credentials: Verifying the credentials configuration

You can verify that your cluster is using short-term security credentials for individual components.

.Prerequisites

* You deployed an {product-title} cluster using the Cloud Credential Operator utility (`ccoctl`) to implement short-term credentials.

* You installed the {oc-first}.


.Procedure

. Log in as a user with `cluster-admin` privileges.

. Verify that the cluster does not have `root` credentials by running the following command:
+
[source,terminal]
----
$ oc get secrets -n kube-system <secret_name>
----
+
where `<secret_name>` is the name of the root secret for your cloud provider.
+
[cols=2,options=header]
|===
|Platform
|Secret name

|AWS
|`aws-creds`

|Azure
|`azure-credentials`

|GCP
|`gcp-credentials`

|===
+
An error confirms that the root secret is not present on the cluster. The following example shows the expected output from an AWS cluster:
+
.Example output
[source,text]
----
Error from server (NotFound): secrets "aws-creds" not found
----

. Verify that the components are using short-term security credentials for individual components by running the following command:
+
[source,terminal]
----
$ oc get authentication cluster \
  -o jsonpath \
  --template='{ .spec.serviceAccountIssuer }'
----
+
This command displays the value of the `.spec.serviceAccountIssuer` parameter in the cluster `Authentication` object. An output of a URL that is associated with your cloud provider indicates that the cluster is using manual mode with short-term credentials that are created and managed from outside of the cluster.