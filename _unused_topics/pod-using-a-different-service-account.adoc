// Module included in the following assemblies:
//
// * orphaned

[id="pod-using-a-different-service-account_{context}"]
= Running a pod with a different service account

You can run a pod with a service account other than the default:

.Prerequisites

* Install the `oc` command line interface.
* Configure a service account.
* Create a DeploymentConfig.

.Procedure

. Edit the DeploymentConfig:
+
----
$ oc edit dc/<deployment_config>
----

. Add the `serviceAccount` and `serviceAccountName` parameters to the `spec`
field, and specify the service account that you want to use:
+
----
spec:
  securityContext: {}
  serviceAccount: <service_account>
  serviceAccountName: <service_account>
----
