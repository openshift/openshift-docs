:_mod-docs-content-type: ASSEMBLY
include::_attributes/common-attributes.adoc[]
[id='creating-a-single-component-application-with-odo']
= Creating a single-component application with {odo-title}

:context: creating-a-single-component-application-with-odo

toc::[]

With `{odo-title}`, you can create and deploy applications on  clusters.

.Prerequisites

* `{odo-title}` is installed.
* You have a running cluster. You can use link:https://access.redhat.com/documentation/en-us/red_hat_openshift_local/[{openshift-local-productname}] to deploy a local cluster quickly.

include::modules/developer-cli-odo-creating-a-project.adoc[leveloffset=+1]

include::modules/developer-cli-odo-creating-and-deploying-a-nodejs-application-with-odo.adoc[leveloffset=+1]

include::modules/developer-cli-odo-modifying-your-application-code.adoc[leveloffset=+1]

include::modules/developer-cli-odo-adding-storage-to-the-application-components.adoc[leveloffset=+1]

include::modules/developer-cli-odo-adding-a-custom-builder-to-specify-a-build-image.adoc[leveloffset=+1]

include::modules/developer-cli-odo-connecting-your-application-to-multiple-services-using-openshift-service-catalog.adoc[leveloffset=+1]

include::modules/developer-cli-odo-deleting-an-application.adoc[leveloffset=+1]
