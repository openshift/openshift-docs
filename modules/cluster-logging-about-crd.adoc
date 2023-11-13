// Module included in the following assemblies:
//
// * logging/cluster-logging.adoc

:_mod-docs-content-type: CONCEPT
[id="cluster-logging-about-crd_{context}"]
= About the ClusterLogging custom resource

To make changes to your {logging} environment, create and modify the `ClusterLogging` custom resource (CR).

.Sample `ClusterLogging` custom resource (CR)
[source,yaml]
----
apiVersion: "logging.openshift.io/v1"
kind: "ClusterLogging"
metadata:
  name: "instance" <1>
  namespace: "openshift-logging" <2>
spec:
  managementState: "Managed" <3>
# ...
----
<1> The CR name must be `instance`.
<2> The CR must be installed to the `openshift-logging` namespace.
<3> The Red Hat OpenShift Logging Operator management state. When set to `unmanaged` the operator is in an unsupported state and will not get updates.
