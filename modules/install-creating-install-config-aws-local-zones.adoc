// Module included in the following assemblies:
// * installing/installing_aws/installing-aws-localzone.adoc

:_mod-docs-content-type: PROCEDURE
[id="install-creating-install-config-aws-local-zones_{context}"]
= Modifying an installation configuration file to use AWS Local Zones

Modify an `install-config.yaml` file to include AWS Local Zones.

.Prerequisites

* You have configured an AWS account.
* You added your AWS keys and region to your local AWS profile by running `aws configure`.
* You have read the configuration limitations that apply when you specify the installation program to automatically create subnets for your {product-title} cluster. See the section named "Cluster limitations in AWS Local Zones".
* You opted in to the Local Zone group for each zone.
* You created an `install-config.yaml` file by using the procedure "Creating the installation configuration file".

.Procedure

. Modify the `install-config.yaml` file by specifying Local Zone names in the `platform.aws.zones` property of the edge compute pool. For example:
+
[source,yaml]
----
...
platform:
  aws:
    region: <region_name> <1>
compute:
- name: edge
  platform:
    aws:
      zones: <2>
      - <local_zone_name>
#...
----
<1> The AWS Region name.
<2> The list of Local Zone names that must belong in the same AWS Region.
+
.Example of a configuration to install a cluster in the `us-west-2` AWS Region that extends edge nodes to Local Zones in `Los Angeles` and `Las Vegas` locations.
+
[source,yaml]
----
apiVersion: v1
baseDomain: example.com
metadata:
  name: cluster-name
platform:
  aws:
    region: us-west-2
compute:
- name: edge
  platform:
    aws:
      zones:
      - us-west-2-lax-1a
      - us-west-2-lax-1b
      - us-west-2-las-1a
pullSecret: '{"auths": ...}'
sshKey: 'ssh-ed25519 AAAA...'
#...
----

. Deploy your cluster.
