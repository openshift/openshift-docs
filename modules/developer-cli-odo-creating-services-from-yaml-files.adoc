// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/creating-instances-of-services-managed-by-the-operators.adoc

[id="creating-services-from-yaml-files_{context}"]

= Creating services from YAML files

If the YAML definition of the service or custom resource (CR) has invalid or placeholder data, you can use the `--dry-run` flag to get the YAML definition, specify the correct values, and start the service using the corrected YAML definition.
Printing and modifying the YAML used to start a service
`{odo-title}` provides the feature to print the YAML definition of the service or CR provided by the Operator before starting a service.

. To display the YAML of the service, run:
+
[source,terminal]
----
$ odo service create <operator-name> --dry-run
----
+
For example, to print YAML definition of `EtcdCluster` provided by the `etcdoperator.v0.9.4` Operator, run:
+
[source,terminal]
----
$ odo service create etcdoperator.v0.9.4 --dry-run
----
+
The YAML is saved as the `etcd.yaml` file.

. Modify the `etcd.yaml` file:
+
[source,yaml]
----
apiVersion: etcd.database.coreos.com/v1beta2
kind: EtcdCluster
metadata:
  name: my-etcd-cluster // <1>
spec:
  size: 1 // <2>
  version: 3.2.13
----
+
<1> Change the name from `example` to `my-etcd-cluster`
<2> Reduce the size from `3` to `1`

. Start a service from the YAML file:
+
[source,terminal]
----
$ odo service create --from-file etcd.yaml
----

. Verify that the `EtcdCluster` service has started with one pod instead of the preconfigured three pods:
+
[source,terminal]
----
$ oc get pods | grep my-etcd-cluster
----
