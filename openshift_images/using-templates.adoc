:_mod-docs-content-type: ASSEMBLY
[id="using-templates"]
= Using templates
include::_attributes/common-attributes.adoc[]
:context: using-templates

toc::[]

The following sections provide an overview of templates, as well as how to use and create them.

include::modules/templates-overview.adoc[leveloffset=+1]

include::modules/templates-uploading.adoc[leveloffset=+1]

include::modules/templates-creating-from-console.adoc[leveloffset=+1]

include::modules/templates-using-the-cli.adoc[leveloffset=+1]

include::modules/templates-cli-labels.adoc[leveloffset=+2]

include::modules/templates-cli-parameters.adoc[leveloffset=+2]

include::modules/templates-cli-generating-list-of-objects.adoc[leveloffset=+2]

include::modules/templates-modifying-uploaded-template.adoc[leveloffset=+1]

// cannot patch resource "templates" 
ifndef::openshift-rosa,openshift-dedicated[]
include::modules/templates-using-instant-app-quickstart.adoc[leveloffset=+1]

include::modules/templates-quickstart.adoc[leveloffset=+2]
endif::openshift-rosa,openshift-dedicated[]

include::modules/templates-writing.adoc[leveloffset=+1]

include::modules/templates-writing-description.adoc[leveloffset=+2]

include::modules/templates-writing-labels.adoc[leveloffset=+2]

include::modules/templates-writing-parameters.adoc[leveloffset=+2]

include::modules/templates-writing-object-list.adoc[leveloffset=+2]

include::modules/templates-marking-as-bindable.adoc[leveloffset=+2]

include::modules/templates-exposing-object-fields.adoc[leveloffset=+2]

include::modules/templates-waiting-for-readiness.adoc[leveloffset=+2]

include::modules/templates-create-from-existing-object.adoc[leveloffset=+2]


//Add quick start and other relevant tutorials here.
