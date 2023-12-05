:_mod-docs-content-type: ASSEMBLY
[id="deploying-machine-health-checks"]
= Deploying machine health checks
include::_attributes/common-attributes.adoc[]
:context: deploying-machine-health-checks

toc::[]

You can configure and deploy a machine health check to automatically repair damaged machines in a machine pool.

include::modules/machine-user-provisioned-limitations.adoc[leveloffset=+1]

include::modules/machine-health-checks-about.adoc[leveloffset=+1]
[role="_additional-resources"]
.Additional resources
* xref:../nodes/nodes/nodes-nodes-viewing.adoc#nodes-nodes-viewing-listing_nodes-nodes-viewing[About listing all the nodes in a cluster]
* xref:../machine_management/deploying-machine-health-checks.adoc#machine-health-checks-short-circuiting_deploying-machine-health-checks[Short-circuiting machine health check remediation]
* xref:../machine_management/control_plane_machine_management/cpmso-about.adoc#cpmso-about[About the Control Plane Machine Set Operator]

include::modules/machine-health-checks-resource.adoc[leveloffset=+1]

include::modules/machine-health-checks-creating.adoc[leveloffset=+1]

You can configure and deploy a machine health check to detect and repair unhealthy bare metal nodes.

include::modules/mgmt-power-remediation-baremetal-about.adoc[leveloffset=+1]
