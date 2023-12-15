// Module is included in the following assemblies:
// logging/cluster-logging-loki.adoc
:_mod-docs-content-type: PROCEDURE
[id="logging-clo-cli-install_{context}"]
= Installing {clo} using the {product-title} CLI

To install and configure logging on your {product-title} cluster, additional Operators must be installed. This can be done from the {product-title} CLI.

{Product-title} Operators use custom resources (CR) to manage applications and their components. High-level configuration and settings are provided by the user within a CR. The Operator translates high-level directives into low-level actions, based on best practices embedded within the Operator’s logic. A custom resource definition (CRD) defines a CR and lists all the configurations available to users of the Operator. Installing an Operator creates the CRDs, which are then used to generate CRs.

.Prerequisites

* Supported object store (AWS S3, Google Cloud Storage, Azure, Swift, Minio, OpenShift Data Foundation)

.Procedure

. Install the {clo} by creating the following objects:

.. Create an `Operator Group` object YAML file (for example, `olo-og.yaml`) using the template below:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: cluster-logging
  namespace: openshift-logging # <1>
spec:
  targetNamespaces:
  - openshift-logging
----
<1> You must specify the `openshift-logging` namespace.

.. Create a `Subscription` object YAML file (for example, `olo-sub.yaml`) to subscribe a namespace to the {clo} using the template below:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----
+
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: cluster-logging
  namespace: openshift-logging # <1>
spec:
  channel: stable # <2>
  name: cluster-logging
  source: redhat-operators # <3>
  sourceNamespace: openshift-marketplace
----
<1> You must specify the `openshift-logging` namespace.
<2> Specify `stable`, or `stable-5.<y>` as the channel.
<3> Specify `redhat-operators`. If your {product-title} cluster is installed on a restricted network, also known as a disconnected cluster, specify the name of the `CatalogSource` object you created when you configured the Operator Lifecycle Manager (OLM).


.. Verify the Operator installation.
+
There should be a {clo} in the `openshift-logging` namespace. The version number might be different than what is shown.
+
[source,terminal]
----
$ oc get csv -n openshift-logging
----
+
.Example output
[source,terminal]
----
NAME                            DISPLAY                            VERSION   REPLACES                        PHASE
cluster-logging.v5.7.4          Red Hat OpenShift Logging          5.7.4     cluster-logging.v5.7.3          Succeeded
----

. Create a {clo} instance:

.. Create an `instance` object YAML file (for example, `olo-instance.yaml`) using the template below:
+
[source,terminal]
----
$ oc create -f <file-name>.yaml
----
+
[source,yaml]
----
apiVersion: logging.openshift.io/v1
kind: ClusterLogging
metadata:
  name: instance
  namespace: openshift-logging
spec:
  logStore:
    type: lokistack
    lokistack:
      name: logging-loki
  collection:
    type: vector
----

.Verification

Verify the installation by listing the pods in the *openshift-logging* project by running the following command:

[source,terminal]
----
$ oc get pods -n openshift-logging
----

You should see several pods for components of the Logging subsystem, similar to the following list:

.Example output
[source,terminal]
----
$ oc get pods -n openshift-logging
NAME                                               READY   STATUS    RESTARTS   AGE
cluster-logging-operator-fb7f7cf69-8jsbq           1/1     Running   0          98m
collector-222js                                    2/2     Running   0          18m
collector-g9ddv                                    2/2     Running   0          18m
collector-hfqq8                                    2/2     Running   0          18m
collector-sphwg                                    2/2     Running   0          18m
collector-vv7zn                                    2/2     Running   0          18m
collector-wk5zz                                    2/2     Running   0          18m
logging-view-plugin-6f76fbb78f-n2n4n               1/1     Running   0          18m
lokistack-sample-compactor-0                       1/1     Running   0          42m
lokistack-sample-distributor-7d7688bcb9-dvcj8      1/1     Running   0          42m
lokistack-sample-gateway-5f6c75f879-bl7k9          2/2     Running   0          42m
lokistack-sample-gateway-5f6c75f879-xhq98          2/2     Running   0          42m
lokistack-sample-index-gateway-0                   1/1     Running   0          42m
lokistack-sample-ingester-0                        1/1     Running   0          42m
lokistack-sample-querier-6b7b56bccc-2v9q4          1/1     Running   0          42m
lokistack-sample-query-frontend-84fb57c578-gq2f7   1/1     Running   0          42m
----
