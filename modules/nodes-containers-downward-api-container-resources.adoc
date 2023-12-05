// Module included in the following assemblies:
//
// * nodes/nodes-containers-downward-api.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-containers-downward-api-container-resources-api_{context}"]
= Understanding how to consume container resources using the Downward API

When creating pods, you can use the Downward API to inject information about
computing resource requests and limits so that image and application authors can
correctly create an image for specific environments.

You can do this using environment variable or a volume plugin.

