// Module included in the following assemblies:
//
// * ingress/configure-ingress-operator.adoc
:_mod-docs-content-type: REFERENCE
[id="nw-ingress-controller-configuration-parameters_{context}"]
= Ingress Controller configuration parameters

The `ingresscontrollers.operator.openshift.io` resource offers the following
configuration parameters.

[cols="3a,8a",options="header"]
|===
|Parameter |Description

|`domain`
|`domain` is a DNS name serviced by the Ingress Controller and is used to configure multiple features:

* For the `LoadBalancerService` endpoint publishing strategy, `domain` is used to configure DNS records. See `endpointPublishingStrategy`.

* When using a generated default certificate, the certificate is valid for `domain` and its `subdomains`. See `defaultCertificate`.

* The value is published to individual Route statuses so that users know where to target external DNS records.

The `domain` value must be unique among all Ingress Controllers and cannot be updated.

If empty, the default value is `ingress.config.openshift.io/cluster` `.spec.domain`.

|`replicas`
|`replicas` is the desired number of Ingress Controller replicas. If not set, the default value is `2`.

|`endpointPublishingStrategy`
|`endpointPublishingStrategy` is used to publish the Ingress Controller endpoints to other networks, enable load balancer integrations, and provide access to other systems.

ifndef::openshift-rosa,openshift-dedicated[]
On GCP, AWS, and Azure you can configure the following `endpointPublishingStrategy` fields:
endif::openshift-rosa,openshift-dedicated[]

ifdef::openshift-rosa,openshift-dedicated[]
You can configure the following `endpointPublishingStrategy` fields:
endif::openshift-rosa,openshift-dedicated[]

* `loadBalancer.scope`
* `loadBalancer.allowedSourceRanges`

If not set, the default value is based on `infrastructure.config.openshift.io/cluster` `.status.platform`:

ifdef::openshift-rosa,openshift-dedicated[]
* Amazon Web Services (AWS): `LoadBalancerService` (with External scope)
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-dedicated[]
* Google Cloud Platform (GCP): `LoadBalancerService` (with External scope)
endif::openshift-dedicated[]
ifndef::openshift-rosa,openshift-dedicated[]
* Azure: `LoadBalancerService` (with External scope)
* Google Cloud Platform (GCP): `LoadBalancerService` (with External scope)
* Bare metal: `NodePortService`
* Other: `HostNetwork`
endif::openshift-rosa,openshift-dedicated[]
+
[NOTE]
====
`HostNetwork` has a `hostNetwork` field with the following default values for the optional binding ports: `httpPort: 80`, `httpsPort: 443`, and `statsPort: 1936`.
With the binding ports, you can deploy multiple Ingress Controllers on the same node for the `HostNetwork` strategy.

.Example
[source,yaml]
----
apiVersion: operator.openshift.io/v1
kind: IngressController
metadata:
  name: internal
  namespace: openshift-ingress-operator
spec:
  domain: example.com
  endpointPublishingStrategy:
    type: HostNetwork
    hostNetwork:
      httpPort: 80
      httpsPort: 443
      statsPort: 1936
----
====
+
[NOTE]
====
On {rh-openstack-first}, the `LoadBalancerService` endpoint publishing strategy is only supported if a cloud provider is configured to create health monitors. For {rh-openstack} 16.2, this strategy is only possible if you use the Amphora Octavia provider.

For more information, see the "Setting cloud provider options" section of the {rh-openstack} installation documentation.
====
ifndef::openshift-rosa[]
For most platforms, the `endpointPublishingStrategy` value can be updated. On GCP, you can configure the following `endpointPublishingStrategy` fields:

* `loadBalancer.scope`
* `loadbalancer.providerParameters.gcp.clientAccess`
* `hostNetwork.protocol`
* `nodePort.protocol`
endif::openshift-rosa[]

|`defaultCertificate`
|The `defaultCertificate` value is a reference to a secret that contains the default certificate that is served by the Ingress Controller. When Routes do not specify their own certificate, `defaultCertificate` is used.

The secret must contain the following keys and data:
* `tls.crt`: certificate file contents
* `tls.key`: key file contents

If not set, a wildcard certificate is automatically generated and used. The certificate is valid for the Ingress Controller `domain` and `subdomains`, and
the generated certificate's CA is automatically integrated with the
cluster's trust store.

The in-use certificate, whether generated or user-specified, is automatically integrated with {product-title} built-in OAuth server.

|`namespaceSelector`
|`namespaceSelector` is used to filter the set of namespaces serviced by the
Ingress Controller. This is useful for implementing shards.

|`routeSelector`
|`routeSelector` is used to filter the set of Routes serviced by the Ingress Controller. This is useful for implementing shards.

|`nodePlacement`
|`nodePlacement` enables explicit control over the scheduling of the Ingress Controller.

If not set, the defaults values are used.

[NOTE]
====
The `nodePlacement` parameter includes two parts, `nodeSelector` and `tolerations`. For example:

[source,yaml]
----
nodePlacement:
 nodeSelector:
   matchLabels:
     kubernetes.io/os: linux
 tolerations:
 - effect: NoSchedule
   operator: Exists
----
====

|`tlsSecurityProfile`
|`tlsSecurityProfile` specifies settings for TLS connections for Ingress Controllers.

If not set, the default value is based on the `apiservers.config.openshift.io/cluster` resource.

When using the `Old`, `Intermediate`, and `Modern` profile types, the effective profile configuration is subject to change between releases. For example, given a specification to use the `Intermediate` profile deployed on release `X.Y.Z`, an upgrade to release `X.Y.Z+1` may cause a new profile configuration to be applied to the Ingress Controller, resulting in a rollout.

The minimum TLS version for Ingress Controllers is `1.1`, and the maximum TLS version is `1.3`.

[NOTE]
====
Ciphers and the minimum TLS version of the configured security profile are reflected in the `TLSProfile` status.
====

[IMPORTANT]
====
The Ingress Operator converts the TLS `1.0` of an `Old` or `Custom` profile to `1.1`.
====

|`clientTLS`
|`clientTLS` authenticates client access to the cluster and services; as a result, mutual TLS authentication is enabled. If not set, then client TLS is not enabled.

`clientTLS` has the required subfields, `spec.clientTLS.clientCertificatePolicy` and `spec.clientTLS.ClientCA`.

The `ClientCertificatePolicy` subfield accepts one of the two values: `Required` or `Optional`. The `ClientCA` subfield specifies a config map that is in the openshift-config namespace. The config map should contain a CA certificate bundle.

The `AllowedSubjectPatterns` is an optional value that specifies a list of regular expressions, which are matched against the distinguished name on a valid client certificate to filter requests. The regular expressions must use PCRE syntax. At least one pattern must match a client certificate's distinguished name; otherwise, the Ingress Controller rejects the certificate and denies the connection. If not specified, the Ingress Controller does not reject certificates based on the distinguished name.

|`routeAdmission`
|`routeAdmission` defines a policy for handling new route claims, such as allowing or denying claims across namespaces.

`namespaceOwnership` describes how hostname claims across namespaces should be handled. The default is `Strict`.

* `Strict`: does not allow routes to claim the same hostname across namespaces.
* `InterNamespaceAllowed`: allows routes to claim different paths of the same hostname across namespaces.

`wildcardPolicy` describes how routes with wildcard policies are handled by the Ingress Controller.

* `WildcardsAllowed`: Indicates routes with any wildcard policy are admitted by the Ingress Controller.

* `WildcardsDisallowed`: Indicates only routes with a wildcard policy of `None` are admitted by the Ingress Controller. Updating `wildcardPolicy` from `WildcardsAllowed` to `WildcardsDisallowed` causes admitted routes with a wildcard policy of `Subdomain` to stop working. These routes must be recreated to a wildcard policy of `None` to be readmitted by the Ingress Controller. `WildcardsDisallowed` is the default setting.

|`IngressControllerLogging`
|`logging` defines parameters for what is logged where. If this field is empty, operational logs are enabled but access logs are disabled.

* `access` describes how client requests are logged. If this field is empty, access logging is disabled.
** `destination` describes a destination for log messages.
*** `type` is the type of destination for logs:
**** `Container` specifies that logs should go to a sidecar container. The Ingress Operator configures the container, named *logs*, on the Ingress Controller pod and configures the Ingress Controller to write logs to the container. The expectation is that the administrator configures a custom logging solution that reads logs from this container. Using container logs means that logs may be dropped if the rate of logs exceeds the container runtime capacity or the custom logging solution capacity.
**** `Syslog` specifies that logs are sent to a Syslog endpoint. The administrator must specify an endpoint that can receive Syslog messages. The expectation is that the administrator has configured a custom Syslog instance.
*** `container` describes parameters for the `Container` logging destination type. Currently there are no parameters for container logging, so this field must be empty.
*** `syslog` describes parameters for the `Syslog` logging destination type:
**** `address` is the IP address of the syslog endpoint that receives log messages.
**** `port` is the UDP port number of the syslog endpoint that receives log messages.
**** `maxLength` is the maximum length of the syslog message. It must be between `480` and `4096` bytes. If this field is empty, the maximum length is set to the default value of `1024` bytes.
**** `facility` specifies the syslog facility of log messages. If this field is empty, the facility is `local1`. Otherwise, it must specify a valid syslog facility: `kern`, `user`, `mail`, `daemon`, `auth`, `syslog`, `lpr`, `news`, `uucp`, `cron`, `auth2`, `ftp`, `ntp`, `audit`, `alert`, `cron2`, `local0`, `local1`, `local2`, `local3`. `local4`, `local5`, `local6`, or `local7`.
** `httpLogFormat` specifies the format of the log message for an HTTP request. If this field is empty, log messages use the implementation's default HTTP log format. For HAProxy's default HTTP log format, see link:http://cbonte.github.io/haproxy-dconv/2.0/configuration.html#8.2.3[the HAProxy documentation].

|`httpHeaders`
|`httpHeaders` defines the policy for HTTP headers.

By setting the `forwardedHeaderPolicy` for the `IngressControllerHTTPHeaders`, you specify when and how the Ingress Controller sets the `Forwarded`, `X-Forwarded-For`, `X-Forwarded-Host`, `X-Forwarded-Port`, `X-Forwarded-Proto`, and `X-Forwarded-Proto-Version` HTTP headers.

By default, the policy is set to `Append`.

* `Append` specifies that the Ingress Controller appends the headers, preserving any existing headers.
* `Replace` specifies that the Ingress Controller sets the headers, removing any existing headers.
* `IfNone` specifies that the Ingress Controller sets the headers if they are not already set.
* `Never` specifies that the Ingress Controller never sets the headers, preserving any existing headers.

By setting `headerNameCaseAdjustments`, you can specify case adjustments that can be applied to HTTP header names. Each adjustment is specified as an HTTP header name with the desired capitalization. For example, specifying `X-Forwarded-For` indicates that the `x-forwarded-for` HTTP header should be adjusted to have the specified capitalization.

These adjustments are only applied to cleartext, edge-terminated, and re-encrypt routes, and only when using HTTP/1.

For request headers, these adjustments are applied only for routes that have the `haproxy.router.openshift.io/h1-adjust-case=true` annotation. For response headers, these adjustments are applied to all HTTP responses. If this field is empty, no request headers are adjusted.

`actions` specifies options for performing certain actions on headers. Headers cannot be set or deleted for TLS passthrough connections. The `actions` field has additional subfields `spec.httpHeader.actions.response` and `spec.httpHeader.actions.request`:

* The `response` subfield specifies a list of HTTP response headers to set or delete.

* The `request` subfield specifies a list of HTTP request headers to set or delete.

|`httpCompression`
|`httpCompression` defines the policy for HTTP traffic compression.

* `mimeTypes` defines a list of MIME types to which compression should be applied. For example, `text/css; charset=utf-8`, `text/html`, `text/*`, `image/svg+xml`, `application/octet-stream`, `X-custom/customsub`, using the format pattern, `type/subtype; [;attribute=value]`. The `types` are: application, image, message, multipart, text, video, or a custom type prefaced by `X-`; e.g. To see the full notation for MIME types and subtypes, see link:https://datatracker.ietf.org/doc/html/rfc1341#page-7[RFC1341]

|`httpErrorCodePages`
|`httpErrorCodePages` specifies custom HTTP error code response pages. By default, an IngressController uses error pages built into the IngressController image.

|`httpCaptureCookies`
|`httpCaptureCookies` specifies HTTP cookies that you want to capture in access logs. If the `httpCaptureCookies` field is empty, the access logs do not capture the cookies.

For any cookie that you want to capture, the following parameters must be in your `IngressController` configuration:

* `name` specifies the name of the cookie.
* `maxLength` specifies tha maximum length of the cookie.
* `matchType` specifies if the field `name` of the cookie exactly matches the capture cookie setting or is a prefix of the capture cookie setting. The `matchType` field uses the `Exact` and `Prefix` parameters.

For example:
[source,yaml]
----
  httpCaptureCookies:
  - matchType: Exact
    maxLength: 128
    name: MYCOOKIE
----

|`httpCaptureHeaders`
|`httpCaptureHeaders` specifies the HTTP headers that you want to capture in the access logs. If the `httpCaptureHeaders` field is empty, the access logs do not capture the headers.

`httpCaptureHeaders` contains two lists of headers to capture in the access logs. The two lists of header fields are `request` and `response`. In both lists, the `name` field must specify the header name and the `maxlength` field must specify the maximum length of the header. For example:

[source,yaml]
----
  httpCaptureHeaders:
    request:
    - maxLength: 256
      name: Connection
    - maxLength: 128
      name: User-Agent
    response:
    - maxLength: 256
      name: Content-Type
    - maxLength: 256
      name: Content-Length
----
|`tuningOptions`
|`tuningOptions` specifies options for tuning the performance of Ingress Controller pods.

* `clientFinTimeout` specifies how long a connection is held open while waiting for the client response to the server closing the connection. The default timeout is `1s`.

* `clientTimeout` specifies how long a connection is held open while waiting for a client response. The default timeout is `30s`.

* `headerBufferBytes` specifies how much memory is reserved, in bytes, for Ingress Controller connection sessions. This value must be at least `16384` if HTTP/2 is enabled for the Ingress Controller. If not set, the default value is `32768` bytes. Setting this field not recommended because `headerBufferBytes` values that are too small can break the Ingress Controller, and `headerBufferBytes` values that are too large could cause the Ingress Controller to use significantly more memory than necessary.

* `headerBufferMaxRewriteBytes` specifies how much memory should be reserved, in bytes, from `headerBufferBytes` for HTTP header rewriting and appending for Ingress Controller connection sessions. The minimum value for `headerBufferMaxRewriteBytes` is `4096`. `headerBufferBytes` must be greater than `headerBufferMaxRewriteBytes` for incoming HTTP requests. If not set, the default value is `8192` bytes. Setting this field not recommended because `headerBufferMaxRewriteBytes` values that are too small can break the Ingress Controller and `headerBufferMaxRewriteBytes` values that are too large could cause the Ingress Controller to use significantly more memory than necessary.

* `healthCheckInterval` specifies how long the router waits between health checks. The default is `5s`.

* `serverFinTimeout` specifies how long a connection is held open while waiting for the server response to the client that is closing the connection. The default timeout is `1s`.

* `serverTimeout` specifies how long a connection is held open while waiting for a server response. The default timeout is `30s`.

* `threadCount` specifies the number of threads to create per HAProxy process. Creating more threads allows each Ingress Controller pod to handle more connections, at the cost of more system resources being used. HAProxy
supports up to `64` threads. If this field is empty, the Ingress Controller uses the default value of `4` threads. The default value can change in future releases. Setting this field is not recommended because increasing the number of HAProxy threads allows Ingress Controller pods to use more CPU time under load, and prevent other pods from receiving the CPU resources they need to perform. Reducing the number of threads can cause the Ingress Controller to perform poorly.

* `tlsInspectDelay` specifies how long the router can hold data to find a matching route. Setting this value too short can cause the router to fall back to the default certificate for edge-terminated, reencrypted, or passthrough routes, even when using a better matched certificate. The default inspect delay is `5s`.

* `tunnelTimeout` specifies how long a tunnel connection, including websockets, remains open while the tunnel is idle. The default timeout is `1h`.

* `maxConnections` specifies the maximum number of simultaneous connections that can be established per HAProxy process. Increasing this value allows each ingress controller pod to handle more connections at the cost of additional system resources. Permitted values are `0`, `-1`, any value within the range `2000` and `2000000`, or the field can be left empty.

** If this field is left empty or has the value `0`, the Ingress Controller will use the default value of `50000`. This value is subject to change in future releases.

** If the field has the value of `-1`, then HAProxy will dynamically compute a maximum value based on the available `ulimits` in the running container. This process results in a large computed value that will incur significant memory usage compared to the current default value of `50000`.

** If the field has a value that is greater than the current operating system limit, the HAProxy process will not start.

** If you choose a discrete value and the router pod is migrated to a new node, it is possible the new node does not have an identical `ulimit` configured. In such cases, the pod fails to start.

** If you have nodes with different `ulimits` configured, and you choose a discrete value, it is recommended to use the value of `-1` for this field so that the maximum number of connections is calculated at runtime.


|`logEmptyRequests`
|`logEmptyRequests` specifies connections for which no request is received and logged. These empty requests come from load balancer health probes or web browser speculative connections (preconnect) and logging these requests can be undesirable. However, these requests can be caused by network errors, in which case logging empty requests can be useful for diagnosing the errors. These requests can be caused by port scans, and logging empty requests can aid in detecting intrusion attempts. Allowed values for this field are `Log` and `Ignore`. The default value is `Log`.

The `LoggingPolicy` type accepts either one of two values:

* `Log`: Setting this value to `Log` indicates that an event should be logged.
* `Ignore`: Setting this value to `Ignore` sets the `dontlognull` option in the HAproxy configuration.

|`HTTPEmptyRequestsPolicy`
|`HTTPEmptyRequestsPolicy` describes how HTTP connections are handled if the connection times out before a request is received. Allowed values for this field are `Respond` and `Ignore`. The default value is `Respond`.

The `HTTPEmptyRequestsPolicy` type accepts either one of two values:

* `Respond`: If the field is set to `Respond`, the Ingress Controller sends an HTTP `400` or `408` response, logs the connection if access logging is enabled, and counts the connection in the appropriate metrics.
* `Ignore`: Setting this option to `Ignore` adds the `http-ignore-probes` parameter in the HAproxy configuration. If the field is set to `Ignore`, the Ingress Controller closes the connection without sending a response, then logs the connection, or incrementing metrics.

These connections come from load balancer health probes or web browser speculative connections (preconnect) and can be safely ignored. However, these requests can be caused by network errors, so setting this field to `Ignore` can impede detection and diagnosis of problems. These requests can be caused by port scans, in which case logging empty requests can aid in detecting intrusion attempts.
|===


[NOTE]
====
All parameters are optional.
====
