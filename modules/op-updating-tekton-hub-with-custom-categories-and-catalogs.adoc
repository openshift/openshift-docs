// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-hub-with-openshift-pipelines.adoc

:_mod-docs-content-type: PROCEDURE
[id="updating-tekton-hub-with-custom-categories-and-catalogs_{context}"]
= Updating {tekton-hub} with custom categories and catalogs

[role="_abstract"]
Cluster administrators can update Tekton Hub with custom categories, catalogs, scopes, and default scopes that reflect the context of their organization.

[discrete]
.Procedure

. Optional: Edit the `categories`, `catalogs`, `scopes`, and `default:scopes` fields in the Tekton Hub CR.
+
[NOTE]
====
The default information for categories, catalog, scopes, and default scopes are pulled from the {tekton-hub} API config map. If you provide custom values in the `TektonHub` CR, it overrides the default values.
====

. Apply the {tekton-hub} CR.
+
[source,terminal]
----
$ oc apply -f <tekton-hub-cr>.yaml
----

. Observe the {tekton-hub} status.
+
[source,terminal]
----
$ oc get tektonhub.operator.tekton.dev
----
+
.Sample output
[source,terminal]
----
NAME   VERSION   READY   REASON   APIURL                  UIURL
hub    v1.9.0    True             https://api.route.url   https://ui.route.url
----