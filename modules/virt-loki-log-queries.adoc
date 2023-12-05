// Module included in the following assemblies:
//
// * virt/support/virt-troubleshooting.adoc

:_mod-docs-content-type: reference
[id="virt-loki-log-queries_{context}"]
= {VirtProductName} LogQL queries

You can view and filter aggregated logs for {VirtProductName} components by running Loki Query Language (LogQL) queries on the *Observe* -> *Logs* page in the web console.

The default log type is _infrastructure_. The `virt-launcher` log type is _application_.

Optional: You can include or exclude strings or regular expressions by using line filter expressions.

[NOTE]
====
If the query matches a large number of logs, the query might time out.
====

.{VirtProductName} LogQL example queries
[cols="1a,6a",options="header"]
|====
|Component
|LogQL query

|All
|[source,text]
----
{log_type=~".+"}\|json
\|kubernetes_labels_app_kubernetes_io_part_of="hyperconverged-cluster"
----

|`cdi-apiserver`

`cdi-deployment`

`cdi-operator`
|[source,text]
----
{log_type=~".+"}\|json
\|kubernetes_labels_app_kubernetes_io_part_of="hyperconverged-cluster"
\|kubernetes_labels_app_kubernetes_io_component="storage"
----

|`hco-operator`
|[source,text]
----
{log_type=~".+"}\|json
\|kubernetes_labels_app_kubernetes_io_part_of="hyperconverged-cluster"
\|kubernetes_labels_app_kubernetes_io_component="deployment"
----

|`kubemacpool`
|[source,text]
----
{log_type=~".+"}\|json
\|kubernetes_labels_app_kubernetes_io_part_of="hyperconverged-cluster"
\|kubernetes_labels_app_kubernetes_io_component="network"
----

|`virt-api`

`virt-controller`

`virt-handler`

`virt-operator`
|[source,text]
----
{log_type=~".+"}\|json
\|kubernetes_labels_app_kubernetes_io_part_of="hyperconverged-cluster"
\|kubernetes_labels_app_kubernetes_io_component="compute"
----

|`ssp-operator`
|[source,text]
----
{log_type=~".+"}\|json
\|kubernetes_labels_app_kubernetes_io_part_of="hyperconverged-cluster"
\|kubernetes_labels_app_kubernetes_io_component="schedule"
----

|Container|[source,text]
----
{log_type=~".+",kubernetes_container_name=~"<container>\|<container>"} <1>
\|json\|kubernetes_labels_app_kubernetes_io_part_of="hyperconverged-cluster"
----
<1> Specify one or more containers separated by a pipe (`\|`).

|`virt-launcher`
|You must select *application* from the log type list before running this query.

[source,text]
----
{log_type=~".+", kubernetes_container_name="compute"}\|json
\|!= "custom-ga-command" <1>
----
<1> `\|!= "custom-ga-command"` excludes libvirt logs that contain the string `custom-ga-command`. (https://bugzilla.redhat.com/show_bug.cgi?id=2177684[*BZ#2177684*])
|====

You can filter log lines to include or exclude strings or regular expressions by using line filter expressions.

.Line filter expressions
[cols="1a,2",options="header"]
|====
|Line filter expression|Description
|`\|= "<string>"` |Log line contains string
|`!= "<string>"` |Log line does not contain string
|`\|~ "<regex>"` |Log line contains regular expression
|`!~ "<regex>"` |Log line does not contain regular expression
|====

.Example line filter expression
[source,text]
----
{log_type=~".+"}|json
|kubernetes_labels_app_kubernetes_io_part_of="hyperconverged-cluster"
|= "error" != "timeout"
----