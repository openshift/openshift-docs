// Module included in the following assemblies:
//
// * migrating_from_ocp_3_to_4/installing-3-4.adoc
// * migrating_from_ocp_3_to_4/installing-restricted-3-4.adoc
// * migration_toolkit_for_containers/installing-mtc.adoc
// * migration_toolkit_for_containers/installing-mtc-restricted.adoc

:_mod-docs-content-type: PROCEDURE
[id="migration-configuring-proxies_{context}"]
= Configuring proxies

.Prerequisites

* You must be logged in as a user with `cluster-admin` privileges on all clusters.

.Procedure

. Get the `MigrationController` CR manifest:
+
[source,terminal]
----
$ oc get migrationcontroller <migration_controller> -n openshift-migration
----

. Update the proxy parameters:
+
[source,yaml]
----
apiVersion: migration.openshift.io/v1alpha1
kind: MigrationController
metadata:
  name: <migration_controller>
  namespace: openshift-migration
...
spec:
  stunnel_tcp_proxy: http://<username>:<password>@<ip>:<port> <1>
  noProxy: example.com <2>
----
<1> Stunnel proxy URL for direct volume migration.
<2> Comma-separated list of destination domain names, domains, IP addresses, or other network CIDRs to exclude proxying.
+
Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass proxy for all destinations.
If you scale up workers that are not included in the network defined by the `networking.machineNetwork[].cidr` field from the installation configuration, you must add them to this list to prevent connection issues.
+
This field is ignored if neither the `httpProxy` nor the `httpsProxy` field is set.

. Save the manifest as `migration-controller.yaml`.
. Apply the updated manifest:
+
[source,terminal]
----
$ oc replace -f migration-controller.yaml -n openshift-migration
----
