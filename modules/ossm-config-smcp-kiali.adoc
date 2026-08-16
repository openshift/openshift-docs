// Module included in the following assemblies:
//* service_mesh/v2x/ossm-reference-kiali.adoc
:_mod-docs-content-type: REFERENCE
[id="ossm-smcp-kiali_{context}"]
= Specifying Kiali configuration in the SMCP

You can configure Kiali under the `addons` section of the `ServiceMeshControlPlane` resource. Kiali is enabled by default. To disable Kiali, set `spec.addons.kiali.enabled` to `false`.

You can specify your Kiali configuration in either of two ways:

* Specify the Kiali configuration in the `ServiceMeshControlPlane` resource under `spec.addons.kiali.install`. This approach has some limitations, because the complete list of Kiali configurations is not available in the SMCP.

* Configure and deploy a Kiali instance and specify the name of the Kiali resource as the value for `spec.addons.kiali.name` in the `ServiceMeshControlPlane` resource. You must create the CR in the same namespace as the {SMProductShortName} control plane, for example, `istio-system`. If a Kiali resource matching the value of `name` exists, the control plane will configure that Kiali resource for use with the control plane. This approach lets you fully customize your Kiali configuration in the Kiali resource. Note that with this approach, various fields in the Kiali resource are overwritten by the {SMProductShortName} Operator, specifically, the `accessible_namespaces` list, as well as the endpoints for Grafana, Prometheus, and tracing.

.Example SMCP parameters for Kiali
[source,yaml]
----
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: basic
spec:
  addons:
    kiali:
      name: kiali
      enabled: true
      install:
        dashboard:
          viewOnly: false
          enableGrafana: true
          enableTracing: true
          enablePrometheus: true
        service:
          ingress:
            contextPath: /kiali
----

.`ServiceMeshControlPlane` Kiali parameters
[options="header"]
[cols="l, a, a, a"]
|===
|Parameter |Description |Values |Default value
|spec:
  addons:
    kiali:
      name:
|Name of Kiali custom resource. If a Kiali CR matching the value of `name` exists, the {SMProductShortname} Operator will use that CR for the installation. If no Kiali CR exists, the Operator will create one using this `name` and the configuration options specified in the SMCP.
|string
|`kiali`

|kiali:
  enabled:
|This parameter enables or disables Kiali. Kiali is enabled by default.
|`true`/`false`
|`true`

|kiali:
  install:
|Install a Kiali resource if the named Kiali resource is not present. The `install` section is ignored if `addons.kiali.enabled` is set to `false`.
|
|

|kiali:
  install:
    dashboard:
|Configuration parameters for the dashboards shipped with Kiali.
|
|

|kiali:
  install:
    dashboard:
      viewOnly:
|This parameter enables or disables view-only mode for the Kiali console. When view-only mode is enabled, users cannot use the Kiali console to make changes to the {SMProductShortname}.
|`true`/`false`
|`false`

|kiali:
  install:
    dashboard:
      enableGrafana:
|Grafana endpoint configured based on `spec.addons.grafana` configuration.
|`true`/`false`
|`true`

|kiali:
  install:
    dashboard:
      enablePrometheus:
|Prometheus endpoint configured based on `spec.addons.prometheus` configuration.
|`true`/`false`
|`true`

|kiali:
  install:
    dashboard:
      enableTracing:
|Tracing endpoint configured based on Jaeger custom resource configuration.
|`true`/`false`
|`true`

|kiali:
  install:
    service:
|Configuration parameters for the Kubernetes service associated with the Kiali installation.
|
|

|kiali:
  install:
    service:
      metadata:
|Use to specify additional metadata to apply to resources.
|N/A
|N/A

|kiali:
  install:
    service:
      metadata:
        annotations:
|Use to specify additional annotations to apply to the component's service.
|string
|N/A

|kiali:
  install:
    service:
      metadata:
        labels:
|Use to specify additional labels to apply to the component's service.
|string
|N/A

|kiali:
  install:
    service:
      ingress:
|Use to specify details for accessing the component’s service through an OpenShift Route.
|N/A
|N/A

|kiali:
  install:
    service:
      ingress:
        metadata:
          annotations:
|Use to specify additional annotations to apply to the component's service ingress.
|string
|N/A

|kiali:
  install:
    service:
      ingress:
        metadata:
          labels:
|Use to specify additional labels to apply to the component's service ingress.
|string
|N/A

|kiali:
  install:
    service:
      ingress:
        enabled:
|Use to customize an OpenShift Route for the service associated with a component.
|`true`/`false`
|`true`

|kiali:
  install:
    service:
      ingress:
        contextPath:
|Use to specify the context path to the service.
|string
|N/A

|install:
  service:
    ingress:
      hosts:
|Use to specify a single hostname per OpenShift route. An empty hostname implies a default hostname for the Route.
|string
|N/A

|install:
  service:
    ingress:
      tls:
|Use to configure the TLS for the OpenShift route.
|
|N/A

|kiali:
  install:
    service:
      nodePort:
|Use to specify the `nodePort` for the component's service `Values.<component>.service.nodePort.port`
|integer
|N/A
|===
