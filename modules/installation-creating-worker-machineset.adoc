// Module included in the following assemblies:
//
// * none

[id="installation-creating-worker-machineset_{context}"]
= Creating worker nodes that the cluster manages

After your cluster initializes, you can create workers that are controlled by
a MachineSet in your Amazon Web Services (AWS) user-provisioned Infrastructure
cluster.

.Prerequisites

* Install a cluster on AWS using infrastructer that you provisioned.

.Procedure

. Optional: Launch worker nodes that are controlled by the machine API.
. View the list of MachineSets in the `openshift-machine-api` namespace:
+
----
$ oc get machinesets --namespace openshift-machine-api
NAME                           DESIRED   CURRENT   READY     AVAILABLE   AGE
test-tkh7l-worker-us-east-2a   1         1                               11m
test-tkh7l-worker-us-east-2b   1         1                               11m
test-tkh7l-worker-us-east-2c   1         1                               11m
----
+
Note the `NAME` of each MachineSet. Because you use a different subnet than the
installation program expects, the worker MachineSets do not use the correct
network settings. You must edit each of these MachineSets.

. Edit each worker MachineSet to provide the correct values for your cluster:
+
----
$ oc edit machineset --namespace openshift-machine-api test-tkh7l-worker-us-east-2a -o yaml
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  creationTimestamp: 2019-03-14T14:03:03Z
  generation: 1
  labels:
    machine.openshift.io/cluster-api-cluster: test-tkh7l
    machine.openshift.io/cluster-api-machine-role: worker
    machine.openshift.io/cluster-api-machine-type: worker
  name: test-tkh7l-worker-us-east-2a
  namespace: openshift-machine-api
  resourceVersion: "2350"
  selfLink: /apis/machine.openshift.io/v1beta1/namespaces/openshift-machine-api/machinesets/test-tkh7l-worker-us-east-2a
  uid: e2a6c8a6-4661-11e9-a9b0-0296069fd3a2
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: test-tkh7l
      machine.openshift.io/cluster-api-machineset: test-tkh7l-worker-us-east-2a
  template:
    metadata:
      creationTimestamp: null
      labels:
        machine.openshift.io/cluster-api-cluster: test-tkh7l
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: test-tkh7l-worker-us-east-2a
    spec:
      metadata:
        creationTimestamp: null
      providerSpec:
        value:
          ami:
            id: ami-07e0e0e0035b5a3fe <1>
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
            id: test-tkh7l-worker-profile
          instanceType: m4.large
          kind: AWSMachineProviderConfig
          metadata:
            creationTimestamp: null
          placement:
            availabilityZone: us-east-2a
            region: us-east-2
          publicIp: null
          securityGroups:
          - filters:
            - name: tag:Name
              values:
              -  test-tkh7l-worker-sg <2>
          subnet:
            filters:
            - name: tag:Name
              values:
              - test-tkh7l-private-us-east-2a
          tags:
          - name: kubernetes.io/cluster/test-tkh7l
            value: owned
          userDataSecret:
            name: worker-user-data
      versions:
        kubelet: ""
status:
  fullyLabeledReplicas: 1
  observedGeneration: 1
  replicas: 1
----
<1> Specify the {op-system-first} AMI to use for your worker nodes. Use the same
value that you specified in the parameter values for your control plane and
bootstrap templates.
<2> Specify the name of the worker security group that you created in the form
`<InfrastructureName>-worker-sg`. `<InfrastructureName>` is the same
infrastructure name that you extracted from the Ignition config metadata,
which has the format `<cluster-name>-<random-string>`.

////
. Optional: Replace the `subnet` stanza with one that specifies the subnet
to deploy the machines on:
+
----
subnet:
  filters:
  - name: tag:<value> <1>
    values:
    - test-tkh7l-private-us-east-2a <2>
----
<1> Set the `<value>` of the tag to `Name`, `ID`, or `ARN`.
<2> Specify the `Name`, `ID`, or `ARN` value for the subnet. This value must
match the `tag` type that you specify.
////

. View the machines in the `openshift-machine-api` namespace and confirm that
they are launching:
+
----
$ oc get machines --namespace openshift-machine-api
NAME                                 INSTANCE              STATE     TYPE         REGION      ZONE         AGE
test-tkh7l-worker-us-east-2a-hxlqn   i-0e7f3a52b2919471e   pending   m4.4xlarge   us-east-2   us-east-2a   3s
----
