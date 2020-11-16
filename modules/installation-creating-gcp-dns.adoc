// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

ifeval::["{context}" == "installing-gcp-user-infra-vpc"]
:shared-vpc:
endif::[]

[id="installation-creating-gcp-dns_{context}"]
= Creating networking and load balancing components in GCP

You must configure networking and load balancing in Google Cloud Platform (GCP) for your
{product-title} cluster to use. One way to create these components is
to modify the provided Deployment Manager template.

[NOTE]
====
If you do not use the provided Deployment Manager template to create your GCP
infrastructure, you must review the provided information and manually create
the infrastructure. If your cluster does not initialize correctly, you might
have to contact Red Hat support with your installation logs.
====

.Prerequisites

* Configure a GCP account.
* Generate the Ignition config files for your cluster.
* Create and configure a VPC and associated subnets in GCP.

.Procedure

. Copy the template from the *Deployment Manager template for the network and load balancers*
section of this topic and save it as `02_infra.py` on your computer. This
template describes the networking and load balancing objects that your cluster
requires.

. Export the following variable required by the resource definition:
+
ifndef::shared-vpc[]
[source,terminal]
----
$ export CLUSTER_NETWORK=`gcloud compute networks describe ${INFRA_ID}-network --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT} --format json | jq -r .selfLink`
----
endif::shared-vpc[]
ifdef::shared-vpc[]
[source,terminal]
----
$ export CLUSTER_NETWORK=`gcloud compute networks describe ${HOST_PROJECT_NETWORK} --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT} --format json | jq -r .selfLink`
----
+
Where `<network_name>` is the name of the network that hosts the shared VPC.
endif::shared-vpc[]

. Create a `02_infra.yaml` resource definition file:
+
[source,terminal]
----
$ cat <<EOF >02_infra.yaml
imports:
- path: 02_infra.py

resources:
- name: cluster-infra
  type: 02_infra.py
  properties:
    infra_id: '${INFRA_ID}' <1>
    region: '${REGION}' <2>

    cluster_domain: '${CLUSTER_NAME}.${BASE_DOMAIN}' <3>
    cluster_network: '${CLUSTER_NETWORK}' <4>
EOF
----
<1> `infra_id` is the `INFRA_ID` infrastructure name from the extraction step.
<2> `region` is the region to deploy the cluster into, for example `us-central1`.
<3> `cluster_domain` is the domain for the cluster, for example `openshift.example.com`.
<4> `cluster_network` is the `selfLink` URL to the cluster network.

. Create the deployment by using the `gcloud` CLI:
+
[source,terminal]
----
$ gcloud deployment-manager deployments create ${INFRA_ID}-infra --config 02_infra.yaml
----

. The templates do not create DNS entries due to limitations of Deployment
Manager, so you must create them manually:

.. Export the following variable:
+
[source,terminal]
----
$ export CLUSTER_IP=`gcloud compute addresses describe ${INFRA_ID}-cluster-public-ip --region=${REGION} --format json | jq -r .address`
----

.. Add external DNS entries:
+
[source,terminal]
----
$ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
$ gcloud dns record-sets transaction start --zone ${BASE_DOMAIN_ZONE_NAME}
$ gcloud dns record-sets transaction add ${CLUSTER_IP} --name api.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${BASE_DOMAIN_ZONE_NAME}
$ gcloud dns record-sets transaction execute --zone ${BASE_DOMAIN_ZONE_NAME}
----

.. Add internal DNS entries:
+
[source,terminal]
----
$ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
$ gcloud dns record-sets transaction start --zone ${INFRA_ID}-private-zone
$ gcloud dns record-sets transaction add ${CLUSTER_IP} --name api.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${INFRA_ID}-private-zone
$ gcloud dns record-sets transaction add ${CLUSTER_IP} --name api-int.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${INFRA_ID}-private-zone
$ gcloud dns record-sets transaction execute --zone ${INFRA_ID}-private-zone
----

ifeval::["{context}" == "installing-gcp-user-infra-vpc"]
:!shared-vpc:
endif::[]
