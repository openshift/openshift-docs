// Module included in the following assemblies:
//
// * support/troubleshooting/troubleshooting-s2i.adoc

:_mod-docs-content-type: PROCEDURE
[id="gathering-s2i-diagnostic-data_{context}"]
= Gathering Source-to-Image diagnostic data

The S2I tool runs a build pod and a deployment pod in sequence. The deployment pod is responsible for deploying the application pods based on the application container image created in the build stage. Watch build, deployment and application pod status to determine where in the S2I process a failure occurs. Then, focus diagnostic data collection accordingly.

.Prerequisites

ifndef::openshift-rosa,openshift-dedicated[]
* You have access to the cluster as a user with the `cluster-admin` role.
endif::openshift-rosa,openshift-dedicated[]
ifdef::openshift-rosa,openshift-dedicated[]
* You have access to the cluster as a user with the `dedicated-admin` role.
endif::openshift-rosa,openshift-dedicated[]
* Your API service is still functional.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. Watch the pod status throughout the S2I process to determine at which stage a failure occurs:
+
[source,terminal]
----
$ oc get pods -w  <1>
----
<1> Use `-w` to monitor pods for changes until you quit the command using `Ctrl+C`.

. Review a failed pod's logs for errors.
+
* *If the build pod fails*, review the build pod's logs:
+
[source,terminal]
----
$ oc logs -f pod/<application_name>-<build_number>-build
----
+
[NOTE]
====
Alternatively, you can review the build configuration's logs using `oc logs -f bc/<application_name>`. The build configuration's logs include the logs from the build pod.
====
+
* *If the deployment pod fails*, review the deployment pod's logs:
+
[source,terminal]
----
$ oc logs -f pod/<application_name>-<build_number>-deploy
----
+
[NOTE]
====
Alternatively, you can review the deployment configuration's logs using `oc logs -f dc/<application_name>`. This outputs logs from the deployment pod until the deployment pod completes successfully. The command outputs logs from the application pods if you run it after the deployment pod has completed. After a deployment pod completes, its logs can still be accessed by running `oc logs -f pod/<application_name>-<build_number>-deploy`.
====
+
* *If an application pod fails, or if an application is not behaving as expected within a running application pod*, review the application pod's logs:
+
[source,terminal]
----
$ oc logs -f pod/<application_name>-<build_number>-<random_string>
----
