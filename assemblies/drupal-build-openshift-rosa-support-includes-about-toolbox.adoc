// Module included in the following assemblies:
//
// * support/gathering-cluster-data.adoc

:_mod-docs-content-type: CONCEPT
[id="about-toolbox_{context}"]
= About `toolbox`

ifndef::openshift-origin[]
`toolbox` is a tool that starts a container on a {op-system-first} system. The tool is primarily used to start a container that includes the required binaries and plugins that are needed to run commands such as `sosreport` and `redhat-support-tool`.

The primary purpose for a `toolbox` container is to gather diagnostic information and to provide it to Red Hat Support. However, if additional diagnostic tools are required, you can add RPM packages or run an image that is an alternative to the standard support tools image.
endif::openshift-origin[]

ifdef::openshift-origin[]
`toolbox` is a tool that starts a container on a {op-system-first} system. The tool is primarily used to start a container that includes the required binaries and plugins that are needed to run your favorite debugging or admin tools.
endif::openshift-origin[]
