:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id="empty-dir"]
= EmptyDir volumes
:context: empty-dir

`emptyDir` volumes are empty volumes that are created when a pod is created, and are used to provide temporary working disk space. `emptyDir` volumes are deleted when the pod they were created for is deleted.

// enable emptydirs
include::modules/serverless-config-emptydir.adoc[leveloffset=+1]

