
// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc
// * rosa_architecture/rosa_policy_service_definition/rosa-hcp-service-definition.adoc

ifeval::["{context}" == "rosa-hcp-service-definition"]
:rosa-with-hcp:
endif::[]

:_mod-docs-content-type: CONCEPT
[id="rosa-sdpolicy-regions-az_{context}"]
= Regions and availability zones

The following AWS regions are currently available
ifdef::rosa-with-hcp[]
for {hcp-title}.
endif::rosa-with-hcp[]
ifndef::rosa-with-hcp[]
for Red Hat OpenShift 4 and are supported for {product-title}.
endif::rosa-with-hcp[]

[NOTE]
====
China and GovCloud (US) regions are not supported, regardless of their support on OpenShift 4.
====

.AWS Regions
[%collapsible]
====
ifndef::rosa-with-hcp[]
* af-south-1 (Cape Town, AWS opt-in required)
* ap-east-1 (Hong Kong, AWS opt-in required)
* ap-northeast-1 (Tokyo)
* ap-northeast-2 (Seoul)
* ap-northeast-3 (Osaka)
* ap-south-1 (Mumbai)
* ap-south-2 (Hyderabad, AWS opt-in required)
* ap-southeast-1 (Singapore)
* ap-southeast-2 (Sydney)
endif::rosa-with-hcp[]
* ap-southeast-3 (Jakarta, AWS opt-in required)
ifndef::rosa-with-hcp[]
* ap-southeast-4 (Melbourne, AWS opt-in required)
* ca-central-1 (Central Canada)
endif::rosa-with-hcp[]
* eu-central-1 (Frankfurt)
ifndef::rosa-with-hcp[]
* eu-central-2 (Zurich, AWS opt-in required)
* eu-north-1 (Stockholm)
* eu-south-1 (Milan, AWS opt-in required)
* eu-south-2 (Spain, AWS opt-in required)
endif::rosa-with-hcp[]
* eu-west-1 (Ireland)
ifndef::rosa-with-hcp[]
* eu-west-2 (London)
* eu-west-3 (Paris)
* me-central-1 (UAE, AWS opt-in required)
* me-south-1 (Bahrain, AWS opt-in required)
* sa-east-1 (São Paulo)
endif::rosa-with-hcp[]
* us-east-1 (N. Virginia)
* us-east-2 (Ohio)
ifndef::rosa-with-hcp[]
* us-west-1 (N. California)
endif::rosa-with-hcp[]
* us-west-2 (Oregon)
====

Multiple availability zone clusters can only be deployed in regions with at least 3 availability zones. For more information, see the link:https://aws.amazon.com/about-aws/global-infrastructure/regions_az/[Regions and Availability Zones] section in the AWS documentation.

Each new
ifndef::rosa-with-hcp[]
{product-title}
endif::rosa-with-hcp[]
ifdef::rosa-with-hcp[]
{hcp-title}
endif::rosa-with-hcp[]
cluster is installed within
ifdef::rosa-with-hcp[]
a
endif::rosa-with-hcp[]
ifndef::rosa-with-hcp[]
an installer-created or
endif::rosa-with-hcp[]
preexisting Virtual Private Cloud (VPC) in a single region, with the option to deploy
ifndef::rosa-with-hcp[]
into a single availability zone (Single-AZ) or across multiple availability zones (Multi-AZ).
endif::rosa-with-hcp[]
ifdef::rosa-with-hcp[]
up to the total number of availability zones for the given region.
endif::rosa-with-hcp[]
This provides cluster-level network and resource isolation, and enables cloud-provider VPC settings, such as VPN connections and VPC Peering. Persistent volumes (PVs) are backed by Amazon Elastic Block Storage (Amazon EBS), and are specific to the availability zone in which they are provisioned. Persistent volume claims (PVCs) do not bind to a volume until the associated pod resource is assigned into a specific availability zone to prevent unschedulable pods. Availability zone-specific resources are only usable by resources in the same availability zone.

[WARNING]
====
The region
ifndef::rosa-with-hcp[]
and the choice of single or multiple availability zone
endif::rosa-with-hcp[]
cannot be changed after a cluster has been deployed.
====

ifeval::["{context}" == "rosa-hcp-service-definition"]
:!rosa-with-hcp:
endif::[]
