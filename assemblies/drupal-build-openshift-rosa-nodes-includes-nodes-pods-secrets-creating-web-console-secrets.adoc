// Module included in the following assemblies:
//
// * nodes/pods/nodes-pods-secrets.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-pods-secrets-creating-web-console-secrets_{context}"]
= Creating a secret using the web console

You can create secrets using the web console.

.Procedure

. Navigate to *Workloads* -> *Secrets*.
. Click *Create* -> *From YAML*.
.. Edit the YAML manually to your specifications, or drag and drop a file into the YAML editor.
For example:
+
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: example
  namespace: <namespace>
type: Opaque <1>
data:
  username: <base64 encoded username>
  password: <base64 encoded password>
stringData: <2>
  hostname: myapp.mydomain.com
----
<1> This example specifies an opaque secret; however, you may see other secret types such as service account token secret, basic authentication secret, SSH authentication secret, or a secret that uses Docker configuration.
<2> Entries in the `stringData` map are converted to base64 and the entry will then be moved to the `data` map automatically. This field is write-only; the value will only be returned via the `data` field.

. Click *Create*.
. Click *Add Secret to workload*.
.. From the drop-down menu, select the workload to add.
.. Click *Save*.
