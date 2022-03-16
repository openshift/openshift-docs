// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-mode-sts.adoc
// * authentication/managing_cloud_provider_credentials/cco-mode-gcp-workload-identity.adoc

ifeval::["{context}" == "cco-mode-sts"]
:aws-sts:
endif::[]
ifeval::["{context}" == "cco-mode-gcp-workload-identity"]
:google-cloud-platform:
endif::[]

[id="sts-mode-installing-verifying_{context}"]
= Verifying the installation

. Connect to the {product-title} cluster.

. Verify that the cluster does not have `root` credentials:
+
ifdef::aws-sts[]
[source,terminal]
----
$ oc get secrets -n kube-system aws-creds
----
endif::aws-sts[]
ifdef::google-cloud-platform[]
[source,terminal]
----
$ oc get secrets -n kube-system gcp-credentials
----
endif::google-cloud-platform[]
+
The output should look similar to:
+
ifdef::aws-sts[]
[source,terminal]
----
Error from server (NotFound): secrets "aws-creds" not found
----
endif::aws-sts[]
ifdef::google-cloud-platform[]
[source,terminal]
----
Error from server (NotFound): secrets "gcp-credentials" not found
----
endif::google-cloud-platform[]

. Verify that the components are assuming the
ifdef::aws-sts[]
IAM roles
endif::aws-sts[]
ifdef::google-cloud-platform[]
service accounts
endif::google-cloud-platform[]
that are specified in the secret manifests, instead of using credentials that are created by the CCO:
+
.Example command with the Image Registry Operator
ifdef::aws-sts[]
[source,terminal]
----
$ oc get secrets -n openshift-image-registry installer-cloud-credentials -o json | jq -r .data.credentials | base64 --decode
----
endif::aws-sts[]
ifdef::google-cloud-platform[]
[source,terminal]
----
$ oc get secrets -n openshift-image-registry installer-cloud-credentials -o json | jq -r '.data."service_account.json"' | base64 -d
----
endif::google-cloud-platform[]
+
The output should show the role and web identity token that are used by the component and look similar to:
+
.Example output with the Image Registry Operator
ifdef::aws-sts[]
[source,terminal]
----
[default]
role_arn = arn:aws:iam::123456789:role/openshift-image-registry-installer-cloud-credentials
web_identity_token_file = /var/run/secrets/openshift/serviceaccount/token
----
endif::aws-sts[]
ifdef::google-cloud-platform[]
[source,json]
----
{
   "type": "external_account", <1>
   "audience": "//iam.googleapis.com/projects/123456789/locations/global/workloadIdentityPools/test-pool/providers/test-provider",
   "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
   "token_url": "https://sts.googleapis.com/v1/token",
   "service_account_impersonation_url": "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/<client-email-address>:generateAccessToken", <2>
   "credential_source": {
      "file": "/var/run/secrets/openshift/serviceaccount/token",
      "format": {
         "type": "text"
      }
   }
}
----
<1> The credential type is `external_account`.
<2> The resource URL of the service account used by the Image Registry Operator.
endif::google-cloud-platform[]

ifeval::["{context}" == "cco-mode-sts"]
:!aws-sts:
endif::[]
ifeval::["{context}" == "cco-mode-gcp-workload-identity"]
:!google-cloud-platform:
endif::[]
