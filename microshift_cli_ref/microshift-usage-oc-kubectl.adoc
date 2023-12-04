:_mod-docs-content-type: ASSEMBLY
[id="microshift-usage-oc-kubectl"]
= Using oc and kubectl commands
include::_attributes/attributes-microshift.adoc[]
:context: usage-oc-kubectl

toc::[]

The Kubernetes command-line interface (CLI), `kubectl`, can be used to run commands against a Kubernetes cluster. Because {product-title} is a certified Kubernetes distribution, you can use the supported `kubectl` CLI tool that ships with {product-title}, or you can gain extended functionality by using the `oc` CLI tool.

[id="microshift-kubectl-binary_{context}"]
== The kubectl CLI tool

You can use the `kubectl` CLI tool to interact with Kubernetes primitives on your {product-title} cluster. You can also use existing `kubectl` workflows and scripts for new {product-title} users coming from another Kubernetes environment, or for those who prefer to use the `kubectl` CLI.

The `kubectl` CLI tool is included in the archive if you download the `oc` CLI tool.

For more information, read the link:https://kubernetes.io/docs/reference/kubectl/overview/[Kubernetes CLI tool documentation].

[id="microshift-oc-binary_{context}"]
== The oc CLI tool

The `oc` CLI tool offers the same capabilities as the `kubectl` CLI tool, but it extends to natively support additional {product-title} features, including:

* **Route resource**
+
The `Route` resource object is specific to {product-title} distributions, and builds upon standard Kubernetes primitives.
+
* **Additional commands**
+
The additional command `oc new-app`, for example, makes it easier to get new applications started using existing source code or pre-built images.

[IMPORTANT]
====
If you installed an earlier version of the `oc` CLI tool, you cannot use it to complete all of the commands in {product-title} {ocp-version}. If you want the latest features, you must download and install the latest version of the `oc` CLI tool corresponding to your {product-title} version.
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
