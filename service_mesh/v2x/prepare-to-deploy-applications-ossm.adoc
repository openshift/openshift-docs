:_mod-docs-content-type: ASSEMBLY
[id="deploying-applications-ossm"]
= Enabling sidecar injection
include::_attributes/common-attributes.adoc[]
:context: deploying-applications-ossm

toc::[]

After adding the namespaces that contain your services to your mesh, the next step is to enable automatic sidecar injection in the Deployment resource for your application. You must enable automatic sidecar injection for each deployment.

If you have installed the Bookinfo sample application, the application was deployed and the sidecars were injected as part of the installation procedure. If you are using your own project and service, deploy your applications on {product-title}.

ifdef::openshift-enterprise[]
For more information, see the {product-title} documentation, xref:../../applications/deployments/what-deployments-are.adoc[Understanding deployments].
endif::[]

[NOTE]
====
Traffic started by Init Containers, specialized containers that run before the application containers in a pod, cannot travel outside of the service mesh by default. Any action Init Containers perform that requires establishing a network traffic connection outside of the mesh fails.

For more information about connecting Init Containers to a service, see the Red Hat Knowledgebase solution link:https://access.redhat.com/solutions/6653601[initContainer in CrashLoopBackOff on pod with Service Mesh sidecar injected]
====

== Prerequisites

* xref:../../service_mesh/v2x/ossm-create-mesh.adoc#ossm-tutorial-bookinfo-overview_ossm-create-mesh[Services deployed to the mesh], for example the Bookinfo sample application.

* A Deployment resource file.

include::modules/ossm-automatic-sidecar-injection.adoc[leveloffset=+1]

include::modules/ossm-sidecar-validate-kiali.adoc[leveloffset=+1]

For information about enabling Envoy access logs, see the xref:../../service_mesh/v2x/ossm-troubleshooting-istio.adoc#enabling-envoy-access-logs[Troubleshooting] section.

For information about viewing Envoy logs, see xref:../../service_mesh/v2x/ossm-observability.adoc#ossm-viewing-logs_observability[Viewing logs in the Kiali console]

include::modules/ossm-sidecar-injection-env-var.adoc[leveloffset=+1]

include::modules/ossm-update-app-sidecar.adoc[leveloffset=+1]

== Next steps

Configure {SMProductName} features for your environment.

* xref:../../service_mesh/v2x/ossm-security.adoc#ossm-security[Security]
* xref:../../service_mesh/v2x/ossm-traffic-manage.adoc#ossm-routing-traffic[Traffic management]
* xref:../../service_mesh/v2x/ossm-observability.adoc#ossm-observability[Metrics, logs, and traces]
