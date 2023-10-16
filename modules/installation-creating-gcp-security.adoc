// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra.adoc
// * installing/installing_gcp/installing-restricted-networks-gcp.adoc

[id="installation-creating-gcp-security_{context}"]
= Creating firewall rules and IAM roles in GCP

You must create security groups and roles in Google Cloud Platform (GCP) for your
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

. Copy the template from the *Deployment Manager template for firewall rules and IAM roles*
section of this topic and save it as `03_security.py` on your computer. This
template describes the security groups and roles that your cluster requires.

. Export the following variables required by the resource definition:
+
[source,terminal]
----
$ export MASTER_NAT_IP=`gcloud compute addresses describe ${INFRA_ID}-master-nat-ip --region ${REGION} --format json | jq -r .address`
$ export WORKER_NAT_IP=`gcloud compute addresses describe ${INFRA_ID}-worker-nat-ip --region ${REGION} --format json | jq -r .address`
----

. Create a `03_security.yaml` resource definition file:
+
[source,terminal]
----
$ cat <<EOF >03_security.yaml
imports:
- path: 03_security.py

resources:
- name: cluster-security
  type: 03_security.py
  properties:
    allowed_external_cidr: '0.0.0.0/0' <1>
    infra_id: '${INFRA_ID}' <2>
    region: '${REGION}' <3>
    cluster_network: '${CLUSTER_NETWORK}' <4>
    network_cidr: '${NETWORK_CIDR}' <5>
    master_nat_ip: '${MASTER_NAT_IP}' <6>
    worker_nat_ip: '${WORKER_NAT_IP}' <7>
EOF
----
<1> `allowed_external_cidr` is the CIDR range that can access the cluster API and SSH to the bootstrap host. For an internal cluster, set this value to `${NETWORK_CIDR}`.
<2> `infra_id` is the `INFRA_ID` infrastructure name from the extraction step.
<3> `region` is the region to deploy the cluster into, for example `us-central1`.
<4> `cluster_network` is the `selfLink` URL to the cluster network.
<5> `network_cidr` is the CIDR of the VPC network, for example `10.0.0.0/16`.
<6> `master_nat_ip` is the IP address of the master NAT, for example `34.94.100.1`.
<7> `worker_nat_ip` is the IP address of the worker NAT, for example `34.94.200.1`.

. Create the deployment by using the `gcloud` CLI:
+
[source,terminal]
----
$ gcloud deployment-manager deployments create ${INFRA_ID}-security --config 03_security.yaml
----

. Export the variable for the master service account:
+
[source,terminal]
----
$ export MASTER_SERVICE_ACCOUNT=`gcloud iam service-accounts list --filter "email~^${INFRA_ID}-m@${PROJECT_NAME}." --format json | jq -r '.[0].email'`
----

. Export the variable for the worker service account:
+
[source,terminal]
----
$ export WORKER_SERVICE_ACCOUNT=`gcloud iam service-accounts list --filter "email~^${INFRA_ID}-w@${PROJECT_NAME}." --format json | jq -r '.[0].email'`
----

. The templates do not create the policy bindings due to limitations of Deployment
Manager, so you must create them manually:
+
[source,terminal]
----
$ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.instanceAdmin"
$ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.networkAdmin"
$ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.securityAdmin"
$ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/iam.serviceAccountUser"
$ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/storage.admin"

$ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${WORKER_SERVICE_ACCOUNT}" --role "roles/compute.viewer"
$ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${WORKER_SERVICE_ACCOUNT}" --role "roles/storage.admin"
----

. Create a service account key and store it locally for later use:
+
[source,terminal]
----
$ gcloud iam service-accounts keys create service-account-key.json --iam-account=${MASTER_SERVICE_ACCOUNT}
----
