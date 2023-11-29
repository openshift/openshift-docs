// Module included in the following assemblies:
//
// * networking/network-verification.adoc

:_mod-docs-content-type: CONCEPT
[id="automatic-network-verification-bypassing_{context}"]
= Automatic network verification bypassing

You can bypass the automatic network verification if you want to deploy
ifdef::openshift-dedicated[]
an {product-title}
endif::openshift-dedicated[]
ifdef::openshift-rosa[]
a {product-title} (ROSA)
endif::openshift-rosa[]
cluster with known network configuration issues into an existing Virtual Private Cloud (VPC).

If you bypass the network verification when you create a cluster, the cluster has a limited support status. After installation, you can resolve the issues and then manually run the network verification. The limited support status is removed after the verification succeeds.

ifdef::openshift-rosa[]
.Bypassing automatic network verification by using {cluster-manager}

endif::openshift-rosa[]
When you install a cluster into an existing VPC by using {cluster-manager-first}, you can bypass the automatic verification by selecting *Bypass network verification* on the *Virtual Private Cloud (VPC) subnet settings* page.

//Commented out due to updates made in OSDOCS-7033
//ifdef::openshift-rosa[]
//.Bypassing automatic network verification by using the ROSA CLI (`rosa`)

//When you install a cluster into an existing VPC by using the `rosa create cluster` command, you can bypass the automatic verification by including the `--bypass-network-verify --force` arguments. The following example bypasses the network verification before creating a cluster:

//[source,terminal]
//----
//$ rosa create cluster --cluster-name mycluster \
//                      --subnet-ids subnet-03146b9b52b6024cb,subnet-///03146b9b52b2034cc \
//                      --bypass-network-verify --force
//----

//[NOTE]
//====
//Alternatively, you can specify the `--interactive` argument and select the option in the interactive prompts to bypass the network verification checks.
//====
//endif::openshift-rosa[]
