// Module included in the following assemblies:
//
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-gcp.adoc

[id="windows-machineset-gcp_{context}"]
= Sample YAML for a Windows MachineSet object on GCP

This sample YAML file defines a Windows `MachineSet` object running on Google Cloud Platform (GCP) that the Windows Machine Config Operator (WMCO) can use.

[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id> <1>
  name: <infrastructure_id>-windows-worker-<zone_suffix> <2>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id> <1>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-windows-worker-<zone_suffix> <2>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id> <1>
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-windows-worker-<zone_suffix> <2>
        machine.openshift.io/os-id: Windows <3>
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/worker: "" <4>
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1beta1
          canIPForward: false
          credentialsSecret:
            name: gcp-cloud-credentials
          deletionProtection: false
          disks:
          - autoDelete: true
            boot: true
            image: <windows_server_image> <5>
            sizeGb: 128
            type: pd-ssd
          kind: GCPMachineProviderSpec
          machineType: n1-standard-4
          networkInterfaces:
          - network: <infrastructure_id>-network <1>
            subnetwork: <infrastructure_id>-worker-subnet
          projectID: <project_id> <6>
          region: <region> <7>
          serviceAccounts:
          - email: <infrastructure_id>-w@<project_id>.iam.gserviceaccount.com
            scopes:
            - https://www.googleapis.com/auth/cloud-platform
          tags:
          - <infrastructure_id>-worker
          userDataSecret:
            name: windows-user-data <8>
          zone: <zone> <9>
----
<1> Specify the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. You can obtain the infrastructure ID by running the following command:
+
[source,terminal]
----
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
----
<2> Specify the infrastructure ID, worker label, and zone suffix (such as `a`).
<3> Configure the machine set as a Windows machine.
<4> Configure the Windows node as a compute machine.
<5> Specify the full path to an image of a supported version of Windows Server. 
<6> Specify the GCP project that this cluster was created in.
<7> Specify the GCP region, such as `us-central1`. 
<8> Created by the WMCO when it configures the first Windows machine. After that, the `windows-user-data` is available for all subsequent machine sets to consume.
<9> Specify the zone within the chosen region, such as `us-central1-a`.
