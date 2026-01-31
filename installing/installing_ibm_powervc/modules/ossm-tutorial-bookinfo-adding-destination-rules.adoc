////
This PROCEDURE module included in the following assemblies:
* service_mesh/v1x/prepare-to-deploy-applications-ossm.adoc
* service_mesh/v2x/prepare-to-deploy-applications-ossm.adoc
////

:_mod-docs-content-type: PROCEDURE
[id="ossm-tutorial-bookinfo-adding-destination-rules_{context}"]
= Adding default destination rules

Before you can use the Bookinfo application, you must first add default destination rules. There are two preconfigured YAML files, depending on whether or not you enabled mutual transport layer security (TLS) authentication.

.Procedure

. To add destination rules, run one of the following commands:
** If you did not enable mutual TLS:
+

[source,bash,subs="attributes"]
----
$ oc apply -n bookinfo -f https://raw.githubusercontent.com/Maistra/istio/maistra-{MaistraVersion}/samples/bookinfo/networking/destination-rule-all.yaml
----
+
** If you enabled mutual TLS:
+

[source,bash,subs="attributes"]
----
$ oc apply -n bookinfo -f https://raw.githubusercontent.com/Maistra/istio/maistra-{MaistraVersion}/samples/bookinfo/networking/destination-rule-all-mtls.yaml
----
+
You should see output similar to the following:
+
[source,terminal]
----
destinationrule.networking.istio.io/productpage created
destinationrule.networking.istio.io/reviews created
destinationrule.networking.istio.io/ratings created
destinationrule.networking.istio.io/details created
----
