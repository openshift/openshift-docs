// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-about.adoc

[id="osdk-workflow_{context}"]
= Development workflow

The Operator SDK provides the following workflow to develop a new Operator:

. Create an Operator project by using the Operator SDK command-line interface (CLI).
. Define new resource APIs by adding custom resource definitions (CRDs).
. Specify resources to watch by using the Operator SDK API.
. Define the Operator reconciling logic in a designated handler and use the Operator SDK API to interact with resources.
. Use the Operator SDK CLI to build and generate the Operator deployment manifests.

.Operator SDK workflow
image::osdk-workflow.png[]

At a high level, an Operator that uses the Operator SDK processes events for watched resources in an Operator author-defined handler and takes actions to reconcile the state of the application.
