// Module included in the following assemblies:
//
// * networking/network-verification.adoc

:_mod-docs-content-type: PROCEDURE
[discrete]
[id="running-network-verification-manually-cli_{context}"]
= Running the network verification manually using the CLI

You can manually run the network verification checks for an existing {product-title} (ROSA) cluster by using the ROSA CLI (`rosa`).

When you run the network verification, you can specify a set of VPC subnet IDs or a cluster name.

.Prerequisites

* You have installed and configured the latest ROSA CLI (`rosa`) on your installation host.
* You have an existing ROSA cluster.
* You are the cluster owner or you have the cluster editor role.

.Procedure

* Verify the network configuration by using one of the following methods:
** Verify the network configuration by specifying the cluster name. The subnet IDs are automatically detected:
+
[source,terminal]
----
$ rosa verify network --cluster <cluster_name> <1>
----
<1> Replace `<cluster_name>` with the name of your cluster.
+
.Example output
[source,terminal]
----
I: Verifying the following subnet IDs are configured correctly: [subnet-03146b9b52b6024cb subnet-03146b9b52b2034cc]
I: subnet-03146b9b52b6024cb: pending
I: subnet-03146b9b52b2034cc: passed
I: Run the following command to wait for verification to all subnets to complete:
rosa verify network --watch --status-only --region us-east-1 --subnet-ids subnet-03146b9b52b6024cb,subnet-03146b9b52b2034cc
----
*** Ensure that verification to all subnets has been completed:
+
[source,terminal]
----
$ rosa verify network --watch \ <1>
                      --status-only \ <2>
                      --region <region_name> \ <3>
                      --subnet-ids subnet-03146b9b52b6024cb,subnet-03146b9b52b2034cc <4>
----
<1> The `watch` flag causes the command to complete after all the subnets under test are in a failed or passed state.
<2> The `status-only` flag does not trigger a run of network verification but returns the current state, for example, `subnet-123 (verification still in-progress)`. By default, without this option, a call to this command always triggers a verification of the specified subnets.
<3> Use a specific AWS region that overrides the _AWS_REGION_ environment variable.
<4> Enter a list of subnet IDs separated by commas to verify. If any of the subnets do not exist, the error message `Network verification for subnet 'subnet-<subnet_number> not found` displays and no subnets are checked.
+
.Example output
[source,terminal]
----
I: Checking the status of the following subnet IDs: [subnet-03146b9b52b6024cb subnet-03146b9b52b2034cc]
I: subnet-03146b9b52b6024cb: passed
I: subnet-03146b9b52b2034cc: passed
----
+
[TIP]
====
To output the full list of verification tests, you can include the `--debug` argument when you run the `rosa verify network` command.
====
+
** Verify the network configuration by specifying the VPC subnets IDs. Replace `<region_name>` with your AWS region and `<AWS_account_ID>` with your AWS account ID:
+
[source,terminal]
----
$ rosa verify network --subnet-ids 03146b9b52b6024cb,subnet-03146b9b52b2034cc --region <region_name> --role-arn arn:aws:iam::<AWS_account_ID>:role/my-Installer-Role
----
+
.Example output
[source,terminal]
----
I: Verifying the following subnet IDs are configured correctly: [subnet-03146b9b52b6024cb subnet-03146b9b52b2034cc]
I: subnet-03146b9b52b6024cb: pending
I: subnet-03146b9b52b2034cc: passed
I: Run the following command to wait for verification to all subnets to complete:
rosa verify network --watch --status-only --region us-east-1 --subnet-ids subnet-03146b9b52b6024cb,subnet-03146b9b52b2034cc
----
*** Ensure that verification to all subnets has been completed:
+
[source,terminal]
----
$ rosa verify network --watch --status-only --region us-east-1 --subnet-ids subnet-03146b9b52b6024cb,subnet-03146b9b52b2034cc
----
+
.Example output
[source,terminal]
----
I: Checking the status of the following subnet IDs: [subnet-03146b9b52b6024cb subnet-03146b9b52b2034cc]
I: subnet-03146b9b52b6024cb: passed
I: subnet-03146b9b52b2034cc: passed
----
