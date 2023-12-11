// Modules included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-ingress-setting-max-connections_{context}"]
= Setting the Ingress Controller maximum connections
A cluster administrator can set the maximum number of simultaneous connections for OpenShift router deployments. You can patch an existing Ingress Controller to increase the maximum number of connections.

.Prerequisites
* The following assumes that you already created an Ingress Controller

.Procedure
* Update the Ingress Controller to change the maximum number of connections for HAProxy:
+
[source,terminal]
----
$ oc -n openshift-ingress-operator patch ingresscontroller/default --type=merge -p '{"spec":{"tuningOptions": {"maxConnections": 7500}}}'
----
+
[WARNING]
====
If you set the `spec.tuningOptions.maxConnections` value greater than the current operating system limit, the HAProxy process will not start. See the table in the "Ingress Controller configuration parameters" section for more information about this parameter.
====
