// Module included in the following assemblies:
//
// * serverless/reference/kn-serving-ref.adoc

:_mod-docs-content-type: CONCEPT
[id="kn-service-offline-about_{context}"]
= About the Knative CLI offline mode

When you execute `kn service` commands, the changes immediately propagate to the cluster. However, as an alternative, you can execute `kn service` commands in offline mode. When you create a service in offline mode, no changes happen on the cluster, and instead the service descriptor file is created on your local machine.

:FeatureName: The offline mode of the Knative CLI
include::snippets/technology-preview.adoc[leveloffset=+1]

After the descriptor file is created, you can manually modify it and track it in a version control system. You can also propagate changes to the cluster by using the `kn service create -f`, `kn service apply -f`, or `oc apply -f` commands on the descriptor files.
// Once `update` works, add it here and make it into a list

The offline mode has several uses:

* You can manually modify the descriptor file before using it to make changes on the cluster.
* You can locally track the descriptor file of a service in a version control system. This enables you to reuse the descriptor file in places other than the target cluster, for example in continuous integration (CI) pipelines, development environments, or demos.
* You can examine the created descriptor files to learn about Knative services. In particular, you can see how the resulting service is influenced by the different arguments passed to the `kn` command.

The offline mode has its advantages: it is fast, and does not require a connection to the cluster. However, offline mode lacks server-side validation. Consequently, you cannot, for example, verify that the service name is unique or that the specified image can be pulled.
