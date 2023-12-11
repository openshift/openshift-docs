// This is included in the following assemblies:
//
// networking/routes/route-configuration.adoc

:_mod-docs-content-type: PROCEDURE
[id="creating-edge-route-with-default-certificate_{context}"]
= Creating a route using the default certificate through an Ingress object

If you create an Ingress object without specifying any TLS configuration, {product-title} generates an insecure route. To create an Ingress object that generates a secure, edge-terminated route using the default ingress certificate, you can specify an empty TLS configuration as follows.

.Prerequisites

* You have a service that you want to expose.
* You have access to the OpenShift CLI (`oc`).

.Procedure

. Create a YAML file for the Ingress object.  In this example, the file is called `example-ingress.yaml`:
+
.YAML definition of an Ingress object
[source,yaml]
----
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: frontend
  ...
spec:
  rules:
    ...
  tls:
  - {} <1>
----
+
<1> Use this exact syntax to specify TLS without specifying a custom certificate.

. Create the Ingress object by running the following command:
+
[source,terminal]
----
$ oc create -f example-ingress.yaml
----

.Verification
* Verify that {product-title} has created the expected route for the Ingress object by running the following command:
+
[source,terminal]
----
$ oc get routes -o yaml
----
+
.Example output
[source,yaml]
----
apiVersion: v1
items:
- apiVersion: route.openshift.io/v1
  kind: Route
  metadata:
    name: frontend-j9sdd <1>
    ...
  spec:
  ...
    tls: <2>
      insecureEdgeTerminationPolicy: Redirect
      termination: edge <3>
  ...
----
<1> The name of the route includes the name of the Ingress object followed by a random suffix.
<2> In order to use the default certificate, the route should not specify `spec.certificate`.
<3> The route should specify the `edge` termination policy.
