// Module included in the following assemblies:
//
// * machine_management/cpmso-disabling.adoc

:_mod-docs-content-type: PROCEDURE
[id="cpmso-deleting_{context}"]
= Deleting the control plane machine set

To stop managing control plane machines with the control plane machine set on your cluster, you must delete the `ControlPlaneMachineSet` custom resource (CR).

.Procedure

* Delete the control plane machine set CR by running the following command:
+
[source,terminal]
----
$ oc delete controlplanemachineset.machine.openshift.io cluster \
  -n openshift-machine-api
----

.Verification

* Check the control plane machine set custom resource state. A result of `Inactive` indicates that the removal and replacement process is successful. A `ControlPlaneMachineSet` CR exists but is not activated.
