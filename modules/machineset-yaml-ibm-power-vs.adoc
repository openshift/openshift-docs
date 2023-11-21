// Module included in the following assemblies:
//
// * machine_management/creating_machinesets/creating-machineset-ibm-power-vs.adoc

:_mod-docs-content-type: REFERENCE
[id="machineset-yaml-ibm-power-vs_{context}"]
= Sample YAML for a compute machine set custom resource on {ibm-power-server-title}

This sample YAML file defines a compute machine set that runs in a specified {ibm-power-server-name} zone in a region and creates nodes that are labeled with `node-role.kubernetes.io/<role>: ""`.

In this sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<role>` is the node label to add.

[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id> <1>
    machine.openshift.io/cluster-api-machine-role: <role> <2>
    machine.openshift.io/cluster-api-machine-type: <role> <2>
  name: <infrastructure_id>-<role>-<region> <3>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id> <1>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<region> <3>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id> <1>
        machine.openshift.io/cluster-api-machine-role: <role> <2>
        machine.openshift.io/cluster-api-machine-type: <role> <2>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<region> <3>
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/<role>: ""
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1
          credentialsSecret:
            name: powervs-credentials
          image:
            name: rhcos-<infrastructure_id> <4>
            type: Name
          keyPairName: <infrastructure_id>-key
          kind: PowerVSMachineProviderConfig
          memoryGiB: 32
          network:
            regex: ^DHCPSERVER[0-9a-z]{32}_Private$
            type: RegEx
          processorType: Shared
          processors: "0.5"
          serviceInstance:
            id: <ibm_power_vs_service_instance_id>
            type: ID <5>
          systemType: s922
          userDataSecret:
            name: <role>-user-data
----
<1> The infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI installed, you can obtain the infrastructure ID by running the following command:
+
[source,terminal]
----
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
----
<2> The node label to add.
<3> The infrastructure ID, node label, and region.
<4> The custom {op-system-first} image that was used for cluster installation.
<5> The infrastructure ID within your region to place machines on.
