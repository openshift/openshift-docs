// Module included in the following assemblies:
//
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-azure.adoc

[id="windows-machineset-azure_{context}"]
= Sample YAML for a Windows MachineSet object on Azure

This sample YAML defines a Windows `MachineSet` object running on Microsoft Azure that the Windows Machine Config Operator (WMCO) can react upon.

[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id> <1>
  name: <windows_machine_set_name> <2>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id> <1>
      machine.openshift.io/cluster-api-machineset: <windows_machine_set_name> <2>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id> <1>
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: <windows_machine_set_name> <2>
        machine.openshift.io/os-id: Windows <3>
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/worker: "" <4>
      providerSpec:
        value:
          apiVersion: azureproviderconfig.openshift.io/v1beta1
          credentialsSecret:
            name: azure-cloud-credentials
            namespace: openshift-machine-api
          image: <5>
            offer: WindowsServer
            publisher: MicrosoftWindowsServer
            resourceID: ""
            sku: 2019-Datacenter-with-Containers
            version: latest
          kind: AzureMachineProviderSpec
          location: <location> <6>
          managedIdentity: <infrastructure_id>-identity <1>
          networkResourceGroup: <infrastructure_id>-rg <1>
          osDisk:
            diskSizeGB: 128
            managedDisk:
              storageAccountType: Premium_LRS
            osType: Windows
          publicIP: false
          resourceGroup: <infrastructure_id>-rg <1>
          subnet: <infrastructure_id>-worker-subnet
          userDataSecret:
            name: windows-user-data <7>
            namespace: openshift-machine-api
          vmSize: Standard_D2s_v3
          vnet: <infrastructure_id>-vnet <1>
          zone: "<zone>" <8>
----
<1> Specify the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. You can obtain the infrastructure ID by running the following command:
+
[source,terminal]
----
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
----
<2> Specify the Windows compute machine set name. Windows machine names on Azure cannot be more than 15 characters long. Therefore, the compute machine set name cannot be more than 9 characters long, due to the way machine names are generated from it.
<3> Configure the compute machine set as a Windows machine.
<4> Configure the Windows node as a compute machine.
<5> Specify a `WindowsServer` image offering that defines the `2019-Datacenter-with-Containers` SKU.
<6> Specify the Azure region, like `centralus`.
<7> Created by the WMCO when it is configuring the first Windows machine. After that, the `windows-user-data` is available for all subsequent compute machine sets to consume.
<8> Specify the zone within your region to place machines on. Be sure that your region supports the zone that you specify.
