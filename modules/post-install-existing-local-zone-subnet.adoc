// Module included in the following assemblies:
//
// * post_installation_configuration/aws-compute-edge-tasks.adoc

:_mod-docs-content-type: CONCEPT
[id="post-install-existing-local-zone-subnet_{context}"]
= Extend existing clusters to use AWS Local Zones

If you want a Machine API to create an Amazon EC2 instance in a remote zone location, you must create a subnet in a Local Zone location. You can use any provisioning tool, such as Ansible or Terraform, to create subnets in the existing Virtual Private Cloud (VPC). You can configure the CloudFormation template to meet your requirements.

The following subsections include steps that use CloudFormation templates. Considering the limitation of NAT Gateways in AWS Local Zones, CloudFormation templates support only public subnets. You can reuse the template to create public subnets for each edge location to where you need to extend your cluster.