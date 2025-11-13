// Module included in the following assemblies:
//
// * builds/creating-build-inputs.adoc

[id="builds-custom-strategy_{context}"]
= Custom strategy

When using a Custom strategy, all the defined input secrets and config maps are available in the builder container in the `/var/run/secrets/openshift.io/build` directory. The custom build image must use these secrets and config maps appropriately. With the Custom strategy, you can define secrets as described in Custom strategy options.

There is no technical difference between existing strategy secrets and the input secrets. However, your builder image can distinguish between them and use them differently, based on your build use case.

The input secrets are always mounted into the `/var/run/secrets/openshift.io/build` directory, or your builder can parse the `$BUILD` environment variable, which includes the full build object.

[IMPORTANT]
====
If a pull secret for the registry exists in both the namespace and the node, builds default to using the pull secret in the namespace.
====
