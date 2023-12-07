// Module included in the following assemblies:
// * openshift_images/image-streams-managing.adoc

:_mod-docs-content-type: PROCEDURE
[id="images-getting-info-about-imagestreams_{context}"]
= Getting information about image streams

You can get general information about the image stream and detailed information about all the tags it is pointing to.

.Procedure

* To get general information about the image stream and detailed information about all the tags it is pointing to, enter the following command:
+
[source,terminal]
----
$ oc describe is/<image-name>
----
+
For example:
+
[source,terminal]
----
$ oc describe is/python
----
+
.Example output
[source,terminal]
----
Name:			python
Namespace:		default
Created:		About a minute ago
Labels:			<none>
Annotations:		openshift.io/image.dockerRepositoryCheck=2017-10-02T17:05:11Z
Docker Pull Spec:	docker-registry.default.svc:5000/default/python
Image Lookup:		local=false
Unique Images:		1
Tags:			1

3.5
  tagged from centos/python-35-centos7

  * centos/python-35-centos7@sha256:49c18358df82f4577386404991c51a9559f243e0b1bdc366df25
      About a minute ago
----

* To get all of the information available about a particular image stream tag, enter the following command:
+
[source,terminal]
----
$ oc describe istag/<image-stream>:<tag-name>
----
+
For example:
+
[source,terminal]
----
$ oc describe istag/python:latest
----
+
.Example output
[source,terminal]
----
Image Name:	sha256:49c18358df82f4577386404991c51a9559f243e0b1bdc366df25
Docker Image:	centos/python-35-centos7@sha256:49c18358df82f4577386404991c51a9559f243e0b1bdc366df25
Name:		sha256:49c18358df82f4577386404991c51a9559f243e0b1bdc366df25
Created:	2 minutes ago
Image Size:	251.2 MB (first layer 2.898 MB, last binary layer 72.26 MB)
Image Created:	2 weeks ago
Author:		<none>
Arch:		amd64
Entrypoint:	container-entrypoint
Command:	/bin/sh -c $STI_SCRIPTS_PATH/usage
Working Dir:	/opt/app-root/src
User:		1001
Exposes Ports:	8080/tcp
Docker Labels:	build-date=20170801
----
+
[NOTE]
====
More information is output than shown.
====

* Enter the following command to discover which architecture or operating system that an image stream tag supports:
+
[source,terminal]
----
$ oc get istag <image-stream-tag> -ojsonpath="{range .image.dockerImageManifests[*]}{.os}/{.architecture}{'\n'}{end}"
----
+
For example:
+
[source,terminal]
----
$ oc get istag busybox:latest -ojsonpath="{range .image.dockerImageManifests[*]}{.os}/{.architecture}{'\n'}{end}"
----
+
.Example output
[source,terminal]
----
linux/amd64
linux/arm
linux/arm64
linux/386
linux/mips64le
linux/ppc64le
linux/riscv64
linux/s390x
----