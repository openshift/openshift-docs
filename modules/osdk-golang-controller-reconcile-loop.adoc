// Module included in the following assemblies:
//
// * operators/operator_sdk/golang/osdk-golang-tutorial.adoc

[id="osdk-golang-controller-reconcile-loop_{context}"]
= Reconcile loop

Every controller has a reconciler object with a `Reconcile()` method that implements the reconcile loop. The reconcile loop is passed the `Request` argument, which is a namespace and name key used to find the primary resource object, `Memcached`, from the cache:

[source,go]
----
import (
	ctrl "sigs.k8s.io/controller-runtime"

	cachev1 "github.com/example-inc/memcached-operator/api/v1"
	...
)

func (r *MemcachedReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
  // Lookup the Memcached instance for this reconcile request
  memcached := &cachev1.Memcached{}
  err := r.Get(ctx, req.NamespacedName, memcached)
  ...
}
----

Based on the return values, result, and error, the request might be requeued and the reconcile loop might be triggered again:

[source,go]
----
// Reconcile successful - don't requeue
return ctrl.Result{}, nil
// Reconcile failed due to error - requeue
return ctrl.Result{}, err
// Requeue for any reason other than an error
return ctrl.Result{Requeue: true}, nil
----

You can set the `Result.RequeueAfter` to requeue the request after a grace period as well:

[source,go]
----
import "time"

// Reconcile for any reason other than an error after 5 seconds
return ctrl.Result{RequeueAfter: time.Second*5}, nil
----

[NOTE]
====
You can return `Result` with `RequeueAfter` set to periodically reconcile a CR.
====

For more on reconcilers, clients, and interacting with resource events, see the link:https://sdk.operatorframework.io/docs/building-operators/golang/references/client/[Controller Runtime Client API] documentation.
