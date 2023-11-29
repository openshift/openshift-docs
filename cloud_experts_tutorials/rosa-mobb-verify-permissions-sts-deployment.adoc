:_mod-docs-content-type: ASSEMBLY
[id="rosa-mobb-verify-permissions-sts-deployment"]
= Tutorial: Verifying Permissions for a ROSA STS Deployment
include::_attributes/attributes-openshift-dedicated.adoc[]
:context: rosa-mobb-verify-permissions-sts-deployment

toc::[]

// ---
// date: '2022-10-04'
// title: "Verify Permissions for ROSA STS Deployment"
// authors:
//   - Tyler Stacey
//   - Kumudu Herath
// tags: ["AWS", "ROSA", "STS"]
// ---

To proceed with the deployment of a ROSA cluster, an account must support the required roles and permissions.
AWS Service Control Policies (SCPs) cannot block the API calls made by the installer or operator roles.

Details about the IAM resources required for an STS-enabled installation of ROSA can be found here: xref:../rosa_architecture/rosa-sts-about-iam-resources.adoc#rosa-sts-about-iam-resources[About IAM resources for ROSA clusters that use STS]

This guide is validated for ROSA v4.11.X.

== Prerequisites

* link:https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html[AWS CLI]
* xref:../cli_reference/rosa_cli/rosa-get-started-cli.adoc#rosa-get-started-cli[ROSA CLI] v1.2.6
* link:https://stedolan.github.io/jq/[jq CLI]
* link:https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_testing-policies.html[AWS role with required permissions]

[id="verify-ROSA-permissions_{context}"]
== Verifying ROSA permissions
To verify the permissions required for ROSA, we can run the script included in the following section without ever creating any AWS resources.

The script uses the `rosa`, `aws`, and `jq` CLI commands to create files in the working directory that will be used to verify permissions in the account connected to the current AWS configuration.

The AWS Policy Simulator is used to verify the permissions of each role policy against the API calls extracted by `jq`; results are then stored in a text file appended with `.results`.

This script is designed to verify the permissions for the current account and region.

[id="usage-instructions_{context}"]
== Usage Instructions

. To use the script, run the following commands in a `bash` terminal (the -p option defines a prefix for the roles):
+
[source,terminal]
----
$ mkdir scratch
$ cd scratch
$ cat << 'EOF' > verify-permissions.sh
#!/bin/bash
while getopts 'p:' OPTION; do
  case "$OPTION" in
    p)
      PREFIX="$OPTARG"
      ;;
    ?)
      echo "script usage: $(basename \$0) [-p PREFIX]" >&2
      exit 1
      ;;
  esac
done
shift "$(($OPTIND -1))"
rosa create account-roles --mode manual --prefix $PREFIX
INSTALLER_POLICY=$(cat sts_installer_permission_policy.json | jq )
CONTROL_PLANE_POLICY=$(cat sts_instance_controlplane_permission_policy.json | jq)
WORKER_POLICY=$(cat sts_instance_worker_permission_policy.json | jq)
SUPPORT_POLICY=$(cat sts_support_permission_policy.json | jq)
simulatePolicy () {
    outputFile="${2}.results"
    echo $2
    aws iam simulate-custom-policy --policy-input-list "$1" --action-names $(jq '.Statement | map(select(.Effect == "Allow"))[].Action | if type == "string" then . else .[] end' "$2" -r) --output text > $outputFile
}
simulatePolicy "$INSTALLER_POLICY" "sts_installer_permission_policy.json"
simulatePolicy "$CONTROL_PLANE_POLICY" "sts_instance_controlplane_permission_policy.json"
simulatePolicy "$WORKER_POLICY" "sts_instance_worker_permission_policy.json"
simulatePolicy "$SUPPORT_POLICY" "sts_support_permission_policy.json"
EOF
$ chmod +x verify-permissions.sh
$ ./verify-permissions.sh -p SimPolTest
----

. After the script completes, review each results file to ensure that none of the required API calls are blocked:
+
[source,terminal]
----
$ for file in $(ls *.results); do echo $file; cat $file; done
----
+
The output will look similar to the following:
+
[source,terminal]
----
sts_installer_permission_policy.json.results
EVALUATIONRESULTS       autoscaling:DescribeAutoScalingGroups   allowed *
MATCHEDSTATEMENTS       PolicyInputList.1       IAM Policy
ENDPOSITION     6       195
STARTPOSITION   17      3
EVALUATIONRESULTS       ec2:AllocateAddress     allowed *
MATCHEDSTATEMENTS       PolicyInputList.1       IAM Policy
ENDPOSITION     6       195
STARTPOSITION   17      3
EVALUATIONRESULTS       ec2:AssociateAddress    allowed *
MATCHEDSTATEMENTS       PolicyInputList.1       IAM Policy
...
----
+
[NOTE]
====
If any actions are blocked, review the error provided by AWS and consult with your Administrator to determine if SCPs are blocking the required API calls.
====