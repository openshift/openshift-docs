// Module included in the following assemblies:
//
// * service_mesh/v1x/customizing-installation-ossm.adoc

[id="ossm-cr-pilot-1x_{context}"]
= Istio Pilot configuration

Here is an example that illustrates the Istio Pilot parameters for the `ServiceMeshControlPlane` and a description of the available parameters with appropriate values.

.Example pilot parameters
[source,yaml]
----
  pilot:
    resources:
      requests:
        cpu: 100m
        memory: 128Mi
    autoscaleEnabled: false
    traceSampling: 100
----

.Istio Pilot parameters
|===
|Parameter |Description |Values |Default value

|`cpu`
|The percentage of CPU resources requested for Pilot.
|CPU resources in millicores based on your environment's configuration.
|`10m`

|`memory`
|The amount of memory requested for Pilot.
|Available memory in bytes (for example, 200Ki, 50Mi, 5Gi) based on your environment's configuration.
|`128Mi`

|`autoscaleEnabled`
|This parameter enables/disables autoscaling. Disable this for small environments.
|`true`/`false`
|`true`


|`traceSampling`
|This value controls how often random sampling occurs. *Note:* Increase for development or testing.
|A valid percentage.
|`1.0`
|===
