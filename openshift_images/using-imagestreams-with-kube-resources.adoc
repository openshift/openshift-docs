:_mod-docs-content-type: ASSEMBLY
[id="using-imagestreams-with-kube-resources"]
= Using image streams with Kubernetes resources
include::_attributes/common-attributes.adoc[]
:context: using-imagestreams-with-kube-resources

toc::[]

Image streams, being {product-title} native resources, work with all native resources available in {product-title}, such as `Build` or `DeploymentConfigs` resources. It is also possible to make them work with native Kubernetes resources, such as `Job`, `ReplicationController`, `ReplicaSet` or Kubernetes `Deployment` resources.

include::modules/images-managing-images-enabling-imagestreams-kube.adoc[leveloffset=+1]
