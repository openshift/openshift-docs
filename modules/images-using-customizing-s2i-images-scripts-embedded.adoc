// Module included in the following assemblies:
//
// * openshift_images/using_images/customizing-s2i-images.adoc

:_mod-docs-content-type: PROCEDURE
[id="images-using-customizing-s2i-images-scripts-embedded_{context}"]
= Invoking scripts embedded in an image

Builder images provide their own version of the source-to-image (S2I) scripts that cover the most common use-cases. If these scripts do not fulfill your needs, S2I provides a way of overriding them by adding custom ones in the `.s2i/bin` directory. However, by doing this, you are completely replacing the standard scripts. In some cases, replacing the scripts is acceptable, but, in other scenarios, you can run a few commands before or after the scripts while retaining the logic of the script provided in the image. To reuse the standard scripts, you can create a wrapper script that runs custom logic and delegates further work to the default scripts in the image.

.Procedure

. Look at the value of the `io.openshift.s2i.scripts-url` label to determine the location of the scripts inside of the builder image:
+
[source,terminal]
----
$ podman inspect --format='{{ index .Config.Labels "io.openshift.s2i.scripts-url" }}' wildfly/wildfly-centos7
----
+
.Example output
[source,terminal]
----
image:///usr/libexec/s2i
----
+
You inspected the `wildfly/wildfly-centos7` builder image and found out that the scripts are in the `/usr/libexec/s2i` directory.
+
. Create a script that includes an invocation of one of the standard scripts wrapped in other commands:
+
.`.s2i/bin/assemble` script
[source,bash]
----
#!/bin/bash
echo "Before assembling"

/usr/libexec/s2i/assemble
rc=$?

if [ $rc -eq 0 ]; then
    echo "After successful assembling"
else
    echo "After failed assembling"
fi

exit $rc
----
+
This example shows a custom assemble script that prints the message, runs the standard assemble script from the image, and prints another message depending on the exit code of the assemble script.
+
[IMPORTANT]
====
When wrapping the run script, you must use `exec` for invoking it to ensure signals are handled properly. The use of `exec` also precludes the ability to run additional commands after invoking the default image run script.
====
+
.`.s2i/bin/run` script
[source,bash]
----
#!/bin/bash
echo "Before running application"
exec /usr/libexec/s2i/run
----
