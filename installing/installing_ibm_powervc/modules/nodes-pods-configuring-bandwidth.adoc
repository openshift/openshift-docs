// Module included in the following assemblies:
//
// * nodes/nodes-pods-configuring.adoc
// * nodes/nodes-cluster-pods-configuring

:_mod-docs-content-type: PROCEDURE
[id="nodes-pods-configuring-bandwidth_{context}"]
= Limiting the bandwidth available to pods

You can apply quality-of-service traffic shaping to a pod and effectively limit
its available bandwidth. Egress traffic (from the pod) is handled by policing,
which simply drops packets in excess of the configured rate. Ingress traffic (to
the pod) is handled by shaping queued packets to effectively handle data. The
limits you place on a pod do not affect the bandwidth of other pods.

.Procedure

To limit the bandwidth on a pod:

. Write an object definition JSON file, and specify the data traffic speed using
`kubernetes.io/ingress-bandwidth` and `kubernetes.io/egress-bandwidth`
annotations. For example, to limit both pod egress and ingress bandwidth to 10M/s:
+
.Limited `Pod` object definition
[source,json]
----
{
    "kind": "Pod",
    "spec": {
        "containers": [
            {
                "image": "openshift/hello-openshift",
                "name": "hello-openshift"
            }
        ]
    },
    "apiVersion": "v1",
    "metadata": {
        "name": "iperf-slow",
        "annotations": {
            "kubernetes.io/ingress-bandwidth": "10M",
            "kubernetes.io/egress-bandwidth": "10M"
        }
    }
}
----

. Create the pod using the object definition:
+
[source,terminal]
----
$ oc create -f <file_or_dir_path>
----
