// Module included in the following assemblies:
//
// * applications/quotas/quotas-setting-per-project.adoc

:_mod-docs-content-type: PROCEDURE
[id="quota-creating-object-count-quotas_{context}"]
= Creating object count quotas

You can create an object count quota for all standard namespaced resource types on {product-title}, such as `BuildConfig` and `DeploymentConfig` objects. An object quota count places a defined quota on all standard namespaced resource types.

When using a resource quota, an object is charged against the quota upon creation. These types of quotas are useful to protect against exhaustion of resources. The quota can only be created if there are enough spare resources within the project.

.Procedure

To configure an object count quota for a resource:

. Run the following command:
+
[source,terminal]
----
$ oc create quota <name> \
    --hard=count/<resource>.<group>=<quota>,count/<resource>.<group>=<quota> <1>
----
<1> The `<resource>` variable is the name of the resource, and `<group>` is the API group, if applicable. Use the `oc api-resources` command for a list of resources and their associated API groups.
+
For example:
+
[source,terminal]
----
$ oc create quota test \
    --hard=count/deployments.extensions=2,count/replicasets.extensions=4,count/pods=3,count/secrets=4
----
+
.Example output
[source,terminal]
----
resourcequota "test" created
----
+
This example limits the listed resources to the hard limit in each project in the cluster.

. Verify that the quota was created:
+
[source,terminal]
----
$ oc describe quota test
----
+
.Example output
[source,terminal]
----
Name:                         test
Namespace:                    quota
Resource                      Used  Hard
--------                      ----  ----
count/deployments.extensions  0     2
count/pods                    0     3
count/replicasets.extensions  0     4
count/secrets                 0     4
----
