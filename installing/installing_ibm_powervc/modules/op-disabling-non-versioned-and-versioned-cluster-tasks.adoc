// This module is part of the following assembly:
//
// *cicd/pipelines/managing-nonversioned-and-versioned-cluster-tasks.adoc
:_mod-docs-content-type: PROCEDURE
[id="disabling-non-versioned-and-versioned-cluster-tasks_{context}"]
= Disabling non-versioned and versioned cluster tasks

As a cluster administrator, you can disable cluster tasks that the {pipelines-shortname} Operator installed.

.Procedure

. To delete all non-versioned cluster tasks and latest versioned cluster tasks, edit the `TektonConfig` custom resource definition (CRD) and set the `clusterTasks` parameter in `spec.addon.params` to `false`.
+
.Example `TektonConfig` CR
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonConfig
metadata:
  name: config
spec:
  params:
  - name: createRbacResource
    value: "false"
  profile: all
  targetNamespace: openshift-pipelines
  addon:
    params:
    - name: clusterTasks
      value: "false"
...
----
+
When you disable cluster tasks, the Operator removes all the non-versioned cluster tasks and only the latest version of the versioned cluster tasks from the cluster.
+
[NOTE]
====
Re-enabling cluster tasks installs the non-versioned cluster tasks.
====

. Optional: To delete earlier versions of the versioned cluster tasks, use any one of the following methods:
.. To delete individual earlier versioned cluster tasks, use the `oc delete clustertask` command followed by the versioned cluster task name. For example:
+
[source,terminal]
----
$ oc delete clustertask buildah-1-6-0
----
.. To delete all versioned cluster tasks created by an old version of the Operator, you can delete the corresponding installer set. For example:
+
[source,terminal]
----
$ oc delete tektoninstallerset versioned-clustertask-1-6-k98as
----
+
[CAUTION]
====
If you delete an old versioned cluster task, you cannot restore it. You can only restore versioned and non-versioned cluster tasks that the current version of the Operator has created.
====

