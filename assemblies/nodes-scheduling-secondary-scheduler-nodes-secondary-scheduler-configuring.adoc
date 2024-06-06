:_mod-docs-content-type: ASSEMBLY
[id="secondary-scheduler-configuring"]
= Scheduling pods using a secondary scheduler
include::_attributes/common-attributes.adoc[]
:context: secondary-scheduler-configuring

You can run a custom secondary scheduler in {product-title} by installing the {secondary-scheduler-operator}, deploying the secondary scheduler, and setting the secondary scheduler in the pod definition.

toc::[]

// Installing the {secondary-scheduler-operator}
include::modules/nodes-secondary-scheduler-install-console.adoc[leveloffset=+1]

// Deploying a secondary scheduler
include::modules/nodes-secondary-scheduler-configuring-console.adoc[leveloffset=+1]

// Scheduling a pod using the secondary scheduler
include::modules/nodes-secondary-scheduler-pod-console.adoc[leveloffset=+1]
