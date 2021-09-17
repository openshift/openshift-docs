// Module included in the following assemblies:
//
// * web_console/disabling-web-console.adoc

[id="web-console-disable_{context}"]
= Disabling the web console

You can disable the web console by editing the
`consoles.operator.openshift.io` resource.

* Edit the `consoles.operator.openshift.io` resource:
+
[source,terminal]
----
$ oc edit consoles.operator.openshift.io cluster
----
+
The following example displays the parameters from this resource that you can
modify:
+
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
spec:
  managementState: Removed <1>
----
<1> Set the `managementState` parameter value to `Removed` to disable the web
console. The other valid values for this parameter are `Managed`, which enables
the console under the cluster's control, and `Unmanaged`, which means that you
are taking control of web console management.
