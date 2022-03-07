== Supported metrics

KEDA emits the following Kubernetes events:

.Metrics
[cols="3a,5a,5a",options="header"]
|===

|Metric |Description |API version

|ScaledObjectReady
|Normal
|On the first time a ScaledObject is ready, or if the previous ready condition status of the object was Unknown or False

|ScaledJobReady
|Normal
|On the first time a ScaledJob is ready, or if the previous ready condition status of the object was Unknown or False

|ScaledObjectCheckFailed
|Warning
|If the check validation for a ScaledObject fails

|ScaledJobCheckFailed
|Warning
|If the check validation for a ScaledJob fails

|ScaledObjectDeleted
|Normal
|When a ScaledObject is deleted and removed from KEDA watch

|ScaledJobDeleted
|Normal
|When a ScaledJob is deleted and removed from KEDA watch

|KEDAScalersStarted
|Normal
|When Scalers watch loop have started for a ScaledObject or ScaledJob

|KEDAScalersStopped
|Normal
|When Scalers watch loop have stopped for a ScaledObject or a ScaledJob

|KEDAScalerFailed
|Warning
|When a Scaler fails to create or check its event source

|KEDAScaleTargetActivated
|Normal
|When the scale target (Deployment, StatefulSet, etc) of a ScaledObject is scaled to 1

|KEDAScaleTargetDeactivated
|Normal
|When the scale target (Deployment, StatefulSet, etc) of a ScaledObject is scaled to 0

|KEDAScaleTargetActivationFailed
|Warning
|When KEDA fails to scale the scale target of a ScaledObject to 1

|KEDAScaleTargetDeactivationFailed
|Warning
|When KEDA fails to scale the scale target of a ScaledObject to 0

|KEDAJobsCreated
|Normal
|When KEDA creates jobs for a ScaledJob

|TriggerAuthenticationAdded
|Normal
|When a new TriggerAuthentication is added

|TriggerAuthenticationDeleted
|Normal
|When a TriggerAuthentication is deleted

|ClusterTriggerAuthenticationAdded
|Normal
|When a new ClusterTriggerAuthentication is added

|ClusterTriggerAuthenticationDeleted
|Normal
|When a ClusterTriggerAuthentication is deleted

|===
