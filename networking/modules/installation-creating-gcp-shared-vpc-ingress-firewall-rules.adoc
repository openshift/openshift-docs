// Module included in the following assemblies:
//
// * installing/installing_gcp/installing-gcp-user-infra-vpc.adoc

[id="installation-creating-gcp-shared-vpc-ingress-firewall-rules_{context}"]
= Creating ingress firewall rules for a shared VPC in GCP

You must create ingress firewall rules to allow the access that the {product-title} cluster requires.

.Prerequisites

* You exported the variables that the Deployment Manager templates require to deploy your cluster.
* You created the networking and load balancing components in GCP that your cluster requires.

.Procedure

* Add ingress firewall rules:
** For an external cluster:
+
----
$ gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} compute firewall-rules create --allow='tc p:30000-32767,udp:30000-32767' --network="${CLUSTER_NETWORK}" --source-ranges='130.211.0.0/22,35.191.0.0/16, 209.85.152.0/22,209.85.204.0/22' --target-tags="${INFRA_ID}-master,${INFRA_ID}-worker" ${INFRA_ID}-ingress-h c
417
418 gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} compute firewall-rules create --allow='tc p:80,tcp:443' --network="${CLUSTER_NETWORK}" --source-ranges="0.0.0.0/0" --target-tags="${INFRA_ID}-master,$ {INFRA_ID}-worker" ${INFRA_ID}-ingress
----

** For an internal cluster:
+
----
$ gcloud compute firewall-rules create --allow='tcp:30000-32767,udp:30000-32767' --network="${CLUSTER_NETWORK }" --source-ranges='130.211.0.0/22,35.191.0.0/16,209.85.152.0/22,209.85.204.0/22' --target-tags="${INFRA_ID} -master,${INFRA_ID}-worker" ${INFRA_ID}-ingress-hc
383
gcloud compute firewall-rules create --allow='tcp:80,tcp:443' --network="${CLUSTER_NETWORK}" --source-ranges="${NETWORK_CIDR}" --target-tags="${INFRA_ID}-master,${INFRA_ID}-worker" ${INFRA_ID}-ingress
----
