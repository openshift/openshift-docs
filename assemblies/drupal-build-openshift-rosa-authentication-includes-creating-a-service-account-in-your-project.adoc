// Module included in the following assemblies:
//
// * authentication/assuming-an-aws-iam-role-for-a-service-account.adoc

:_mod-docs-content-type: PROCEDURE
[id="creating-a-service-account-in-your-project_{context}"]
= Creating a service account in your project

Add a service account in your user-defined project. Include an `eks.amazonaws.com/role-arn` annotation in the service account configuration that references the Amazon Resource Name (ARN) for the AWS Identity and Access Management (IAM) role that you want the service account to assume.

.Prerequisites

* You have created an AWS IAM role for your service account. For more information, see _Setting up an AWS IAM role for a service account_.
* You have access to a {product-title} with AWS Security Token Service (STS) cluster. Admin-level user privileges are not required.
* You have installed the OpenShift CLI (`oc`).

.Procedure

. In your {product-title} cluster, create a project:
+
[source,terminal]
----
$ oc new-project <project_name> <1>
----
<1> Replace `<project_name>` with the name of your project. The name must match the project name that you specified in your AWS IAM role configuration.
+
[NOTE]
====
You are automatically switched to the project when it is created.
====

. Create a file named `test-service-account.yaml` with the following service account configuration:
+
[source,yaml]
----
apiVersion: v1
kind: ServiceAccount
metadata:
  name: <service_account_name> <1>
  namespace: <project_name> <2>
  annotations:
    eks.amazonaws.com/role-arn: "<aws_iam_role_arn>" <3>
----
// Add these annotations in the preceding code block later:
//    eks.amazonaws.com/sts-regional-endpoints: "true" <4>
//    eks.amazonaws.com/token-expiration: "86400" <5>
<1> Replace `<service_account_name>` with the name of your service account. The name must match the service account name that you specified in your AWS IAM role configuration.
<2> Replace `<project_name>` with the name of your project. The name must match the project name that you specified in your AWS IAM role configuration.
<3> Specifies the ARN of the AWS IAM role that the service account assumes for use within your pod. Replace `<aws_iam_role_arn>` with the ARN for the AWS IAM role that you created for your service account. The format of the role ARN is `arn:aws:iam::<aws_account_id>:role/<aws_iam_role_name>`.
// Add these call outs when the additional annotations are added later:
//<4> Optional: When set to `true`, the `AWS_STS_REGIONAL_ENDPOINTS=regional` environment variable is defined in the pod and AWS STS requests are sent to endpoints for the active region. When this option is not set to `true`, the AWS STS requests are by default sent to the global endpoint \https://sts.amazonaws.com. For more information, see link:https://docs.aws.amazon.com/sdkref/latest/guide/feature-sts-regionalized-endpoints.html[AWS STS Regionalized endpoints] in the AWS documentation.
//<5> Optional: Specifies the token expiration time in seconds. The default is `86400`.

. Create the service account in your project:
+
[source,terminal]
----
$ oc create -f test-service-account.yaml
----
+
.Example output:
[source,terminal]
----
serviceaccount/<service_account_name> created
----

. Review the details of the service account:
+
[source,terminal]
----
$ oc describe serviceaccount <service_account_name> <1>
----
<1> Replace `<service_account_name>` with the name of your service account.
+
.Example output:
+
[source,terminal]
----
Name:                <service_account_name> <1>
Namespace:           <project_name> <2>
Labels:              <none>
Annotations:         eks.amazonaws.com/role-arn: <aws_iam_role_arn> <3>
Image pull secrets:  <service_account_name>-dockercfg-rnjkq
Mountable secrets:   <service_account_name>-dockercfg-rnjkq
Tokens:              <service_account_name>-token-4gbjp
Events:              <none>
----
// Add these annotations in the preceding code block later:
//                     eks.amazonaws.com/sts-regional-endpoints: true <3>
//                     eks.amazonaws.com/token-expiration: 86400 <3>
<1> Specifies the name of the service account.
<2> Specifies the project that contains the service account.
<3> Lists the annotation for the ARN of the AWS IAM role that the service account assumes.
// Update the preceding call out to the following when the additional annotations are added later:
//<3> Lists the annotations for the ARN of the AWS IAM role that the service account assumes, the optional regional endpoint configuration, and the optional token expiration specification.
