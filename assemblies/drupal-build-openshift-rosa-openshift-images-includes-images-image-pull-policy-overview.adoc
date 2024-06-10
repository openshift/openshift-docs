// Module included in the following assemblies:
// * openshift_images/image-pull-policy

:_mod-docs-content-type: CONCEPT
[id="images-image-pull-policy-overview_{context}"]
= Image pull policy overview

When {product-title} creates containers, it uses the container `imagePullPolicy` to determine if the image should be pulled prior to starting the container. There are three possible values for `imagePullPolicy`:

.`imagePullPolicy` values
[width="50%",options="header"]
|===
|Value |Description

|`Always`
|Always pull the image.

|`IfNotPresent`
|Only pull the image if it does not already exist on the node.

|`Never`
|Never pull the image.
|===


If a container `imagePullPolicy` parameter is not specified, {product-title} sets it based on the image tag:

. If the tag is `latest`, {product-title} defaults `imagePullPolicy` to `Always`.
. Otherwise, {product-title} defaults `imagePullPolicy` to `IfNotPresent`.
