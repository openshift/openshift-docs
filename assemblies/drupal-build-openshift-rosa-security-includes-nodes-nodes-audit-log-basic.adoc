// Module included in the following assemblies:
//
// * security/audit-log-view.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-pods-audit-log-basic_{context}"]
= About the API audit log

Audit works at the API server level, logging all requests coming to the server. Each audit log contains the following information:

.Audit log fields
[cols="1,2",options="header"]
|===
|Field |Description
|`level` | The audit level at which the event was generated.
|`auditID` |A unique audit ID, generated for each request.
|`stage` |The stage of the request handling when this event instance was generated.
|`requestURI` |The request URI as sent by the client to a server.
|`verb` |The Kubernetes verb associated with the request. For non-resource requests, this is the lowercase HTTP method.
|`user` |The authenticated user information.
|`impersonatedUser` |Optional. The impersonated user information, if the request is impersonating another user.
|`sourceIPs` |Optional. The source IPs, from where the request originated and any intermediate proxies.
|`userAgent` |Optional. The user agent string reported by the client. Note that the user agent is provided by the client, and must not be trusted.
|`objectRef` |Optional. The object reference this request is targeted at. This does not apply for `List`-type requests, or non-resource requests.
|`responseStatus` |Optional. The response status, populated even when the `ResponseObject` is not a `Status` type. For successful responses, this will only include the code. For non-status type error responses, this will be auto-populated with the error message.
|`requestObject` |Optional. The API object from the request, in JSON format. The `RequestObject` is recorded as is in the request (possibly re-encoded as JSON), prior to version conversion, defaulting, admission or merging. It is an external versioned object type, and might not be a valid object on its own. This is omitted for non-resource requests and is only logged at request level and higher.
|`responseObject` |Optional. The API object returned in the response, in JSON format. The `ResponseObject` is recorded after conversion to the external type, and serialized as JSON. This is omitted for non-resource requests and is only logged at response level.
|`requestReceivedTimestamp` |The time that the request reached the API server.
|`stageTimestamp` |The time that the request reached the current audit stage.
|`annotations` |Optional. An unstructured key value map stored with an audit event that may be set by plugins invoked in the request serving chain, including authentication, authorization and admission plugins. Note that these annotations are for the audit event, and do not correspond to the `metadata.annotations` of the submitted object. Keys should uniquely identify the informing component to avoid name collisions, for example `podsecuritypolicy.admission.k8s.io/policy`. Values should be short. Annotations are included in the metadata level.
|===

Example output for the Kubernetes API server:

[source,json]
----
{"kind":"Event","apiVersion":"audit.k8s.io/v1","level":"Metadata","auditID":"ad209ce1-fec7-4130-8192-c4cc63f1d8cd","stage":"ResponseComplete","requestURI":"/api/v1/namespaces/openshift-kube-controller-manager/configmaps/cert-recovery-controller-lock?timeout=35s","verb":"update","user":{"username":"system:serviceaccount:openshift-kube-controller-manager:localhost-recovery-client","uid":"dd4997e3-d565-4e37-80f8-7fc122ccd785","groups":["system:serviceaccounts","system:serviceaccounts:openshift-kube-controller-manager","system:authenticated"]},"sourceIPs":["::1"],"userAgent":"cluster-kube-controller-manager-operator/v0.0.0 (linux/amd64) kubernetes/$Format","objectRef":{"resource":"configmaps","namespace":"openshift-kube-controller-manager","name":"cert-recovery-controller-lock","uid":"5c57190b-6993-425d-8101-8337e48c7548","apiVersion":"v1","resourceVersion":"574307"},"responseStatus":{"metadata":{},"code":200},"requestReceivedTimestamp":"2020-04-02T08:27:20.200962Z","stageTimestamp":"2020-04-02T08:27:20.206710Z","annotations":{"authorization.k8s.io/decision":"allow","authorization.k8s.io/reason":"RBAC: allowed by ClusterRoleBinding \"system:openshift:operator:kube-controller-manager-recovery\" of ClusterRole \"cluster-admin\" to ServiceAccount \"localhost-recovery-client/openshift-kube-controller-manager\""}}
----
