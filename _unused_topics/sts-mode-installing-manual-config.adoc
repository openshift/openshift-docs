// Module included in the following assemblies:
//
// * authentication/managing_cloud_provider_credentials/cco-mode-sts.adoc

[id="sts-mode-installing-manual-config_{context}"]
= Creating AWS resources manually

To install an {product-title} cluster that is configured to use the CCO in manual mode with STS, you must first manually create the required AWS resources.

.Procedure

. Generate a private key to sign the `ServiceAccount` object:
+
[source,terminal]
----
$ openssl genrsa -out sa-signer 4096
----

. Generate a `ServiceAccount` object public key:
+
[source,terminal]
----
$ openssl rsa -in sa-signer -pubout -out sa-signer.pub
----

. Create an S3 bucket to hold the OIDC configuration:
+
[source,terminal]
----
$ aws s3api create-bucket --bucket <oidc_bucket_name> --region <aws_region> --create-bucket-configuration LocationConstraint=<aws_region>
----
+
[NOTE]
====
If the value of `<aws_region>` is `us-east-1`, do not specify the `LocationConstraint` parameter.
====

. Retain the S3 bucket URL:
+
[source,terminal]
----
OPENID_BUCKET_URL="https://<oidc_bucket_name>.s3.<aws_region>.amazonaws.com"
----

. Build an OIDC configuration:

.. Create a file named `keys.json` that contains the following information:
+
[source,json]
----
{
    "keys": [
        {
            "use": "sig",
            "kty": "RSA",
            "kid": "<public_signing_key_id>",
            "alg": "RS256",
            "n": "<public_signing_key_modulus>",
            "e": "<public_signing_key_exponent>"
        }
    ]
}
----
+
where:

*** `<public_signing_key_id>` is generated from the public key with:
+
[source,terminal]
----
$ openssl rsa -in sa-signer.pub -pubin --outform DER | openssl dgst -binary -sha256 | openssl base64 | tr '/+' '_-' | tr -d '='
----
+
This command converts the public key to DER format, performs a SHA-256 checksum on the binary representation, encodes the data with base64 encoding, and then changes the base64-encoded output to base64URL encoding.

*** `<public_signing_key_modulus>` is generated from the public key with:
+
[source,terminal]
----
$ openssl rsa -pubin -in sa-signer.pub -modulus -noout | sed  -e 's/Modulus=//' | xxd -r -p | base64 -w0 | tr '/+' '_-' | tr -d '='
----
+
This command prints the modulus of the public key, extracts the hex representation of the modulus, converts the ASCII hex to binary, encodes the data with base64 encoding, and then changes the base64-encoded output to base64URL encoding.

*** `<public_signing_key_exponent>` is generated from the public key with:
+
[source,terminal]
----
$ printf "%016x" $(openssl rsa -pubin -in sa-signer.pub -noout -text | grep Exponent | awk '{ print $2 }') |  awk '{ sub(/(00)+/, "", $1); print $1 }' | xxd -r -p | base64 -w0 | tr '/+' '_-' | tr -d '='
----
+
This command extracts the decimal representation of the public key exponent, prints it as hex with a padded `0` if needed, removes leading `00` pairs, converts the ASCII hex to binary, encodes the data with base64 encoding, and then changes the base64-encoded output to use only characters that can be used in a URL.

.. Create a file named `openid-configuration` that contains the following information:
+
[source,json]
----
{
	"issuer": "$OPENID_BUCKET_URL",
	"jwks_uri": "${OPENID_BUCKET_URL}/keys.json",
    "response_types_supported": [
        "id_token"
    ],
    "subject_types_supported": [
        "public"
    ],
    "id_token_signing_alg_values_supported": [
        "RS256"
    ],
    "claims_supported": [
        "aud",
        "exp",
        "sub",
        "iat",
        "iss",
        "sub"
    ]
}
----

. Upload the OIDC configuration:
+
[source,terminal]
----
$ aws s3api put-object --bucket <oidc_bucket_name> --key keys.json --body ./keys.json
----
+
[source,terminal]
----
$ aws s3api put-object --bucket <oidc_bucket_name> --key '.well-known/openid-configuration' --body ./openid-configuration
----
+
Where `<oidc_bucket_name>` is the S3 bucket that was created to hold the OIDC configuration.

. Allow the AWS IAM OpenID Connect (OIDC) identity provider to read these files:
+
[source,terminal]
----
$ aws s3api put-object-acl --bucket <oidc_bucket_name> --key keys.json --acl public-read
----
+
[source,terminal]
----
$ aws s3api put-object-acl --bucket <oidc_bucket_name> --key '.well-known/openid-configuration' --acl public-read
----

. Create an AWS IAM OIDC identity provider:

.. Get the certificate chain from the server that hosts the OIDC configuration:
+
[source,terminal]
----
$ echo | openssl s_client -servername $<oidc_bucket_name>.s3.$<aws_region>.amazonaws.com -connect $<oidc_bucket_name>.s3.$<aws_region>.amazonaws.com:443 -showcerts 2>/dev/null | awk '/BEGIN/,/END/{ if(/BEGIN/){a++}; out="cert"a".pem"; print >out}'
----

.. Calculate the fingerprint for the certificate at the root of the chain:
+
[source,terminal]
----
$ export BUCKET_FINGERPRINT=$(openssl x509 -in cert<number>.pem -fingerprint -noout | sed -e 's/.*Fingerprint=//' -e 's/://g')
----
+
Where `<number>` is the highest number in the files that were saved. For example, if `2` is the highest number in the files that were saved, use `cert2.pem`.

.. Create the identity provider:
+
[source,terminal]
----
$ aws iam create-open-id-connect-provider --url $OPENID_BUCKET_URL --thumbprint-list $BUCKET_FINGERPRINT --client-id-list openshift sts.amazonaws.com
----

.. Retain the returned ARN of the newly created identity provider. This ARN is later referred to as `<aws_iam_openid_arn>`.

. Generate IAM roles:

.. Locate all `CredentialsRequest` CRs in this release image that target the cloud you are deploying on:
+
[source,terminal]
----
$ oc adm release extract quay.io/openshift-release-dev/ocp-release:4.<y>.<z>-x86_64 --credentials-requests --cloud=aws
----
+
Where `<y>` and `<z>` are the numbers corresponding to the version of {product-title} you are installing.

.. For each `CredentialsRequest` CR, create an IAM role of type `Web identity` using the previously created IAM Identity Provider that grants the necessary permissions and establishes a trust relationship that trusts the  identity provider previously created.
+
For example, for the openshift-machine-api-operator `CredentialsRequest` CR in `0000_30_machine-api-operator_00_credentials-request.yaml`, create an IAM role that allows an identity from the created OIDC provider created for the cluster, similar to the following:
+
[source,json]
----
{
    "Role": {
        "Path": "/",
        "RoleName": "openshift-machine-api-aws-cloud-credentials",
        "RoleId": "ARSOMEROLEID",
        "Arn": "arn:aws:iam::123456789012:role/openshift-machine-api-aws-cloud-credentials",
        "CreateDate": "2021-01-06T15:54:13Z",
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "Federated": "<aws_iam_openid_arn>"
                    },
                    "Action": "sts:AssumeRoleWithWebIdentity",
                    "Condition": {
                        "StringEquals": {
                            "<oidc_bucket_name>.s3.<aws_region>.amazonaws.com/$BUCKET_NAME:aud": "openshift"
                        }
                    }
                }
            ]
        },
        "Description": "OpenShift role for openshift-machine-api/aws-cloud-credentials",
        "MaxSessionDuration": 3600,
        "RoleLastUsed": {
            "LastUsedDate": "2021-02-03T02:51:24Z",
            "Region": "<aws_region>"
        }
    }
}
----
+
Where `<aws_iam_openid_arn>` is the returned ARN of the newly created identity provider.

.. To further restrict the role such that only specific cluster `ServiceAccount` objects can assume the role, modify the trust relationship of each role by updating the `.Role.AssumeRolePolicyDocument.Statement[].Condition` field to the specific `ServiceAccount` objects for each component.

*** Modify the trust relationship of the `cluster-image-registry-operator` role to have the following condition:
+
[source,json]
----
"Condition": {
  "StringEquals": {
    "<oidc_bucket_name>.s3.<aws_region>.amazonaws.com:sub": [
      "system:serviceaccount:openshift-image-registry:registry",
      "system:serviceaccount:openshift-image-registry:cluster-image-registry-operator"
    ]
  }
}
----

*** Modify the trust relationship of the `openshift-ingress-operator` to have the following condition:
+
[source,json]
----
"Condition": {
  "StringEquals": {
    "<oidc_bucket_name>.s3.<aws_region>.amazonaws.com:sub": [
      "system:serviceaccount:openshift-ingress-operator:ingress-operator"
    ]
  }
}
----

*** Modify the trust relationship of the `openshift-cluster-csi-drivers` to have the following condition:
+
[source,json]
----
"Condition": {
  "StringEquals": {
    "<oidc_bucket_name>.s3.<aws_region>.amazonaws.com:sub": [
      "system:serviceaccount:openshift-cluster-csi-drivers:aws-ebs-csi-driver-operator",
      "system:serviceaccount:openshift-cluster-csi-drivers:aws-ebs-csi-driver-controller-sa"
    ]
  }
}
----

*** Modify the trust relationship of the `openshift-machine-api` to have the following condition:
+
[source,json]
----
"Condition": {
  "StringEquals": {
    "<oidc_bucket_name>.s3.<aws_region>.amazonaws.com:sub": [
      "system:serviceaccount:openshift-machine-api:machine-api-controllers"
    ]
  }
}
----

. For each IAM role, attach an IAM policy to the role that reflects the required permissions from the corresponding `CredentialsRequest` objects.
+
For example, for `openshift-machine-api`, attach an IAM policy similar to the following:
+
[source,json]
----
{
    "RoleName": "openshift-machine-api-aws-cloud-credentials",
    "PolicyName": "openshift-machine-api-aws-cloud-credentials",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": [
                    "ec2:CreateTags",
                    "ec2:DescribeAvailabilityZones",
                    "ec2:DescribeDhcpOptions",
                    "ec2:DescribeImages",
                    "ec2:DescribeInstances",
                    "ec2:DescribeSecurityGroups",
                    "ec2:DescribeSubnets",
                    "ec2:DescribeVpcs",
                    "ec2:RunInstances",
                    "ec2:TerminateInstances",
                    "elasticloadbalancing:DescribeLoadBalancers",
                    "elasticloadbalancing:DescribeTargetGroups",
                    "elasticloadbalancing:RegisterInstancesWithLoadBalancer",
                    "elasticloadbalancing:RegisterTargets",
                    "iam:PassRole",
                    "iam:CreateServiceLinkedRole"
                ],
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "kms:Decrypt",
                    "kms:Encrypt",
                    "kms:GenerateDataKey",
                    "kms:GenerateDataKeyWithoutPlainText",
                    "kms:DescribeKey"
                ],
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "kms:RevokeGrant",
                    "kms:CreateGrant",
                    "kms:ListGrants"
                ],
                "Resource": "*",
                "Condition": {
                    "Bool": {
                        "kms:GrantIsForAWSResource": true
                    }
                }
            }
        ]
    }
}
----
. Prepare to run the {product-title} installer:

.. Create the `install-config.yaml` file:
+
[source,terminal]
----
$ ./openshift-install create install-config
----

.. Configure the cluster to install with the CCO in manual mode:
+
[source,terminal]
----
$ echo "credentialsMode: Manual" >> install-config.yaml
----

.. Create install manifests:
+
[source,terminal]
----
$ ./openshift-install create manifests
----

.. Create a `tls` directory, and copy the private key generated previously there:
+
[NOTE]
====
The target file name must be `./tls/bound-service-account-signing-key.key`.
====
+
[source,terminal]
----
$ mkdir tls ; cp <path_to_service_account_signer> ./tls/bound-service-account-signing-key.key
----

.. Create a custom `Authentication` CR with the file name `cluster-authentication-02-config.yaml`:
+
[source,terminal]
----
$ cat << EOF > manifests/cluster-authentication-02-config.yaml
apiVersion: config.openshift.io/v1
kind: Authentication
metadata:
  name: cluster
spec:
  serviceAccountIssuer: $OPENID_BUCKET_URL
EOF
----

.. For each `CredentialsRequest` CR that is extracted from the release image, create a secret with the target namespace and target name that is indicated in each `CredentialsRequest`, substituting the AWS IAM role ARN created previously for each component:
+
.Example secret manifest for `openshift-machine-api`:
+
[source,terminal]
----
$ cat manifests/openshift-machine-api-aws-cloud-credentials-credentials.yaml
apiVersion: v1
stringData:
  credentials: |-
    [default]
    role_arn = arn:aws:iam::123456789012:role/openshift-machine-api-aws-cloud-credentials
    web_identity_token_file = /var/run/secrets/openshift/serviceaccount/token
kind: Secret
metadata:
  name: aws-cloud-credentials
  namespace: openshift-machine-api
type: Opaque
----
