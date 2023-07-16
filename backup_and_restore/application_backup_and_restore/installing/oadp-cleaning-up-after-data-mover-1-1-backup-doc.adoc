[id="oadp-cleaning-up-after-data-mover-1-1-backup-doc"]
= Cleaning up after a backup using OADP 1.1 Data Mover
include::_attributes/common-attributes.adoc[]
:context: datamover11

toc::[]

For OADP 1.1 Data Mover, you must perform a data cleanup after you perform a backup.

The cleanup consists of deleting the following resources:

* Snapshots in a bucket
* Cluster resources
* Volume snapshot backups (VSBs) after a backup procedure that is either run by a schedule or is run repetitively

include::modules/oadp-cleaning-up-after-data-mover-snapshots.adoc[leveloffset=+1]

[id="deleting-cluster-resources-data-mover"]
== Deleting cluster resources

OADP 1.1 Data Mover might leave cluster resources whether or not it successfully backs up your container storage interface (CSI) volume snapshots to a remote object store.

include::modules/oadp-deleting-cluster-resources-following-success.adoc[leveloffset=+2]
include::modules/oadp-deleting-cluster-resources-following-failure.adoc[leveloffset=+2]

include::modules/oadp-vsb-cleanup-after-scheduler.adoc[leveloffset=+1]
