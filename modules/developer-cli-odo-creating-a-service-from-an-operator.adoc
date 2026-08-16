// Module included in the following assemblies:
//
// * cli_reference/developer_cli_odo/creating-instances-of-services-managed-by-the-operators.adoc

[id="creating-a-service-from-an-operator_{context}"]

= Creating a service from an Operator

If an Operator has valid values defined in its `metadata` to start the requested service, you can use the service with `odo service create`.

. Print the YAML of the service as a file on your local drive:
+
[source,terminal]
----
$ oc get csv/etcdoperator.v0.9.4 -o yaml
----

. Verify that the values of the service are valid:
+
[source,terminal]
----
apiVersion: etcd.database.coreos.com/v1beta2
kind: EtcdCluster
metadata:
  name: example
spec:
  size: 3
  version: 3.2.13
----

. Start an `EtcdCluster` service from the `etcdoperator.v0.9.4` Operator:
+
[source,terminal]
----
$ odo service create etcdoperator.v0.9.4 EtcdCluster
----

. Verify that a service has started:
+
[source,terminal]
----
$ oc get EtcdCluster
----
