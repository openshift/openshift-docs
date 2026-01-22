// Module included in the following assemblies:
//
// * machine_management/machine-phases-lifecycle.adoc

:_mod-docs-content-type: PROCEDURE
[id="machine-determine-phase-gui_{context}"]
= Determining the phase of a machine by using the web console

You can find the phase of a machine by using the {product-title} web console.

.Prerequisites

* You have access to an {product-title} cluster using an account with `cluster-admin` permissions.

.Procedure

. Log in to the web console as a user with the `cluster-admin` role.

. Navigate to *Compute* -> *Machines*.

. On the *Machines* page, select the name of the machine that you want to find the phase of.

. On the *Machine details* page, select the *YAML* tab.

. In the YAML block, find the value of the `status.phase` field.
+
.Example YAML snippet
+
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: Machine
metadata:
  name: mycluster-5kbsp-worker-us-west-1a-fmx8t
# ...
status:
  phase: Running # <1>
----
<1> In this example, the phase is `Running`.