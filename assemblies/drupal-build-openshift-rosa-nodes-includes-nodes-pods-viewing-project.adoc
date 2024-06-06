// Module included in the following assemblies:
//
// * nodes/nodes-pods-viewing.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-pods-viewing-project_{context}"]
= Viewing pods in a project

You can view a list of pods associated with the current project, including the number of replica, the current status, number or restarts and the age of the pod.

.Procedure

To view the pods in a project:

. Change to the project:
+
[source,terminal]
----
$ oc project <project-name>
----

. Run the following command:
+
[source,terminal]
----
$ oc get pods
----
+
For example:
+
[source,terminal]
----
$ oc get pods
----
+
.Example output
[source,terminal]
----
NAME                       READY   STATUS    RESTARTS   AGE
console-698d866b78-bnshf   1/1     Running   2          165m
console-698d866b78-m87pm   1/1     Running   2          165m
----
+
Add the `-o wide` flags to view the pod IP address and the node where the pod is located.
+
[source,terminal]
----
$ oc get pods -o wide
----
+
.Example output
[source,terminal]
----
NAME                       READY   STATUS    RESTARTS   AGE    IP            NODE                           NOMINATED NODE
console-698d866b78-bnshf   1/1     Running   2          166m   10.128.0.24   ip-10-0-152-71.ec2.internal    <none>
console-698d866b78-m87pm   1/1     Running   2          166m   10.129.0.23   ip-10-0-173-237.ec2.internal   <none>
----
