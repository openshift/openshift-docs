:_mod-docs-content-type: ASSEMBLY
[id="unprivileged-building-of-container-images-using-buildah"]
= Building of container images using Buildah as a non-root user
include::_attributes/common-attributes.adoc[]
:context: unprivileged-building-of-container-images-using-buildah

toc::[]

Running {pipelines-shortname} as the root user on a container can expose the container processes and the host to other potentially malicious resources. You can reduce this type of exposure by running the workload as a specific non-root user in the container. To run builds of container images using Buildah as a non-root user, you can perform the following steps:

* Define custom service account (SA) and security context constraint (SCC).
* Configure Buildah to use the `build` user with id `1000`.
* Start a task run with a custom config map, or integrate it with a pipeline run.

include::modules/op-configuring-custom-sa-and-scc.adoc[leveloffset=+1]
include::modules/op-configuring-buildah-to-use-build-user.adoc[leveloffset=+1]
include::modules/op-starting-a-task-run-pipeline-run-build-user.adoc[leveloffset=+1]
include::modules/op-limitations-of-unprivileged-builds.adoc[leveloffset=+1]


.Additional resources

* xref:../../authentication/managing-security-context-constraints.adoc#managing-pod-security-policies[Managing security context constraints (SCCs)]
