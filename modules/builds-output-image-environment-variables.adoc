// Module included in the following assemblies:
//
// * builds/managing-build-output.adoc

[id="builds-output-image-environment-variables_{context}"]
= Output image environment variables

ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
docker and
endif::[]
source-to-image (S2I) strategy builds set the following environment variables on output images:

[options="header"]
|===

|Variable |Description

|`OPENSHIFT_BUILD_NAME`
|Name of the build

|`OPENSHIFT_BUILD_NAMESPACE`
|Namespace of the build

|`OPENSHIFT_BUILD_SOURCE`
|The source URL of the build

|`OPENSHIFT_BUILD_REFERENCE`
|The Git reference used in the build

|`OPENSHIFT_BUILD_COMMIT`
|Source commit used in the build
|===

Additionally, any user-defined environment variable, for example those configured with
S2I]
ifdef::openshift-enterprise,openshift-webscale,openshift-origin[]
or docker
endif::[]
strategy options, will also be part of the output image environment variable list.
