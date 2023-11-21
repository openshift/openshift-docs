// Module included in the following assemblies:
//
// * nodes/nodes-containers-downward-api.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-containers-downward-api-container-values_{context}"]
= Understanding how to consume container values using the downward API

You containers can consume API values using environment variables or a volume plugin.
Depending on the method you choose, containers can consume:

* Pod name

* Pod project/namespace

* Pod annotations

* Pod labels

Annotations and labels are available using only a volume plugin.

