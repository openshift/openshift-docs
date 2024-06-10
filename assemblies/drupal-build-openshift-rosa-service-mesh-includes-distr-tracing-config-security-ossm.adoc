////
This module included in the following assemblies:
service_mesh/v2x/ossm-reference-jaeger.adoc
////
:_mod-docs-content-type: CONCEPT
[id="distr-tracing-config-security-ossm_{context}"]
= Configuring distributed tracing security for service mesh

The {JaegerShortName} uses OAuth for default authentication. However {SMProductName} uses a secret called `htpasswd` to facilitate communication between dependent services such as Grafana, Kiali, and the {JaegerShortName}. When you configure your {JaegerShortName} in the `ServiceMeshControlPlane` the {SMProductShortName} automatically configures security settings to use `htpasswd`.

If you are specifying your {JaegerShortName} configuration in a Jaeger custom resource, you must manually configure the `htpasswd` settings and ensure the `htpasswd` secret is mounted into your Jaeger instance so that Kiali can communicate with it.
