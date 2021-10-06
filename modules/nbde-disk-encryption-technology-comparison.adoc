// Module included in the following assemblies:
//
// security/nbde-implementation-guide.adoc

[id="nbde-disk-encryption-technology-comparison_{context}"]
= Disk encryption technology comparison

To understand the merits of Network-Bound Disk Encryption (NBDE) for securing data at rest on edge servers, compare key escrow and TPM disk encryption without Clevis to NBDE on systems running {op-system-base-full}.

The following table presents some tradeoffs to consider around the threat model and the complexity of each encryption solution.

[cols="1,1,1,1"]
|===
| Scenario | Key escrow | TPM disk encryption (without Clevis) | NBDE

| Protects against single-disk theft
| X
| X
| X

| Protects against entire-server theft
| X
|
| X

| Systems can reboot independently from the network
|
| X
|

| No periodic rekeying
|
| X
|

| Key is never transmitted over a network
|
| X
| X

| Supported by OpenShift
|
| X
| X

|===
