// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-short-term-creds.adoc

:_mod-docs-content-type: REFERENCE
[id="cco-short-term-creds-format-aws_{context}"]
= AWS component secret formats

Using manual mode with the AWS Security Token Service (STS) changes the content of the AWS credentials that are provided to individual {product-title} components. Compare the following secret formats:

.AWS secret format using long-term credentials

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  namespace: <target_namespace> <1>
  name: <target_secret_name> <2>
data:
  aws_access_key_id: <base64_encoded_access_key_id>
  aws_secret_access_key: <base64_encoded_secret_access_key>
----
<1> The namespace for the component.
<2> The name of the component secret.

.AWS secret format using AWS STS

[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  namespace: <target_namespace> <1>
  name: <target_secret_name> <2>
stringData:
  credentials: |-
    [default]
    sts_regional_endpoints = regional
    role_name: <operator_role_name> <3>
    web_identity_token_file: <path_to_token> <4>
----
<1> The namespace for the component.
<2> The name of the component secret.
<3> The IAM role for the component.
<4> The path to the service account token inside the pod. By convention, this is `/var/run/secrets/openshift/serviceaccount/token` for {product-title} components.