// Module included in the following assemblies:
//
// * service_mesh/v1x/customizing-installation-ossm.adoc
// * service_mesh/v2x/customizing-installation-ossm.adoc

[id="ossm-cr-istio-global_{context}"]
= Istio global example

Here is an example that illustrates the Istio global parameters for the `ServiceMeshControlPlane` and a description of the available parameters with appropriate values.

[NOTE]
====
In order for the 3scale Istio Adapter to work, `disablePolicyChecks` must be `false`.
====

.Example global parameters
[source,yaml]
----
  istio:
    global:
      tag: 1.1.0
      hub: registry.redhat.io/openshift-service-mesh/
      proxy:
        resources:
          requests:
            cpu: 10m
            memory: 128Mi
          limits:
      mtls:
        enabled: false
      disablePolicyChecks: true
      policyCheckFailOpen: false
      imagePullSecrets:
        - MyPullSecret
----

.Global parameters
|===
|Parameter |Description |Values |Default value

|`disablePolicyChecks`
|This parameter enables/disables policy checks.
|`true`/`false`
|`true`

|`policyCheckFailOpen`
|This parameter indicates whether traffic is allowed to pass through to the Envoy sidecar when the Mixer policy service cannot be reached.
|`true`/`false`
|`false`

|`tag`
|The tag that the Operator uses to pull the Istio images.
|A valid container image tag.
|`1.1.0`

|`hub`
|The hub that the Operator uses to pull Istio images.
|A valid image repository.
|`maistra/` or `registry.redhat.io/openshift-service-mesh/`

|`mtls`
|This parameter controls whether to enable/disable Mutual Transport Layer Security (mTLS) between services by default.
|`true`/`false`
|`false`

|`imagePullSecrets`
|If access to the registry providing the Istio images is secure, list an link:https://kubernetes.io/docs/concepts/containers/images/#specifying-imagepullsecrets-on-a-pod[imagePullSecret] here.
|redhat-registry-pullsecret OR quay-pullsecret
|None
|===

These parameters are specific to the proxy subset of global parameters.

.Proxy parameters
|===
|Type |Parameter |Description |Values |Default value

|`requests`
|`cpu`
|The amount of CPU resources requested for Envoy proxy.
|CPU resources, specified in cores or millicores (for example, 200m, 0.5, 1) based on your environment's configuration.
|`10m`

|
|`memory`
|The amount of memory requested for Envoy proxy
|Available memory in bytes(for example, 200Ki, 50Mi, 5Gi) based on your environment's configuration.
|`128Mi`

|Limits
|`cpu`
|The maximum amount of CPU resources requested for Envoy proxy.
|CPU resources, specified in cores or millicores (for example, 200m, 0.5, 1) based on your environment's configuration.
|`2000m`

|
|`memory`
|The maximum amount of memory Envoy proxy is permitted to use.
|Available memory in bytes (for example, 200Ki, 50Mi, 5Gi) based on your environment's configuration.
|`1024Mi`
|===
