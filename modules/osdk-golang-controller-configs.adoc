// Module included in the following assemblies:
//
// * operators/operator_sdk/golang/osdk-golang-tutorial.adoc

[id="osdk-golang-controller-configs_{context}"]
= Controller configurations

You can initialize a controller by using many other useful configurations. For example:

* Set the maximum number of concurrent reconciles for the controller by using the `MaxConcurrentReconciles` option, which defaults to `1`:
+
[source,go]
----
func (r *MemcachedReconciler) SetupWithManager(mgr ctrl.Manager) error {
    return ctrl.NewControllerManagedBy(mgr).
        For(&cachev1.Memcached{}).
        Owns(&appsv1.Deployment{}).
        WithOptions(controller.Options{
            MaxConcurrentReconciles: 2,
        }).
        Complete(r)
}
----

* Filter watch events using predicates.

* Choose the type of link:https://pkg.go.dev/sigs.k8s.io/controller-runtime/pkg/handler#EventHandler[EventHandler] to change how a watch event translates to reconcile requests for the reconcile loop. For Operator relationships that are more complex than primary and secondary resources, you can use the `EnqueueRequestsFromMapFunc` handler to transform a watch event into an arbitrary set of reconcile requests.

For more details on these and other configurations, see the upstream link:https://godoc.org/github.com/kubernetes-sigs/controller-runtime/pkg/builder#example-Builder[Builder] and link:https://godoc.org/github.com/kubernetes-sigs/controller-runtime/pkg/controller[Controller] GoDocs.
