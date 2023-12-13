// Module included in the following assemblies:
//
// pipelines/creating-applications-with-cicd-pipelines

:_mod-docs-content-type: PROCEDURE
[id="op-mirroring-images-to-run-pipelines-in-restricted-environment_{context}"]
=  Mirroring images to run pipelines in a restricted environment


To run {pipelines-shortname} in a disconnected cluster or a cluster provisioned in a restricted environment, ensure that either the Samples Operator is configured for a restricted network, or a cluster administrator has created a cluster with a mirrored registry.

The following procedure uses the `pipelines-tutorial` example to create a pipeline for an application in a restricted environment using a cluster with a mirrored registry. To ensure that the `pipelines-tutorial` example works in a restricted environment, you must mirror the respective builder images from the mirror registry for the front-end interface, `pipelines-vote-ui`; back-end interface, `pipelines-vote-api`; and the `cli`.

.Procedure

. Mirror the builder image from the mirror registry for the front-end interface, `pipelines-vote-ui`.
.. Verify that the required images tag is not imported:
+
[source,terminal]
----
$ oc describe imagestream python -n openshift
----
+
.Example output
[source,terminal]
----
Name:			python
Namespace:		openshift
[...]

3.8-ubi9 (latest)
  tagged from registry.redhat.io/ubi9/python-38:latest
    prefer registry pullthrough when referencing this tag

  Build and run Python 3.8 applications on UBI 8. For more information about using this builder image, including OpenShift considerations, see https://github.com/sclorg/s2i-python-container/blob/master/3.8/README.md.
  Tags: builder, python
  Supports: python:3.8, python
  Example Repo: https://github.com/sclorg/django-ex.git

[...]
----

.. Mirror the supported image tag to the private registry:
+
[source,terminal]
----
$ oc image mirror registry.redhat.io/ubi9/python-39:latest <mirror-registry>:<port>/ubi9/python-39
----

.. Import the image:
+
[source,terminal]
----
$ oc tag <mirror-registry>:<port>/ubi9/python-39 python:latest --scheduled -n openshift
----
+
You must periodically re-import the image. The `--scheduled` flag enables automatic re-import of the image.

.. Verify that the images with the given tag have been imported:
+
[source,terminal]
----
$ oc describe imagestream python -n openshift
----
+
.Example output
[source,terminal]
----
Name:			python
Namespace:		openshift
[...]

latest
  updates automatically from registry  <mirror-registry>:<port>/ubi9/python-39

  *  <mirror-registry>:<port>/ubi9/python-39@sha256:3ee...

[...]
----

. Mirror the builder image from the mirror registry for the back-end interface, `pipelines-vote-api`.
.. Verify that the required images tag is not imported:
+
[source,terminal]
----
$ oc describe imagestream golang -n openshift
----
+
.Example output
[source,terminal]
----
Name:			golang
Namespace:		openshift
[...]

1.14.7-ubi8 (latest)
  tagged from registry.redhat.io/ubi8/go-toolset:1.14.7
    prefer registry pullthrough when referencing this tag

  Build and run Go applications on UBI 8. For more information about using this builder image, including OpenShift considerations, see https://github.com/sclorg/golang-container/blob/master/README.md.
  Tags: builder, golang, go
  Supports: golang
  Example Repo: https://github.com/sclorg/golang-ex.git

[...]
----

.. Mirror the supported image tag to the private registry:
+
[source,terminal]
----
$ oc image mirror registry.redhat.io/ubi9/go-toolset:latest <mirror-registry>:<port>/ubi9/go-toolset
----

.. Import the image:
+
[source,terminal]
----
$ oc tag <mirror-registry>:<port>/ubi9/go-toolset golang:latest --scheduled -n openshift
----
+
You must periodically re-import the image. The `--scheduled` flag enables automatic re-import of the image.

.. Verify that the images with the given tag have been imported:
+
[source,terminal]
----
$ oc describe imagestream golang -n openshift
----
+
.Example output
[source,terminal]
----
Name:			golang
Namespace:		openshift
[...]

latest
  updates automatically from registry <mirror-registry>:<port>/ubi9/go-toolset

  * <mirror-registry>:<port>/ubi9/go-toolset@sha256:59a74d581df3a2bd63ab55f7ac106677694bf612a1fe9e7e3e1487f55c421b37

[...]
----

. Mirror the builder image from the mirror registry for the `cli`.
.. Verify that the required images tag is not imported:
+
[source,terminal]
----
$ oc describe imagestream cli -n openshift
----
+
.Example output
[source,terminal]
----
Name:                   cli
Namespace:              openshift
[...]

latest
  updates automatically from registry quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:65c68e8c22487375c4c6ce6f18ed5485915f2bf612e41fef6d41cbfcdb143551

  * quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:65c68e8c22487375c4c6ce6f18ed5485915f2bf612e41fef6d41cbfcdb143551

[...]
----

.. Mirror the supported image tag to the private registry:
+
[source,terminal]
----
$ oc image mirror quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:65c68e8c22487375c4c6ce6f18ed5485915f2bf612e41fef6d41cbfcdb143551 <mirror-registry>:<port>/openshift-release-dev/ocp-v4.0-art-dev:latest
----

.. Import the image:
+
[source,terminal]
----
$ oc tag <mirror-registry>:<port>/openshift-release-dev/ocp-v4.0-art-dev cli:latest --scheduled -n openshift
----
+
You must periodically re-import the image. The `--scheduled` flag enables automatic re-import of the image.

.. Verify that the images with the given tag have been imported:
+
[source,terminal]
----
$ oc describe imagestream cli -n openshift
----
+
.Example output
[source,terminal]
----
Name:                   cli
Namespace:              openshift
[...]

latest
  updates automatically from registry <mirror-registry>:<port>/openshift-release-dev/ocp-v4.0-art-dev

  * <mirror-registry>:<port>/openshift-release-dev/ocp-v4.0-art-dev@sha256:65c68e8c22487375c4c6ce6f18ed5485915f2bf612e41fef6d41cbfcdb143551

[...]
----
