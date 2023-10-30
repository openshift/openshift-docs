// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-pkgman-to-bundle.adoc

:_mod-docs-content-type: CONCEPT
[id="osdk-about-pkg-format-migration_{context}"]
= About packaging format migration

The Operator SDK `pkgman-to-bundle` command helps in migrating Operator Lifecycle Manager (OLM) package manifests to bundles. The command takes an input package manifest directory and generates bundles for each of the versions of manifests present in the input directory. You can also then build bundle images for each of the generated bundles.

For example, consider the following `packagemanifests/` directory for a project in the package manifest format:

.Example package manifest format layout
[source,terminal]
----
packagemanifests/
└── etcd
    ├── 0.0.1
    │   ├── etcdcluster.crd.yaml
    │   └── etcdoperator.clusterserviceversion.yaml
    ├── 0.0.2
    │   ├── etcdbackup.crd.yaml
    │   ├── etcdcluster.crd.yaml
    │   ├── etcdoperator.v0.0.2.clusterserviceversion.yaml
    │   └── etcdrestore.crd.yaml
    └── etcd.package.yaml
----

After running the migration, the following bundles are generated in the `bundle/` directory:

.Example bundle format layout
[source,terminal]
----
bundle/
├── bundle-0.0.1
│   ├── bundle.Dockerfile
│   ├── manifests
│   │   ├── etcdcluster.crd.yaml
│   │   ├── etcdoperator.clusterserviceversion.yaml
│   ├── metadata
│   │   └── annotations.yaml
│   └── tests
│       └── scorecard
│           └── config.yaml
└── bundle-0.0.2
    ├── bundle.Dockerfile
    ├── manifests
    │   ├── etcdbackup.crd.yaml
    │   ├── etcdcluster.crd.yaml
    │   ├── etcdoperator.v0.0.2.clusterserviceversion.yaml
    │   ├── etcdrestore.crd.yaml
    ├── metadata
    │   └── annotations.yaml
    └── tests
        └── scorecard
            └── config.yaml
----

Based on this generated layout, bundle images for both of the bundles are also built with the following names:

* `quay.io/example/etcd:0.0.1`
* `quay.io/example/etcd:0.0.2`
