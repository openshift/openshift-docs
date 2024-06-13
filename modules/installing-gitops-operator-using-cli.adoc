// Module is included in the following assemblies:
//
// * /cicd/gitops/installing-openshift-gitops.adoc

:_mod-docs-content-type: PROCEDURE
[id="installing-gitops-operator-using-cli_{context}"]
= Installing {gitops-title} Operator using CLI

[role="_abstract"]
You can install {gitops-title} Operator from the OperatorHub using the CLI.

.Procedure

. Create a Subscription object YAML file to subscribe a namespace to the {gitops-title}, for example, `sub.yaml`:
+
.Example Subscription
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-gitops-operator
  namespace: openshift-operators
spec:
  channel: latest <1>
  installPlanApproval: Automatic
  name: openshift-gitops-operator <2>
  source: redhat-operators <3>
  sourceNamespace: openshift-marketplace <4>
----
<1> Specify the channel name from where you want to subscribe the Operator.
<2> Specify the name of the Operator to subscribe to.
<3> Specify the name of the CatalogSource that provides the Operator.
<4> The namespace of the CatalogSource. Use `openshift-marketplace` for the default OperatorHub CatalogSources.
+
. Apply the `Subscription` to the cluster:
+
[source,terminal]
----
$ oc apply -f openshift-gitops-sub.yaml
----
. After the installation is complete, ensure that all the pods in the `openshift-gitops` namespace are running:
+
[source,terminal]
----
$ oc get pods -n openshift-gitops
----
.Example output
+
[source,terminal]
----
NAME                                                      	READY   STATUS	RESTARTS   AGE
cluster-b5798d6f9-zr576                                   	1/1 	Running   0      	65m
kam-69866d7c48-8nsjv                                      	1/1 	Running   0      	65m
openshift-gitops-application-controller-0                 	1/1 	Running   0      	53m
openshift-gitops-applicationset-controller-6447b8dfdd-5ckgh 1/1 	Running   0      	65m
openshift-gitops-redis-74bd8d7d96-49bjf                   	1/1 	Running   0      	65m
openshift-gitops-repo-server-c999f75d5-l4rsg              	1/1 	Running   0      	65m
openshift-gitops-server-5785f7668b-wj57t                  	1/1 	Running   0      	53m
----