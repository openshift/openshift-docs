:_mod-docs-content-type: ASSEMBLY
[id="serverless-autoscaling-developer-scale-bounds"]
= Scale bounds
include::_attributes/common-attributes.adoc[]
:context: serverless-serving-scale-bounds

toc::[]

Scale bounds determine the minimum and maximum numbers of replicas that can serve an application at any given time. You can set scale bounds for an application to help prevent cold starts or control computing costs.

// minscale docs
include::modules/serverless-autoscaling-developer-minscale.adoc[leveloffset=+1]
include::modules/serverless-autoscaling-minscale-kn.adoc[leveloffset=+2]

// maxscale docs
include::modules/serverless-autoscaling-developer-maxscale.adoc[leveloffset=+1]
include::modules/serverless-autoscaling-maxscale-kn.adoc[leveloffset=+2]
