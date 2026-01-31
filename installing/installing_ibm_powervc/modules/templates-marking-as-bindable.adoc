// Module included in the following assemblies:
//
// * openshift_images/using-templates.adoc

:_mod-docs-content-type: PROCEDURE
[id="templates-marking-as-bindable_{context}"]
= Marking a template as bindable

The {tsb-name} advertises one service in its catalog for each template object of which it is aware. By default, each of these services is advertised as being bindable, meaning an end user is permitted to bind against the provisioned service.

.Procedure

Template authors can prevent end users from binding against services provisioned from a given template.

* Prevent end user from binding against services provisioned from a given template by adding the annotation `template.openshift.io/bindable: "false"` to the template.
