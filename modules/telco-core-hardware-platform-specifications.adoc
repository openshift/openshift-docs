// Module included in the following assemblies:
//
// * telco_ref_design_specs/ran/telco-ran-ref-validation-artifacts.adoc

:_mod-docs-content-type: REFERENCE
[id="telco-core-hardware-platform-specifications_{context}"]
= Hardware platform specifications

The telco core DU reference configuration is validated with the following hardware:

.Validated {sno} DU cluster hardware
[cols="1,3", width="90%", options="header"]
|====
|Server
|Specifications

|Dell PowerEdge R640
a|* 192G RAM
* 64 cores

|HP ProLiant e910
a|* 96G RAM
* 48 cores
|====

.Validated  CNF compute cluster hardware
[cols="1,3", width="90%", options="header"]
|====
|Server
|Specifications

|Dell R640/750 (2-sockets)
a|* 2 x Intel Xeon Gold 6248 CPUs
* 196 to 256GB RAM
* 2.5 to 3 TB HD
|====

.Validated NICs
[cols="1,3", width="90%", options="header"]
|====
|Network interface
|Description

|Intel X722
a|* 10/1 GbE backplane

|Mellanox ConnectX-4 Lx
a|* 2 ports
* 25 GbE
* PCIe 3.0
|====

.Validated Storage
[cols="1,3", width="90%", options="header"]
|====
|Device
|Description

|NVME drive
a|
|====