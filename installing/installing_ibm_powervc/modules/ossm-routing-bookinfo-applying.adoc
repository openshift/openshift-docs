:_mod-docs-content-type: PROCEDURE
[id="ossm-routing-bookinfo-applying_{context}"]
= Applying a virtual service

In the following procedure, the virtual service routes all traffic to `v1` of each micro-service by applying virtual services that set the default version for the micro-services.

.Procedure

. Apply the virtual services.
+
[source,bash,subs="attributes"]
----
$ oc apply -f https://raw.githubusercontent.com/Maistra/istio/maistra-{MaistraVersion}/samples/bookinfo/networking/virtual-service-all-v1.yaml
----

. To verify that you applied the virtual services, display the defined routes with the following command:
+
[source,terminal]
----
$ oc get virtualservices -o yaml
----
+
That command returns a resource of `kind: VirtualService` in YAML format.

You have configured {SMProductShortName} to route to the `v1` version of the Bookinfo microservices including the `reviews` service version 1.
