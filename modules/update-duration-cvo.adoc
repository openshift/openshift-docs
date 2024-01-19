// Module included in the following assemblies:
//
// * updating/understanding_updates/understanding-openshift-update-duration.adoc

:_mod-docs-content-type: CONCEPT
[id="cluster-version-operator_{context}"]
= Cluster Version Operator target update payload deployment

The Cluster Version Operator (CVO) retrieves the target update release image and applies to the cluster. All components which run as pods are updated during this phase, whereas the host components are updated by the Machine Config Operator (MCO). This process might take 60 to 120 minutes.

[NOTE]
====
The CVO phase of the update does not restart the nodes.
====
