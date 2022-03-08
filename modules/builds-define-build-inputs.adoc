// Module included in the following assemblies:
//
//* builds/creating-build-inputs.adoc

[id="builds-define-build-inputs_{context}"]
= Build inputs

A build input provides source content for builds to operate on. You can use the following build inputs to provide sources in {product-title}, listed in order of precedence:

ifndef::openshift-online[]
* Inline Dockerfile definitions
endif::[]
* Content extracted from existing images
* Git repositories
* Binary (Local) inputs
* Input secrets
* External artifacts

ifdef::openshift-online[]
[IMPORTANT]
====
The docker build strategy is not supported in {product-title}. Therefore, inline Dockerfile definitions are not accepted.
====
endif::[]

You can combine multiple inputs in a single build.
ifndef::openshift-online[]
However, as the inline Dockerfile takes precedence, it can overwrite any other file named Dockerfile provided by another input.
endif::[]
Binary (local) input and Git repositories are mutually exclusive inputs.

You can use input secrets when you do not want certain resources or credentials used during a build to be available in the final application image produced by the build, or want to consume a value that is defined in a secret resource. External artifacts can be used to pull in additional files that are not available as one of the other build input types.

When you run a build:

. A working directory is constructed and all input content is placed in the working directory. For example, the input Git repository is cloned into the working directory, and files specified from input images are copied into the working directory using the target path.

. The build process changes directories into the `contextDir`, if one is defined.

ifndef::openshift-online[]
. The inline Dockerfile, if any, is written to the current directory.
endif::[]

. The content from the current directory is provided to the build process
for reference by the
ifndef::openshift-online[]
Dockerfile, custom builder logic, or
endif::[]
`assemble` script. This means any input content that resides outside the `contextDir` is ignored by the build.

The following example of a source definition includes multiple input types and an explanation of how they are combined. For more details on how each input type is defined, see the specific sections for each input type.

[source,yaml]
----
source:
  git:
    uri: https://github.com/openshift/ruby-hello-world.git <1>
    ref: "master"
  images:
  - from:
      kind: ImageStreamTag
      name: myinputimage:latest
      namespace: mynamespace
    paths:
    - destinationDir: app/dir/injected/dir <2>
      sourcePath: /usr/lib/somefile.jar
  contextDir: "app/dir" <3>
ifndef::openshift-online[]
  dockerfile: "FROM centos:7\nRUN yum install -y httpd" <4>
endif::[]
----
<1> The repository to be cloned into the working directory for the build.
<2> `/usr/lib/somefile.jar` from `myinputimage` is stored in `<workingdir>/app/dir/injected/dir`.
<3> The working directory for the build becomes `<original_workingdir>/app/dir`.
ifndef::openshift-online[]
<4> A Dockerfile with this content is created in `<original_workingdir>/app/dir`, overwriting any existing file with that name.
endif::[]
