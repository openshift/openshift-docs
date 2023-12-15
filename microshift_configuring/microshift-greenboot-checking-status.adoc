:_mod-docs-content-type: ASSEMBLY
[id="microshift-greenboot-checking-status"]
= Checking Greenboot scripts status
include::_attributes/attributes-microshift.adoc[]
:context: microshift-greenboot-script-status

toc::[]

To deploy applications or make other changes through the {microshift-short} API with tools other than `kustomize` manifests, you must wait until the Greenboot health checks have finished. This ensures that your changes are not lost if Greenboot rolls your `rpm-ostree` system back to an earlier state.

The `greenboot-healthcheck` service runs one time and then exits. After Greenboot has exited and the system is in a healthy state, you can proceed with configuration changes and deployments.

include::modules/microshift-greenboot-check-status.adoc[leveloffset=+1]