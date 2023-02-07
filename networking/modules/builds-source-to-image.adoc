// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-source-to-image_{context}"]
= Source-to-image strategy

When using a `Source` strategy, all defined input secrets are copied to their respective `destinationDir`. If you left `destinationDir` empty, then the secrets are placed in the working directory of the builder image.

The same rule is used when a `destinationDir` is a relative path. The secrets are placed in the paths that are relative to the working directory of the image. The final directory in the `destinationDir` path is created if it does not exist in the builder image. All preceding directories in the `destinationDir` must exist, or an error will occur.

[NOTE]
====
Input secrets are added as world-writable, have `0666` permissions, and are truncated to size zero after executing the `assemble` script. This means that the secret files exist in the resulting image, but they are empty for security reasons.

Input config maps are not truncated after the `assemble` script completes.
====
