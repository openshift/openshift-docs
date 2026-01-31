// Module included in the following assemblies:
//
// cli_reference/developer_cli_odo/using_odo_in_a_restricted_environment/creating-and-deploying-a-component-to-the-disconnected-cluster

:_mod-docs-content-type: PROCEDURE
[id="mirroring-a-supported-builder-image_{context}"]
= Mirroring a supported builder image

To use npm packages for Node.js dependencies and Maven packages for Java dependencies and configure a runtime environment for your application, you must mirror a respective builder image from the mirror registry.


.Procedure

. Verify that the required images tag is not imported:
+
[source,terminal]
----
$ oc describe is nodejs -n openshift
----
+
.Example output
[source,terminal]
----
Name:                   nodejs
Namespace:              openshift
[...]

10
  tagged from <mirror-registry>:<port>/rhoar-nodejs/nodejs-10
    prefer registry pullthrough when referencing this tag

  Build and run Node.js 10 applications on RHEL 7. For more information about using this builder image, including OpenShift considerations, see https://github.com/nodeshift/centos7-s2i-nodejs.
  Tags: builder, nodejs, hidden
  Example Repo: https://github.com/sclorg/nodejs-ex.git

  ! error: Import failed (NotFound): dockerimage.image.openshift.io "<mirror-registry>:<port>/rhoar-nodejs/nodejs-10:latest" not found
      About an hour ago

10-SCL (latest)
  tagged from <mirror-registry>:<port>/rhscl/nodejs-10-rhel7
    prefer registry pullthrough when referencing this tag

  Build and run Node.js 10 applications on RHEL 7. For more information about using this builder image, including OpenShift considerations, see https://github.com/nodeshift/centos7-s2i-nodejs.
  Tags: builder, nodejs
  Example Repo: https://github.com/sclorg/nodejs-ex.git

  ! error: Import failed (NotFound): dockerimage.image.openshift.io "<mirror-registry>:<port>/rhscl/nodejs-10-rhel7:latest" not found
      About an hour ago

[...]
----

. Mirror the supported image tag to the private registry:
+
[source,terminal]
----
$ oc image mirror registry.access.redhat.com/rhscl/nodejs-10-rhel7:<tag> <private_registry>/rhscl/nodejs-10-rhel7:<tag>
----

. Import the image:
+
[source,terminal]
----
$ oc tag <mirror-registry>:<port>/rhscl/nodejs-10-rhel7:<tag> nodejs-10-rhel7:latest --scheduled
----
+
You must periodically re-import the image. The `--scheduled` flag enables automatic re-import of the image.

. Verify that the images with the given tag have been imported:
+
[source,terminal]
----
$ oc describe is nodejs -n openshift
----
+
.Example output
[source,terminal]
----
Name:                   nodejs
[...]
10-SCL (latest)
  tagged from <mirror-registry>:<port>/rhscl/nodejs-10-rhel7
    prefer registry pullthrough when referencing this tag

  Build and run Node.js 10 applications on RHEL 7. For more information about using this builder image, including OpenShift considerations, see https://github.com/nodeshift/centos7-s2i-nodejs.
  Tags: builder, nodejs
  Example Repo: https://github.com/sclorg/nodejs-ex.git

  * <mirror-registry>:<port>/rhscl/nodejs-10-rhel7@sha256:d669ecbc11ac88293de50219dae8619832c6a0f5b04883b480e073590fab7c54
      3 minutes ago

[...]
----
