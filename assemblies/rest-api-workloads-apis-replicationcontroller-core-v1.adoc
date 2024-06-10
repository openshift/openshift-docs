[id="replicationcontroller-core-v1"]
= ReplicationController [core/v1]
ifdef::product-title[]
include::_attributes/common-attributes.adoc[]
endif::[]

toc::[]


Description::
+
--
ReplicationController represents the configuration of a replication controller.
--

Type::
  `object`



== Specification

[cols="1,1,1",options="header"]
|===
| Property | Type | Description

| `apiVersion`
| `string`
| APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources

| `kind`
| `string`
| Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds

| `metadata`
| xref:../objects/index.adoc#objectmeta-meta-v1[`ObjectMeta meta/v1`]
| If the Labels of a ReplicationController are empty, they are defaulted to be the same as the Pod(s) that the replication controller manages. Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata

| `spec`
| `object`
| ReplicationControllerSpec is the specification of a replication controller.

| `status`
| `object`
| ReplicationControllerStatus represents the current status of a replication controller.

|===
..spec
Description::
+
--
ReplicationControllerSpec is the specification of a replication controller.
--

Type::
  `object`




[cols="1,1,1",options="header"]
|===
| Property | Type | Description

| `minReadySeconds`
| `integer`
| Minimum number of seconds for which a newly created pod should be ready without any of its container crashing, for it to be considered available. Defaults to 0 (pod will be considered available as soon as it is ready)

| `replicas`
| `integer`
| Replicas is the number of desired replicas. This is a pointer to distinguish between explicit zero and unspecified. Defaults to 1. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller

| `selector`
| `object (string)`
| Selector is a label query over pods that should match the Replicas count. If Selector is empty, it is defaulted to the labels present on the Pod template. Label keys and values that must match in order to be controlled by this replication controller, if empty defaulted to labels on Pod template. More info: https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#label-selectors

| `template`
| `object`
| PodTemplateSpec describes the data a pod should have when created from a template

|===
..spec.template
Description::
+
--
PodTemplateSpec describes the data a pod should have when created from a template
--

Type::
  `object`




[cols="1,1,1",options="header"]
|===
| Property | Type | Description

| `metadata`
| xref:../objects/index.adoc#objectmeta-meta-v1[`ObjectMeta meta/v1`]
| Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata

| `spec`
| `object`
| PodSpec is a description of a pod.

|===
..spec.template.spec
Description::
+
--
PodSpec is a description of a pod.
--

Type::
  `object`

Required::
  - `containers`



[cols="1,1,1",options="header"]
|===
| Property | Type | Description

| `activeDeadlineSeconds`
| `integer`
| Optional duration in seconds the pod may be active on the node relative to StartTime before the system will actively try to mark it failed and kill associated containers. Value must be a positive integer.

| `affinity`
| xref:../objects/index.adoc#affinity-core-v1[`Affinity core/v1`]
| If specified, the pod's scheduling constraints

| `automountServiceAccountToken`
| `boolean`
| AutomountServiceAccountToken indicates whether a service account token should be automatically mounted.

| `containers`
| xref:../objects/index.adoc#container-core-v1[`array (Container core/v1)`]
| List of containers belonging to the pod. Containers cannot currently be added or removed. There must be at least one container in a Pod. Cannot be updated.

| `dnsConfig`
| xref:../objects/index.adoc#poddnsconfig-core-v1[`PodDNSConfig core/v1`]
| Specifies the DNS parameters of a pod. Parameters specified here will be merged to the generated DNS configuration based on DNSPolicy.

| `dnsPolicy`
| `string`
| Set DNS policy for the pod. Defaults to "ClusterFirst". Valid values are 'ClusterFirstWithHostNet', 'ClusterFirst', 'Default' or 'None'. DNS parameters given in DNSConfig will be merged with the policy selected with DNSPolicy. To have DNS options set along with hostNetwork, you have to specify DNS policy explicitly to 'ClusterFirstWithHostNet'.

| `enableServiceLinks`
| `boolean`
| EnableServiceLinks indicates whether information about services should be injected into pod's environment variables, matching the syntax of Docker links. Optional: Defaults to true.

| `ephemeralContainers`
| xref:../objects/index.adoc#ephemeralcontainer-core-v1[`array (EphemeralContainer core/v1)`]
| List of ephemeral containers run in this pod. Ephemeral containers may be run in an existing pod to perform user-initiated actions such as debugging. This list cannot be specified when creating a pod, and it cannot be modified by updating the pod spec. In order to add an ephemeral container to an existing pod, use the pod's ephemeralcontainers subresource. This field is alpha-level and is only honored by servers that enable the EphemeralContainers feature.

| `hostAliases`
| xref:../objects/index.adoc#hostalias-core-v1[`array (HostAlias core/v1)`]
| HostAliases is an optional list of hosts and IPs that will be injected into the pod's hosts file if specified. This is only valid for non-hostNetwork pods.

| `hostIPC`
| `boolean`
| Use the host's ipc namespace. Optional: Default to false.

| `hostNetwork`
| `boolean`
| Host networking requested for this pod. Use the host's network namespace. If this option is set, the ports that will be used must be specified. Default to false.

| `hostPID`
| `boolean`
| Use the host's pid namespace. Optional: Default to false.

| `hostname`
| `string`
| Specifies the hostname of the Pod If not specified, the pod's hostname will be set to a system-defined value.

| `imagePullSecrets`
| xref:../objects/index.adoc#localobjectreference-core-v1[`array (LocalObjectReference core/v1)`]
| ImagePullSecrets is an optional list of references to secrets in the same namespace to use for pulling any of the images used by this PodSpec. If specified, these secrets will be passed to individual puller implementations for them to use. For example, in the case of docker, only DockerConfig type secrets are honored. More info: https://kubernetes.io/docs/concepts/containers/images#specifying-imagepullsecrets-on-a-pod

| `initContainers`
| xref:../objects/index.adoc#container-core-v1[`array (Container core/v1)`]
| List of initialization containers belonging to the pod. Init containers are executed in order prior to containers being started. If any init container fails, the pod is considered to have failed and is handled according to its restartPolicy. The name for an init container or normal container must be unique among all containers. Init containers may not have Lifecycle actions, Readiness probes, Liveness probes, or Startup probes. The resourceRequirements of an init container are taken into account during scheduling by finding the highest request/limit for each resource type, and then using the max of of that value or the sum of the normal containers. Limits are applied to init containers in a similar fashion. Init containers cannot currently be added or removed. Cannot be updated. More info: https://kubernetes.io/docs/concepts/workloads/pods/init-containers/

| `nodeName`
| `string`
| NodeName is a request to schedule this pod onto a specific node. If it is non-empty, the scheduler simply schedules this pod onto that node, assuming that it fits resource requirements.

| `nodeSelector`
| `object (string)`
| NodeSelector is a selector which must be true for the pod to fit on a node. Selector which must match a node's labels for the pod to be scheduled on that node. More info: https://kubernetes.io/docs/concepts/configuration/assign-pod-node/

| `overhead`
| xref:../objects/index.adoc#quantity-api-none[`object (Quantity api/none)`]
| Overhead represents the resource overhead associated with running a pod for a given RuntimeClass. This field will be autopopulated at admission time by the RuntimeClass admission controller. If the RuntimeClass admission controller is enabled, overhead must not be set in Pod create requests. The RuntimeClass admission controller will reject Pod create requests which have the overhead already set. If RuntimeClass is configured and selected in the PodSpec, Overhead will be set to the value defined in the corresponding RuntimeClass, otherwise it will remain unset and treated as zero. More info: https://git.k8s.io/enhancements/keps/sig-node/688-pod-overhead/README.md This field is beta-level as of Kubernetes v1.18, and is only honored by servers that enable the PodOverhead feature.

| `preemptionPolicy`
| `string`
| PreemptionPolicy is the Policy for preempting pods with lower priority. One of Never, PreemptLowerPriority. Defaults to PreemptLowerPriority if unset. This field is beta-level, gated by the NonPreemptingPriority feature-gate.

| `priority`
| `integer`
| The priority value. Various system components use this field to find the priority of the pod. When Priority Admission Controller is enabled, it prevents users from setting this field. The admission controller populates this field from PriorityClassName. The higher the value, the higher the priority.

| `priorityClassName`
| `string`
| If specified, indicates the pod's priority. "system-node-critical" and "system-cluster-critical" are two special keywords which indicate the highest priorities with the former being the highest priority. Any other name must be defined by creating a PriorityClass object with that name. If not specified, the pod priority will be default or zero if there is no default.

| `readinessGates`
| xref:../objects/index.adoc#podreadinessgate-core-v1[`array (PodReadinessGate core/v1)`]
| If specified, all readiness gates will be evaluated for pod readiness. A pod is ready when all its containers are ready AND all conditions specified in the readiness gates have status equal to "True" More info: https://git.k8s.io/enhancements/keps/sig-network/580-pod-readiness-gates

| `restartPolicy`
| `string`
| Restart policy for all containers within the pod. One of Always, OnFailure, Never. Default to Always. More info: https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#restart-policy

| `runtimeClassName`
| `string`
| RuntimeClassName refers to a RuntimeClass object in the node.k8s.io group, which should be used to run this pod.  If no RuntimeClass resource matches the named class, the pod will not be run. If unset or empty, the "legacy" RuntimeClass will be used, which is an implicit class with an empty definition that uses the default runtime handler. More info: https://git.k8s.io/enhancements/keps/sig-node/585-runtime-class This is a beta feature as of Kubernetes v1.14.

| `schedulerName`
| `string`
| If specified, the pod will be dispatched by specified scheduler. If not specified, the pod will be dispatched by default scheduler.

| `securityContext`
| xref:../objects/index.adoc#podsecuritycontext-core-v1[`PodSecurityContext core/v1`]
| SecurityContext holds pod-level security attributes and common container settings. Optional: Defaults to empty.  See type description for default values of each field.

| `serviceAccount`
| `string`
| DeprecatedServiceAccount is a depreciated alias for ServiceAccountName. Deprecated: Use serviceAccountName instead.

| `serviceAccountName`
| `string`
| ServiceAccountName is the name of the ServiceAccount to use to run this pod. More info: https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/

| `setHostnameAsFQDN`
| `boolean`
| If true the pod's hostname will be configured as the pod's FQDN, rather than the leaf name (the default). In Linux containers, this means setting the FQDN in the hostname field of the kernel (the nodename field of struct utsname). In Windows containers, this means setting the registry value of hostname for the registry key HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters to FQDN. If a pod does not have FQDN, this has no effect. Default to false.

| `shareProcessNamespace`
| `boolean`
| Share a single process namespace between all of the containers in a pod. When this is set containers will be able to view and signal processes from other containers in the same pod, and the first process in each container will not be assigned PID 1. HostPID and ShareProcessNamespace cannot both be set. Optional: Default to false.

| `subdomain`
| `string`
| If specified, the fully qualified Pod hostname will be "<hostname>.<subdomain>.<pod namespace>.svc.<cluster domain>". If not specified, the pod will not have a domainname at all.

| `terminationGracePeriodSeconds`
| `integer`
| Optional duration in seconds the pod needs to terminate gracefully. May be decreased in delete request. Value must be non-negative integer. The value zero indicates stop immediately via the kill signal (no opportunity to shut down). If this value is nil, the default grace period will be used instead. The grace period is the duration in seconds after the processes running in the pod are sent a termination signal and the time when the processes are forcibly halted with a kill signal. Set this value longer than the expected cleanup time for your process. Defaults to 30 seconds.

| `tolerations`
| xref:../objects/index.adoc#toleration-core-v1[`array (Toleration core/v1)`]
| If specified, the pod's tolerations.

| `topologySpreadConstraints`
| xref:../objects/index.adoc#topologyspreadconstraint-core-v1[`array (TopologySpreadConstraint core/v1)`]
| TopologySpreadConstraints describes how a group of pods ought to spread across topology domains. Scheduler will schedule pods in a way which abides by the constraints. All topologySpreadConstraints are ANDed.

| `volumes`
| xref:../objects/index.adoc#volume-core-v1[`array (Volume core/v1)`]
| List of volumes that can be mounted by containers belonging to the pod. More info: https://kubernetes.io/docs/concepts/storage/volumes

|===
..status
Description::
+
--
ReplicationControllerStatus represents the current status of a replication controller.
--

Type::
  `object`

Required::
  - `replicas`



[cols="1,1,1",options="header"]
|===
| Property | Type | Description

| `availableReplicas`
| `integer`
| The number of available replicas (ready for at least minReadySeconds) for this replication controller.

| `conditions`
| xref:../objects/index.adoc#replicationcontrollercondition-core-v1[`array (ReplicationControllerCondition core/v1)`]
| Represents the latest available observations of a replication controller's current state.

| `fullyLabeledReplicas`
| `integer`
| The number of pods that have labels matching the labels of the pod template of the replication controller.

| `observedGeneration`
| `integer`
| ObservedGeneration reflects the generation of the most recently observed replication controller.

| `readyReplicas`
| `integer`
| The number of ready replicas for this replication controller.

| `replicas`
| `integer`
| Replicas is the most recently oberved number of replicas. More info: https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller#what-is-a-replicationcontroller

|===

== API endpoints

The following API endpoints are available:

* `/api/v1/replicationcontrollers`
- `GET`: list or watch objects of kind ReplicationController
* `/api/v1/namespaces/{namespace}/replicationcontrollers`
- `DELETE`: delete collection of ReplicationController
- `GET`: list or watch objects of kind ReplicationController
- `POST`: create a ReplicationController
* `/api/v1/namespaces/{namespace}/replicationcontrollers/{name}`
- `DELETE`: delete a ReplicationController
- `GET`: read the specified ReplicationController
- `PATCH`: partially update the specified ReplicationController
- `PUT`: replace the specified ReplicationController
* `/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale`
- `GET`: read scale of the specified ReplicationController
- `PATCH`: partially update scale of the specified ReplicationController
- `PUT`: replace scale of the specified ReplicationController
* `/api/v1/namespaces/{namespace}/replicationcontrollers/{name}/status`
- `GET`: read status of the specified ReplicationController
- `PATCH`: partially update status of the specified ReplicationController
- `PUT`: replace status of the specified ReplicationController


=== /api/v1/replicationcontrollers


.Global query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `allowWatchBookmarks`
| `boolean`
| allowWatchBookmarks requests watch events with type &quot;BOOKMARK&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#x27;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored.
| `continue`
| `string`
| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the &quot;next key&quot;.

This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
| `fieldSelector`
| `string`
| A selector to restrict the list of returned objects by their fields. Defaults to everything.
| `labelSelector`
| `string`
| A selector to restrict the list of returned objects by their labels. Defaults to everything.
| `limit`
| `integer`
| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.

The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
| `pretty`
| `string`
| If &#x27;true&#x27;, then the output is pretty printed.
| `resourceVersion`
| `string`
| resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.

Defaults to unset
| `resourceVersionMatch`
| `string`
| resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.

Defaults to unset
| `timeoutSeconds`
| `integer`
| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
| `watch`
| `boolean`
| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
|===

HTTP method::
  `GET`

Description::
  list or watch objects of kind ReplicationController


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../objects/index.adoc#replicationcontrollerlist-core-v1[`ReplicationControllerList core/v1`]
|===


=== /api/v1/namespaces/{namespace}/replicationcontrollers

.Global path parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `namespace`
| `string`
| object name and auth scope, such as for teams and projects
|===

.Global query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `pretty`
| `string`
| If &#x27;true&#x27;, then the output is pretty printed.
|===

HTTP method::
  `DELETE`

Description::
  delete collection of ReplicationController


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `continue`
| `string`
| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the &quot;next key&quot;.

This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
| `dryRun`
| `string`
| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
| `fieldSelector`
| `string`
| A selector to restrict the list of returned objects by their fields. Defaults to everything.
| `gracePeriodSeconds`
| `integer`
| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
| `labelSelector`
| `string`
| A selector to restrict the list of returned objects by their labels. Defaults to everything.
| `limit`
| `integer`
| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.

The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
| `orphanDependents`
| `boolean`
| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the &quot;orphan&quot; finalizer will be added to/removed from the object&#x27;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
| `propagationPolicy`
| `string`
| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#x27;Orphan&#x27; - orphan the dependents; &#x27;Background&#x27; - allow the garbage collector to delete the dependents in the background; &#x27;Foreground&#x27; - a cascading policy that deletes all dependents in the foreground.
| `resourceVersion`
| `string`
| resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.

Defaults to unset
| `resourceVersionMatch`
| `string`
| resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.

Defaults to unset
| `timeoutSeconds`
| `integer`
| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
|===

.Body parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `body`
| xref:../objects/index.adoc#deleteoptions-meta-v1[`DeleteOptions meta/v1`]
| 
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../objects/index.adoc#status-meta-v1[`Status meta/v1`]
|===

HTTP method::
  `GET`

Description::
  list or watch objects of kind ReplicationController


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `allowWatchBookmarks`
| `boolean`
| allowWatchBookmarks requests watch events with type &quot;BOOKMARK&quot;. Servers that do not implement bookmarks may ignore this flag and bookmarks are sent at the server&#x27;s discretion. Clients should not assume bookmarks are returned at any specific interval, nor may they assume the server will send any BOOKMARK event during a session. If this is not a watch, this field is ignored.
| `continue`
| `string`
| The continue option should be set when retrieving more results from the server. Since this value is server defined, clients may only use the continue value from a previous query result with identical query parameters (except for the value of continue) and the server may reject a continue value it does not recognize. If the specified continue value is no longer valid whether due to expiration (generally five to fifteen minutes) or a configuration change on the server, the server will respond with a 410 ResourceExpired error together with a continue token. If the client needs a consistent list, it must restart their list without the continue field. Otherwise, the client may send another list request with the token received with the 410 error, the server will respond with a list starting from the next key, but from the latest snapshot, which is inconsistent from the previous list results - objects that are created, modified, or deleted after the first list request will be included in the response, as long as their keys are after the &quot;next key&quot;.

This field is not supported when watch is true. Clients may start a watch from the last resourceVersion value returned by the server and not miss any modifications.
| `fieldSelector`
| `string`
| A selector to restrict the list of returned objects by their fields. Defaults to everything.
| `labelSelector`
| `string`
| A selector to restrict the list of returned objects by their labels. Defaults to everything.
| `limit`
| `integer`
| limit is a maximum number of responses to return for a list call. If more items exist, the server will set the &#x60;continue&#x60; field on the list metadata to a value that can be used with the same initial query to retrieve the next set of results. Setting a limit may return fewer than the requested amount of items (up to zero items) in the event all requested objects are filtered out and clients should only use the presence of the continue field to determine whether more results are available. Servers may choose not to support the limit argument and will return all of the available results. If limit is specified and the continue field is empty, clients may assume that no more results are available. This field is not supported if watch is true.

The server guarantees that the objects returned when using continue will be identical to issuing a single list call without a limit - that is, no objects created, modified, or deleted after the first request is issued will be included in any subsequent continued requests. This is sometimes referred to as a consistent snapshot, and ensures that a client that is using limit to receive smaller chunks of a very large result can ensure they see all possible objects. If objects are updated during a chunked list the version of the object that was present at the time the first list result was calculated is returned.
| `resourceVersion`
| `string`
| resourceVersion sets a constraint on what resource versions a request may be served from. See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.

Defaults to unset
| `resourceVersionMatch`
| `string`
| resourceVersionMatch determines how resourceVersion is applied to list calls. It is highly recommended that resourceVersionMatch be set for list calls where resourceVersion is set See https://kubernetes.io/docs/reference/using-api/api-concepts/#resource-versions for details.

Defaults to unset
| `timeoutSeconds`
| `integer`
| Timeout for the list/watch call. This limits the duration of the call, regardless of any activity or inactivity.
| `watch`
| `boolean`
| Watch for changes to the described resources and return them as a stream of add, update, and remove notifications. Specify resourceVersion.
|===


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../objects/index.adoc#replicationcontrollerlist-core-v1[`ReplicationControllerList core/v1`]
|===

HTTP method::
  `POST`

Description::
  create a ReplicationController


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `dryRun`
| `string`
| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
| `fieldManager`
| `string`
| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
|===

.Body parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `body`
| xref:../workloads_apis/replicationcontroller-core-v1.adoc#replicationcontroller-core-v1[`ReplicationController core/v1`]
| 
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../workloads_apis/replicationcontroller-core-v1.adoc#replicationcontroller-core-v1[`ReplicationController core/v1`]
|===


=== /api/v1/namespaces/{namespace}/replicationcontrollers/{name}

.Global path parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `name`
| `string`
| name of the ReplicationController
| `namespace`
| `string`
| object name and auth scope, such as for teams and projects
|===

.Global query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `pretty`
| `string`
| If &#x27;true&#x27;, then the output is pretty printed.
|===

HTTP method::
  `DELETE`

Description::
  delete a ReplicationController


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `dryRun`
| `string`
| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
| `gracePeriodSeconds`
| `integer`
| The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately.
| `orphanDependents`
| `boolean`
| Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the &quot;orphan&quot; finalizer will be added to/removed from the object&#x27;s finalizers list. Either this field or PropagationPolicy may be set, but not both.
| `propagationPolicy`
| `string`
| Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: &#x27;Orphan&#x27; - orphan the dependents; &#x27;Background&#x27; - allow the garbage collector to delete the dependents in the background; &#x27;Foreground&#x27; - a cascading policy that deletes all dependents in the foreground.
|===

.Body parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `body`
| xref:../objects/index.adoc#deleteoptions-meta-v1[`DeleteOptions meta/v1`]
| 
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../objects/index.adoc#status-meta-v1[`Status meta/v1`]
|===

HTTP method::
  `GET`

Description::
  read the specified ReplicationController


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../workloads_apis/replicationcontroller-core-v1.adoc#replicationcontroller-core-v1[`ReplicationController core/v1`]
|===

HTTP method::
  `PATCH`

Description::
  partially update the specified ReplicationController


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `dryRun`
| `string`
| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
| `fieldManager`
| `string`
| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
| `force`
| `boolean`
| Force is going to &quot;force&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
|===

.Body parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `body`
| xref:../objects/index.adoc#patch-meta-v1[`Patch meta/v1`]
| 
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../workloads_apis/replicationcontroller-core-v1.adoc#replicationcontroller-core-v1[`ReplicationController core/v1`]
|===

HTTP method::
  `PUT`

Description::
  replace the specified ReplicationController


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `dryRun`
| `string`
| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
| `fieldManager`
| `string`
| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
|===

.Body parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `body`
| xref:../workloads_apis/replicationcontroller-core-v1.adoc#replicationcontroller-core-v1[`ReplicationController core/v1`]
| 
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../workloads_apis/replicationcontroller-core-v1.adoc#replicationcontroller-core-v1[`ReplicationController core/v1`]
|===


=== /api/v1/namespaces/{namespace}/replicationcontrollers/{name}/scale

.Global path parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `name`
| `string`
| name of the Scale
| `namespace`
| `string`
| object name and auth scope, such as for teams and projects
|===

.Global query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `pretty`
| `string`
| If &#x27;true&#x27;, then the output is pretty printed.
|===

HTTP method::
  `GET`

Description::
  read scale of the specified ReplicationController


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../objects/index.adoc#scale-autoscaling-v1[`Scale autoscaling/v1`]
|===

HTTP method::
  `PATCH`

Description::
  partially update scale of the specified ReplicationController


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `dryRun`
| `string`
| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
| `fieldManager`
| `string`
| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
| `force`
| `boolean`
| Force is going to &quot;force&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
|===

.Body parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `body`
| xref:../objects/index.adoc#patch-meta-v1[`Patch meta/v1`]
| 
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../objects/index.adoc#scale-autoscaling-v1[`Scale autoscaling/v1`]
|===

HTTP method::
  `PUT`

Description::
  replace scale of the specified ReplicationController


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `dryRun`
| `string`
| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
| `fieldManager`
| `string`
| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
|===

.Body parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `body`
| xref:../objects/index.adoc#scale-autoscaling-v1[`Scale autoscaling/v1`]
| 
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../objects/index.adoc#scale-autoscaling-v1[`Scale autoscaling/v1`]
|===


=== /api/v1/namespaces/{namespace}/replicationcontrollers/{name}/status

.Global path parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `name`
| `string`
| name of the ReplicationController
| `namespace`
| `string`
| object name and auth scope, such as for teams and projects
|===

.Global query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `pretty`
| `string`
| If &#x27;true&#x27;, then the output is pretty printed.
|===

HTTP method::
  `GET`

Description::
  read status of the specified ReplicationController


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../workloads_apis/replicationcontroller-core-v1.adoc#replicationcontroller-core-v1[`ReplicationController core/v1`]
|===

HTTP method::
  `PATCH`

Description::
  partially update status of the specified ReplicationController


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `dryRun`
| `string`
| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
| `fieldManager`
| `string`
| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint. This field is required for apply requests (application/apply-patch) but optional for non-apply patch types (JsonPatch, MergePatch, StrategicMergePatch).
| `force`
| `boolean`
| Force is going to &quot;force&quot; Apply requests. It means user will re-acquire conflicting fields owned by other people. Force flag must be unset for non-apply patch requests.
|===

.Body parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `body`
| xref:../objects/index.adoc#patch-meta-v1[`Patch meta/v1`]
| 
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../workloads_apis/replicationcontroller-core-v1.adoc#replicationcontroller-core-v1[`ReplicationController core/v1`]
|===

HTTP method::
  `PUT`

Description::
  replace status of the specified ReplicationController


.Query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `dryRun`
| `string`
| When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed
| `fieldManager`
| `string`
| fieldManager is a name associated with the actor or entity that is making these changes. The value must be less than or 128 characters long, and only contain printable characters, as defined by https://golang.org/pkg/unicode/#IsPrint.
|===

.Body parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `body`
| xref:../workloads_apis/replicationcontroller-core-v1.adoc#replicationcontroller-core-v1[`ReplicationController core/v1`]
| 
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../workloads_apis/replicationcontroller-core-v1.adoc#replicationcontroller-core-v1[`ReplicationController core/v1`]
|===


