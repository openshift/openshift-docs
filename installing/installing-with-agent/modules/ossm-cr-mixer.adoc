// Module included in the following assemblies:
//
// * service_mesh/v2x/customizing-installation-ossm.adoc

[id="ossm-cr-mixer_{context}"]
= Istio Mixer configuration

Here is an example that illustrates the Mixer parameters for the `ServiceMeshControlPlane` and a description of the available parameters with appropriate values.

.Example mixer parameters
[source,yaml]
----
mixer:
  enabled: true
  policy:
    autoscaleEnabled: false
  telemetry:
    autoscaleEnabled: false
    resources:
    requests:
      cpu: 10m
      memory: 128Mi
      limits:
----


.Istio Mixer policy parameters
|===
|Parameter |Description |Values |Default value

|`enabled`
|This parameter enables/disables Mixer.
|`true`/`false`
|`true`

|`autoscaleEnabled`
|This parameter enables/disables autoscaling. Disable this for small environments.
|`true`/`false`
|`true`

|`autoscaleMin`
|The minimum number of pods to deploy based on the `autoscaleEnabled` setting.
|A valid number of allocatable pods based on your environment's configuration.
|`1`

|`autoscaleMax`
|The maximum number of pods to deploy based on the `autoscaleEnabled` setting.
|A valid number of allocatable pods based on your environment's configuration.
|`5`
|===


.Istio Mixer telemetry parameters
|===
|Type |Parameter |Description |Values |Default

|`requests`
|`cpu`
|The percentage of CPU resources requested for Mixer telemetry.
|CPU resources in millicores based on your environment's configuration.
|`10m`

|
|`memory`
|The amount of memory requested for Mixer telemetry.
|Available memory in bytes (for example, 200Ki, 50Mi, 5Gi) based on your environment's configuration.
|`128Mi`

|`limits`
|`cpu`
|The maximum percentage of CPU resources Mixer telemetry is permitted to use.
|CPU resources in millicores based on your environment's configuration.
|`4800m`

|
|`memory`
|The maximum amount of memory Mixer telemetry is permitted to use.
|Available memory in bytes (for example, 200Ki, 50Mi, 5Gi) based on your environment's configuration.
|`4G`
|===
