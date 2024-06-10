// Module included in the following assemblies:
//
// * storage/persistent_storage-aws.adoc

= Creating the persistent volume claim

.Prerequisites

Storage must exist in the underlying infrastructure before it can be mounted as
a volume in {product-title}.

.Procedure

. In the {product-title} console, click *Storage* -> *Persistent Volume Claims*.

. In the persistent volume claims overview, click *Create Persistent Volume
Claim*.

. Define the desired options on the page that appears.

.. Select the previously-created storage class from the drop-down menu.

.. Enter a unique name for the storage claim.

.. Select the access mode. This selection determines the read and write access for the storage claim.

.. Define the size of the storage claim.

. Click *Create* to create the persistent volume claim and generate a persistent
volume.
