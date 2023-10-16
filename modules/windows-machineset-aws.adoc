// Module included in the following assemblies:
//
// * windows_containers/creating_windows_machinesets/creating-windows-machineset-aws.adoc

[id="windows-machineset-aws_{context}"]
= Sample YAML for a Windows MachineSet object on AWS

This sample YAML defines a Windows `MachineSet` object running on Amazon Web Services (AWS) that the Windows Machine Config Operator (WMCO) can react upon.

[source,yaml]
----
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id> <1>
  name: <infrastructure_id>-windows-worker-<zone> <2>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id> <1>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-windows-worker-<zone> <2>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id> <1>
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-windows-worker-<zone> <2>
        machine.openshift.io/os-id: Windows <3>
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/worker: "" <4>
      providerSpec:
        value:
          ami:
            id: <windows_container_ami> <5>
          apiVersion: awsproviderconfig.openshift.io/v1beta1
          blockDevices:
            - ebs:
                iops: 0
                volumeSize: 120
                volumeType: gp2
          credentialsSecret:
            name: aws-cloud-credentials
          deviceIndex: 0
          iamInstanceProfile:
            id: <infrastructure_id>-worker-profile <1>
          instanceType: m5a.large
          kind: AWSMachineProviderConfig
          placement:
            availabilityZone: <zone> <6>
            region: <region> <7>
          securityGroups:
            - filters:
                - name: tag:Name
                  values:
                    - <infrastructure_id>-worker-sg <1>
          subnet:
            filters:
              - name: tag:Name
                values:
                  - <infrastructure_id>-private-<zone> <1>
          tags:
            - name: kubernetes.io/cluster/<infrastructure_id> <1>
              value: owned
          userDataSecret:
            name: windows-user-data <8>
            namespace: openshift-machine-api
----
<1> Specify the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. You can obtain the infrastructure ID by running the following command:
+
[source,terminal]
----
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
----
<2> Specify the infrastructure ID, worker label, and zone.
<3> Configure the compute machine set as a Windows machine.
<4> Configure the Windows node as a compute machine.
<5> Specify the AMI ID of a supported Windows image with a container runtime installed.
<6> Specify the AWS zone, like `us-east-1a`.
<7> Specify the AWS region, like `us-east-1`.
<8> Created by the WMCO when it is configuring the first Windows machine. After that, the `windows-user-data` is available for all subsequent compute machine sets to consume.
