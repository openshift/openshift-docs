# Additional requirements for installing on a single node on AWS

The AWS documentation for installer-provisioned installation is written with a high availability cluster consisting of three control plane nodes. When referring to the AWS documentation, consider the differences between the requirements for a {sno} cluster and a high availability cluster.

* The required machines for cluster installation in AWS documentation indicates a temporary bootstrap machine, three control plane machines, and at least two compute machines. You require only a temporary bootstrap machine and one AWS instance for the control plane node and no worker nodes.
* The minimum resource requirements for cluster installation in the AWS documentation indicates a control plane node with 4 vCPUs and 100GB of storage. For a single node cluster, you must have a minimum of 8 vCPU cores and 120GB of storage.
* The `controlPlane.replicas` setting in the `install-config.yaml` file should be set to `1`.
* The `compute.replicas` setting in the `install-config.yaml` file should be set to `0`.
This makes the control plane node schedulable.
