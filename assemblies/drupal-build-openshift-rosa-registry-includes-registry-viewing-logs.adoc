// Module included in the following assemblies:
//
// * registry/accessing-the-registry.adoc

:_mod-docs-content-type: PROCEDURE
[id="registry-viewing-logs_{context}"]
= Viewing registry logs

You can view the logs for the registry by using the `oc logs` command.

.Procedure

* Use the `oc logs` command with deployments to view the logs for the container
image registry:
+
[source,terminal]
----
$ oc logs deployments/image-registry -n openshift-image-registry
----
+
.Example output
[source,terminal]
----
2015-05-01T19:48:36.300593110Z time="2015-05-01T19:48:36Z" level=info msg="version=v2.0.0+unknown"
2015-05-01T19:48:36.303294724Z time="2015-05-01T19:48:36Z" level=info msg="redis not configured" instance.id=9ed6c43d-23ee-453f-9a4b-031fea646002
2015-05-01T19:48:36.303422845Z time="2015-05-01T19:48:36Z" level=info msg="using inmemory layerinfo cache" instance.id=9ed6c43d-23ee-453f-9a4b-031fea646002
2015-05-01T19:48:36.303433991Z time="2015-05-01T19:48:36Z" level=info msg="Using OpenShift Auth handler"
2015-05-01T19:48:36.303439084Z time="2015-05-01T19:48:36Z" level=info msg="listening on :5000" instance.id=9ed6c43d-23ee-453f-9a4b-031fea646002
----
