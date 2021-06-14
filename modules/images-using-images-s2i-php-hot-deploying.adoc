// Module included in the following assemblies:
//
// * openshift_images/using_images/using-images-source-to-image.adoc
// * Unused. Can be removed by 4.9 if still unused. Request full peer review for the module if it’s used.

[id="images-using-images-s2i-hot-deploying_{context}"]
= Hot deploying for PHP

Hot deployment allows you to quickly make and deploy changes to your application without having to generate a new source-to-image (S2I) build. In order to immediately pick up changes made in your application source code, you must run your built image with the `OPCACHE_REVALIDATE_FREQ=0` environment variable.

You can use the `oc env` command to update environment variables of existing objects.

[WARNING]
====
You should only use this option while developing or debugging. It is not recommended to turn this on in your production environment.
====

.Procedure

. To change your source code in a running pod, use the `oc rsh` command to enter the container:
+
[source,terminal]
----
$ oc rsh <pod_id>
----

After you enter into the running container, your current directory is set to `/opt/app-root/src`, where the source code is located.
