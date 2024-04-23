:_mod-docs-content-type: ASSEMBLY
[id="cloud-experts-dynamic-certificate-custom-domain"]
= Tutorial: Dynamically issuing certificates using the cert-manager Operator on ROSA
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: cloud-experts-dynamic-certificate-custom-domain

toc::[]

//Mobb content metadata
//Brought into ROSA product docs 2023-09-20
//---
//date: '2022-10-11'
//title: Dynamic Certificates for ROSA Custom Domain
//weight: 1
//tags: ["AWS", "ROSA"]
//authors:
//   Kevin Collins
//---

While wildcard certificates provide simplicity by securing all first-level subdomains of a given domain with a single certificate, other use cases can require the use of individual certificates per domain.

Learn how to use the link:https://docs.openshift.com/container-platform/latest/security/cert_manager_operator/index.html[cert-manager Operator for Red Hat OpenShift] and link:https://letsencrypt.org/[Let's Encrypt] to dynamically issue certificates for routes created using a custom domain.

[id="cloud-experts-dynamic-certificate-custom-domain-prerequisites"]
== Prerequisites

* A ROSA cluster
* A user account with `cluster-admin` privileges
* The OpenShift CLI (`oc`)
* The Amazon Web Services (AWS) CLI (`aws`)
* A unique domain, such as `*.apps.<company_name>.io`
* An Amazon Route 53 public hosted zone for the above domain

[id="cloud-experts-dynamic-certificate-custom-domain-environment-setup"]
== Setting up your environment

. Configure the following environment variables:
+
[source,terminal]
----
$ export DOMAIN=apps.<company_name>.io <1>
$ export EMAIL=<youremail@company_name.io> <2>
$ export AWS_PAGER=""
$ export CLUSTER_NAME=$(oc get infrastructure cluster -o=jsonpath="{.status.infrastructureName}"  | sed 's/-[a-z0-9]\{5\}$//')
$ export OIDC_ENDPOINT=$(oc get authentication.config.openshift.io cluster -o json | jq -r .spec.serviceAccountIssuer | sed  's|^https://||')
$ export REGION=$(oc get infrastructure cluster -o=jsonpath="{.status.platformStatus.aws.region}")
$ export AWS_ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
$ export SCRATCH="/tmp/${CLUSTER_NAME}/dynamic-certs"
$ mkdir -p ${SCRATCH}
----
<1> The custom domain.
<2> The e-mail Let's Encrypt will use to send notifications about your certificates.
. Ensure all fields output correctly before moving to the next section:
+
[source,terminal]
----
$ echo "Cluster: ${CLUSTER_NAME}, Region: ${REGION}, OIDC Endpoint: ${OIDC_ENDPOINT}, AWS Account ID: ${AWS_ACCOUNT_ID}"
----

[id="cloud-experts-dynamic-certificate-prep-aws"]
== Preparing your AWS account

When cert-manager requests a certificate from Let’s Encrypt (or another ACME certificate issuer), Let's Encrypt servers validate that you control the domain name in that certificate using _challenges_. For this tutorial, you are using a link:https://letsencrypt.org/docs/challenge-types/#dns-01-challenge[DNS-01 challenge] that proves that you control the DNS for your domain name by putting a specific value in a TXT record under that domain name. This is all done automatically by cert-manager. To allow cert-manager permission to modify the Amazon Route 53 public hosted zone for your domain, you need to create an Identity Access Management (IAM) role with specific policy permissions and a trust relationship to allow access to the pod.

The public hosted zone that is used in this tutorial is in the same AWS account as the ROSA cluster. If your public hosted zone is in a different account, a few additional steps for link:https://cert-manager.io/docs/configuration/acme/dns01/route53/#cross-account-access[Cross Account Access] are required.

. Retrieve the Amazon Route 53 public hosted zone ID:
+
[NOTE]
====
This command looks for a public hosted zone that matches the custom domain you specified earlier as the `DOMAIN` environment variable. You can manually specify the Amazon Route 53 public hosted zone by running `export ZONE_ID=<zone_ID>`, replacing `<zone_ID>` with your specific Amazon Route 53 public hosted zone ID.
====
+
[source,terminal]
----
$ export ZONE_ID=$(aws route53 list-hosted-zones-by-name --output json \
  --dns-name "${DOMAIN}." --query 'HostedZones[0]'.Id --out text | sed 's/\/hostedzone\///')
----
+
. Create an AWS IAM policy document for the `cert-manager` Operator that provides the ability to update _only_ the specified public hosted zone:
+
[source,terminal]
----
$ cat <<EOF > "${SCRATCH}/cert-manager-policy.json"
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "route53:GetChange",
      "Resource": "arn:aws:route53:::change/*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "route53:ChangeResourceRecordSets",
        "route53:ListResourceRecordSets"
      ],
      "Resource": "arn:aws:route53:::hostedzone/${ZONE_ID}"
    },
    {
      "Effect": "Allow",
      "Action": "route53:ListHostedZonesByName",
      "Resource": "*"
    }
  ]
}
EOF
----
+
. Create the IAM policy using the file you created in the previous step:
+
[source,terminal]
----
$ POLICY_ARN=$(aws iam create-policy --policy-name "${CLUSTER_NAME}-cert-manager-policy" \
  --policy-document file://${SCRATCH}/cert-manager-policy.json \
  --query 'Policy.Arn' --output text)
----
. Create an AWS IAM trust policy for the `cert-manager` Operator:
+
[source,terminal]
----
$ cat <<EOF > "${SCRATCH}/trust-policy.json"
{
 "Version": "2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Condition": {
   "StringEquals" : {
     "${OIDC_ENDPOINT}:sub": "system:serviceaccount:cert-manager:cert-manager"
   }
 },
 "Principal": {
   "Federated": "arn:aws:iam::$AWS_ACCOUNT_ID:oidc-provider/${OIDC_ENDPOINT}"
 },
 "Action": "sts:AssumeRoleWithWebIdentity"
 }
 ]
}
EOF
----
+
. Create an IAM role for the `cert-manager` Operator using the trust policy you created in the previous step:
+
[source,terminal]
----
$ ROLE_ARN=$(aws iam create-role --role-name "${CLUSTER_NAME}-cert-manager-operator" \
   --assume-role-policy-document "file://${SCRATCH}/trust-policy.json" \
   --query Role.Arn --output text)
----
+
. Attach the permissions policy to the role:
+
[source,terminal]
----
$ aws iam attach-role-policy --role-name "${CLUSTER_NAME}-cert-manager-operator" \
  --policy-arn ${POLICY_ARN}
----

[id="cloud-experts-dynamic-certificate-custom-domain-install-cert-man-op"]
== Installing the cert-manager Operator

. Create a project to install the `cert-manager` Operator into:
+
[source,terminal]
----
$ oc new-project cert-manager-operator
----
+
[IMPORTANT]
====
Do not attempt to use more than one `cert-manager` Operator in your cluster. If you have a community `cert-manager` Operator installed in your cluster, you must uninstall it before installing the `cert-manager` Operator for Red Hat OpenShift.
====
+
. Install the `cert-manager` Operator for Red Hat OpenShift:
+
[source,terminal]
----
$ cat << EOF | oc apply -f -
apiVersion: operators.coreos.com/v1
kind: OperatorGroup
metadata:
  name: openshift-cert-manager-operator-group
  namespace: cert-manager-operator
spec:
  targetNamespaces:
  - cert-manager-operator
---
apiVersion: operators.coreos.com/v1alpha1
kind: Subscription
metadata:
  name: openshift-cert-manager-operator
  namespace: cert-manager-operator
spec:
  channel: stable-v1
  installPlanApproval: Automatic
  name: openshift-cert-manager-operator
  source: redhat-operators
  sourceNamespace: openshift-marketplace
EOF
----
+
[NOTE]
====
It takes a few minutes for this Operator to install and complete its set up.
====
+
. Verify that the `cert-manager` Operator is running:
+
[source,terminal]
----
$ oc -n cert-manager-operator get pods
----
.Example output
+
[source,text]
----
NAME                                                        READY   STATUS    RESTARTS   AGE
cert-manager-operator-controller-manager-84b8799db5-gv8mx   2/2     Running   0          12s
----
+
. Annotate the service account used by the `cert-manager` pods with the AWS IAM role you created earlier:
+
[source,terminal]
----
$ oc -n cert-manager annotate serviceaccount cert-manager eks.amazonaws.com/role-arn=${ROLE_ARN}
----
+
. Restart the existing `cert-manager` controller pod by running the following command:
+
[source,terminal]
----
$ oc -n cert-manager delete pods -l app.kubernetes.io/name=cert-manager
----
+
. Patch the Operator's configuration to use external nameservers to prevent DNS-01 challenge resolution issues:
+
[source,terminal]
----
$ oc patch certmanager.operator.openshift.io/cluster --type merge \
  -p '{"spec":{"controllerConfig":{"overrideArgs":["--dns01-recursive-nameservers-only","--dns01-recursive-nameservers=1.1.1.1:53"]}}}'
----
+
. Create a `ClusterIssuer` resource to use Let's Encrypt by running the following command:
+
[source,terminal]
----
$ cat << EOF | oc apply -f -
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-production
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: ${EMAIL}
    # This key doesn't exist, cert-manager creates it
    privateKeySecretRef:
      name: prod-letsencrypt-issuer-account-key
    solvers:
    - dns01:
        route53:
         hostedZoneID: ${ZONE_ID}
         region: ${REGION}
         secretAccessKeySecretRef:
           name: ''
EOF
----
+
. Verify the `ClusterIssuer` resource is ready:
+
[source,terminal]
----
$ oc get clusterissuer.cert-manager.io/letsencrypt-production
----
+
.Example output
+
[source,text]
----
NAME                     READY   AGE
letsencrypt-production   True    47s
----

[id="cloud-experts-dynamic-certificate-custom-domain-create-cd-ingress-con"]
== Creating a custom domain Ingress Controller

. Create a new project:
+
[source,terminal]
----
$ oc new-project custom-domain-ingress
----
+
. Create and configure a certificate resource to provision a certificate for the custom domain Ingress Controller:
+
[NOTE]
====
The following example uses a single domain certificate. SAN and wildcard certificates are also supported.
====
+
[source,terminal]
----
$ cat << EOF | oc apply -f -
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: custom-domain-ingress-cert
  namespace: custom-domain-ingress
spec:
  secretName: custom-domain-ingress-cert-tls
  issuerRef:
     name: letsencrypt-production
     kind: ClusterIssuer
  commonName: "${DOMAIN}"
  dnsNames:
  - "${DOMAIN}"
EOF
----
+
. Verify the certificate has been issued:
+
[NOTE]
====
It takes a few minutes for this certificate to be issued by Let's Encrypt. If it takes longer than 5 minutes, run `oc -n custom-domain-ingress describe certificate.cert-manager.io/custom-domain-ingress-cert` to see any issues reported by cert-manager.
====
+
[source,terminal]
----
$ oc -n custom-domain-ingress get certificate.cert-manager.io/custom-domain-ingress-cert
----
+
.Example output
+
[source,text]
----
NAME                         READY   SECRET                           AGE
custom-domain-ingress-cert   True    custom-domain-ingress-cert-tls   9m53s
----
+
. Create a new `CustomDomain` custom resource (CR):
+
[source,terminal]
----
$ cat << EOF | oc apply -f -
apiVersion: managed.openshift.io/v1alpha1
kind: CustomDomain
metadata:
  name: custom-domain-ingress
spec:
  domain: ${DOMAIN}
  scope: External
  loadBalancerType: NLB
  certificate:
    name: custom-domain-ingress-cert-tls
    namespace: custom-domain-ingress
EOF
----
. Verify that your custom domain Ingress Controller has been deployed and has a `Ready` status:
+
[source,terminal]
----
$ oc get customdomains
----
+
.Example output
[source,terminal]
----
NAME                    ENDPOINT                                                               DOMAIN            STATUS
custom-domain-ingress   tfoxdx.custom-domain-ingress.cluster.1234.p1.openshiftapps.com         example.com       Ready
----
+
. Prepare a document with the necessary DNS changes to enable DNS resolution for your custom domain Ingress Controller:
+
[source,terminal]
----
$ INGRESS=$(oc get customdomain.managed.openshift.io/custom-domain-ingress --template={{.status.endpoint}})
$ cat << EOF > "${SCRATCH}/create-cname.json"
{
  "Comment":"Add CNAME to custom domain endpoint",
  "Changes":[{
      "Action":"CREATE",
      "ResourceRecordSet":{
        "Name": "*.${DOMAIN}",
      "Type":"CNAME",
      "TTL":30,
      "ResourceRecords":[{
        "Value": "${INGRESS}"
      }]
    }
  }]
}
EOF
----
+
. Submit your changes to Amazon Route 53 for propagation:
+
[source,terminal]
----
$ aws route53 change-resource-record-sets \
  --hosted-zone-id ${ZONE_ID} \
  --change-batch file://${SCRATCH}/create-cname.json
----
+
[NOTE]
====
While the wildcard CNAME record avoids the need to create a new record for every new application you deploy using the custom domain Ingress Controller, the certificate that each of these applications use *is not* a wildcard certificate.
====

[id="cloud-experts-dynamic-certificate-custom-domain-config-dynamic-cert"]
== Configuring dynamic certificates for custom domain routes

Now you can expose cluster applications on any first-level subdomains of the specified domain, but the connection will not be secured with a TLS certificate that matches the domain of the application. To ensure these cluster applications have valid certificates for each domain name, configure cert-manager to dynamically issue a certificate to every new route created under this domain.

. Create the necessary OpenShift resources cert-manager requires to manage certificates for OpenShift routes.
+
This step creates a new deployment (and therefore a pod) that specifically monitors annotated routes in the cluster. If the `issuer-kind` and `issuer-name` annotations are found in a new route, it requests the Issuer (ClusterIssuer in this case) for a new certificate that is unique to this route and which will honor the hostname that was specified while creating the route.
+
[NOTE]
====
If the cluster does not have access to GitHub, you can save the raw contents locally and run `oc apply -f localfilename.yaml -n cert-manager`.
====
+
[source,terminal]
----
$ oc -n cert-manager apply -f https://github.com/cert-manager/openshift-routes/releases/latest/download/cert-manager-openshift-routes.yaml
----
+
The following additional OpenShift resources are also created in this step:
+
* `ClusterRole` - grants permissions to watch and update the routes across the cluster
* `ServiceAccount` - uses permissions to run the newly created pod
* `ClusterRoleBinding` -  binds these two resources
+
. Ensure that the new `cert-manager-openshift-routes` pod is running successfully:
+
[source,terminal]
----
$ oc -n cert-manager get pods
----
+
.Example result
+
[source,terminal]
----
NAME                                             READY   STATUS    RESTARTS   AGE
cert-manager-866d8f788c-9kspc                    1/1     Running   0          4h21m
cert-manager-cainjector-6885c585bd-znws8         1/1     Running   0          4h41m
cert-manager-openshift-routes-75b6bb44cd-f8kd5   1/1     Running   0          6s
cert-manager-webhook-8498785dd9-bvfdf            1/1     Running   0          4h41m
----

[id="cloud-experts-dynamic-certificate-custom-domain-config-deploy-sample-app"]
== Deploying a sample application

Now that dynamic certificates are configured, you can deploy a sample application to confirm that certificates are provisioned and trusted when you expose a new route.

. Create a new project for your sample application:
+
[source,terminal]
----
$ oc new-project hello-world
----
+
. Deploy a hello world application:
+
[source,terminal]
----
$ oc -n hello-world new-app --image=docker.io/openshift/hello-openshift
----
+
. Create a route to expose the application from outside the cluster:
+
[source,terminal]
----
$ oc -n hello-world create route edge --service=hello-openshift hello-openshift-tls --hostname hello.${DOMAIN}
----
+
. Verify the certificate for the route is untrusted:
+
[source,terminal]
----
$ curl -I https://hello.${DOMAIN}
----
.Example output
+
[source,text]
----
curl: (60) SSL: no alternative certificate subject name matches target host name 'hello.example.com'
More details here: https://curl.se/docs/sslcerts.html

curl failed to verify the legitimacy of the server and therefore could not
establish a secure connection to it. To learn more about this situation and
how to fix it, please visit the web page mentioned above.
----
+
. Annotate the route to trigger cert-manager to provision a certificate for the custom domain:
+
[source,terminal]
----
$ oc -n hello-world annotate route hello-openshift-tls cert-manager.io/issuer-kind=ClusterIssuer cert-manager.io/issuer-name=letsencrypt-production
----
+
[NOTE]
====
It takes 2-3 minutes for the certificate to be created. The renewal of the certificate will automatically be managed by the `cert-manager` Operator as it approaches expiration.
====
. Verify the certificate for the route is now trusted:
+
[source,terminal]
----
$ curl -I https://hello.${DOMAIN}
----
+
.Example output
+
[source,terminal]
----
HTTP/2 200
date: Thu, 05 Oct 2023 23:45:33 GMT
content-length: 17
content-type: text/plain; charset=utf-8
set-cookie: 52e4465485b6fb4f8a1b1bed128d0f3b=68676068bb32d24f0f558f094ed8e4d7; path=/; HttpOnly; Secure; SameSite=None
cache-control: private
----

[id="cloud-experts-dynamic-certificate-custom-domain-troubleshoot"]
== Troubleshooting dynamic certificate provisioning
[NOTE]
====
The validation process usually takes 2-3 minutes to complete while creating certificates.
====

If annotating your route does not trigger certificate creation during the certificate create step, run `oc describe` against each of the `certificate`,`certificaterequest`,`order`, and `challenge` resources to view the events or reasons that can help identify the cause of the issue.

[source,terminal]
----
$ oc get certificate,certificaterequest,order,challenge
----

For troubleshooting, you can refer to this link:https://cert-manager.io/docs/faq/acme/[helpful guide in debugging certificates].

You can also use the link:https://cert-manager.io/docs/reference/cmctl/[cmctl] CLI tool for various certificate management activities, such as checking the status of certificates and testing renewals.
