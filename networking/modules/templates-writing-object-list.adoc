// Module included in the following assemblies:
//
// * openshift_images/using-templates.adoc

[id="templates-writing-object-list_{context}"]
= Writing the template object list

The main portion of the template is the list of objects which is created when the template is instantiated. This can be any valid API object, such as a build configuration, deployment configuration, or service. The object is created exactly as defined here, with any parameter values substituted in prior to creation. The definition of these objects can reference parameters defined earlier.

The following is an example of an object list:

[source,yaml]
----
kind: "Template"
apiVersion: "v1"
metadata:
  name: my-template
objects:
  - kind: "Service" <1>
    apiVersion: "v1"
    metadata:
      name: "cakephp-mysql-example"
      annotations:
        description: "Exposes and load balances the application pods"
    spec:
      ports:
        - name: "web"
          port: 8080
          targetPort: 8080
      selector:
        name: "cakephp-mysql-example"
----
<1> The definition of a service, which is created by this template.


[NOTE]
====
If an object definition metadata includes a fixed `namespace` field value, the field is stripped out of the definition during template instantiation. If the `namespace` field contains a parameter reference, normal parameter substitution is performed and the object is created in whatever namespace the parameter substitution resolved the value to, assuming the user has permission to create objects in that namespace.
====
