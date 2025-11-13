// Module included in the following assemblies:
//
//*builds/build-strategies.adoc
//*builds/understanding-image-builds

[id="builds-strategy-docker-build_{context}"]
= Docker build

{product-title} uses Buildah to build a container image from a Dockerfile. For more information on building container images with Dockerfiles, see link:https://docs.docker.com/engine/reference/builder/[the Dockerfile reference documentation].

[TIP]
====
If you set Docker build arguments by using the `buildArgs` array, see link:https://docs.docker.com/engine/reference/builder/#understand-how-arg-and-from-interact[Understand how ARG and FROM interact] in the Dockerfile reference documentation.
====
