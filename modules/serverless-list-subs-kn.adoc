// Module included in the following assemblies:
//
// * /serverless/develop/serverless-subs.adoc

:_mod-docs-content-type: PROCEDURE
[id="serverless-list-subs-kn_{context}"]
= Listing subscriptions by using the Knative CLI

You can use the `kn subscription list` command to list existing subscriptions on your cluster by using the Knative (`kn`) CLI. Using the Knative CLI to list subscriptions provides a streamlined and intuitive user interface.

.Prerequisites

* You have installed the Knative (`kn`) CLI.

.Procedure

* List subscriptions on your cluster:
+
[source,terminal]
----
$ kn subscription list
----
+
.Example output
[source,terminal]
----
NAME             CHANNEL             SUBSCRIBER           REPLY   DEAD LETTER SINK   READY   REASON
mysubscription   Channel:mychannel   ksvc:event-display                              True
----
// . Optional: List subscriptions in YAML format:
// +
// [source,terminal]
// ----
// $ kn subscription list -o yaml
// ----
// Add this step once I have an example output, optional so non urgent
