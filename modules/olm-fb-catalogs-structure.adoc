// Module included in the following assemblies:
//
// * operators/understanding/olm-packaging-format.adoc

[id="olm-fb-catalogs-structure_{context}"]
= Directory structure

File-based catalogs can be stored and loaded from directory-based file systems. The `opm` CLI loads the catalog by walking the root directory and recursing into subdirectories. The CLI attempts to load every file it finds and fails if any errors occur.

Non-catalog files can be ignored using `.indexignore` files, which have the same rules for patterns and precedence as `.gitignore` files.

.Example `.indexignore` file
[source,terminal]
----
# Ignore everything except non-object .json and .yaml files
**/*
!*.json
!*.yaml
**/objects/*.json
**/objects/*.yaml
----

Catalog maintainers have the flexibility to choose their desired layout, but it is recommended to store each package's file-based catalog blobs in separate subdirectories. Each individual file can be either JSON or YAML; it is not necessary for every file in a catalog to use the same format.

.Basic recommended structure
[source,terminal]
----
catalog
├── packageA
│   └── index.yaml
├── packageB
│   ├── .indexignore
│   ├── index.yaml
│   └── objects
│       └── packageB.v0.1.0.clusterserviceversion.yaml
└── packageC
    └── index.json
----

This recommended structure has the property that each subdirectory in the directory hierarchy is a self-contained catalog, which makes catalog composition, discovery, and navigation trivial file system operations. The catalog could also be included in a parent catalog by copying it into the parent catalog's root directory.
