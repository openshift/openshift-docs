// Module included in the following assemblies:
//
// * rosa_architecture/rosa_architecture_sub/rosa-architecture-models.adoc
[id="rosa-architecture_{context}"]
= ROSA architecture on public and private networks

You can install ROSA using either a public or private network. Configure a private cluster and private network connection during or after the cluster creation process.
Red Hat manages the cluster with limited access through a public network. For more information, see xref:../../rosa_architecture/rosa_policy_service_definition/rosa-service-definition.adoc#rosa-service-definition[ROSA service definition].

.ROSA Classic deployed on public and private networks
image::156_OpenShift_ROSA_Arch_0621_arch.svg[ROSA deployed on public and private networks]

If you are using {hcp-title-first}, you can create your clusters on public and private networks as well. The following images depict the architecture of both public and private networks.

.ROSA with HCP deployed on a public network
image::ROSA-HCP-and-ROSA-Classic-public.png[ROSA with HCP deployed on a public network]

.ROSA with HCP deployed on a private network
image::ROSA-HCP-and-ROSA-Classic-private.png[ROSA with HCP deployed on a private network]

Alternatively, you can install a ROSA Classic cluster using AWS PrivateLink, which is hosted on private subnets only.
