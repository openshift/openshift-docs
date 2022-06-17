[id="cluster-logging-exported-fields-kubernetes_{context}"]

// Normally, the following title would be an H1 prefixed with an `=`. However, because the following content is auto-generated at https://github.com/ViaQ/documentation/blob/main/src/data_model/public/kubernetes.part.adoc and pasted here, it is more efficient to use it as-is with no modifications. Therefore, to "realign" the content, I am going to prefix the title with `==` and use `include::modules/cluster-logging-exported-fields-kubernetes.adoc[leveloffset=0]` in the assembly file.

// DO NOT MODIFY THE FOLLOWING CONTENT. Instead, update https://github.com/ViaQ/documentation/blob/main/src/data_model/model/kubernetes.yaml and run `make` as instructed here: https://github.com/ViaQ/documentation


== kubernetes

The namespace for Kubernetes-specific metadata

[horizontal]
Data type:: group

=== kubernetes.pod_name

The name of the pod

[horizontal]
Data type:: keyword


=== kubernetes.pod_id

The Kubernetes ID of the pod

[horizontal]
Data type:: keyword


=== kubernetes.namespace_name

The name of the namespace in Kubernetes

[horizontal]
Data type:: keyword


=== kubernetes.namespace_id

The ID of the namespace in Kubernetes

[horizontal]
Data type:: keyword


=== kubernetes.host

The Kubernetes node name

[horizontal]
Data type:: keyword



=== kubernetes.container_name

The name of the container in Kubernetes

[horizontal]
Data type:: keyword



=== kubernetes.annotations

Annotations associated with the Kubernetes object

[horizontal]
Data type:: group


=== kubernetes.labels

Labels present on the original Kubernetes Pod

[horizontal]
Data type:: group






=== kubernetes.event

The Kubernetes event obtained from the Kubernetes master API. This event description loosely follows `type Event` in link:https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.23/#event-v1-core[Event v1 core].

[horizontal]
Data type:: group

==== kubernetes.event.verb

The type of event, `ADDED`, `MODIFIED`, or `DELETED`

[horizontal]
Data type:: keyword
Example value:: `ADDED`


==== kubernetes.event.metadata

Information related to the location and time of the event creation

[horizontal]
Data type:: group

===== kubernetes.event.metadata.name

The name of the object that triggered the event creation

[horizontal]
Data type:: keyword
Example value:: `java-mainclass-1.14d888a4cfc24890`


===== kubernetes.event.metadata.namespace

The name of the namespace where the event originally occurred. Note that it differs from `kubernetes.namespace_name`, which is the namespace where the `eventrouter` application is deployed.

[horizontal]
Data type:: keyword
Example value:: `default`


===== kubernetes.event.metadata.selfLink

A link to the event

[horizontal]
Data type:: keyword
Example value:: `/api/v1/namespaces/javaj/events/java-mainclass-1.14d888a4cfc24890`


===== kubernetes.event.metadata.uid

The unique ID of the event

[horizontal]
Data type:: keyword
Example value:: `d828ac69-7b58-11e7-9cf5-5254002f560c`


===== kubernetes.event.metadata.resourceVersion

A string that identifies the server's internal version of the event. Clients can use this string to determine when objects have changed.

[horizontal]
Data type:: integer
Example value:: `311987`



==== kubernetes.event.involvedObject

The object that the event is about.

[horizontal]
Data type:: group

===== kubernetes.event.involvedObject.kind

The type of object

[horizontal]
Data type:: keyword
Example value:: `ReplicationController`


===== kubernetes.event.involvedObject.namespace

The namespace name of the involved object. Note that it may differ from `kubernetes.namespace_name`, which is the namespace where the `eventrouter` application is deployed.

[horizontal]
Data type:: keyword
Example value:: `default`


===== kubernetes.event.involvedObject.name

The name of the object that triggered the event

[horizontal]
Data type:: keyword
Example value:: `java-mainclass-1`


===== kubernetes.event.involvedObject.uid

The unique ID of the object

[horizontal]
Data type:: keyword
Example value:: `e6bff941-76a8-11e7-8193-5254002f560c`


===== kubernetes.event.involvedObject.apiVersion

The version of kubernetes master API

[horizontal]
Data type:: keyword
Example value:: `v1`


===== kubernetes.event.involvedObject.resourceVersion

A string that identifies the server's internal version of the pod that triggered the event. Clients can use this string to determine when objects have changed.

[horizontal]
Data type:: keyword
Example value:: `308882`



==== kubernetes.event.reason

A short machine-understandable string that gives the reason for generating this event

[horizontal]
Data type:: keyword
Example value:: `SuccessfulCreate`


==== kubernetes.event.source_component

The component that reported this event

[horizontal]
Data type:: keyword
Example value:: `replication-controller`


==== kubernetes.event.firstTimestamp

The time at which the event was first recorded

[horizontal]
Data type:: date
Example value:: `2017-08-07 10:11:57.000000000 Z`


==== kubernetes.event.count

The number of times this event has occurred

[horizontal]
Data type:: integer
Example value:: `1`


==== kubernetes.event.type

The type of event, `Normal` or `Warning`. New types could be added in the future.

[horizontal]
Data type:: keyword
Example value:: `Normal`

== OpenShift

The namespace for openshift-logging specific metadata

[horizontal]
Data type:: group

=== openshift.labels

Labels added by the Cluster Log Forwarder configuration

[horizontal]
Data type:: group
