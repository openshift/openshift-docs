:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="removing-openshift-serverless"]
= Removing {ServerlessProductName} overview
:context: removing-openshift-serverless

If you need to remove {ServerlessProductName} from your cluster, you can do so by manually removing the {ServerlessOperatorName} and other {ServerlessProductName} components. Before you can remove the {ServerlessOperatorName}, you must remove Knative Serving and Knative Eventing.

After uninstalling the {ServerlessProductName}, you can remove the Operator and API custom resource definitions (CRDs) that remain on the cluster.

The steps for fully removing {ServerlessProductName} are detailed in the following procedures:

* xref:../../serverless/removing/uninstalling-knative-eventing.adoc#uninstalling-knative-eventing[Uninstalling Knative Eventing].
* xref:../../serverless/removing/uninstalling-knative-serving.adoc#uninstalling-knative-serving[Uninstalling Knative Serving].
* xref:../../serverless/removing/removing-serverless-operator.adoc#removing-serverless-operator[Removing the {ServerlessOperatorName}].
* xref:../../serverless/removing/deleting-serverless-crds.adoc#deleting-serverless-crds[Deleting {ServerlessProductName} custom resource definitions].
