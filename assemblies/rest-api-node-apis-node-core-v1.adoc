[id="node-core-v1"]
= Node [core/v1]
ifdef::product-title[]
include::_attributes/common-attributes.adoc[]
endif::[]

toc::[]


Description::
+
--
Node is a worker node in Kubernetes. Each node will have a unique identifier in the cache (i.e. in etcd).
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
| Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata

| `spec`
| `object`
| NodeSpec describes the attributes that a node is created with.

| `status`
| `object`
| NodeStatus is information about the current status of a node.

|===
..spec
Description::
+
--
NodeSpec describes the attributes that a node is created with.
--

Type::
  `object`




[cols="1,1,1",options="header"]
|===
| Property | Type | Description

| `configSource`
| xref:../objects/index.adoc#nodeconfigsource-core-v1[`NodeConfigSource core/v1`]
| Deprecated. If specified, the source of the node's configuration. The DynamicKubeletConfig feature gate must be enabled for the Kubelet to use this field. This field is deprecated as of 1.22: https://git.k8s.io/enhancements/keps/sig-node/281-dynamic-kubelet-configuration

| `externalID`
| `string`
| Deprecated. Not all kubelets will set this field. Remove field after 1.13. see: https://issues.k8s.io/61966

| `podCIDR`
| `string`
| PodCIDR represents the pod IP range assigned to the node.

| `podCIDRs`
| `array (string)`
| podCIDRs represents the IP ranges assigned to the node for usage by Pods on that node. If this field is specified, the 0th entry must match the podCIDR field. It may contain at most 1 value for each of IPv4 and IPv6.

| `providerID`
| `string`
| ID of the node assigned by the cloud provider in the format: <ProviderName>://<ProviderSpecificNodeID>

| `taints`
| xref:../objects/index.adoc#taint-core-v1[`array (Taint core/v1)`]
| If specified, the node's taints.

| `unschedulable`
| `boolean`
| Unschedulable controls node schedulability of new pods. By default, node is schedulable. More info: https://kubernetes.io/docs/concepts/nodes/node/#manual-node-administration

|===
..status
Description::
+
--
NodeStatus is information about the current status of a node.
--

Type::
  `object`




[cols="1,1,1",options="header"]
|===
| Property | Type | Description

| `addresses`
| xref:../objects/index.adoc#nodeaddress-core-v1[`array (NodeAddress core/v1)`]
| List of addresses reachable to the node. Queried from cloud provider, if available. More info: https://kubernetes.io/docs/concepts/nodes/node/#addresses Note: This field is declared as mergeable, but the merge key is not sufficiently unique, which can cause data corruption when it is merged. Callers should instead use a full-replacement patch. See http://pr.k8s.io/79391 for an example.

| `allocatable`
| xref:../objects/index.adoc#quantity-api-none[`object (Quantity api/none)`]
| Allocatable represents the resources of a node that are available for scheduling. Defaults to Capacity.

| `capacity`
| xref:../objects/index.adoc#quantity-api-none[`object (Quantity api/none)`]
| Capacity represents the total resources of a node. More info: https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity

| `conditions`
| xref:../objects/index.adoc#nodecondition-core-v1[`array (NodeCondition core/v1)`]
| Conditions is an array of current observed node conditions. More info: https://kubernetes.io/docs/concepts/nodes/node/#condition

| `config`
| `object`
| NodeConfigStatus describes the status of the config assigned by Node.Spec.ConfigSource.

| `daemonEndpoints`
| xref:../objects/index.adoc#nodedaemonendpoints-core-v1[`NodeDaemonEndpoints core/v1`]
| Endpoints of daemons running on the Node.

| `images`
| xref:../objects/index.adoc#containerimage-core-v1[`array (ContainerImage core/v1)`]
| List of container images on this node

| `nodeInfo`
| xref:../objects/index.adoc#nodesysteminfo-core-v1[`NodeSystemInfo core/v1`]
| Set of ids/uuids to uniquely identify the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#info

| `phase`
| `string`
| NodePhase is the recently observed lifecycle phase of the node. More info: https://kubernetes.io/docs/concepts/nodes/node/#phase The field is never populated, and now is deprecated.

| `volumesAttached`
| xref:../objects/index.adoc#attachedvolume-core-v1[`array (AttachedVolume core/v1)`]
| List of volumes that are attached to the node.

| `volumesInUse`
| `array (string)`
| List of attachable volumes in use (mounted) by the node.

|===
..status.config
Description::
+
--
NodeConfigStatus describes the status of the config assigned by Node.Spec.ConfigSource.
--

Type::
  `object`




[cols="1,1,1",options="header"]
|===
| Property | Type | Description

| `active`
| xref:../objects/index.adoc#nodeconfigsource-core-v1[`NodeConfigSource core/v1`]
| Active reports the checkpointed config the node is actively using. Active will represent either the current version of the Assigned config, or the current LastKnownGood config, depending on whether attempting to use the Assigned config results in an error.

| `assigned`
| xref:../objects/index.adoc#nodeconfigsource-core-v1[`NodeConfigSource core/v1`]
| Assigned reports the checkpointed config the node will try to use. When Node.Spec.ConfigSource is updated, the node checkpoints the associated config payload to local disk, along with a record indicating intended config. The node refers to this record to choose its config checkpoint, and reports this record in Assigned. Assigned only updates in the status after the record has been checkpointed to disk. When the Kubelet is restarted, it tries to make the Assigned config the Active config by loading and validating the checkpointed payload identified by Assigned.

| `error`
| `string`
| Error describes any problems reconciling the Spec.ConfigSource to the Active config. Errors may occur, for example, attempting to checkpoint Spec.ConfigSource to the local Assigned record, attempting to checkpoint the payload associated with Spec.ConfigSource, attempting to load or validate the Assigned config, etc. Errors may occur at different points while syncing config. Earlier errors (e.g. download or checkpointing errors) will not result in a rollback to LastKnownGood, and may resolve across Kubelet retries. Later errors (e.g. loading or validating a checkpointed config) will result in a rollback to LastKnownGood. In the latter case, it is usually possible to resolve the error by fixing the config assigned in Spec.ConfigSource. You can find additional information for debugging by searching the error message in the Kubelet log. Error is a human-readable description of the error state; machines can check whether or not Error is empty, but should not rely on the stability of the Error text across Kubelet versions.

| `lastKnownGood`
| xref:../objects/index.adoc#nodeconfigsource-core-v1[`NodeConfigSource core/v1`]
| LastKnownGood reports the checkpointed config the node will fall back to when it encounters an error attempting to use the Assigned config. The Assigned config becomes the LastKnownGood config when the node determines that the Assigned config is stable and correct. This is currently implemented as a 10-minute soak period starting when the local record of Assigned config is updated. If the Assigned config is Active at the end of this period, it becomes the LastKnownGood. Note that if Spec.ConfigSource is reset to nil (use local defaults), the LastKnownGood is also immediately reset to nil, because the local default config is always assumed good. You should not make assumptions about the node's method of determining config stability and correctness, as this may change or become configurable in the future.

|===

== API endpoints

The following API endpoints are available:

* `/api/v1/nodes`
- `DELETE`: delete collection of Node
- `GET`: list or watch objects of kind Node
- `POST`: create a Node
* `/api/v1/nodes/{name}`
- `DELETE`: delete a Node
- `GET`: read the specified Node
- `PATCH`: partially update the specified Node
- `PUT`: replace the specified Node
* `/api/v1/nodes/{name}/proxy`
- `DELETE`: connect DELETE requests to proxy of Node
- `GET`: connect GET requests to proxy of Node
- `HEAD`: connect HEAD requests to proxy of Node
- `OPTIONS`: connect OPTIONS requests to proxy of Node
- `PATCH`: connect PATCH requests to proxy of Node
- `POST`: connect POST requests to proxy of Node
- `PUT`: connect PUT requests to proxy of Node
* `/api/v1/nodes/{name}/status`
- `GET`: read status of the specified Node
- `PATCH`: partially update status of the specified Node
- `PUT`: replace status of the specified Node
* `/api/v1/nodes/{name}/proxy/{path}`
- `DELETE`: connect DELETE requests to proxy of Node
- `GET`: connect GET requests to proxy of Node
- `HEAD`: connect HEAD requests to proxy of Node
- `OPTIONS`: connect OPTIONS requests to proxy of Node
- `PATCH`: connect PATCH requests to proxy of Node
- `POST`: connect POST requests to proxy of Node
- `PUT`: connect PUT requests to proxy of Node


=== /api/v1/nodes


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
  delete collection of Node


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
  list or watch objects of kind Node


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
| xref:../objects/index.adoc#nodelist-core-v1[`NodeList core/v1`]
|===

HTTP method::
  `POST`

Description::
  create a Node


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
| xref:../node_apis/node-core-v1.adoc#node-core-v1[`Node core/v1`]
| 
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../node_apis/node-core-v1.adoc#node-core-v1[`Node core/v1`]
|===


=== /api/v1/nodes/{name}

.Global path parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `name`
| `string`
| name of the Node
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
  delete a Node


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
  read the specified Node


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../node_apis/node-core-v1.adoc#node-core-v1[`Node core/v1`]
|===

HTTP method::
  `PATCH`

Description::
  partially update the specified Node


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
| xref:../node_apis/node-core-v1.adoc#node-core-v1[`Node core/v1`]
|===

HTTP method::
  `PUT`

Description::
  replace the specified Node


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
| xref:../node_apis/node-core-v1.adoc#node-core-v1[`Node core/v1`]
| 
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../node_apis/node-core-v1.adoc#node-core-v1[`Node core/v1`]
|===


=== /api/v1/nodes/{name}/proxy

.Global path parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `name`
| `string`
| name of the NodeProxyOptions
|===

.Global query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `path`
| `string`
| Path is the URL path to use for the current proxy request to node.
|===

HTTP method::
  `DELETE`

Description::
  connect DELETE requests to proxy of Node


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| `string`
|===

HTTP method::
  `GET`

Description::
  connect GET requests to proxy of Node


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| `string`
|===

HTTP method::
  `HEAD`

Description::
  connect HEAD requests to proxy of Node


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| `string`
|===

HTTP method::
  `OPTIONS`

Description::
  connect OPTIONS requests to proxy of Node


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| `string`
|===

HTTP method::
  `PATCH`

Description::
  connect PATCH requests to proxy of Node


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| `string`
|===

HTTP method::
  `POST`

Description::
  connect POST requests to proxy of Node


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| `string`
|===

HTTP method::
  `PUT`

Description::
  connect PUT requests to proxy of Node


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| `string`
|===


=== /api/v1/nodes/{name}/status

.Global path parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `name`
| `string`
| name of the Node
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
  read status of the specified Node


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../node_apis/node-core-v1.adoc#node-core-v1[`Node core/v1`]
|===

HTTP method::
  `PATCH`

Description::
  partially update status of the specified Node


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
| xref:../node_apis/node-core-v1.adoc#node-core-v1[`Node core/v1`]
|===

HTTP method::
  `PUT`

Description::
  replace status of the specified Node


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
| xref:../node_apis/node-core-v1.adoc#node-core-v1[`Node core/v1`]
| 
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../node_apis/node-core-v1.adoc#node-core-v1[`Node core/v1`]
|===


=== /api/v1/nodes/{name}/proxy/{path}

.Global path parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `name`
| `string`
| name of the NodeProxyOptions
| `path`
| `string`
| path to the resource
|===

.Global query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `path`
| `string`
| Path is the URL path to use for the current proxy request to node.
|===

HTTP method::
  `DELETE`

Description::
  connect DELETE requests to proxy of Node


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| `string`
|===

HTTP method::
  `GET`

Description::
  connect GET requests to proxy of Node


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| `string`
|===

HTTP method::
  `HEAD`

Description::
  connect HEAD requests to proxy of Node


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| `string`
|===

HTTP method::
  `OPTIONS`

Description::
  connect OPTIONS requests to proxy of Node


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| `string`
|===

HTTP method::
  `PATCH`

Description::
  connect PATCH requests to proxy of Node


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| `string`
|===

HTTP method::
  `POST`

Description::
  connect POST requests to proxy of Node


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| `string`
|===

HTTP method::
  `PUT`

Description::
  connect PUT requests to proxy of Node


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| `string`
|===


