// Module included in the following assemblies:
//
// * updating/updating_a_cluster/updating-cluster-web-console.adoc

[id="update-using-custom-machine-config-pools-canary_{context}"]
= Performing a canary rollout update

In some specific use cases, you might want a more controlled update process where you do not want specific nodes updated concurrently with the rest of the cluster. These use cases include, but are not limited to:

* You have mission-critical applications that you do not want unavailable during the update. You can slowly test the applications on your nodes in small batches after the update.
* You have a small maintenance window that does not allow the time for all nodes to be updated, or you have multiple maintenance windows.

The rolling update process is *not* a typical update workflow. With larger clusters, it can be a time-consuming process that requires you execute multiple commands. This complexity can result in errors that can affect the entire cluster.  It is recommended that you carefully consider whether your organization wants to use a rolling update and carefully plan the implementation of the process before you start.

The rolling update process described in this topic involves:

* Creating one or more custom machine config pools (MCPs).
* Labeling each node that you do not want to  update immediately to move those nodes to the custom MCPs.
* Pausing those custom MCPs, which prevents updates to those nodes.
* Performing the cluster update.
* Unpausing one custom MCP, which triggers the update on those nodes.
* Testing the applications on those nodes to make sure the applications work as expected on those newly-updated nodes.
* Optionally removing the custom labels from the remaining nodes in small batches and testing the applications on those nodes.

//The following wording comes from https://github.com/openshift/openshift-docs/pull/34704, not yet finalized

[NOTE]
====
Pausing an MCP should be done with careful consideration and for short periods of time only.
====

//link that follows is in the assembly: updating-cluster-between-minor
