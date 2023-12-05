// Module included in the following assemblies:
//
// * applications/deployments/what-deployments-are.adoc

[id="deployments-kube-deployments_{context}"]
= Deployments

Kubernetes provides a first-class, native API object type in {product-title} called `Deployment`. `Deployment` objects describe the desired state of a particular component of an application as a pod template. Deployments create replica sets, which orchestrate pod lifecycles.

For example, the following deployment definition creates a replica set to bring up one `hello-openshift` pod:

.Deployment definition
[source,yaml]
----
apiVersion: apps/v1
kind: Deployment
metadata:
  name: hello-openshift
spec:
  replicas: 1
  selector:
    matchLabels:
      app: hello-openshift
  template:
    metadata:
      labels:
        app: hello-openshift
    spec:
      containers:
      - name: hello-openshift
        image: openshift/hello-openshift:latest
        ports:
        - containerPort: 80
----
