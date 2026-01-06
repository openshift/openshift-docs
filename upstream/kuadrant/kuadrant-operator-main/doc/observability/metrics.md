# Metrics

This is a reference page for some of the different metrics used in example
dashboards and alerts. It is not an exhaustive list. The documentation for each
component may provide more details on a per-component basis. Some of the metrics
are sourced from components outside the Kuadrant project, for example, Envoy.
The value of this reference is showing some of the more widely desired metrics,
and how to join the metrics from different sources together in a meaningful way.

## Metrics sources

* Kuadrant components
* [Istio](https://istio.io/latest/docs/reference/config/metrics/)
* [Envoy](https://www.envoyproxy.io/docs/envoy/latest/operations/admin.html#get--stats)
* [Kube State Metrics](https://github.com/kubernetes/kube-state-metrics)
* [Gateway API State Metrics](https://github.com/Kuadrant/gateway-api-state-metrics)
* [Kubernetes metrics](https://kubernetes.io/docs/concepts/cluster-administration/system-metrics/#metrics-in-kubernetes)

## Resource usage metrics

Resource metrics, like CPU, memory and disk usage, primarily come from the Kubernetes
metrics components. These include `container_cpu_usage_seconds_total`, `container_memory_working_set_bytes`
and `kubelet_volume_stats_used_bytes`. A [stable list of metrics](https://github.com/kubernetes/kubernetes/blob/master/test/instrumentation/testdata/stable-metrics-list.yaml) is maintained in
the Kubernetes repository. These low-level metrics typically have a set of
[recording rules](https://prometheus.io/docs/practices/rules/#aggregation) that
aggregate values by labels and time ranges.
For example, `node_namespace_pod_container:container_cpu_usage_seconds_total:sum_irate` or `namespace_workload_pod:kube_pod_owner:relabel`.
If you have deployed the [kube-prometheus](https://github.com/prometheus-operator/kube-prometheus) project, you should have the majority of 
these metrics being scraped.

## Networking metrics

Low-level networking metrics like `container_network_receive_bytes_total` are also
available from the Kubernetes metrics components.
HTTP & GRPC traffic metrics with higher level labels are [available from Istio](https://istio.io/latest/docs/reference/config/metrics/).
One of the main metrics would be `istio_requests_total`, which is a counter incremented for every request handled by an Istio proxy.
Latency metrics are available via the `istio_request_duration_milliseconds` metric, with buckets for varying response times.

Some example dashboards have panels that make use of the request URL path.
The path is *not* added as a label to Istio metrics by default, as it has the potential
to increase metric cardinality, and thus storage requirements.
If you want to make use of the path in your queries or visualisations, you can enable
the request path metric via the [Telemetry resource](https://istio.io/latest/docs/reference/config/telemetry/#MetricSelector-IstioMetric) in istio:

```
apiVersion: telemetry.istio.io/v1alpha1
kind: Telemetry
metadata:
  name: namespace-metrics
  namespace: istio-system
spec:
  metrics:
  - providers:
    - name: prometheus
    overrides:
    - match:
        metric: REQUEST_COUNT
      tagOverrides:
        request_url_path:
          value: "request.url_path"
    - match:      
        metric: REQUEST_DURATION
      tagOverrides:
        request_url_path:
          value: "request.url_path"
```

## State metrics

The [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics/tree/main/docs#default-resources)
project exposes the state of various kuberenetes resources
as metrics and labels. For example, the ready `status` of a `Pod` is available as
`kube_pod_status_ready`, with labels for the pod `name` and `namespace`. This can
be useful for linking lower level container metrics back to a meaningful resource
in the Kubernetes world.

## Joining metrics

Metric queries can be as simple as just the name of the metric, or can be complex
with joining & grouping. A lot of the time it can be useful to tie back low level
metrics to more meaningful Kubernetes resources. For example, if the memory usage
is maxed out on a container and that container is constantly being OOMKilled, it
can be useful to get the Deployment and Namespace of that container for debugging.
Prometheus query language (or promql) allows [vector matching](https://prometheus.io/docs/prometheus/latest/querying/operators/#vector-matching)
or results (sometimes called joining).

When using Gateway API and Kuadrant resources like HTTPRoute and RateLimitPolicy,
the state metrics can be joined to Istio metrics to give a meaningful result set.
Here's an example that queries the number of requests per second, and includes
the name of the HTTPRoute that the traffic is for.

```promql
sum(
    rate(
        istio_requests_total{}[5m]
    )
) by (destination_service_name)

* on(destination_service_name) group_right 
    label_replace(gatewayapi_httproute_labels{}, \"destination_service_name\", \"$1\",\"service\", \"(.+)\")
```

Breaking this query down, there are 2 parts.
The first part is getting the rate of requests hitting the Istio gateway, aggregated
to 5m intervals:

```promql
sum(
    rate(
        destination_service_name{}[5m]
    )
) by (destination_service_name)
```

The result set here will include a label for the destination service name (i.e.
the Service in Kubernetes). This label is key to looking up the HTTPRoute this
traffic belongs to.

The 2nd part of the query uses the `gatewayapi_httproute_labels` metric and the
`label_replace` function. The `gatewayapi_httproute_labels` metric gives a list
of all httproutes, including any labels on them. The HTTPRoute in this example
has a label called 'service', set to be the same as the Istio service name.
This allows us to join the 2 results set.
However, because the label doesn't match exactly (`destination_service_name` and `service`),
we can replace the label so that it does match. That's what the `label_replace`
does.

```promql
    label_replace(gatewayapi_httproute_labels{}, \"destination_service_name\", \"$1\",\"service\", \"(.+)\")
```

The 2 parts are joined together using vector matching.

```promql
* on(destination_service_name) group_right 
```

* `*` is the binary operator i.e. multiplication (gives join like behaviour)
* `on()` specifies which labels to "join" the 2 results with
* `group_right` enables a one to many matching.

See the [Prometheus documentation](https://prometheus.io/docs/prometheus/latest/querying/operators/#vector-matching) for further details on matching.
