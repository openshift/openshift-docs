// Module is included in the following assemblies:
// logging/cluster-logging-loki.adoc
//
:_mod-docs-content-type: PROCEDURE
[id="logging-loki-storage-azure_{context}"]
= Azure storage

.Prerequisites
* You have deployed Loki Operator.
* You have created a link:https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction[bucket] on Azure.

.Procedure
* Create an object storage secret with the name `logging-loki-azure` by running the following command:

[source,terminal,subs="+quotes"]
----
$ oc create secret generic logging-loki-azure \
  --from-literal=container="<azure_container_name>" \
  --from-literal=environment="<azure_environment>" \ # <1>
  --from-literal=account_name="<azure_account_name>" \
  --from-literal=account_key="<azure_account_key>"
----
<1> Supported environment values are: `AzureGlobal`, `AzureChinaCloud`, `AzureGermanCloud`, `AzureUSGovernment`.
