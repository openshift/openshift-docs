// Module included in the following assemblies:
//
// * rosa_cluster_admin/rosa_nodes/rosa-managing-worker-nodes.adoc

:_mod-docs-content-type: CONCEPT
[id="rosa-imds-machine-pools_{context}"]
= Instance Metadata Service on machine pools

There are two types of ways to access instance metadata from a running instance:

* Instance Metadata Service Version 1 (IMDSv1) - a request/response method
* Instance Metadata Service Version 2 (IMDSv2) - a session-oriented method

IMDSv2 uses session-oriented requests. With session-oriented requests, you create a session token that defines the session duration, which can be a minimum of one second and a maximum of six hours. During the specified duration, you can use the same session token for subsequent requests. After the specified duration expires, you must create a new session token to use for future requests.

When creating your ROSA cluster, you select to use either both IMDSv1 and IMDSv2 or specify that your cluster should only use IMDSv2. The instance metadata service distinguishes between IMDSv1 and IMDSv2 requests based on whether, for any given request, either the PUT or GET headers, which are unique to IMDSv2, are present in that request. If you specify to use IMDSv2 only, IMDSv1 ceases to function for your cluster. All machine pools on your cluster will use whichever IMDS type you select.