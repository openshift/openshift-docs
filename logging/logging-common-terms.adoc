:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
include::_attributes/attributes-openshift-dedicated.adoc[]
[id="openshift-logging-common-terms"]
= Glossary
:context: openshift-logging-common-terms

toc::[]

This glossary defines common terms that are used in the {logging} documentation.

Annotation::
You can use annotations to attach metadata to objects.

{clo}::
The {clo} provides a set of APIs to control the collection and forwarding of application, infrastructure, and audit logs.

Custom resource (CR)::
A CR is an extension of the Kubernetes API. To configure the {logging} and log forwarding, you can customize the `ClusterLogging` and the `ClusterLogForwarder` custom resources.

Event router::
The event router is a pod that watches {product-title} events. It collects logs by using the {logging}.

Fluentd::
Fluentd is a log collector that resides on each {product-title} node. It gathers application, infrastructure, and audit logs and forwards them to different outputs.

Garbage collection::
Garbage collection is the process of cleaning up cluster resources, such as terminated containers and images that are not referenced by any running pods.

Elasticsearch::
Elasticsearch is a distributed search and analytics engine. {product-title} uses Elasticsearch as a default log store for the {logging}.

{es-op}::
The {es-op} is used to run an Elasticsearch cluster on {product-title}. The {es-op} provides self-service for the Elasticsearch cluster operations and is used by the {logging}.

Indexing::
Indexing is a data structure technique that is used to quickly locate and access data. Indexing optimizes the performance by minimizing the amount of disk access required when a query is processed.

JSON logging::
The Log Forwarding API enables you to parse JSON logs into a structured object and forward them to either the {Logging} managed Elasticsearch or any other third-party system supported by the Log Forwarding API.

Kibana::
Kibana is a browser-based console interface to query, discover, and visualize your Elasticsearch data through histograms, line graphs, and pie charts.

Kubernetes API server::
Kubernetes API server validates and configures data for the API objects.

Labels::
Labels are key-value pairs that you can use to organize and select subsets of objects, such as a pod.

Logging::
With the {logging}, you can aggregate application, infrastructure, and audit logs throughout your cluster. You can also store them to a default log store, forward them to third party systems, and query and visualize the stored logs in the default log store.

Logging collector::
A logging collector collects logs from the cluster, formats them, and forwards them to the log store or third party systems.

Log store::
A log store is used to store aggregated logs. You can use an internal log store or forward logs to external log stores.

Log visualizer::
Log visualizer is the user interface (UI) component you can use to view information such as logs, graphs, charts, and other metrics.

Node::
A node is a worker machine in the {product-title} cluster. A node is either a virtual machine (VM) or a physical machine.

Operators::
Operators are the preferred method of packaging, deploying, and managing a Kubernetes application in an {product-title} cluster. An Operator takes human operational knowledge and encodes it into software that is packaged and shared with customers.

Pod::
A pod is the smallest logical unit in Kubernetes. A pod consists of one or more containers and runs on a worker node.

Role-based access control (RBAC)::
RBAC is a key security control to ensure that cluster users and workloads have access only to resources required to execute their roles.

Shards::
Elasticsearch organizes log data from Fluentd into datastores, or indices, then subdivides each index into multiple pieces called shards.

Taint::
Taints ensure that pods are scheduled onto appropriate nodes. You can apply one or more taints on a node.

Toleration::
You can apply tolerations to pods. Tolerations allow the scheduler to schedule pods with matching taints.

Web console::
A user interface (UI) to manage {product-title}.
ifdef::openshift-rosa,openshift-dedicated[]
The web console for {product-title} can be found at link:https://console.redhat.com/openshift[https://console.redhat.com/openshift].
endif::[]
