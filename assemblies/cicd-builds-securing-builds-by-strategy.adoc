:_mod-docs-content-type: ASSEMBLY
[id="securing-builds-by-strategy"]
= Securing builds by strategy
include::_attributes/common-attributes.adoc[]
:context: securing-builds-by-strategy

toc::[]

Builds in {product-title} are run in privileged containers. Depending on the build strategy used, if you have privileges, you can run builds to escalate their permissions on the cluster and host nodes. And as a security measure, it limits who can run builds and the strategy that is used for those builds. Custom builds are inherently less safe than source builds, because they can execute any code within a privileged container, and are disabled by default. Grant docker build permissions with caution, because a vulnerability in the Dockerfile processing logic could result in a privileges being granted on the host node.

By default, all users that can create builds are granted permission to use the docker and Source-to-image (S2I) build strategies. Users with cluster administrator privileges can enable the custom build strategy, as referenced in the restricting build strategies to a user globally section.

You can control who can build and which build strategies they can use by using an authorization policy. Each build strategy has a corresponding build subresource. A user must have permission to create a build and permission to create on the build strategy subresource to create builds using that strategy. Default roles are provided that grant the create permission on the build strategy subresource.

.Build Strategy Subresources and Roles
[options="header"]
|===

|Strategy |Subresource |Role

|Docker
|builds/docker
|system:build-strategy-docker

|Source-to-Image
|builds/source
|system:build-strategy-source

|Custom
|builds/custom
|system:build-strategy-custom

|JenkinsPipeline
|builds/jenkinspipeline
|system:build-strategy-jenkinspipeline

|===

include::modules/builds-disabling-build-strategy-globally.adoc[leveloffset=+1]
include::modules/builds-restricting-build-strategy-globally.adoc[leveloffset=+1]
include::modules/builds-restricting-build-strategy-to-user.adoc[leveloffset=+1]
