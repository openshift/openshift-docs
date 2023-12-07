// Module is included in the following assemblies:
// * logging/cluster-logging-loki.adoc
// * network_observability/installing-operators.adoc

ifeval::["{context}" == "cluster-logging-loki"]
:restricted:
endif::[]

:_mod-docs-content-type: CONCEPT
[id="loki-deployment-sizing_{context}"]
= Loki deployment sizing

Sizing for Loki follows the format of `<N>x.<size>` where the value `<N>` is number of instances and `<size>` specifies performance capabilities.

.Loki sizing
[cols="1h,3*",options="header"]
|===
|
|1x.extra-small
|1x.small
|1x.medium

|Data transfer
|100GB/day
|500GB/day
|2TB/day

|Queries per second (QPS)
|1-25 QPS at 200ms
|25-50 QPS at 200ms
|25-75 QPS at 200ms

|Replication factor
|2
|2
|2

|Total CPU requests
|14 vCPUs
|34 vCPUs
|54 vCPUs

ifdef::restricted[]
|Total CPU requests if using the ruler
|16 vCPUs
|42 vCPUs
|70 vCPUs
endif::restricted[]

|Total memory requests
|31Gi
|67Gi
|139Gi

ifdef::restricted[]
|Total memory requests if using the ruler
|35Gi
|83Gi
|171Gi
endif::restricted[]

|Total disk requests
|430Gi
|430Gi
|590Gi

ifdef::restricted[]
|Total disk requests if using the ruler
|650Gi
|650Gi
|910Gi
endif::restricted[]
|===

ifeval::["{context}" == "cluster-logging-loki"]
:!restricted:
endif::[]
