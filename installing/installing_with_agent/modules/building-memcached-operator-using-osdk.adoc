// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-getting-started.adoc

[id="building-memcached-operator-using-osdk_{context}"]
= Building a Go-based Operator using the Operator SDK

This procedure walks through an example of building a simple Memcached Operator using tools and libraries provided by the SDK.

.Prerequisites

- Operator SDK CLI installed on the development workstation
- Operator Lifecycle Manager (OLM) installed on a Kubernetes-based cluster (v1.8
or above to support the `apps/v1beta2` API group), for example {product-title} {product-version}
- Access to the cluster using an account with `cluster-admin` permissions
- OpenShift CLI (`oc`) v{product-version}+ installed

.Procedure

. *Create a new project.*
+
Use the CLI to create a new `memcached-operator` project:
+
[source,terminal]
----
$ mkdir -p $GOPATH/src/github.com/example-inc/
----
+
[source,terminal]
----
$ cd $GOPATH/src/github.com/example-inc/
----
+
[source,terminal]
----
$ operator-sdk new memcached-operator
----
+
[source,terminal]
----
$ cd memcached-operator
----

. *Add a new custom resource definition (CRD).*

.. Use the CLI to add a new CRD API called `Memcached`, with `APIVersion` set to `cache.example.com/v1apha1` and `Kind` set to `Memcached`:
+
[source,terminal]
----
$ operator-sdk add api \
    --api-version=cache.example.com/v1alpha1 \
    --kind=Memcached
----
+
This scaffolds the Memcached resource API under `pkg/apis/cache/v1alpha1/`.

.. Modify the spec and status of the `Memcached` custom resource (CR) at the `pkg/apis/cache/v1alpha1/memcached_types.go` file:
+
[source,go]
----
type MemcachedSpec struct {
	// Size is the size of the memcached deployment
	Size int32 `json:"size"`
}
type MemcachedStatus struct {
	// Nodes are the names of the memcached pods
	Nodes []string `json:"nodes"`
}
----

.. After modifying the `*_types.go` file, always run the following command to update the generated code for that resource type:
+
[source,terminal]
----
$ operator-sdk generate k8s
----

. *Optional: Add custom validation to your CRD.*
+
OpenAPI v3.0 schemas are added to CRD manifests in the `spec.validation` block when the manifests are generated. This validation block allows Kubernetes to validate the properties in a Memcached CR when it is created or updated.
+
Additionally, a `pkg/apis/<group>/<version>/zz_generated.openapi.go` file is generated. This file contains the Go representation of this validation block if the `+k8s:openapi-gen=true annotation` is present above the `Kind` type declaration, which is present by default. This auto-generated code is the OpenAPI model of your Go `Kind` type, from which you can create a full OpenAPI Specification and generate a client.
+
As an Operator author, you can use Kubebuilder markers (annotations) to configure custom validations for your API. These markers must always have a `+kubebuilder:validation` prefix. For example, adding an enum-type specification can be done by adding the following marker:
+
[source,go]
----
// +kubebuilder:validation:Enum=Lion;Wolf;Dragon
type Alias string
----
+
Usage of markers in API code is discussed in the Kubebuilder link:https://book.kubebuilder.io/reference/generating-crd.html[Generating CRDs] and link:https://book.kubebuilder.io/reference/markers.html[Markers for Config/Code Generation] documentation. A full list of OpenAPIv3 validation markers is also available in the Kubebuilder link:https://book.kubebuilder.io/reference/markers/crd-validation.html[CRD Validation] documentation.
+
If you add any custom validations, run the following command to update the OpenAPI validation section in the `deploy/crds/cache.example.com_memcacheds_crd.yaml` file for the CRD:
+
[source,terminal]
----
$ operator-sdk generate crds
----
+
.Example generated YAML
[source,yaml]
----
spec:
  validation:
    openAPIV3Schema:
      properties:
        spec:
          properties:
            size:
              format: int32
              type: integer
----

. *Add a new controller.*

.. Add a new controller to the project to watch and reconcile the `Memcached` resource:
+
[source,terminal]
----
$ operator-sdk add controller \
    --api-version=cache.example.com/v1alpha1 \
    --kind=Memcached
----
+
This scaffolds a new controller implementation under `pkg/controller/memcached/`.

.. For this example, replace the generated controller file `pkg/controller/memcached/memcached_controller.go` with the link:https://github.com/operator-framework/operator-sdk/blob/master/example/memcached-operator/memcached_controller.go.tmpl[example implementation].
+
The example controller executes the following reconciliation logic for each `Memcached` resource:
+
--
* Create a Memcached deployment if it does not exist.
* Ensure that the Deployment size is the same as specified by the `Memcached` CR spec.
* Update the `Memcached` resource status with the names of the Memcached pods.
--
+
The next two sub-steps inspect how the controller watches resources and how the reconcile loop is triggered. You can skip these steps to go directly to building and running the Operator.

.. Inspect the controller implementation at the `pkg/controller/memcached/memcached_controller.go` file to see how the controller watches resources.
+
The first watch is for the `Memcached` type as the primary resource. For each add, update, or delete event, the reconcile loop is sent a reconcile `Request` (a `<namespace>:<name>` key) for that `Memcached` object:
+
[source,go]
----
err := c.Watch(
  &source.Kind{Type: &cachev1alpha1.Memcached{}}, &handler.EnqueueRequestForObject{})
----
+
The next watch is for `Deployment` objects, but the event handler maps each event to a reconcile `Request` for the owner of the deployment. In this case, this is the `Memcached` object for which the deployment was created. This allows the controller to watch deployments as a secondary resource:
+
[source,go]
----
err := c.Watch(&source.Kind{Type: &appsv1.Deployment{}}, &handler.EnqueueRequestForOwner{
		IsController: true,
		OwnerType:    &cachev1alpha1.Memcached{},
	})
----

.. Every controller has a `Reconciler` object with a `Reconcile()` method that implements the reconcile loop. The reconcile loop is passed the `Request` argument which is a `<namespace>:<name>` key used to lookup the primary resource object, `Memcached`, from the cache:
+
[source,go]
----
func (r *ReconcileMemcached) Reconcile(request reconcile.Request) (reconcile.Result, error) {
  // Lookup the Memcached instance for this reconcile request
  memcached := &cachev1alpha1.Memcached{}
  err := r.client.Get(context.TODO(), request.NamespacedName, memcached)
  ...
}
----
+
Based on the return value of the `Reconcile()` function, the reconcile `Request` might be requeued, and the loop might be triggered again:
+
[source,go]
----
// Reconcile successful - don't requeue
return reconcile.Result{}, nil
// Reconcile failed due to error - requeue
return reconcile.Result{}, err
// Requeue for any reason other than error
return reconcile.Result{Requeue: true}, nil
----
[id="building-memcached-operator-using-osdk-build-and-run_{context}"]

. *Build and run the Operator.*

.. Before running the Operator, the CRD must be registered with the Kubernetes API server:
+
[source,terminal]
----
$ oc create \
    -f deploy/crds/cache_v1alpha1_memcached_crd.yaml
----

.. After registering the CRD, there are two options for running the Operator:
+
--
* As a Deployment inside a Kubernetes cluster
* As Go program outside a cluster
--
+
Choose one of the following methods.

... _Option A:_ Running as a deployment inside the cluster.

.... Build the `memcached-operator` image and push it to a registry:
+
[source,terminal]
----
$ operator-sdk build quay.io/example/memcached-operator:v0.0.1
----

.... The deployment manifest is generated at `deploy/operator.yaml`. Update the deployment image as follows since the default is just a placeholder:
+
[source,terminal]
----
$ sed -i 's|REPLACE_IMAGE|quay.io/example/memcached-operator:v0.0.1|g' deploy/operator.yaml
----

.... Ensure you have an account on link:https://quay.io[Quay.io] for the next step, or substitute your preferred container registry. On the registry, link:https://quay.io/new/[create a new public image] repository named `memcached-operator`.

.... Push the image to the registry:
+
[source,terminal]
----
$ podman push quay.io/example/memcached-operator:v0.0.1
----

.... Set up RBAC and create the `memcached-operator` manifests:
+
[source,terminal]
----
$ oc create -f deploy/role.yaml
----
+
[source,terminal]
----
$ oc create -f deploy/role_binding.yaml
----
+
[source,terminal]
----
$ oc create -f deploy/service_account.yaml
----
+
[source,terminal]
----
$ oc create -f deploy/operator.yaml
----

.... Verify that the `memcached-operator` deploy is up and running:
+
[source,terminal]
----
$ oc get deployment
----
+
.Example output
[source,terminal]
----
NAME                     DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
memcached-operator       1         1         1            1           1m
----

... _Option B:_ Running locally outside the cluster.
+
This method is preferred during development cycle to deploy and test faster.
+
Run the Operator locally with the default Kubernetes configuration file present at `$HOME/.kube/config`:
+
[source,terminal]
----
$ operator-sdk run --local --namespace=default
----
+
You can use a specific `kubeconfig` using the flag `--kubeconfig=<path/to/kubeconfig>`.

. *Verify that the Operator can deploy a Memcached application* by creating a `Memcached` CR.

.. Create the example `Memcached` CR that was generated at `deploy/crds/cache_v1alpha1_memcached_cr.yaml`.

.. View the file:
+
[source,terminal]
----
$ cat deploy/crds/cache_v1alpha1_memcached_cr.yaml
----
+
.Example output
[source,terminal]
----
apiVersion: "cache.example.com/v1alpha1"
kind: "Memcached"
metadata:
  name: "example-memcached"
spec:
  size: 3
----

.. Create the object:
+
[source,terminal]
----
$ oc apply -f deploy/crds/cache_v1alpha1_memcached_cr.yaml
----

.. Ensure that `memcached-operator` creates the deployment for the CR:
+
[source,terminal]
----
$ oc get deployment
----
+
.Example output
[source,terminal]
----
NAME                     DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
memcached-operator       1         1         1            1           2m
example-memcached        3         3         3            3           1m
----

.. Check the pods and CR to confirm the CR status is updated with the pod names:
+
[source,terminal]
----
$ oc get pods
----
+
.Example output
[source,terminal]
----
NAME                                  READY     STATUS    RESTARTS   AGE
example-memcached-6fd7c98d8-7dqdr     1/1       Running   0          1m
example-memcached-6fd7c98d8-g5k7v     1/1       Running   0          1m
example-memcached-6fd7c98d8-m7vn7     1/1       Running   0          1m
memcached-operator-7cc7cfdf86-vvjqk   1/1       Running   0          2m
----
+
[source,terminal]
----
$ oc get memcached/example-memcached -o yaml
----
+
.Example output
[source,terminal]
----
apiVersion: cache.example.com/v1alpha1
kind: Memcached
metadata:
  clusterName: ""
  creationTimestamp: 2018-03-31T22:51:08Z
  generation: 0
  name: example-memcached
  namespace: default
  resourceVersion: "245453"
  selfLink: /apis/cache.example.com/v1alpha1/namespaces/default/memcacheds/example-memcached
  uid: 0026cc97-3536-11e8-bd83-0800274106a1
spec:
  size: 3
status:
  nodes:
  - example-memcached-6fd7c98d8-7dqdr
  - example-memcached-6fd7c98d8-g5k7v
  - example-memcached-6fd7c98d8-m7vn7
----

. *Verify that the Operator can manage a deployed Memcached application* by updating the size of the deployment.

.. Change the `spec.size` field in the `memcached` CR from `3` to `4`:
+
[source,terminal]
----
$ cat deploy/crds/cache_v1alpha1_memcached_cr.yaml
----
+
.Example output
[source,terminal]
----
apiVersion: "cache.example.com/v1alpha1"
kind: "Memcached"
metadata:
  name: "example-memcached"
spec:
  size: 4
----

.. Apply the change:
+
[source,terminal]
----
$ oc apply -f deploy/crds/cache_v1alpha1_memcached_cr.yaml
----

.. Confirm that the Operator changes the deployment size:
+
[source,terminal]
----
$ oc get deployment
----
+
.Example output
[source,terminal]
----
NAME                 DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
example-memcached    4         4         4            4           5m
----

. *Clean up the resources:*
+
[source,terminal]
----
$ oc delete -f deploy/crds/cache_v1alpha1_memcached_cr.yaml
----
+
[source,terminal]
----
$ oc delete -f deploy/crds/cache_v1alpha1_memcached_crd.yaml
----
+
[source,terminal]
----
$ oc delete -f deploy/operator.yaml
----
+
[source,terminal]
----
$ oc delete -f deploy/role.yaml
----
+
[source,terminal]
----
$ oc delete -f deploy/role_binding.yaml
----
+
[source,terminal]
----
$ oc delete -f deploy/service_account.yaml
----

[role="_additional-resources"]
.Additional resources

* For more information about OpenAPI v3.0 validation schemas in CRDs, refer to the link:https://kubernetes.io/docs/tasks/access-kubernetes-api/custom-resources/custom-resource-definitions/#specifying-a-structural-schema[Kubernetes documentation].
