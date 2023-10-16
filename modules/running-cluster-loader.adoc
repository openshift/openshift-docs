// Module included in the following assemblies:
//
// scalability_and_performance/using-cluster-loader.adoc

[id="running_cluster_loader_{context}"]
= Running Cluster Loader

.Prerequisites

* The repository will prompt you to authenticate. The registry credentials allow
you to access the image, which is not publicly available. Use your existing
authentication credentials from installation.

.Procedure

. Execute Cluster Loader using the built-in test configuration, which deploys five
template builds and waits for them to complete:
+
[source,terminal]
----
$ podman run -v ${LOCAL_KUBECONFIG}:/root/.kube/config:z -i \
quay.io/openshift/origin-tests:4.9 /bin/bash -c 'export KUBECONFIG=/root/.kube/config && \
openshift-tests run-test "[sig-scalability][Feature:Performance] Load cluster \
should populate the cluster [Slow][Serial] [Suite:openshift]"'
----
+
Alternatively, execute Cluster Loader with a user-defined configuration by
setting the environment variable for `VIPERCONFIG`:
+
[source,terminal]
----
$ podman run -v ${LOCAL_KUBECONFIG}:/root/.kube/config:z \
-v ${LOCAL_CONFIG_FILE_PATH}:/root/configs/:z \
-i quay.io/openshift/origin-tests:4.9 \
/bin/bash -c 'KUBECONFIG=/root/.kube/config VIPERCONFIG=/root/configs/test.yaml \
openshift-tests run-test "[sig-scalability][Feature:Performance] Load cluster \
should populate the cluster [Slow][Serial] [Suite:openshift]"'
----
+
In this example, `${LOCAL_KUBECONFIG}` refers to the path to the `kubeconfig` on
your local file system. Also, there is a directory called
`${LOCAL_CONFIG_FILE_PATH}`, which is mounted into the container that contains a
configuration file called `test.yaml`. Additionally, if the `test.yaml`
references any external template files or podspec files, they should also be
mounted into the container.
