// Text snippet included in the following assemblies:
//
// * applications/projects/working-with-projects.adoc
// * applications/quotas/quotas-setting-across-multiple-projects.adoc
// * openshift_images/image-streams-manage.adoc
//
// Text snippet included in the following modules:
//
// * modules/admission-plug-ins-about.adoc
// * modules/creating-a-project-using-the-CLI.adoc
// * modules/creating-a-project-using-the-web-console.adoc
// * modules/images-managing-images-enabling-imagestreams-kube.adoc
// * modules/odc-creating-projects-using-developer-perspective.adoc
// * modules/rbac-default-projects.adoc
// * modules/security-context-constraints-psa-about.adoc
// * modules/security-context-constraints-rbac.adoc

:_mod-docs-content-type: SNIPPET

[IMPORTANT]
====
Do not run workloads in or share access to default projects. Default projects are reserved for running core cluster components.

The following default projects are considered highly privileged: `default`, `kube-public`, `kube-system`, `openshift`, `openshift-infra`, `openshift-node`, and other system-created projects that have the `openshift.io/run-level` label set to `0` or `1`. Functionality that relies on admission plugins, such as pod security admission, security context constraints, cluster resource quotas, and image reference resolution, does not work in highly privileged projects.
====
