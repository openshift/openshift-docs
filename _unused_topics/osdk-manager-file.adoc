// Module included in the following assemblies:
//
// * operators/operator_sdk/golang/osdk-golang-tutorial.adoc

[id="osdk-manager-file_{context}"]
= Manager file

The main program for the Operator is the manager file at `cmd/manager/main.go`. The manager automatically registers the scheme for all custom resources (CRs) defined under `pkg/apis/` and runs all controllers under `pkg/controller/`.

The manager can restrict the namespace that all controllers watch for resources:

[source,go]
----
mgr, err := manager.New(cfg, manager.Options{Namespace: namespace})
----

By default, the controller watches the namespace that the Operator runs in. To watch all namespaces, you can leave the namespace option empty:

[source,go]
----
mgr, err := manager.New(cfg, manager.Options{Namespace: ""})
----

////
TODO: Doc on manager options(Sync period, leader election, registering 3rd party types)
////
