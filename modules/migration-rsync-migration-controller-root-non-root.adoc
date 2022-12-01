// Module included in the following assemblies:
//
// * migration_toolkit_for_containers/installing-mtc.adoc
// * migration_toolkit_for_containers/installing-mtc-restricted.adoc
[id="migration-rsync-migration-controller-root-non-root_{context}"]
== Configuring the MigrationController CR as root or non-root for all migrations

By default, Rsync runs as non-root.

On the destination cluster, you can configure the `MigrationController` CR to run Rsync as root.

.Procedure

* Configure the `MigrationController` CR as follows:
+
[source,yaml]
----
apiVersion: migration.openshift.io/v1alpha1
kind: MigrationController
metadata:
  name: migration-controller
  namespace: openshift-migration
spec:
  [...]
  migration_rsync_privileged: true
----
+
This configuration will apply to all future migrations.
