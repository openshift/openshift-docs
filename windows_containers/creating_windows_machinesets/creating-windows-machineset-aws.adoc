:_mod-docs-content-type: ASSEMBLY
[id="creating-windows-machineset-aws"]
= Creating a Windows machine set on AWS
include::_attributes/common-attributes.adoc[]
:context: creating-windows-machineset-aws

toc::[]

You can create a Windows `MachineSet` object to serve a specific purpose in your {product-title} cluster on Amazon Web Services (AWS). For example, you might create infrastructure Windows machine sets and related machines so that you can move supporting Windows workloads to the new Windows machines.

[discrete]
== Prerequisites

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You are using a supported Windows Server as the operating system image.
+
Use one of the following `aws` commands, as appropriate for your Windows Server release, to query valid AMI images:
+
.Example Windows Server 2022 command
+
[source,terminal]
----
$ aws ec2 describe-images --region <aws_region_name> --filters "Name=name,Values=Windows_Server-2022*English*Core*Base*" "Name=is-public,Values=true" --query "reverse(sort_by(Images, &CreationDate))[*].{name: Name, id: ImageId}" --output table
----
+
.Example Windows Server 2019 command
+
[source,terminal]
----
$ aws ec2 describe-images --region <aws_region_name> --filters "Name=name,Values=Windows_Server-2019*English*Core*Base*" "Name=is-public,Values=true" --query "reverse(sort_by(Images, &CreationDate))[*].{name: Name, id: ImageId}" --output table
----
+
--
where:

<aws_region_name>:: Specifies the name of your AWS region.
--

include::modules/machine-api-overview.adoc[leveloffset=+1]
include::modules/windows-machineset-aws.adoc[leveloffset=+1]
include::modules/machineset-creating.adoc[leveloffset=+1]

[role="_additional-resources"]
== Additional resources

* xref:../../machine_management/index.adoc#overview-of-machine-management[Overview of machine management]
