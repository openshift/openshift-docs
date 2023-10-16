// Module included in the following assemblies:
//
// * openshift_images/image-configuration.adoc
// * post_installation_configuration/preparing-for-users.adoc

[id="images-configuration-parameters_{context}"]
= Image controller configuration parameters

The `image.config.openshift.io/cluster` resource holds cluster-wide information about how to handle images. The canonical, and only valid name is `cluster`. Its `spec` offers the following configuration parameters.

[NOTE]
====
Parameters such as `DisableScheduledImport`, `MaxImagesBulkImportedPerRepository`, `MaxScheduledImportsPerMinute`, `ScheduledImageImportMinimumIntervalSeconds`, `InternalRegistryHostname` are not configurable.
====

[cols="3a,8a",options="header"]
|===
|Parameter |Description

|`allowedRegistriesForImport`
|Limits the container image registries from which normal users can import images. Set this list to the registries that you trust to contain valid images, and that you want applications to be able to import from. Users with permission to create images or `ImageStreamMappings` from the API are not affected by this policy. Typically only cluster administrators have the appropriate permissions.

Every element of this list contains a location of the registry specified by the registry domain name.

`domainName`: Specifies a domain name for the registry. If the registry uses a non-standard `80` or `443` port, the port should be included in the domain name as well.

`insecure`: Insecure indicates whether the registry is secure or insecure. By default, if not otherwise specified, the registry is assumed to be secure.

|`additionalTrustedCA`
|A reference to a config map containing additional CAs that should be trusted during `image stream import`, `pod image pull`, `openshift-image-registry pullthrough`, and builds.

The namespace for this config map is `openshift-config`. The format of the config map is to use the registry hostname as the key, and the PEM-encoded certificate as the value, for each additional registry CA to trust.

|`externalRegistryHostnames`
|Provides the hostnames for the default external image registry. The external hostname should be set only when the image registry is exposed externally. The first value is used in `publicDockerImageRepository` field in image streams. The value must be in `hostname[:port]` format.

|`registrySources`
|Contains configuration that determines how the container runtime should treat individual registries when accessing images for builds and
pods. For instance, whether or not to allow insecure access. It does not contain configuration for the internal cluster registry.

`insecureRegistries`: Registries which do not have a valid TLS certificate or only support HTTP connections. To specify all subdomains, add the asterisk (`\*`) wildcard character as a prefix to the domain name. For example, `*.example.com`. You can specify an individual repository within a registry. For example: `reg1.io/myrepo/myapp:latest`.

`blockedRegistries`: Registries for which image pull and push actions are denied. To specify all subdomains, add the asterisk (`\*`) wildcard character as a prefix to the domain name. For example, `*.example.com`. You can specify an individual repository within a registry. For example: `reg1.io/myrepo/myapp:latest`. All other registries are allowed.

`allowedRegistries`: Registries for which image pull and push actions are allowed. To specify all subdomains, add the asterisk (`\*`) wildcard character as a prefix to the domain name. For example, `*.example.com`. You can specify an individual repository within a registry. For example: `reg1.io/myrepo/myapp:latest`. All other registries are blocked.

`containerRuntimeSearchRegistries`: Registries for which image pull and push actions are allowed using image short names. All other registries are blocked.

Either `blockedRegistries` or `allowedRegistries` can be set, but not both.

|===

[WARNING]
====
When the `allowedRegistries` parameter is defined, all registries, including `registry.redhat.io` and `quay.io` registries and the default {product-registry}, are blocked unless explicitly listed. When using the parameter, to prevent pod failure, add all registries including the `registry.redhat.io` and `quay.io` registries and the `internalRegistryHostname` to the `allowedRegistries` list, as they are required by payload images within your environment. For disconnected clusters, mirror registries should also be added.
====

The `status` field of the `image.config.openshift.io/cluster` resource holds observed values from the cluster.

[cols="3a,8a",options="header"]
|===
|Parameter |Description

|`internalRegistryHostname`
|Set by the Image Registry Operator, which controls the `internalRegistryHostname`. It sets the hostname for the default {product-registry}. The value must be in `hostname[:port]` format. For backward compatibility, you can still use the `OPENSHIFT_DEFAULT_REGISTRY` environment variable, but this setting overrides the environment variable.

|`externalRegistryHostnames`
|Set by the Image Registry Operator, provides the external hostnames for the image registry when it is exposed externally. The first value is used in `publicDockerImageRepository` field in image streams. The values must be in `hostname[:port]` format.

|===
