// Module included in the following assemblies:
//
//  * openshift_images/using-templates.adoc

[id="templates-writing-labels_{context}"]
= Writing template labels

Templates can include a set of labels. These labels are added to each object created when the template is instantiated. Defining a label in this way makes it easy for users to find and manage all the objects created from a particular template.

The following is an example of template object labels:

[source,yaml]
----
kind: "Template"
apiVersion: "v1"
...
labels:
  template: "cakephp-mysql-example" <1>
  app: "${NAME}" <2>
----
<1> A label that is applied to all objects created from this template.
<2> A parameterized label that is also applied to all objects created from
this template. Parameter expansion is carried out on both label keys and
values.
