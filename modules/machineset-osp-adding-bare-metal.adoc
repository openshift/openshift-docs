[id="machineset-osp-adding-bare-metal_{context}"]
= Adding bare-metal compute machines to a {rh-openstack} cluster
// TODO
// Mothballed
// Reintroduce when feature is available. 
You can add bare-metal compute machines to an {product-title} cluster after you deploy it
on {rh-openstack-first}. In this configuration, all machines are attached to an
existing, installer-provisioned network, and traffic between control plane and
compute machines is routed between subnets.

[NOTE]
====
Bare-metal compute machines are not supported on clusters that use Kuryr.
====

.Prerequisites

* The {rh-openstack} link:https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/bare_metal_provisioning/index[Bare Metal service (Ironic)] is enabled and accessible by using the {rh-openstack} Compute API.

* Bare metal is available as link:https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.1/html/bare_metal_provisioning/sect-configure#creating_the_bare_metal_flavor[an {rh-openstack} flavor].

* You deployed an {product-title} cluster on installer-provisioned infrastructure.

* Your {rh-openstack} cloud provider is configured to route traffic between the installer-created VM
subnet and the pre-existing bare metal subnet.

.Procedure
. Create a file called `baremetalMachineSet.yaml`, and then add the bare metal flavor to it:
+
FIXME: May require update before publication.
.A sample bare metal MachineSet file
[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: <node_role>
    machine.openshift.io/cluster-api-machine-type: <node_role>
  name: <infrastructure_id>-<node_role>
  namespace: openshift-machine-api
spec:
  replicas: <number_of_replicas>
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<node_role>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <node_role>
        machine.openshift.io/cluster-api-machine-type: <node_role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<node_role>
    spec:
      providerSpec:
        value:
          apiVersion: openstackproviderconfig.openshift.io/v1alpha1
          cloudName: openstack
          cloudsSecret:
            name: openstack-cloud-credentials
            namespace: openshift-machine-api
          flavor: <nova_flavor>
          image: <glance_image_name_or_location>
          kind: OpenstackProviderSpec
          networks:
          - filter: {}
            subnets:
            - filter:
                name: <subnet_name>
                tags: openshiftClusterID=<infrastructure_id>
          securityGroups:
          - filter: {}
            name: <infrastructure_id>-<node_role>
          serverMetadata:
            Name: <infrastructure_id>-<node_role>
            openshiftClusterID: <infrastructure_id>
          tags:
          - openshiftClusterID=<infrastructure_id>
          trunk: true
          userDataSecret:
            name: <node_role>-user-data
----

. On a command line, to create the MachineSet resource, type:
+
[source,terminal]
----
$ oc create -v baremetalMachineSet.yaml
----

You can now use bare-metal compute machines in your {product-title} cluster.
