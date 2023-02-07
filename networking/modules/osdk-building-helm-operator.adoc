// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-helm.adoc

[id="osdk-building-helm-operator_{context}"]
= Building a Helm-based Operator using the Operator SDK

This procedure walks through an example of building a simple Nginx Operator powered by a Helm chart using tools and libraries provided by the Operator SDK.

[TIP]
====
It is best practice to build a new Operator for each chart. This can allow for more native-behaving Kubernetes APIs (for example, `oc get Nginx`) and flexibility if you ever want to write a fully-fledged Operator in Go, migrating away from a Helm-based Operator.
====

.Prerequisites

- Operator SDK CLI installed on the development workstation
- Access to a Kubernetes-based cluster v1.11.3+ (for example {product-title} {product-version}) using an account with `cluster-admin` permissions
- OpenShift CLI (`oc`) v{product-version}+ installed

.Procedure

. *Create a new Operator project.* A namespace-scoped Operator watches and manages resources in a single namespace. Namespace-scoped Operators are preferred because of their flexibility. They enable decoupled upgrades, namespace isolation for failures and monitoring, and differing API definitions.
+
To create a new Helm-based, namespace-scoped `nginx-operator` project, use the following command:
+
[source,terminal]
----
$ operator-sdk new nginx-operator \
  --api-version=example.com/v1alpha1 \
  --kind=Nginx \
  --type=helm
----
+
[source,terminal]
----
$ cd nginx-operator
----
+
This creates the `nginx-operator` project specifically for watching the Nginx resource with API version `example.com/v1apha1` and kind `Nginx`.

. *Customize the Operator logic.*
+
For this example, the `nginx-operator` executes the following reconciliation logic for each `Nginx` custom resource (CR):
+
--
* Create an Nginx deployment if it does not exist.
* Create an Nginx service if it does not exist.
* Create an Nginx ingress if it is enabled and does not exist.
* Ensure that the deployment, service, and optional ingress match the desired configuration (for example, replica count, image, service type) as specified by the Nginx CR.
--
+
By default, the `nginx-operator` watches `Nginx` resource events as shown in the `watches.yaml` file and executes Helm releases using the specified chart:
+
[source,yaml]
----
- version: v1alpha1
  group: example.com
  kind: Nginx
  chart: /opt/helm/helm-charts/nginx
----

.. *Review the Nginx Helm chart.*
+
When a Helm Operator project is created, the Operator SDK creates an example Helm chart that contains a set of templates for a simple Nginx release.
+
For this example, templates are available for deployment, service, and ingress resources, along with a `NOTES.txt` template, which Helm chart developers use to convey helpful information about a release.
+
If you are not already familiar with Helm Charts, review the link:https://docs.helm.sh/developing_charts/[Helm Chart developer documentation].

.. *Understand the Nginx CR spec.*
+
Helm uses a concept called link:https://docs.helm.sh/using_helm/#customizing-the-chart-before-installing[values] to provide customizations to the defaults of a Helm chart, which are defined in the `values.yaml` file.
+
Override these defaults by setting the desired values in the CR spec. You can use the number of replicas as an example:

... First, inspect the `helm-charts/nginx/values.yaml` file to find that the chart has a value called `replicaCount` and it is set to `1` by default. To have 2 Nginx instances in your deployment, your CR spec must contain `replicaCount: 2`.
+
Update the `deploy/crds/example.com_v1alpha1_nginx_cr.yaml` file to look like the following:
+
[source,yaml]
----
apiVersion: example.com/v1alpha1
kind: Nginx
metadata:
  name: example-nginx
spec:
  replicaCount: 2
----

... Similarly, the default service port is set to `80`. To instead use `8080`, update the `deploy/crds/example.com_v1alpha1_nginx_cr.yaml` file again by adding the service port override:
+
[source,yaml]
----
apiVersion: example.com/v1alpha1
kind: Nginx
metadata:
  name: example-nginx
spec:
  replicaCount: 2
  service:
    port: 8080
----
+
The Helm Operator applies the entire spec as if it was the contents of a values file, just like the `helm install -f ./overrides.yaml` command works.

. *Deploy the CRD.*
+
Before running the Operator, Kubernetes must know about the new custom resource definition (CRD) that the Operator will be watching. Deploy the following CRD:
+
[source,terminal]
----
$ oc create -f deploy/crds/example_v1alpha1_nginx_crd.yaml
----

. *Build and run the Operator.*
+
There are two ways to build and run the Operator:
+
--
* As a pod inside a Kubernetes cluster.
* As a Go program outside the cluster using the `operator-sdk up` command.
--
+
Choose one of the following methods:

.. *Run as a pod* inside a Kubernetes cluster. This is the preferred
method for production use.

... Build the `nginx-operator` image and push it to a registry:
+
[source,terminal]
----
$ operator-sdk build quay.io/example/nginx-operator:v0.0.1
----
+
[source,terminal]
----
$ podman push quay.io/example/nginx-operator:v0.0.1
----

... Deployment manifests are generated in the `deploy/operator.yaml` file. The deployment image in this file needs to be modified from the placeholder `REPLACE_IMAGE` to the previous built image. To do this, run:
+
[source,terminal]
----
$ sed -i 's|REPLACE_IMAGE|quay.io/example/nginx-operator:v0.0.1|g' deploy/operator.yaml
----

... Deploy the `nginx-operator` manifests:
+
[source,terminal]
----
$ oc create -f deploy/service_account.yaml
----
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
$ oc create -f deploy/operator.yaml
----

... Verify that the `nginx-operator` deployment is up and running:
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
nginx-operator       1         1         1            1           1m
----

.. *Run outside the cluster.* This method is preferred during the development cycle to speed up deployment and testing.
+
It is important that the chart path referenced in the `watches.yaml` file exists on your machine. By default, the `watches.yaml` file is scaffolded to work with an Operator image built with the `operator-sdk build` command. When developing and testing your Operator with the `operator-sdk run --local` command, the SDK looks in your local file system for this path.

... Create a symlink at this location to point to the path of your Helm chart:
+
[source,terminal]
----
$ sudo mkdir -p /opt/helm/helm-charts
----
+
[source,terminal]
----
$ sudo ln -s $PWD/helm-charts/nginx /opt/helm/helm-charts/nginx
----

... To run the Operator locally with the default Kubernetes configuration file present at `$HOME/.kube/config`:
+
[source,terminal]
----
$ operator-sdk run --local
----
+
To run the Operator locally with a provided Kubernetes configuration file:
+
[source,terminal]
----
$ operator-sdk run --local --kubeconfig=<path_to_config>
----

. *Deploy the `Nginx` CR.*
+
Apply the `Nginx` CR that you modified earlier:
+
[source,terminal]
----
$ oc apply -f deploy/crds/example.com_v1alpha1_nginx_cr.yaml
----
+
Ensure that the `nginx-operator` creates the deployment for the CR:
+
[source,terminal]
----
$ oc get deployment
----
+
.Example output
[source,terminal]
----
NAME                                           DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
example-nginx-b9phnoz9spckcrua7ihrbkrt1        2         2         2            2           1m
----
+
Check the pods to confirm two replicas were created:
+
[source,terminal]
----
$ oc get pods
----
+
.Example output
[source,terminal]
----
NAME                                                      READY     STATUS    RESTARTS   AGE
example-nginx-b9phnoz9spckcrua7ihrbkrt1-f8f9c875d-fjcr9   1/1       Running   0          1m
example-nginx-b9phnoz9spckcrua7ihrbkrt1-f8f9c875d-ljbzl   1/1       Running   0          1m
----
+
Check that the service port is set to `8080`:
+
[source,terminal]
----
$ oc get service
----
+
.Example output
[source,terminal]
----
NAME                                      TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)    AGE
example-nginx-b9phnoz9spckcrua7ihrbkrt1   ClusterIP   10.96.26.3   <none>        8080/TCP   1m
----

. *Update the `replicaCount` and remove the port.*
+
Change the `spec.replicaCount` field from `2` to `3`, remove the `spec.service` field, and apply the change:
+
[source,terminal]
----
$ cat deploy/crds/example.com_v1alpha1_nginx_cr.yaml
----
+
.Example output
[source,yaml]
----
apiVersion: "example.com/v1alpha1"
kind: "Nginx"
metadata:
  name: "example-nginx"
spec:
  replicaCount: 3
----
+
[source,terminal]
----
$ oc apply -f deploy/crds/example.com_v1alpha1_nginx_cr.yaml
----
+
Confirm that the Operator changes the deployment size:
+
[source,terminal]
----
$ oc get deployment
----
+
.Example output
[source,terminal]
----
NAME                                           DESIRED   CURRENT   UP-TO-DATE   AVAILABLE   AGE
example-nginx-b9phnoz9spckcrua7ihrbkrt1        3         3         3            3           1m
----
+
Check that the service port is set to the default `80`:
+
[source,terminal]
----
$ oc get service
----
+
.Example output
[source,terminal]
----
NAME                                      TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)  AGE
example-nginx-b9phnoz9spckcrua7ihrbkrt1   ClusterIP   10.96.26.3   <none>        80/TCP   1m
----

. *Clean up the resources:*
+
[source,terminal]
----
$ oc delete -f deploy/crds/example.com_v1alpha1_nginx_cr.yaml
----
+
[source,terminal]
----
$ oc delete -f deploy/operator.yaml
----
+
[source,terminal]
----
$ oc delete -f deploy/role_binding.yaml
----
+
[source,terminal]
----
$ oc delete -f deploy/role.yaml
----
+
[source,terminal]
----
$ oc delete -f deploy/service_account.yaml
----
+
[source,terminal]
----
$ oc delete -f deploy/crds/example_v1alpha1_nginx_crd.yaml
----
