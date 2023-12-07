// Module included in the following assemblies:
//
// * support/troubleshooting/investigating-pod-issues.adoc

:_mod-docs-content-type: CONCEPT
[id="understanding-pod-error-states_{context}"]
= Understanding pod error states

Pod failures return explicit error states that can be observed in the `status` field in the output of `oc get pods`. Pod error states cover image, container, and container network related failures.

The following table provides a list of pod error states along with their descriptions.

.Pod error states
[cols="1,4",options="header"]
|===
| Pod error state | Description

| `ErrImagePull`
|	Generic image retrieval error.

| `ErrImagePullBackOff`
| Image retrieval failed and is backed off.

| `ErrInvalidImageName`
| The specified image name was invalid.

| `ErrImageInspect`
| Image inspection did not succeed.

| `ErrImageNeverPull`
| `PullPolicy` is set to `NeverPullImage` and the target image is not present locally on the host.

| `ErrRegistryUnavailable`
| When attempting to retrieve an image from a registry, an HTTP error was encountered.

| `ErrContainerNotFound`
| The specified container is either not present or not managed by the kubelet, within the declared pod.

| `ErrRunInitContainer`
| Container initialization failed.

| `ErrRunContainer`
| None of the pod's containers started successfully.

| `ErrKillContainer`
| None of the pod's containers were killed successfully.

| `ErrCrashLoopBackOff`
| A container has terminated. The kubelet will not attempt to restart it.

| `ErrVerifyNonRoot`
| A container or image attempted to run with root privileges.

| `ErrCreatePodSandbox`
| Pod sandbox creation did not succeed.

| `ErrConfigPodSandbox`
| Pod sandbox configuration was not obtained.

| `ErrKillPodSandbox`
| A pod sandbox did not stop successfully.

| `ErrSetupNetwork`
| Network initialization failed.

| `ErrTeardownNetwork`
| Network termination failed.
|===
