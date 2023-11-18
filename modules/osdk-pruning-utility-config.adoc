// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-pruning-utility.adoc

:_mod-docs-content-type: REFERENCE
[id="osdk-pruning-utility-config_{context}"]
= Pruning utility configuration

The `operator-lib` pruning utility is written in Go and includes common pruning strategies for Go-based Operators.

.Example configuration
[source,go]
----
cfg = Config{
        log:           logf.Log.WithName("prune"),
        DryRun:        false,
        Clientset:     client,
        LabelSelector: "app=<operator_name>",
        Resources: []schema.GroupVersionKind{
                {Group: "", Version: "", Kind: PodKind},
        },
        Namespaces: []string{"<operator_namespace>"},
        Strategy: StrategyConfig{
                Mode:            MaxCountStrategy,
                MaxCountSetting: 1,
        },
        PreDeleteHook: myhook,
}
----

The pruning utility configuration file defines pruning actions by using the following fields:

[cols="3,7",options="header"]
|===
|Configuration field |Description

|`log`
|Logger used to handle library log messages.

|`DryRun`
|Boolean that determines whether resources should be removed. If set to `true`, the utility runs but does not to remove resources.

|`Clientset`
|Client-go Kubernetes ClientSet used for Kubernetes API calls.

|`LabelSelector`
|Kubernetes label selector expression used to find resources to prune.

|`Resources`
|Kubernetes resource kinds. `PodKind` and `JobKind` are currently supported.

|`Namespaces`
|List of Kubernetes namespaces to search for resources.

|`Strategy`
|Pruning strategy to run.

|`Strategy.Mode`
|`MaxCountStrategy`, `MaxAgeStrategy`, or `CustomStrategy` are currently supported.

|`Strategy.MaxCountSetting`
|Integer value for `MaxCountStrategy` that specifies how many resources should remain after the pruning utility runs.

|`Strategy.MaxAgeSetting`
|Go `time.Duration` string value, such as `48h`, that specifies the age of resources to prune.

|`Strategy.CustomSettings`
|Go map of values that can be passed into a custom strategy function.

|`PreDeleteHook`
|Optional: Go function to call before pruning a resource.

|`CustomStrategy`
|Optional: Go function that implements a custom pruning strategy.
|===

.Pruning execution

You can call the pruning action by running the execute function on the pruning configuration.

[source,go]
----
err := cfg.Execute(ctx)
----

You can also call a pruning action by using a cron package or by calling the pruning utility with a triggering event.
