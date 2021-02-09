// Module included in the following assemblies:
//
// * operators/operator_sdk/golang/osdk-golang-tutorial.adoc

[id="osdk-golang-controller-resources_{context}"]
= Resources watched by the controller

The `SetupWithManager()` function in `controllers/memcached_controller.go` specifies how the controller is built to watch a CR and other resources that are owned and managed by that controller.

[source,go]
----
import (
	...
	appsv1 "k8s.io/api/apps/v1"
	...
)

func (r *MemcachedReconciler) SetupWithManager(mgr ctrl.Manager) error {
	return ctrl.NewControllerManagedBy(mgr).
		For(&cachev1.Memcached{}).
		Owns(&appsv1.Deployment{}).
		Complete(r)
}
----

`NewControllerManagedBy()` provides a controller builder that allows various controller configurations.

`For(&cachev1.Memcached{})` specifies the `Memcached` type as the primary resource to watch. For each Add, Update, or Delete event for a `Memcached` type, the reconcile loop is sent a reconcile `Request` argument, which consists of a namespace and name key, for that `Memcached` object.

`Owns(&appsv1.Deployment{})` specifies the `Deployment` type as the secondary resource to watch. For each `Deployment` type Add, Update, or Delete event, the event handler maps each event to a reconcile request for the owner of the deployment. In this case, the owner is the `Memcached` object for which the deployment was created.
