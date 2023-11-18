// This module is included in the following assembly:
//
// *cicd/pipelines/using-pipelines-as-code.adoc

:_mod-docs-content-type: REFERENCE
[id="splitting-pipelines-as-code-logs-by-namespace_{context}"]
= Splitting {pac} logs by namespace

The logs contain the namespace information to make it possible to filter logs or split the logs by a particular namespace. For example, to view the logs related to the `mynamespace` namespace, enter the following command:

[source,terminal]
----
$ oc logs pipelines-as-code-controller-<unique-id> -n openshift-pipelines | grep mynamespace <1>
----
<1> Replace `pipelines-as-code-controller-<unique-id>` with the {pac} controller name.
