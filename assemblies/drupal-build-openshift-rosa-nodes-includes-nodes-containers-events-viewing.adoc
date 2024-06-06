// Module included in the following assemblies:
//
// * nodes/nodes-containers-events.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-containers-events-viewing-cli_{context}"]
= Viewing events using the CLI

You can get a list of events in a given project using the CLI.

.Procedure

* To view events in a project use the following command:
+
[source,terminal]
----
$ oc get events [-n <project>] <1>
----
<1> The name of the project.
+
For example:
+
[source,terminal]
----
$ oc get events -n openshift-config
----
+
.Example output
[source,terminal]
----
LAST SEEN   TYPE      REASON                   OBJECT                      MESSAGE
97m         Normal    Scheduled                pod/dapi-env-test-pod       Successfully assigned openshift-config/dapi-env-test-pod to ip-10-0-171-202.ec2.internal
97m         Normal    Pulling                  pod/dapi-env-test-pod       pulling image "gcr.io/google_containers/busybox"
97m         Normal    Pulled                   pod/dapi-env-test-pod       Successfully pulled image "gcr.io/google_containers/busybox"
97m         Normal    Created                  pod/dapi-env-test-pod       Created container
9m5s        Warning   FailedCreatePodSandBox   pod/dapi-volume-test-pod    Failed create pod sandbox: rpc error: code = Unknown desc = failed to create pod network sandbox k8s_dapi-volume-test-pod_openshift-config_6bc60c1f-452e-11e9-9140-0eec59c23068_0(748c7a40db3d08c07fb4f9eba774bd5effe5f0d5090a242432a73eee66ba9e22): Multus: Err adding pod to network "openshift-sdn": cannot set "openshift-sdn" ifname to "eth0": no netns: failed to Statfs "/proc/33366/ns/net": no such file or directory
8m31s       Normal    Scheduled                pod/dapi-volume-test-pod    Successfully assigned openshift-config/dapi-volume-test-pod to ip-10-0-171-202.ec2.internal
----


* To view events in your project from the {product-title} console.
+
. Launch the {product-title} console.
+
. Click *Home* -> *Events* and select your project.

. Move to resource that you want to see events. For example: *Home* -> *Projects* -> <project-name> -> <resource-name>.
+
Many objects, such as pods and deployments, have their own
*Events* tab as well, which shows events related to that object.
