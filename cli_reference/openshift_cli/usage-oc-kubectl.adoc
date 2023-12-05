:_mod-docs-content-type: ASSEMBLY
[id="usage-oc-kubectl"]
= Usage of oc and kubectl commands
include::_attributes/common-attributes.adoc[]
:context: usage-oc-kubectl

The Kubernetes command-line interface (CLI), `kubectl`, can be used to run commands against a Kubernetes cluster. Because {product-title}
ifdef::openshift-rosa[]
(ROSA)
endif::openshift-rosa[]
is a certified Kubernetes distribution, you can use the supported `kubectl` binaries that ship with
ifndef::openshift-rosa[]
{product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
ROSA
endif::openshift-rosa[]
, or you can gain extended functionality by using the `oc` binary.

== The oc binary

The `oc` binary offers the same capabilities as the `kubectl` binary, but it extends to natively support additional
ifndef::openshift-rosa[]
{product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
ROSA
endif::openshift-rosa[]
features, including:

* **Full support for
ifndef::openshift-rosa[]
{product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
ROSA
endif::openshift-rosa[]
resources**
+
Resources such as `DeploymentConfig`, `BuildConfig`, `Route`, `ImageStream`, and `ImageStreamTag` objects are specific to
ifndef::openshift-rosa[]
{product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
ROSA
endif::openshift-rosa[]
distributions, and build upon standard Kubernetes primitives.
+
* **Authentication**
+
ifndef::microshift,openshift-rosa,openshift-dedicated[]
The `oc` binary offers a built-in `login` command for authentication and lets you work with projects, which map Kubernetes namespaces to authenticated users.
Read xref:../../authentication/understanding-authentication.adoc#understanding-authentication[Understanding authentication] for more information.
endif::microshift,openshift-rosa,openshift-dedicated[]
+
ifdef::microshift[]
The `oc` binary offers a built-in `login` command for authentication to {product-title}.
endif::[]
+
* **Additional commands**
+
The additional command `oc new-app`, for example, makes it easier to get new applications started using existing source code or pre-built images. Similarly, the additional command `oc new-project` makes it easier to start a project that you can switch to as your default.

[IMPORTANT]
====
If you installed an earlier version of the `oc` binary, you cannot use it to complete all of the commands in
ifndef::openshift-rosa[]
{product-title} {product-version}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
ROSA
endif::openshift-rosa[]
. If you want the latest features, you must download and install the latest version of the `oc` binary corresponding to your
ifndef::openshift-rosa[]
{product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
ROSA
endif::openshift-rosa[]
server version.
====

Non-security API changes will involve, at minimum, two minor releases (4.1 to 4.2 to 4.3, for example) to allow older `oc` binaries to update. Using new capabilities might require newer `oc` binaries. A 4.3 server might have additional capabilities that a 4.2 `oc` binary cannot use and a 4.3 `oc` binary might have additional capabilities that are unsupported by a 4.2 server.

.Compatibility Matrix

[cols="1,1,1"]
|===

|
|*X.Y* (`oc` Client)
|*X.Y+N* footnote:versionpolicyn[Where *N* is a number greater than or equal to 1.] (`oc` Client)

|*X.Y* (Server)
|image:redcircle-1.png[]
|image:redcircle-3.png[]

|*X.Y+N* footnote:versionpolicyn[] (Server)
|image:redcircle-2.png[]
|image:redcircle-1.png[]

|===
image:redcircle-1.png[] Fully compatible.

image:redcircle-2.png[] `oc` client might not be able to access server features.

image:redcircle-3.png[] `oc` client might provide options and features that might not be compatible with the accessed server.

== The kubectl binary

The `kubectl` binary is provided as a means to support existing workflows and scripts for new
ifndef::openshift-rosa[]
{product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
ROSA
endif::openshift-rosa[]
users coming from a standard Kubernetes environment, or for those who prefer to use the `kubectl` CLI. Existing users of `kubectl` can continue to use the binary to interact with Kubernetes primitives, with no changes required to the
ifndef::openshift-rosa[]
{product-title}
endif::openshift-rosa[]
ifdef::openshift-rosa[]
ROSA
endif::openshift-rosa[]
cluster.

You can install the supported `kubectl` binary by following the steps to xref:../../cli_reference/openshift_cli/getting-started-cli.adoc#cli-installing-cli_cli-developer-commands[Install the OpenShift CLI]. The `kubectl` binary is included in the archive if you download the binary, or is installed when you install the CLI by using an RPM.

For more information, see the link:https://kubernetes.io/docs/reference/kubectl/overview/[kubectl documentation].
