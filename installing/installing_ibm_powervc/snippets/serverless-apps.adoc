// Text snippet included in the following modules and assemblies:
//
// * /serverless/develop/serverless-applications.adoc
// * /modules/creating-serverless-apps-admin-console.adoc

:_mod-docs-content-type: SNIPPET

Serverless applications are created and deployed as Kubernetes services, defined by a route and a configuration, and contained in a YAML file. To deploy a serverless application using {ServerlessProductName}, you must create a Knative `Service` object.

.Example Knative `Service` object YAML file
[source,yaml]
----
apiVersion: serving.knative.dev/v1
kind: Service
metadata:
  name: hello <1>
  namespace: default <2>
spec:
  template:
    spec:
      containers:
        - image: docker.io/openshift/hello-openshift <3>
          env:
            - name: RESPONSE <4>
              value: "Hello Serverless!"
----
<1> The name of the application.
<2> The namespace the application uses.
<3> The image of the application.
<4> The environment variable printed out by the sample application.
