////
Module included in the following assemblies:
* service_mesh/v1x/servicemesh-release-notes.adoc
////

[id="ossm-rn-known-issues-1x_{context}"]
= Known issues

////
*Consequence* - What user action or situation would make this problem appear (Selecting the Foo option with the Bar version 1.3 plugin enabled results in an error message)?  What did the customer experience as a result of the issue? What was the symptom?
*Cause* (if it has been identified) - Why did this happen?
*Workaround* (If there is one)- What can you do to avoid or negate the effects of this issue in the meantime?  Sometimes if there is no workaround it is worthwhile telling readers to contact support for advice. Never promise future fixes.
*Result* - If the workaround does not completely address the problem.
////

These limitations exist in {SMProductName}:

* link:https://github.com/istio/old_issues_repo/issues/115[{SMProductName} does not support IPv6], as it is not supported by the upstream Istio project, nor fully supported by {product-title}.

* Graph layout - The layout for the Kiali graph can render differently, depending on your application architecture and the data to display (number of graph nodes and their interactions). Because it is difficult if not impossible to create a single layout that renders nicely for every situation, Kiali offers a choice of several different layouts. To choose a different layout, you can choose a different *Layout Schema* from the *Graph Settings* menu.

* The first time you access related services such as Jaeger and Grafana, from the Kiali console, you must accept the certificate and re-authenticate using your {product-title} login credentials. This happens due to an issue with how the framework displays embedded pages in the console.

[id="ossm-rn-known-issues-ossm_{context}"]
== {SMProductShortName} known issues

These are the known issues in {SMProductName}:

* link:https://access.redhat.com/solutions/4970771[Jaeger/Kiali Operator upgrade blocked with operator pending] When upgrading the Jaeger or Kiali Operators with Service Mesh 1.0.x installed, the operator status shows as Pending.
+
Workaround: See the linked Knowledge Base article for more information.

* link:https://github.com/istio/istio/issues/14743[Istio-14743] Due to limitations in the version of Istio that this release of {SMProductName} is based on, there are several applications that are currently incompatible with {SMProductShortName}. See the linked community issue for details.

* link:https://issues.jboss.org/browse/MAISTRA-858[MAISTRA-858] The following Envoy log messages describing link:https://www.envoyproxy.io/docs/envoy/latest/intro/deprecated[deprecated options and configurations associated with Istio 1.1.x] are expected:
+
** [2019-06-03 07:03:28.943][19][warning][misc] [external/envoy/source/common/protobuf/utility.cc:129] Using deprecated option 'envoy.api.v2.listener.Filter.config'. This configuration will be removed from Envoy soon.
** [2019-08-12 22:12:59.001][13][warning][misc] [external/envoy/source/common/protobuf/utility.cc:174] Using deprecated option 'envoy.api.v2.Listener.use_original_dst' from file lds.proto. This configuration will be removed from Envoy soon.

* link:https://issues.jboss.org/browse/MAISTRA-806[MAISTRA-806] Evicted Istio Operator Pod causes mesh and CNI not to deploy.
+
Workaround: If the `istio-operator` pod is evicted while deploying the control pane, delete the evicted `istio-operator` pod.
+
* link:https://issues.jboss.org/browse/MAISTRA-681[MAISTRA-681] When the control plane has many namespaces, it can lead to performance issues.

* link:https://issues.jboss.org/browse/MAISTRA-465[MAISTRA-465] The Maistra Operator fails to create a service for operator metrics.

* link:https://issues.jboss.org/browse/MAISTRA-453[MAISTRA-453] If you create a new project and deploy pods immediately, sidecar injection does not occur. The operator fails to add the `maistra.io/member-of` before the pods are created, therefore the pods must be deleted and recreated for sidecar injection to occur.

* link:https://issues.jboss.org/browse/MAISTRA-158[MAISTRA-158] Applying multiple gateways referencing the same hostname will cause all gateways to stop functioning.



[id="ossm-rn-known-issues-kiali_{context}"]
== Kiali known issues

[NOTE]
====
New issues for Kiali should be created in the link:https://issues.redhat.com/projects/OSSM/[OpenShift Service Mesh]  project with the `Component` set to `Kiali`.
====

These are the known issues in Kiali:

* link:https://issues.jboss.org/browse/KIALI-2206[KIALI-2206] When you are accessing the Kiali console for the first time, and there is no cached browser data for Kiali, the “View in Grafana” link on the Metrics tab of the Kiali Service Details page redirects to the wrong location. The only way you would encounter this issue is if you are accessing Kiali for the first time.

* link:https://github.com/kiali/kiali/issues/507[KIALI-507] Kiali does not support Internet Explorer 11. This is because the underlying frameworks do not support Internet Explorer. To access the Kiali console, use one of the two most recent versions of the Chrome, Edge, Firefox or Safari browser.
