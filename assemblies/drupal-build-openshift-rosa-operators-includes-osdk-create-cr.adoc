// Module included in the following assemblies:
//
// * operators/operator_sdk/golang/osdk-golang-tutorial.adoc
// * operators/operator_sdk/ansible/osdk-ansible-tutorial.adoc
// * operators/operator_sdk/helm/osdk-helm-tutorial.adoc

ifeval::["{context}" == "osdk-golang-tutorial"]
:golang:
:app-proper: Memcached
:app: memcached
:group: cache
endif::[]
ifeval::["{context}" == "osdk-ansible-tutorial"]
:ansible:
:app-proper: Memcached
:app: memcached
:group: cache
endif::[]
ifeval::["{context}" == "osdk-helm-tutorial"]
:helm:
:app-proper: Nginx
:app: nginx
:group: demo
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="osdk-create-cr_{context}"]
= Creating a custom resource

After your Operator is installed, you can test it by creating a custom resource (CR) that is now provided on the cluster by the Operator.

.Prerequisites

* Example {app-proper} Operator, which provides the `{app-proper}` CR, installed on a cluster

.Procedure

. Change to the namespace where your Operator is installed. For example, if you deployed the Operator using the `make deploy` command:
+
[source,terminal,subs="attributes+"]
----
$ oc project {app}-operator-system
----

. Edit the sample `{app-proper}` CR manifest at `config/samples/{group}_v1_{app}.yaml` to contain the following specification:
+
[source,yaml,subs="attributes+"]
----
apiVersion: {group}.example.com/v1
kind: {app-proper}
metadata:
  name: {app}-sample
...
spec:
...
ifdef::helm[]
  replicaCount: 3
endif::[]
ifndef::helm[]
  size: 3
endif::[]
----

ifdef::helm[]
. The {app-proper} service account requires privileged access to run in {product-title}. Add the following security context constraint (SCC) to the service account for the `{app}-sample` pod:
+
[source,terminal,subs="attributes+"]
----
$ oc adm policy add-scc-to-user \
    anyuid system:serviceaccount:{app}-operator-system:{app}-sample
----
endif::[]

. Create the CR:
+
[source,terminal,subs="attributes+"]
----
$ oc apply -f config/samples/{group}_v1_{app}.yaml
----

. Ensure that the `{app-proper}` Operator creates the deployment for the sample CR with the correct size:
+
[source,terminal]
----
$ oc get deployments
----
+
.Example output
[source,terminal]
ifdef::helm[]
----
NAME                                    READY   UP-TO-DATE   AVAILABLE   AGE
nginx-operator-controller-manager       1/1     1            1           8m
nginx-sample                            3/3     3            3           1m
----
endif::[]
ifndef::helm[]
----
NAME                                    READY   UP-TO-DATE   AVAILABLE   AGE
memcached-operator-controller-manager   1/1     1            1           8m
memcached-sample                        3/3     3            3           1m
----
endif::[]

. Check the pods and CR status to confirm the status is updated with the {app-proper} pod names.

.. Check the pods:
+
[source,terminal]
----
$ oc get pods
----
+
.Example output
[source,terminal]
ifdef::helm[]
----
NAME                                  READY     STATUS    RESTARTS   AGE
nginx-sample-6fd7c98d8-7dqdr          1/1       Running   0          1m
nginx-sample-6fd7c98d8-g5k7v          1/1       Running   0          1m
nginx-sample-6fd7c98d8-m7vn7          1/1       Running   0          1m
----
endif::[]
ifndef::helm[]
----
NAME                                  READY     STATUS    RESTARTS   AGE
memcached-sample-6fd7c98d8-7dqdr      1/1       Running   0          1m
memcached-sample-6fd7c98d8-g5k7v      1/1       Running   0          1m
memcached-sample-6fd7c98d8-m7vn7      1/1       Running   0          1m
----
endif::[]

.. Check the CR status:
+
[source,terminal,subs="attributes+"]
----
$ oc get {app}/{app}-sample -o yaml
----
+
.Example output
[source,yaml,subs="attributes+"]
----
apiVersion: {group}.example.com/v1
kind: {app-proper}
metadata:
...
  name: {app}-sample
...
spec:
ifdef::helm[]
  replicaCount: 3
endif::[]
ifndef::helm[]
  size: 3
endif::[]
status:
  nodes:
  - {app}-sample-6fd7c98d8-7dqdr
  - {app}-sample-6fd7c98d8-g5k7v
  - {app}-sample-6fd7c98d8-m7vn7
----

. Update the deployment size.

.. Update `config/samples/{group}_v1_{app}.yaml` file to change the `spec.size` field in the `{app-proper}` CR from `3` to `5`:
+
[source,terminal,subs="attributes+"]
----
$ oc patch {app} {app}-sample \
ifdef::helm[]
    -p '{"spec":{"replicaCount": 5}}' \
endif::[]
ifndef::helm[]
    -p '{"spec":{"size": 5}}' \
endif::[]
    --type=merge
----

.. Confirm that the Operator changes the deployment size:
+
[source,terminal]
----
$ oc get deployments
----
+
.Example output
[source,terminal]
ifdef::helm[]
----
NAME                                    READY   UP-TO-DATE   AVAILABLE   AGE
nginx-operator-controller-manager       1/1     1            1           10m
nginx-sample                            5/5     5            5           3m
----
endif::[]
ifndef::helm[]
----
NAME                                    READY   UP-TO-DATE   AVAILABLE   AGE
memcached-operator-controller-manager   1/1     1            1           10m
memcached-sample                        5/5     5            5           3m
----
endif::[]

. Delete the CR by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc delete -f config/samples/{group}_v1_{app}.yaml
----

. Clean up the resources that have been created as part of this tutorial.

* If you used the `make deploy` command to test the Operator, run the following command:
+
[source,terminal]
----
$ make undeploy
----

* If you used the `operator-sdk run bundle` command to test the Operator, run the following command:
+
[source,terminal]
----
$ operator-sdk cleanup <project_name>
----


ifeval::["{context}" == "osdk-golang-tutorial"]
:!golang:
:!app-proper:
:!app:
:!group:
endif::[]
ifeval::["{context}" == "osdk-ansible-tutorial"]
:!ansible:
:!app-proper:
:!app:
:!group:
endif::[]
ifeval::["{context}" == "osdk-helm-tutorial"]
:!helm:
:!app-proper:
:!app:
:!group:
endif::[]
