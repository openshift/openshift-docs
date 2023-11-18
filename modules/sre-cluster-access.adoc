// Module included in the following assemblies:
//
// * rosa_architecture/rosa_policy_service_definition/rosa-sre-access.adoc
// * osd_architecture/osd_policy/osd-sre-access.adoc
// * authentication/assuming-an-aws-iam-role-for-a-service-account.adoc

:_mod-docs-content-type: CONCEPT
[id="sre-cluster-access_{context}"]
= SRE cluster access

SRE access to {product-title}
ifdef::openshift-rosa[]
(ROSA)
endif::openshift-rosa[]
clusters is controlled through several layers of required authentication, all of which are managed by strict company policy. All authentication attempts to access a cluster and changes made within a cluster are recorded within audit logs, along with the specific account identity of the SRE responsible for those actions. These audit logs help ensure that all changes made by SREs to a customer's cluster adhere to the strict policies and procedures that make up Red Hat's managed services guidelines.

The information presented below is an overview of the process an SRE must perform to access a customer's cluster.

** SRE requests a refreshed ID token from the Red Hat SSO (Cloud Services). This request is authenticated. The token is valid for fifteen minutes. After the token expires, you can refresh the token again and receive a new token. The ability to refresh to a new token is indefinite; however, the ability to refresh to a new token is revoked after 30 days of inactivity.

** SRE connects to the Red Hat VPN. The authentication to the VPN is completed by the Red Hat Corporate Identity and Access Management system (RH IAM). With RH IAM, SREs are multifactor and can be managed internally per organization by groups and existing onboarding and offboarding processes. After an SRE is authenticated and connected, the SRE can access the cloud services fleet management plane. Changes to the cloud services fleet management plane require many layers of approval and are maintained by strict company policy.

** After authorization is complete, the SRE logs into the fleet management plane and receives a service account token that the fleet management plane created. The token is valid for 15 minutes. After the token is no longer valid, it is deleted.

** With access granted to the fleet management plane, SRE uses various methods to access clusters, depending on network configuration.

*** Accessing a private or public cluster: Request is sent through a specific Network Load Balancer (NLB) by using an encrypted HTTP connection on port 6443.

*** Accessing a PrivateLink cluster: Request is sent to the Red Hat Transit Gateway, which then connects to a Red Hat VPC per region. The VPC that receives the request will be dependent on the target private cluster's region. Within the VPC, there is a private subnet that contains the PrivateLink endpoint to the customer's PrivateLink cluster.

ifdef::openshift-rosa[]
SREs access ROSA clusters through the web console or command line interface (CLI) tools. Authentication requires multi-factor authentication (MFA) with industry-standard requirements for password complexity and account lockouts. SREs must authenticate as individuals to ensure auditability. All authentication attempts are logged to a Security Information and Event Management (SIEM) system.

SREs access private clusters using an encrypted HTTP connection. Connections are permitted only from a secured Red Hat network using either an IP allowlist or a private cloud provider link.

.SRE access to ROSA clusters
image::267_OpenShift_on_AWS_Access_Networking_1222.png[]

[id="rosa-policy-privileged-access-control_{context}"]
== Privileged access controls in ROSA
SRE adheres to the principle of least privilege when accessing ROSA and AWS components. There are four basic categories of manual SRE access:

- SRE admin access through the Red Hat Portal with normal two-factor authentication and no privileged elevation.
- SRE admin access through the Red Hat corporate SSO with normal two-factor authentication and no privileged elevation.
- OpenShift elevation, which is a manual elevation using Red Hat SSO. Access is limited to 2 hours, is fully audited, and requires management approval.
- AWS access or elevation, which is a manual elevation for AWS console or CLI access. Access is limited to 60 minutes and is fully audited.

Each of these access types have different levels of access to components:

[cols= "4a,6a,5a,4a,3a",options="header"]

|===

| Component | Typical SRE admin access (Red Hat Portal) | Typical SRE admin access (Red Hat SSO) |OpenShift elevation | Cloud provider access or elevation

| {cluster-manager} | R/W | No access | No access | No access
| OpenShift console | No access | R/W | R/W | No access
| Node operating system | No access | A specific list of elevated OS and network permissions. | A specific list of elevated OS and network permissions. | No access
| AWS Console | No access | No access, but this is the account used to request cloud provider access. | No access | All cloud provider permissions using the SRE identity.

|===

[id="rosa-policy-sre-aws-infra-access_{context}"]
== SRE access to AWS accounts
Red Hat personnel do not access AWS accounts in the course of routine {product-title} operations. For emergency troubleshooting purposes, the SREs have well-defined and auditable procedures to access cloud infrastructure accounts.

SREs generate a short-lived AWS access token for a reserved role using the AWS Security Token Service (STS). Access to the STS token is audit-logged and traceable back to individual users. Both STS and non-STS clusters use the AWS STS service for SRE access. For non-STS clusters, the `BYOCAdminAccess` role has the `AdministratorAccess` IAM policy attached, and this role is used for administration. For STS clusters, the `ManagedOpenShift-Support-Role` has the `ManagedOpenShift-Support-Access` policy attached, and this role is used for administration.

[id="rosa-sre-sts-view-aws-account_{context}"]
== SRE STS view of AWS accounts

When SREs are on a VPN through two-factor authentication, they and Red Hat Support can assume the `ManagedOpenShift-Support-Role` in your AWS account. The `ManagedOpenShift-Support-Role` has all the permissions necessary for SREs to directly troubleshoot and manage AWS resources. Upon assumption of the `ManagedOpenShift-Support-Role`, SREs use a AWS Security Token Service (STS) to generate a unique, time-expiring URL to the customer's AWS web UI for their account. SREs can then perform multiple troubleshooting actions, which include:

* Viewing CloudTrail logs
* Shutting down a faulty EC2 Instance

All activities performed by SREs arrive from Red Hat IP addresses and are logged to CloudTrail to allow you to audit and review all activity. This role is only used in cases where access to AWS services is required to assist you. The majority of permissions are read-only. However, a select few permissions have more access, including the ability to reboot an instance or spin up a new instance. SRE access is limited to the policy permissions attached to the `ManagedOpenShift-Support-Role`.

For a full list of permissions, see sts_support_permission_policy.json in the link:https://docs.openshift.com/rosa/rosa_architecture/rosa-sts-about-iam-resources.html[About IAM resources for ROSA clusters that use STS] user guide.

[id="rosa-sre-access-privatelink-vpc.adoc_{context}"]
== SRE access through PrivateLink VPC endpoint service

PrivateLink VPC endpoint service is created as part of the ROSA cluster creation.

When you have a PrivateLink ROSA cluster, its Kubernetes API Server is exposed through a load balancer that can only be accessed from within the VPC by default. Red Hat site reliability engineering (SRE) can connect to this load balancer through a VPC Endpoint Service that has an associated VPC Endpoint in a Red Hat-owned AWS account. This endpoint service contains the name of the cluster, which is also in the ARN.

Under the *Allow principals* tab, a Red Hat-owned AWS account is listed. This specific user ensures that other entities cannot create VPC Endpoint connections to the PrivateLink cluster's Kubernetes API Server.

When Red Hat SREs access the API, this fleet management plane can connect to the internal API through the VPC endpoint service.
endif::openshift-rosa[]