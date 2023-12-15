:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="kn-cli-tools"]
= Knative CLI for use with {ServerlessProductName}
:context: kn-cli-tools

toc::[]

The Knative (`kn`) CLI enables simple interaction with Knative components on {product-title}.

[id="kn-cli-tools-key-features"]
== Key features

The Knative (`kn`) CLI is designed to make serverless computing tasks simple and concise.
Key features of the Knative CLI include:

* Deploy serverless applications from the command line.
* Manage features of Knative Serving, such as services, revisions, and traffic-splitting.
* Create and manage Knative Eventing components, such as event sources and triggers.
* Create sink bindings to connect existing Kubernetes applications and Knative services.
* Extend the Knative CLI with flexible plugin architecture, similar to the `kubectl` CLI.
* Configure autoscaling parameters for Knative services.
* Scripted usage, such as waiting for the results of an operation, or deploying custom rollout and rollback strategies.

[id="kn-cli-tools-installing-kn"]
== Installing the Knative CLI

See link:https://docs.openshift.com/serverless/1.28/install/installing-kn.html#installing-kn[Installing the Knative CLI].
