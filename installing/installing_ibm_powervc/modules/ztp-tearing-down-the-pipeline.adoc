// Module included in the following assemblies:
//
// * scalability_and_performance/ztp_far_edge/ztp-deploying-far-edge-sites.adoc

:_mod-docs-content-type: PROCEDURE
[id="ztp-tearing-down-the-pipeline_{context}"]
= Tearing down the {ztp} pipeline

You can remove the ArgoCD pipeline and all generated {ztp-first} artifacts.

.Prerequisites

* You have installed the OpenShift CLI (`oc`).

* You have logged in to the hub cluster as a user with `cluster-admin` privileges.

.Procedure

. Detach all clusters from {rh-rhacm-first} on the hub cluster.

. Delete the `kustomization.yaml` file in the `deployment` directory using the following command:
+
[source,terminal]
----
$ oc delete -k out/argocd/deployment
----

. Commit and push your changes to the site repository.
