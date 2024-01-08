// Module included in the following assemblies:
//
// * networking/network-verification.adoc

:_mod-docs-content-type: CONCEPT
ifdef::openshift-dedicated[]
[id="osd-understanding-network-verification_{context}"]
= Understanding network verification for {product-title} clusters
endif::openshift-dedicated[]
ifdef::openshift-rosa[]
[id="rosa-understanding-network-verification_{context}"]
= Understanding network verification for ROSA clusters
endif::openshift-rosa[]

When you deploy
ifdef::openshift-dedicated[]
an {product-title}
endif::openshift-dedicated[]
ifdef::openshift-rosa[]
a {product-title} (ROSA)
endif::openshift-rosa[]
cluster into an existing Virtual Private Cloud (VPC) or create an additional machine pool with a subnet that is new to your cluster, network verification runs automatically. This helps you identify and resolve configuration issues prior to deployment.

ifdef::openshift-dedicated[]
When you prepare to install your cluster by using {cluster-manager-first}, the automatic checks run after you input a subnet into a subnet ID field on the *Virtual Private Cloud (VPC) subnet settings* page.
endif::openshift-dedicated[]
ifdef::openshift-rosa[]
When you prepare to install your cluster by using {cluster-manager-first}, the automatic checks run after you input a subnet into a subnet ID field on the *Virtual Private Cloud (VPC) subnet settings* page. If you create your cluster by using the ROSA CLI (`rosa`) with the interactive mode, the checks run after you provide the required VPC network information. If you use the CLI without the interactive mode, the checks begin immediately prior to the cluster creation.
endif::openshift-rosa[]

When you add a machine pool with a subnet that is new to your cluster, the automatic network verification checks the subnet to ensure that network connectivity is available before the machine pool is provisioned.

After automatic network verification completes, a record is sent to the service log. The record provides the results of the verification check, including any network configuration errors. You can resolve the identified issues before a deployment and the deployment has a greater chance of success.

You can also run the network verification manually for an existing cluster. This enables you to verify the network configuration for your cluster after making configuration changes. For steps to run the network verification checks manually, see _Running the network verification manually_.
