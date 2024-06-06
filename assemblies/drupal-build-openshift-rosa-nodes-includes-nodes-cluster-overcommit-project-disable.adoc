// Module included in the following assemblies:
//
// * nodes/nodes-cluster-overcommit.adoc
// * post_installation_configuration/node-tasks.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-cluster-overcommit-project-disable_{context}"]
= Disabling overcommitment for a project

When enabled, overcommitment can be disabled per-project. For example, you can allow infrastructure components to be configured independently of overcommitment.

.Procedure

To disable overcommitment in a project:

ifndef::openshift-rosa,openshift-dedicated[]
. Create or edit the namespace object file.
endif::openshift-rosa,openshift-dedicated[]
// Invalid value: "false": field is immutable, try updating the namespace
ifdef::openshift-rosa,openshift-dedicated[]
. Edit the namespace object file.
endif::openshift-rosa,openshift-dedicated[]

. Add the following annotation:
+
[source,yaml]
----
apiVersion: v1
kind: Namespace
metadata:
  annotations:
    quota.openshift.io/cluster-resource-override-enabled: "false" <1>
# ...
----
<1> Setting this annotation to `false` disables overcommit for this namespace.
