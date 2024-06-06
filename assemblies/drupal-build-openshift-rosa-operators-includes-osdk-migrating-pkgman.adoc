// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-pkgman-to-bundle.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-migrating-pkgman_{context}"]
= Migrating a package manifest project to bundle format

Operator authors can use the Operator SDK to migrate a package manifest format Operator project to a bundle format project.

.Prerequisites

* Operator SDK CLI installed
* Operator project initially generated using the Operator SDK in package manifest format

.Procedure

* Use the Operator SDK to migrate your package manifest project to the bundle format and generate bundle images:
+
[source,terminal]
----
$ operator-sdk pkgman-to-bundle <package_manifests_dir> \ <1>
    [--output-dir <directory>] \ <2>
    --image-tag-base <image_name_base> <3>
----
<1> Specify the location of the package manifests directory for the project, such as `packagemanifests/` or `manifests/`.
<2> Optional: By default, the generated bundles are written locally to disk to the `bundle/` directory. You can use the `--output-dir` flag to specify an alternative location.
<3> Set the `--image-tag-base` flag to provide the base of the image name, such as `quay.io/example/etcd`, that will be used for the bundles. Provide the name without a tag, because the tag for the images will be set according to the bundle version. For example, the full bundle image names are generated in the format `<image_name_base>:<bundle_version>`.

////
Reinsert in place after https://bugzilla.redhat.com/show_bug.cgi?id=1967369 is fixed:

    [--build-cmd <command>] \ <3>

<3> Optional: Specify the build command for building container images using the `--build-cmd` flag. The default build command is `docker build`. The command must be in your `PATH`, otherwise you must provide a fully qualified path name.
////

.Verification

* Verify that the generated bundle image runs successfully:
+
[source,terminal]
----
$ operator-sdk run bundle <bundle_image_name>:<tag>
----
+
.Example output
[source,terminal]
----
INFO[0025] Successfully created registry pod: quay-io-my-etcd-0-9-4
INFO[0025] Created CatalogSource: etcd-catalog
INFO[0026] OperatorGroup "operator-sdk-og" created
INFO[0026] Created Subscription: etcdoperator-v0-9-4-sub
INFO[0031] Approved InstallPlan install-5t58z for the Subscription: etcdoperator-v0-9-4-sub
INFO[0031] Waiting for ClusterServiceVersion "default/etcdoperator.v0.9.4" to reach 'Succeeded' phase
INFO[0032]   Waiting for ClusterServiceVersion "default/etcdoperator.v0.9.4" to appear
INFO[0048]   Found ClusterServiceVersion "default/etcdoperator.v0.9.4" phase: Pending
INFO[0049]   Found ClusterServiceVersion "default/etcdoperator.v0.9.4" phase: Installing
INFO[0064]   Found ClusterServiceVersion "default/etcdoperator.v0.9.4" phase: Succeeded
INFO[0065] OLM has successfully installed "etcdoperator.v0.9.4"
----
