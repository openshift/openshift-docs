// Module included in the following assemblies:
//
// * networking/routes/route-configuration.adoc

:_mod-docs-content-type: PROCEDURE
[id="nw-creating-a-route_{context}"]
= Creating an HTTP-based route

A route allows you to host your application at a public URL. It can either be secure or unsecured, depending on the network security configuration of your application. An HTTP-based route is an unsecured route that uses the basic HTTP routing protocol and exposes a service on an unsecured application port.

The following procedure describes how to create a simple HTTP-based route to a web application, using the `hello-openshift` application as an example.
//link:https://github.com/openshift/origin/tree/master/examples/hello-openshift[hello-openshift]

.Prerequisites


* You installed the OpenShift CLI (`oc`).
* You are logged in as an administrator.
* You have a web application that exposes a port and a TCP endpoint listening for traffic on the port.

.Procedure

. Create a project called `hello-openshift` by running the following command:
+
[source,terminal]
----
$ oc new-project hello-openshift
----

. Create a pod in the project by running the following command:
+
[source,terminal]
----
$ oc create -f https://raw.githubusercontent.com/openshift/origin/master/examples/hello-openshift/hello-pod.json
----

. Create a service called `hello-openshift` by running the following command:
+
[source,terminal]
----
$ oc expose pod/hello-openshift
----

. Create an unsecured route to the `hello-openshift` application by running the following command:
+
[source,terminal]
----
$ oc expose svc hello-openshift
----

.Verification

* To verify that the `route` resource that you created, run the following command:
+
[source,terminal]
----
$ oc get routes -o yaml <name of resource> <1>
----
<1> In this example, the route is named `hello-openshift`.

.Sample YAML definition of the created unsecured route:
[source,yaml]
----
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: hello-openshift
spec:
  host: hello-openshift-hello-openshift.<Ingress_Domain> <1>
  port:
    targetPort: 8080 <2>
  to:
    kind: Service
    name: hello-openshift
----
<1> `<Ingress_Domain>` is the default ingress domain name. The `ingresses.config/cluster` object is created during the installation and cannot be changed. If you want to specify a different domain, you can specify an alternative cluster domain using the `appsDomain` option.
<2> `targetPort` is the target port on pods that is selected by the service that this route points to.

+
[NOTE]
====
To display your default ingress domain, run the following command:
[source,terminal]
----
$ oc get ingresses.config/cluster -o jsonpath={.spec.domain}
----
====
