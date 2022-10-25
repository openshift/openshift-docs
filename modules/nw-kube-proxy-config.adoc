// Module included in the following assemblies:
//
// * networking/openshift_sdn/configuring-kube-proxy.adoc

[id="nw-kube-proxy-config_{context}"]
= kube-proxy configuration parameters

You can modify the following `kubeProxyConfig` parameters.

[NOTE]
====
Because of performance improvements introduced in {product-title} 4.3 and greater, adjusting the `iptablesSyncPeriod` parameter is no longer necessary.
====

.Parameters
[cols="30%,30%,30%,10%",options="header"]
|====
|Parameter|Description|Values|Default

|`iptablesSyncPeriod`
|The refresh period for `iptables` rules.
|A time interval, such as `30s` or `2m`. Valid
suffixes include `s`, `m`, and `h` and are described in the
link:https://golang.org/pkg/time/#ParseDuration[Go time package] documentation.
|`30s`

|`proxyArguments.iptables-min-sync-period`
|The minimum duration before refreshing `iptables` rules. This parameter ensures
that the refresh does not happen too frequently. By default, a refresh starts as soon as a change that affects `iptables` rules occurs.
|A time interval, such as `30s` or `2m`. Valid suffixes include `s`,
`m`, and `h` and are described in the
link:https://golang.org/pkg/time/#ParseDuration[Go time package]
|`0s`

|====
