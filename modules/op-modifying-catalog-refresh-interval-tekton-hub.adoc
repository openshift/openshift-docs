// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-hub-with-openshift-pipelines.adoc

:_mod-docs-content-type: PROCEDURE
[id="modifying-catalog-refresh-interval-tekton-hub_{context}"]
= Modifying the catalog refresh interval of {tekton-hub}

[role="_abstract"]
The default catalog refresh interval for {tekton-hub} is 30 minutes. Cluster administrators can modify the automatic catalog refresh interval by modifying the value of the `catalogRefreshInterval` field in the `TektonHub` CR.

[discrete]
.Procedure
. Modify the value of the `catalogRefreshInterval` field in the `TektonHub` CR.
+
[source,yaml]
----
apiVersion: operator.tekton.dev/v1alpha1
kind: TektonHub
metadata:
  name: hub
spec:
  targetNamespace: openshift-pipelines <1>
  api:
    catalogRefreshInterval: 30m <2>
----
<1> The namespace where {tekton-hub} is installed; default is `openshift-pipelines`.
<2> The time interval after which the catalog refreshes automatically. The supported units of time are seconds (`s`), minutes (`m`), hours (`h`), days (`d`), and weeks (`w`). The default interval is 30 minutes.

. Apply the `TektonHub` CR.
+
[source,terminal]
----
$ oc apply -f <tekton-hub-cr>.yaml
----

. Check the status of the installation. The `TektonHub` CR might take some time to attain steady state.
+
[source,terminal]
----
$ oc get tektonhub.operator.tekton.dev
----
+
.Sample output
[source,terminal]
----
NAME   VERSION   READY   REASON   APIURL                    UIURL
hub    v1.9.0    True             https://api.route.url/    https://ui.route.url/
----