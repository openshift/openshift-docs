// Module included in the following assemblies:
//
// * openshift_images/using-templates.adoc

:_mod-docs-content-type: CONCEPT
[id="templates-overview_{context}"]
= Understanding templates

A template describes a set of objects that can be parameterized and processed to produce a list of objects for creation by {product-title}. A template can be processed to create anything you have permission to create within a project, for example services, build configurations, and deployment configurations. A template can also define a set of labels to apply to every object defined in the template.

You can create a list of objects from a template using the CLI or, if a template has been uploaded to your project or the global template library, using the web console.

//[role="_additional-resources"]
//.Additional resources
//For a curated set of templates, see the
//link:https://github.com/openshift/library[OpenShift ImageStreams and Templates
//library].
