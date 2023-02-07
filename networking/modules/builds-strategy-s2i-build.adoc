// Module included in the following assemblies:
//
//* builds/build-strategies.adoc
//* builds/understanding-image-builds.adoc

[id="builds-strategy-s2i-build_{context}"]
= Source-to-image build

Source-to-image (S2I) is a tool for building reproducible container images. It produces ready-to-run images by injecting application source into a container image and assembling a new image. The new image incorporates the base image, the builder, and built source and is ready to use with the `buildah run` command. S2I supports incremental builds, which re-use previously downloaded dependencies, previously built artifacts, and so on.


////
The advantages of S2I include the following:

[horizontal]
Image flexibility:: S2I scripts can be written to inject application code into almost any existing Docker-formatted container image, taking advantage of the existing ecosystem. Note that, currently, S2I relies on `tar` to inject application source, so the image needs to be able to process tarred content.

Speed:: With S2I, the assemble process can perform a large number of complex operations without creating a new layer at each step, resulting in a fast process. In addition, S2I scripts can be written to re-use artifacts stored in a previous version of the application image, rather than having to download or build them each time the build is run.

Patchability:: S2I allows you to rebuild the application consistently if an underlying image needs a patch due to a security issue.

Operational efficiency:: By restricting build operations instead of allowing arbitrary actions, as a Dockerfile would allow, the PaaS operator can avoid accidental or intentional abuses of the build system.

Operational security:: Building an arbitrary Dockerfile exposes the host system to root privilege escalation. This can be exploited by a malicious user because the entire Docker build process is run as a user with Docker privileges. S2I restricts the operations performed as a root user and can run the scripts as a non-root user.

User efficiency:: S2I prevents developers from performing arbitrary `yum install` type operations, which could slow down development iteration, during their application build.

Ecosystem:: S2I encourages a shared ecosystem of images where you can leverage best practices for your applications.

Reproducibility:: Produced images can include all inputs including specific versions of build tools and dependencies. This ensures that the image can be reproduced precisely.
////
