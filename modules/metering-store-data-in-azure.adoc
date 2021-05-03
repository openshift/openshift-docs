// Module included in the following assemblies:
//
// * metering/configuring_metering/metering-configure-persistent-storage.adoc

[id="metering-store-data-in-azure_{context}"]
= Storing data in Microsoft Azure

To store data in Azure blob storage, you must use an existing container.

.Procedure

. Edit the `spec.storage` section in the `azure-blob-storage.yaml` file:
+
.Example `azure-blob-storage.yaml` file
[source,yaml]
----
apiVersion: metering.openshift.io/v1
kind: MeteringConfig
metadata:
  name: "operator-metering"
spec:
  storage:
    type: "hive"
    hive:
      type: "azure"
      azure:
        container: "bucket1" <1>
        secretName: "my-azure-secret" <2>
        rootDirectory: "/testDir" <3>
----
<1> Specify the container name.
<2> Specify a secret in the metering namespace. See the example `Secret` object below for more details.
<3> Optional: Specify the directory where you would like to store your data.

. Use the following `Secret` object as a template:
+
.Example Azure `Secret` object
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: my-azure-secret
data:
  azure-storage-account-name: "dGVzdAo="
  azure-secret-access-key: "c2VjcmV0Cg=="
----

. Create the secret:
+
[source,terminal]
----
$ oc create secret -n openshift-metering generic my-azure-secret \
  --from-literal=azure-storage-account-name=my-storage-account-name \
  --from-literal=azure-secret-access-key=my-secret-key
----
