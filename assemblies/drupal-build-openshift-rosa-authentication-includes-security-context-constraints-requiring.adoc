// Module included in the following assemblies:
//
// * authentication/managing-security-context-constraints.adoc

:_mod-docs-content-type: PROCEDURE
[id="security-context-constraints-requiring_{context}"]
= Configuring a workload to require a specific SCC

You can configure a workload to require a certain security context constraint (SCC). This is useful in scenarios where you want to pin a specific SCC to the workload or if you want to prevent your required SCC from being preempted by another SCC in the cluster.

To require a specific SCC, set the `openshift.io/required-scc` annotation on your workload. You can set this annotation on any resource that can set a pod manifest template, such as a deployment or daemon set.

The SCC must exist in the cluster and must be applicable to the workload, otherwise pod admission fails. An SCC is considered applicable to the workload if the user creating the pod or the pod's service account has `use` permissions for the SCC in the pod's namespace.

[WARNING]
====
Do not change the `openshift.io/required-scc` annotation in the live pod's manifest, because doing so causes the pod admission to fail. To change the required SCC, update the annotation in the underlying pod template, which causes the pod to be deleted and re-created.
====

.Prerequisites

* The SCC must exist in the cluster.

.Procedure

. Create a YAML file for the deployment and specify a required SCC by setting the `openshift.io/required-scc` annotation:
+
.Example `deployment.yaml`
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Deployment
apiVersion: apps/v1
spec:
# ...
  template:
    metadata:
      annotations:
        openshift.io/required-scc: "my-scc" <1>
# ...
----
<1> Specify the name of the SCC to require.

. Create the resource by running the following command:
+
[source,terminal]
----
$ oc create -f deployment.yaml
----

.Verification

* Verify that the deployment used the specified SCC:

.. View the value of the pod's `openshift.io/scc` annotation by running the following command:
+
[source,terminal]
----
$ oc get pod <pod_name> -o jsonpath='{.metadata.annotations.openshift\.io\/scc}{"\n"}' <1>
----
<1> Replace `<pod_name>` with the name of your deployment pod.

.. Examine the output and confirm that the displayed SCC matches the SCC that you defined in the deployment:
+
.Example output
[source,terminal]
----
my-scc
----
