// Module included in the following assemblies:
//
// * installing/installing_aws/uninstalling-cluster-aws.adoc
// * installing/installing_gcp/uninstalling-cluster-gcp.adoc
// * installing/installing_azure/uninstalling-cluster-azure.adoc

ifeval::["{context}" == "uninstall-cluster-aws"]
:cp-first: Amazon Web Services
:cp: AWS
:cp-name: aws
:aws-sts:
endif::[]
ifeval::["{context}" == "uninstalling-cluster-gcp"]
:cp-first: Google Cloud Platform
:cp: GCP
:cp-name: gcp
:gcp-workload-id:
endif::[]
ifeval::["{context}" == "uninstall-cluster-azure"]
:cp-first: Microsoft Azure
:cp: Azure
:cp-name: azure
:azure-workload-id:
endif::[]

:_mod-docs-content-type: PROCEDURE
[id="cco-ccoctl-deleting-sts-resources_{context}"]
= Deleting {cp-first} resources with the Cloud Credential Operator utility

After uninstalling an {product-title} cluster that uses short-term credentials managed outside the cluster, you can use the CCO utility (`ccoctl`) to remove the {cp-first} ({cp}) resources that `ccoctl` created during installation.

.Prerequisites

* Extract and prepare the `ccoctl` binary.
* Uninstall an {product-title} cluster on {cp} that uses short-term credentials.

.Procedure
//GCP has extra prep steps
ifdef::gcp-workload-id[]
. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:
+
[source,terminal]
----
$ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
----

. Extract the list of `CredentialsRequest` custom resources (CRs) from the {product-title} release image by running the following command:
+
[source,terminal,subs="attributes+"]
----
$ oc adm release extract \
  --from=$RELEASE_IMAGE \
  --credentials-requests \
  --included \// <1>
  --to=<path_to_directory_for_credentials_requests> <2>
----
<1> The `--included` parameter includes only the manifests that your specific cluster configuration requires.
<2> Specify the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

. Delete the {cp} resources that `ccoctl` created by running the following command:
endif::gcp-workload-id[]
ifdef::aws-sts,azure-workload-id[]
* Delete the {cp} resources that `ccoctl` created by running the following command:
endif::aws-sts,azure-workload-id[]
+
[source,terminal,subs="attributes+"]
----
$ ccoctl {cp-name} delete \
  --name=<name> \// <1>
ifdef::aws-sts[  --region=<{cp-name}_region> <2>]
ifdef::gcp-workload-id[]
  --project=<{cp-name}_project_id> \// <2>
  --credentials-requests-dir=<path_to_credentials_requests_directory>
endif::gcp-workload-id[]
ifdef::azure-workload-id[]
  --region=<{cp-name}_region> \// <2>
  --subscription-id=<{cp-name}_subscription_id> \// <3>
  --delete-oidc-resource-group
endif::azure-workload-id[]
----
+
<1> `<name>` matches the name that was originally used to create and tag the cloud resources.
ifdef::aws-sts,azure-workload-id[<2> `<{cp-name}_region>` is the {cp} region in which to delete cloud resources.]
ifdef::gcp-workload-id[<2> `<{cp-name}_project_id>` is the {cp} project ID in which to delete cloud resources.]
ifdef::azure-workload-id[<3> `<{cp-name}_subscription_id>` is the {cp} subscription ID for which to delete cloud resources.]
ifdef::aws-sts[]
+
.Example output
[source,text]
----
2021/04/08 17:50:41 Identity Provider object .well-known/openid-configuration deleted from the bucket <name>-oidc
2021/04/08 17:50:42 Identity Provider object keys.json deleted from the bucket <name>-oidc
2021/04/08 17:50:43 Identity Provider bucket <name>-oidc deleted
2021/04/08 17:51:05 Policy <name>-openshift-cloud-credential-operator-cloud-credential-o associated with IAM Role <name>-openshift-cloud-credential-operator-cloud-credential-o deleted
2021/04/08 17:51:05 IAM Role <name>-openshift-cloud-credential-operator-cloud-credential-o deleted
2021/04/08 17:51:07 Policy <name>-openshift-cluster-csi-drivers-ebs-cloud-credentials associated with IAM Role <name>-openshift-cluster-csi-drivers-ebs-cloud-credentials deleted
2021/04/08 17:51:07 IAM Role <name>-openshift-cluster-csi-drivers-ebs-cloud-credentials deleted
2021/04/08 17:51:08 Policy <name>-openshift-image-registry-installer-cloud-credentials associated with IAM Role <name>-openshift-image-registry-installer-cloud-credentials deleted
2021/04/08 17:51:08 IAM Role <name>-openshift-image-registry-installer-cloud-credentials deleted
2021/04/08 17:51:09 Policy <name>-openshift-ingress-operator-cloud-credentials associated with IAM Role <name>-openshift-ingress-operator-cloud-credentials deleted
2021/04/08 17:51:10 IAM Role <name>-openshift-ingress-operator-cloud-credentials deleted
2021/04/08 17:51:11 Policy <name>-openshift-machine-api-aws-cloud-credentials associated with IAM Role <name>-openshift-machine-api-aws-cloud-credentials deleted
2021/04/08 17:51:11 IAM Role <name>-openshift-machine-api-aws-cloud-credentials deleted
2021/04/08 17:51:39 Identity Provider with ARN arn:aws:iam::<aws_account_id>:oidc-provider/<name>-oidc.s3.<aws_region>.amazonaws.com deleted
----
//Would love a GCP and Azure version of the above output.
endif::aws-sts[]

.Verification

* To verify that the resources are deleted, query {cp}. For more information, refer to {cp} documentation.

ifeval::["{context}" == "uninstall-cluster-aws"]
:!cp-first: Amazon Web Services
:!cp: AWS
:!aws-sts:
endif::[]
ifeval::["{context}" == "uninstalling-cluster-gcp"]
:!cp-first: Google Cloud Platform
:!cp: GCP
:!gcp-workload-id:
endif::[]
ifeval::["{context}" == "uninstall-cluster-azure"]
:!cp-first: Microsoft Azure
:!cp: Azure
:!azure-workload-id:
endif::[]