// Module included in the following assemblies:
//
// * nodes/cluster/limit-ranges.adoc

[id="nodes-cluster-limit-viewing_{context}"]
= Viewing a limit

You can view any limits defined in a project by navigating in the web
console to the project's *Quota* page.

You can also use the CLI to view limit range details:

. Get the list of `LimitRange` object defined in the project. For example, for a
project called *demoproject*:
+
[source,terminal]
----
$ oc get limits -n demoproject
----
+
[source,terminal]
----
NAME              CREATED AT
resource-limits   2020-07-15T17:14:23Z
----

. Describe the `LimitRange` object you are interested in, for example the
`resource-limits` limit range:
+

[source,terminal]
----
$ oc describe limits resource-limits -n demoproject
----
+

[source,terminal]
----
Name:                           resource-limits
Namespace:                      demoproject
Type                            Resource                Min     Max     Default Request Default Limit   Max Limit/Request Ratio
----                            --------                ---     ---     --------------- -------------   -----------------------
Pod                             cpu                     200m    2       -               -               -
Pod                             memory                  6Mi     1Gi     -               -               -
Container                       cpu                     100m    2       200m            300m            10
Container                       memory                  4Mi     1Gi     100Mi           200Mi           -
openshift.io/Image              storage                 -       1Gi     -               -               -
openshift.io/ImageStream        openshift.io/image      -       12      -               -               -
openshift.io/ImageStream        openshift.io/image-tags -       10      -               -               -
PersistentVolumeClaim           storage                 -       50Gi    -               -               -
----

