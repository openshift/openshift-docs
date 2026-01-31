// This module is included in the following assembly:
//
// *cicd/pipelines/using-tekton-hub-with-openshift-pipelines.adoc

:_mod-docs-content-type: PROCEDURE
[id="adding-new-users-in-tekton-hub-configuration_{context}"]
= Adding new users in {tekton-hub} configuration

[role="_abstract"]
Cluster administrators can add new users to {tekton-hub} with different scopes.

[discrete]
.Procedure
. Modify the `TektonHub` CR to add new users with different scopes.
+
[source,yaml]
----
...
scopes:
  - name: agent:create
    users: [<username_1>, <username_2>] <1>
  - name: catalog:refresh
    users: [<username_3>, <username_4>]
  - name: config:refresh
    users: [<username_5>, <username_6>]

default:
  scopes:
    - rating:read
    - rating:write
...
----
<1> The usernames registered with the Git repository hosting service provider.
+
[NOTE]
====
A new user signing in to {tekton-hub} for the first time will have only the default scope. To activate additional scopes, ensure the user's username is added in the `scopes` field of the `TektonHub` CR.
====

. Apply the updated `TektonHub` CR.
+
[source,terminal]
----
$ oc apply -f <tekton-hub-cr>.yaml
----

. Check the status of the {tekton-hub}. The updated `TektonHub` CR might take some time to attain a steady state.
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

. Refresh the configuration.
+
[source,terminal]
----
$ curl -X POST -H "Authorization: <access-token>" \ <1>
    --header "Content-Type: application/json" \
    --data '{"force": true} \
    <api-route>/system/config/refresh
----
<1> The JWT token.