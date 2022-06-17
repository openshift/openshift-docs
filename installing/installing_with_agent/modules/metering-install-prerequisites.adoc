// Module included in the following assemblies:
//
// * metering/metering-installing-metering.adoc

[id="metering-install-prerequisites_{context}"]
= Prerequisites

Metering requires the following components:

* A `StorageClass` resource for dynamic volume provisioning. Metering supports a number of different storage solutions.
* 4GB memory and 4 CPU cores available cluster capacity and at least one node with 2 CPU cores and 2GB memory capacity available.
* The minimum resources needed for the largest single pod installed by metering are 2GB of memory and 2 CPU cores.
** Memory and CPU consumption may often be lower, but will spike when running reports, or collecting data for larger clusters.
