// Module included in the following assemblies:
//
// * service_mesh/v1x/customizing-installation-ossm.adoc

[id="ossm-cr-example-1x_{context}"]
= {SMProductName} custom resources

[NOTE]
====
The `istio-system` project is used as an example throughout the {SMProductShortName} documentation, but you can use other projects as necessary.
====

A _custom resource_ allows you to extend the API in an {SMProductName} project or cluster. When you deploy {SMProductShortName} it creates a default `ServiceMeshControlPlane` that you can modify to change the project parameters.

The {SMProductShortName} operator extends the API by adding the `ServiceMeshControlPlane` resource type, which enables you to create `ServiceMeshControlPlane` objects within projects. By creating a `ServiceMeshControlPlane` object, you instruct the Operator to install a {SMProductShortName} control plane into the project, configured with the parameters you set in the `ServiceMeshControlPlane` object.

This example `ServiceMeshControlPlane` definition contains all of the supported parameters and deploys {SMProductName} {SMProductVersion1x} images based on Red Hat Enterprise Linux (RHEL).

[IMPORTANT]
====
The 3scale Istio Adapter is deployed and configured in the custom resource file. It also requires a working 3scale account (link:https://www.3scale.net/signup/[SaaS] or link:https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.4/html/infrastructure/onpremises-installation[On-Premises]).
====

.Example istio-installation.yaml

[source,yaml]
----
apiVersion: maistra.io/v1
kind: ServiceMeshControlPlane
metadata:
  name: basic-install
spec:

  istio:
    global:
      proxy:
        resources:
          requests:
            cpu: 100m
            memory: 128Mi
          limits:
            cpu: 500m
            memory: 128Mi

    gateways:
      istio-egressgateway:
        autoscaleEnabled: false
      istio-ingressgateway:
        autoscaleEnabled: false
        ior_enabled: false

    mixer:
      policy:
        autoscaleEnabled: false

      telemetry:
        autoscaleEnabled: false
        resources:
          requests:
            cpu: 100m
            memory: 1G
          limits:
            cpu: 500m
            memory: 4G

    pilot:
      autoscaleEnabled: false
      traceSampling: 100

    kiali:
      enabled: true

    grafana:
      enabled: true

    tracing:
      enabled: true
      jaeger:
        template: all-in-one
----
