// Module included in the following assemblies:
//
// * nodes/scheduling/nodes-scheduler-taints-tolerations.adoc
// * post_installation_configuration/node-tasks.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-scheduler-taints-tolerations-projects_{context}"]
= Creating a project with a node selector and toleration

You can create a project that uses a node selector and toleration, which are set as annotations, to control the placement of pods onto specific nodes. Any subsequent resources created in the project are then scheduled on nodes that have a taint matching the toleration.

.Prerequisites

* A label for node selection has been added to one or more nodes by using a compute machine set or editing the node directly.
* A taint has been added to one or more nodes by using a compute machine set or editing the node directly.

.Procedure

. Create a `Project` resource definition, specifying a node selector and toleration in the `metadata.annotations` section:
+
.Example `project.yaml` file
[source,yaml]
----
kind: Project
apiVersion: project.openshift.io/v1
metadata:
  name: <project_name> <1>
  annotations:
    openshift.io/node-selector: '<label>' <2>
    scheduler.alpha.kubernetes.io/defaultTolerations: >-
      [{"operator": "Exists", "effect": "NoSchedule", "key":
      "<key_name>"} <3>
      ]
----
<1> The project name.
<2> The default node selector label.
<3> The toleration parameters, as described in the *Taint and toleration components* table. This example uses the `NoSchedule` effect, which allows existing pods on the node to remain, and the `Exists` operator, which does not take a value.

. Use the `oc apply` command to create the project:
+
[source,terminal]
----
$ oc apply -f project.yaml
----

Any subsequent resources created in the `<project_name>` namespace should now be scheduled on the specified nodes.
