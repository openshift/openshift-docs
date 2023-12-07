// Module included in the following assemblies:
//
// * post_installation_configuration/aws-compute-edge-tasks.adoc

:_mod-docs-content-type: PROCEDURE
[id="post-install-edge-aws-extend-machineset"]
= Creating a machine set manifest for an AWS Local Zones node

After you create subnets in AWS Local Zones, you can create a machine set manifest.

The installation program sets the following labels for the `edge` machine pools at cluster installation time:

* `machine.openshift.io/parent-zone-name: <value_of_ParentZoneName>`
* `machine.openshift.io/zone-group: <value_of_ZoneGroup>`
* `machine.openshift.io/zone-type: <value_of_ZoneType>`

The following procedure details how you can create a machine set configuraton that matches the `edge` compute pool configuration.

.Prerequisites

* You have created subnets in AWS Local Zones.

.Procedure

* Manually preserve `edge` machine pool labels when creating the machine set manifest by gathering the AWS API. To complete this action, enter the following command in your command-line interface (CLI):
+
[source,terminal]
----
$ aws ec2 describe-availability-zones --region <value_of_Region> \// <1>
    --query 'AvailabilityZones[].{
	ZoneName: ZoneName,
	ParentZoneName: ParentZoneName,
	GroupName: GroupName,
	ZoneType: ZoneType}' \
    --filters Name=zone-name,Values=<value_of_ZoneName> \// <2>
    --all-availability-zones
----
<1> For `<value_of_Region>`, specify the name of the region for the zone.
<2> For `<value_of_ZoneName>`, specify the name of the Local Zone.

.Example output for Local Zone `us-east-1-nyc-1a`
[source,terminal]
----
[
    {
        "ZoneName": "us-east-1-nyc-1a",
        "ParentZoneName": "us-east-1f",
        "GroupName": "us-east-1-nyc-1",
        "ZoneType": "local-zone"
    }
]
----
