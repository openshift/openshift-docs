[id="service-core-v1"]
= Service [core/v1]
ifdef::product-title[]
include::_attributes/common-attributes.adoc[]
endif::[]

toc::[]


Description::
+
--
Service is a named abstraction of software service (for example, mysql) consisting of local port (for example 3306) that the proxy listens on, and the selector that determines which pods will answer requests sent through the proxy.
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
| ServiceSpec describes the attributes that a user creates on a service.

| `status`
| `object`
| ServiceStatus represents the current status of a service.

|===
..spec
Description::
+
--
ServiceSpec describes the attributes that a user creates on a service.
--

Type::
  `object`




[cols="1,1,1",options="header"]
|===
| Property | Type | Description

| `allocateLoadBalancerNodePorts`
| `boolean`
| allocateLoadBalancerNodePorts defines if NodePorts will be automatically allocated for services with type LoadBalancer.  Default is "true". It may be set to "false" if the cluster load-balancer does not rely on NodePorts.  If the caller requests specific NodePorts (by specifying a value), those requests will be respected, regardless of this field. This field may only be set for services with type LoadBalancer and will be cleared if the type is changed to any other type. This field is beta-level and is only honored by servers that enable the ServiceLBNodePortControl feature.

| `clusterIP`
| `string`
| clusterIP is the IP address of the service and is usually assigned randomly. If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be blank) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above).  Valid values are "None", empty string (""), or a valid IP address. Setting this to "None" makes a "headless service" (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required.  Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a Service of type ExternalName, creation will fail. This field will be wiped when updating a Service to type ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies

| `clusterIPs`
| `array (string)`
| ClusterIPs is a list of IP addresses assigned to this service, and are usually assigned randomly.  If an address is specified manually, is in-range (as per system configuration), and is not in use, it will be allocated to the service; otherwise creation of the service will fail. This field may not be changed through updates unless the type field is also being changed to ExternalName (which requires this field to be empty) or the type field is being changed from ExternalName (in which case this field may optionally be specified, as describe above).  Valid values are "None", empty string (""), or a valid IP address.  Setting this to "None" makes a "headless service" (no virtual IP), which is useful when direct endpoint connections are preferred and proxying is not required.  Only applies to types ClusterIP, NodePort, and LoadBalancer. If this field is specified when creating a Service of type ExternalName, creation will fail. This field will be wiped when updating a Service to type ExternalName.  If this field is not specified, it will be initialized from the clusterIP field.  If this field is specified, clients must ensure that clusterIPs[0] and clusterIP have the same value.

Unless the "IPv6DualStack" feature gate is enabled, this field is limited to one value, which must be the same as the clusterIP field.  If the feature gate is enabled, this field may hold a maximum of two entries (dual-stack IPs, in either order).  These IPs must correspond to the values of the ipFamilies field. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies

| `externalIPs`
| `array (string)`
| externalIPs is a list of IP addresses for which nodes in the cluster will also accept traffic for this service.  These IPs are not managed by Kubernetes.  The user is responsible for ensuring that traffic arrives at a node with this IP.  A common example is external load-balancers that are not part of the Kubernetes system.

| `externalName`
| `string`
| externalName is the external reference that discovery mechanisms will return as an alias for this service (e.g. a DNS CNAME record). No proxying will be involved.  Must be a lowercase RFC-1123 hostname (https://tools.ietf.org/html/rfc1123) and requires `type` to be "ExternalName".

| `externalTrafficPolicy`
| `string`
| externalTrafficPolicy denotes if this Service desires to route external traffic to node-local or cluster-wide endpoints. "Local" preserves the client source IP and avoids a second hop for LoadBalancer and Nodeport type services, but risks potentially imbalanced traffic spreading. "Cluster" obscures the client source IP and may cause a second hop to another node, but should have good overall load-spreading.

| `healthCheckNodePort`
| `integer`
| healthCheckNodePort specifies the healthcheck nodePort for the service. This only applies when type is set to LoadBalancer and externalTrafficPolicy is set to Local. If a value is specified, is in-range, and is not in use, it will be used.  If not specified, a value will be automatically allocated.  External systems (e.g. load-balancers) can use this port to determine if a given node holds endpoints for this service or not.  If this field is specified when creating a Service which does not need it, creation will fail. This field will be wiped when updating a Service to no longer need it (e.g. changing type).

| `internalTrafficPolicy`
| `string`
| InternalTrafficPolicy specifies if the cluster internal traffic should be routed to all endpoints or node-local endpoints only. "Cluster" routes internal traffic to a Service to all endpoints. "Local" routes traffic to node-local endpoints only, traffic is dropped if no node-local endpoints are ready. The default value is "Cluster".

| `ipFamilies`
| `array (string)`
| IPFamilies is a list of IP families (e.g. IPv4, IPv6) assigned to this service, and is gated by the "IPv6DualStack" feature gate.  This field is usually assigned automatically based on cluster configuration and the ipFamilyPolicy field. If this field is specified manually, the requested family is available in the cluster, and ipFamilyPolicy allows it, it will be used; otherwise creation of the service will fail.  This field is conditionally mutable: it allows for adding or removing a secondary IP family, but it does not allow changing the primary IP family of the Service.  Valid values are "IPv4" and "IPv6".  This field only applies to Services of types ClusterIP, NodePort, and LoadBalancer, and does apply to "headless" services.  This field will be wiped when updating a Service to type ExternalName.

This field may hold a maximum of two entries (dual-stack families, in either order).  These families must correspond to the values of the clusterIPs field, if specified. Both clusterIPs and ipFamilies are governed by the ipFamilyPolicy field.

| `ipFamilyPolicy`
| `string`
| IPFamilyPolicy represents the dual-stack-ness requested or required by this Service, and is gated by the "IPv6DualStack" feature gate.  If there is no value provided, then this field will be set to SingleStack. Services can be "SingleStack" (a single IP family), "PreferDualStack" (two IP families on dual-stack configured clusters or a single IP family on single-stack clusters), or "RequireDualStack" (two IP families on dual-stack configured clusters, otherwise fail). The ipFamilies and clusterIPs fields depend on the value of this field.  This field will be wiped when updating a service to type ExternalName.

| `loadBalancerClass`
| `string`
| loadBalancerClass is the class of the load balancer implementation this Service belongs to. If specified, the value of this field must be a label-style identifier, with an optional prefix, e.g. "internal-vip" or "example.com/internal-vip". Unprefixed names are reserved for end-users. This field can only be set when the Service type is 'LoadBalancer'. If not set, the default load balancer implementation is used, today this is typically done through the cloud provider integration, but should apply for any default implementation. If set, it is assumed that a load balancer implementation is watching for Services with a matching class. Any default load balancer implementation (e.g. cloud providers) should ignore Services that set this field. This field can only be set when creating or updating a Service to type 'LoadBalancer'. Once set, it can not be changed. This field will be wiped when a service is updated to a non 'LoadBalancer' type.

| `loadBalancerIP`
| `string`
| Only applies to Service Type: LoadBalancer LoadBalancer will get created with the IP specified in this field. This feature depends on whether the underlying cloud-provider supports specifying the loadBalancerIP when a load balancer is created. This field will be ignored if the cloud-provider does not support the feature.

| `loadBalancerSourceRanges`
| `array (string)`
| If specified and supported by the platform, this will restrict traffic through the cloud-provider load-balancer will be restricted to the specified client IPs. This field will be ignored if the cloud-provider does not support the feature." More info: https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/

| `ports`
| xref:../objects/index.adoc#serviceport-core-v1[`array (ServicePort core/v1)`]
| The list of ports that are exposed by this service. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies

| `publishNotReadyAddresses`
| `boolean`
| publishNotReadyAddresses indicates that any agent which deals with endpoints for this Service should disregard any indications of ready/not-ready. The primary use case for setting this field is for a StatefulSet's Headless Service to propagate SRV DNS records for its Pods for the purpose of peer discovery. The Kubernetes controllers that generate Endpoints and EndpointSlice resources for Services interpret this to mean that all endpoints are considered "ready" even if the Pods themselves are not. Agents which consume only Kubernetes generated endpoints through the Endpoints or EndpointSlice resources can safely assume this behavior.

| `selector`
| `object (string)`
| Route service traffic to pods with label keys and values matching this selector. If empty or not present, the service is assumed to have an external process managing its endpoints, which Kubernetes will not modify. Only applies to types ClusterIP, NodePort, and LoadBalancer. Ignored if type is ExternalName. More info: https://kubernetes.io/docs/concepts/services-networking/service/

| `sessionAffinity`
| `string`
| Supports "ClientIP" and "None". Used to maintain session affinity. Enable client IP based session affinity. Must be ClientIP or None. Defaults to None. More info: https://kubernetes.io/docs/concepts/services-networking/service/#virtual-ips-and-service-proxies

| `sessionAffinityConfig`
| xref:../objects/index.adoc#sessionaffinityconfig-core-v1[`SessionAffinityConfig core/v1`]
| sessionAffinityConfig contains the configurations of session affinity.

| `type`
| `string`
| type determines how the Service is exposed. Defaults to ClusterIP. Valid options are ExternalName, ClusterIP, NodePort, and LoadBalancer. "ClusterIP" allocates a cluster-internal IP address for load-balancing to endpoints. Endpoints are determined by the selector or if that is not specified, by manual construction of an Endpoints object or EndpointSlice objects. If clusterIP is "None", no virtual IP is allocated and the endpoints are published as a set of endpoints rather than a virtual IP. "NodePort" builds on ClusterIP and allocates a port on every node which routes to the same endpoints as the clusterIP. "LoadBalancer" builds on NodePort and creates an external load-balancer (if supported in the current cloud) which routes to the same endpoints as the clusterIP. "ExternalName" aliases this service to the specified externalName. Several other fields do not apply to ExternalName services. More info: https://kubernetes.io/docs/concepts/services-networking/service/#publishing-services-service-types

|===
..status
Description::
+
--
ServiceStatus represents the current status of a service.
--

Type::
  `object`




[cols="1,1,1",options="header"]
|===
| Property | Type | Description

| `conditions`
| xref:../objects/index.adoc#condition-meta-v1[`array (Condition meta/v1)`]
| Current service state

| `loadBalancer`
| `object`
| LoadBalancerStatus represents the status of a load-balancer.

|===
..status.loadBalancer
Description::
+
--
LoadBalancerStatus represents the status of a load-balancer.
--

Type::
  `object`




[cols="1,1,1",options="header"]
|===
| Property | Type | Description

| `ingress`
| xref:../objects/index.adoc#loadbalanceringress-core-v1[`array (LoadBalancerIngress core/v1)`]
| Ingress is a list containing ingress points for the load-balancer. Traffic intended for the service should be sent to these ingress points.

|===

== API endpoints

The following API endpoints are available:

* `/api/v1/services`
- `GET`: list or watch objects of kind Service
* `/api/v1/namespaces/{namespace}/services`
- `GET`: list or watch objects of kind Service
- `POST`: create a Service
* `/api/v1/namespaces/{namespace}/services/{name}`
- `DELETE`: delete a Service
- `GET`: read the specified Service
- `PATCH`: partially update the specified Service
- `PUT`: replace the specified Service
* `/api/v1/namespaces/{namespace}/services/{name}/proxy`
- `DELETE`: connect DELETE requests to proxy of Service
- `GET`: connect GET requests to proxy of Service
- `HEAD`: connect HEAD requests to proxy of Service
- `OPTIONS`: connect OPTIONS requests to proxy of Service
- `PATCH`: connect PATCH requests to proxy of Service
- `POST`: connect POST requests to proxy of Service
- `PUT`: connect PUT requests to proxy of Service
* `/api/v1/namespaces/{namespace}/services/{name}/status`
- `GET`: read status of the specified Service
- `PATCH`: partially update status of the specified Service
- `PUT`: replace status of the specified Service
* `/api/v1/namespaces/{namespace}/services/{name}/proxy/{path}`
- `DELETE`: connect DELETE requests to proxy of Service
- `GET`: connect GET requests to proxy of Service
- `HEAD`: connect HEAD requests to proxy of Service
- `OPTIONS`: connect OPTIONS requests to proxy of Service
- `PATCH`: connect PATCH requests to proxy of Service
- `POST`: connect POST requests to proxy of Service
- `PUT`: connect PUT requests to proxy of Service


=== /api/v1/services


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
  list or watch objects of kind Service


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../objects/index.adoc#servicelist-core-v1[`ServiceList core/v1`]
|===


=== /api/v1/namespaces/{namespace}/services

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
  `GET`

Description::
  list or watch objects of kind Service


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
| xref:../objects/index.adoc#servicelist-core-v1[`ServiceList core/v1`]
|===

HTTP method::
  `POST`

Description::
  create a Service


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
| xref:../network_apis/service-core-v1.adoc#service-core-v1[`Service core/v1`]
| 
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../network_apis/service-core-v1.adoc#service-core-v1[`Service core/v1`]
|===


=== /api/v1/namespaces/{namespace}/services/{name}

.Global path parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `name`
| `string`
| name of the Service
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
  delete a Service


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
  read the specified Service


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../network_apis/service-core-v1.adoc#service-core-v1[`Service core/v1`]
|===

HTTP method::
  `PATCH`

Description::
  partially update the specified Service


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
| xref:../network_apis/service-core-v1.adoc#service-core-v1[`Service core/v1`]
|===

HTTP method::
  `PUT`

Description::
  replace the specified Service


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
| xref:../network_apis/service-core-v1.adoc#service-core-v1[`Service core/v1`]
| 
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../network_apis/service-core-v1.adoc#service-core-v1[`Service core/v1`]
|===


=== /api/v1/namespaces/{namespace}/services/{name}/proxy

.Global path parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `name`
| `string`
| name of the ServiceProxyOptions
| `namespace`
| `string`
| object name and auth scope, such as for teams and projects
|===

.Global query parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `path`
| `string`
| Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy.
|===

HTTP method::
  `DELETE`

Description::
  connect DELETE requests to proxy of Service


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
  connect GET requests to proxy of Service


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
  connect HEAD requests to proxy of Service


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
  connect OPTIONS requests to proxy of Service


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
  connect PATCH requests to proxy of Service


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
  connect POST requests to proxy of Service


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
  connect PUT requests to proxy of Service


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| `string`
|===


=== /api/v1/namespaces/{namespace}/services/{name}/status

.Global path parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `name`
| `string`
| name of the Service
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
  read status of the specified Service


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../network_apis/service-core-v1.adoc#service-core-v1[`Service core/v1`]
|===

HTTP method::
  `PATCH`

Description::
  partially update status of the specified Service


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
| xref:../network_apis/service-core-v1.adoc#service-core-v1[`Service core/v1`]
|===

HTTP method::
  `PUT`

Description::
  replace status of the specified Service


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
| xref:../network_apis/service-core-v1.adoc#service-core-v1[`Service core/v1`]
| 
|===

.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| xref:../network_apis/service-core-v1.adoc#service-core-v1[`Service core/v1`]
|===


=== /api/v1/namespaces/{namespace}/services/{name}/proxy/{path}

.Global path parameters
[cols="1,1,2",options="header"]
|===
| Parameter | Type | Description
| `name`
| `string`
| name of the ServiceProxyOptions
| `namespace`
| `string`
| object name and auth scope, such as for teams and projects
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
| Path is the part of URLs that include service endpoints, suffixes, and parameters to use for the current proxy request to service. For example, the whole request URL is http://localhost/api/v1/namespaces/kube-system/services/elasticsearch-logging/_search?q&#x3D;user:kimchy. Path is _search?q&#x3D;user:kimchy.
|===

HTTP method::
  `DELETE`

Description::
  connect DELETE requests to proxy of Service


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
  connect GET requests to proxy of Service


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
  connect HEAD requests to proxy of Service


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
  connect OPTIONS requests to proxy of Service


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
  connect PATCH requests to proxy of Service


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
  connect POST requests to proxy of Service


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
  connect PUT requests to proxy of Service


.HTTP responses
[cols="1,1",options="header"]
|===
| HTTP code | Reponse body
| 200 - OK
| `string`
|===


