// Module included in the following assemblies:
//
// * networking/verifying-connectivity-endpoint.adoc

[id="nw-pod-network-connectivity-implementation_{context}"]
= Implementation of connection health checks

The connectivity check controller orchestrates connection verification checks in your cluster. The results for the connection tests are stored in `PodNetworkConnectivity` objects in the `openshift-network-diagnostics` namespace. Connection tests are performed every minute in parallel.

The Cluster Network Operator (CNO) deploys several resources to the cluster to send and receive connectivity health checks:

Health check source:: This program deploys in a single pod replica set managed by a `Deployment` object. The program consumes `PodNetworkConnectivity` objects and connects to the `spec.targetEndpoint` specified in each object.

Health check target:: A pod deployed as part of a daemon set on every node in the cluster. The pod listens for inbound health checks. The presence of this pod on every node allows for the testing of connectivity to each node.
