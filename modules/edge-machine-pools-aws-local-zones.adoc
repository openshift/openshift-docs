// Module included in the following assemblies:
// * installing/installing_aws/installing-aws-localzone.adoc
// * post_installation_configuration/aws-compute-edge-tasks.adoc

ifeval::["{context}" == "aws-compute-edge-tasks"]
:edge:
endif::[]

:_mod-docs-content-type: CONCEPT
[id="edge-machine-pools-aws-local-zones_{context}"]
= Edge compute pools and AWS Local Zones

Edge worker nodes are tainted worker nodes that run in AWS Local Zones locations.

When deploying a cluster that uses Local Zones, consider the following points:

* Amazon EC2 instances in the Local Zones are more expensive than Amazon EC2 instances in the Availability Zones.
* Latency between applications and end users is lower in Local Zones, and latency might vary by location. A latency impact exists for some workloads if, for example, ingress traffic is mixed between Local Zones and Availability Zones.

[IMPORTANT]
====
Generally, the maximum transmission unit (MTU) between an Amazon EC2 instance in a Local Zone and an Amazon EC2 instance in the Region is 1300. For more information, see link:https://docs.aws.amazon.com/local-zones/latest/ug/how-local-zones-work.html[How Local Zones work] in the AWS documentation.
The cluster network MTU must be always less than the EC2 MTU to account for the overhead. The specific overhead is determined by the network plugin, for example:

- OVN-Kubernetes: `100 bytes`
- OpenShift SDN: `50 bytes`

The network plugin can provide additional features, like IPsec, that also must be decreased the MTU. For additional information, see the documentation.
====

{product-title} 4.12 introduced a new compute pool, _edge_, that is designed for use in remote zones. The edge compute pool configuration is common between AWS Local Zones locations. Because of the type and size limitations of resources like EC2 and EBS on Local Zone resources, the default instance type can vary from the traditional worker pool.

The default Elastic Block Store (EBS) for Local Zone locations is `gp2`, which differs from the regular worker pool. The instance type used for each Local Zone on edge compute pool also might differ from worker pools, depending on the instance offerings on the zone.

The edge compute pool creates new labels that developers can use to deploy applications onto AWS Local Zones nodes. The new labels are:

* `node-role.kubernetes.io/edge=''`
* `machine.openshift.io/zone-type=local-zone`
* `machine.openshift.io/zone-group=$ZONE_GROUP_NAME`

////
By default, the system creates the edge compute pool manifests only if users add AWS Local Zones subnet IDs to the list `platform.aws.subnets`.
////

By default, the machine sets for the edge compute pool defines the taint of `NoSchedule` to prevent regular workloads from spreading on Local Zone instances. Users can only run user workloads if they define tolerations in the pod specification.

ifndef::edge[]
The following examples show `install-config.yaml` files that use the edge machine pool.

.Configuration that uses an edge pool with a custom instance type
[source,yaml]
----
apiVersion: v1
baseDomain: devcluster.openshift.com
metadata:
  name: ipi-localzone
compute:
- name: edge
  platform:
    aws:
      type: m5.4xlarge
platform:
  aws:
    region: us-west-2
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
----

Instance types differ between locations. To verify availability in the Local Zone in which the cluster runs, see the AWS documentation.

.Configuration that uses an edge pool with a custom EBS type
[source,yaml]
----
apiVersion: v1
baseDomain: devcluster.openshift.com
metadata:
  name: ipi-localzone
compute:
- name: edge
  platform:
    aws:
      rootVolume:
        type: gp3
        size: 120
platform:
  aws:
    region: us-west-2
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
----

EBS types differ between locations. Check the AWS documentation to verify availability in the Local Zone in which the cluster runs.

.Configuration that uses an edge pool with custom security groups
[source,yaml]
----
apiVersion: v1
baseDomain: devcluster.openshift.com
metadata:
  name: ipi-localzone
compute:
- name: edge
  platform:
    aws:
      additionalSecurityGroupIDs:
        - sg-1 <1>
        - sg-2
platform:
  aws:
    region: us-west-2
pullSecret: '{"auths": ...}'
sshKey: ssh-ed25519 AAAA...
----
<1> Specify the name of the security group as it appears in the Amazon EC2 console, including the `sg` prefix.
endif::edge[]

ifeval::["{context}" == "aws-compute-edge-tasks"]
:!edge:
endif::[]
