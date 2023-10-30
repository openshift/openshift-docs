:_mod-docs-content-type: ASSEMBLY
[id="serverless-applications"]
= Serverless applications
include::_attributes/common-attributes.adoc[]
:context: serverless-applications

toc::[]

include::snippets/serverless-apps.adoc[]

You can create a serverless application by using one of the following methods:

* Create a Knative service from the {product-title} web console.
+
ifdef::openshift-enterprise[]
See xref:../../../applications/creating_applications/odc-creating-applications-using-developer-perspective.adoc#odc-creating-applications-using-developer-perspective[Creating applications using the Developer perspective] for more information.
endif::[]
* Create a Knative service by using the Knative (`kn`) CLI.
* Create and apply a Knative `Service` object as a YAML file, by using the `oc` CLI.

// create service using CLI
include::modules/creating-serverless-apps-kn.adoc[leveloffset=+1]

// create service using YAML
include::modules/creating-serverless-apps-yaml.adoc[leveloffset=+1]

If you do not want to switch to the *Developer* perspective in the {product-title} web console or use the Knative (`kn`) CLI or YAML files, you can create Knative components by using the *Administator* perspective of the {product-title} web console.

// Create services as an admin
include::modules/creating-serverless-apps-admin-console.adoc[leveloffset=+1]

// offline mode
include::modules/kn-service-offline-create.adoc[leveloffset=+1]

[id="additional-resources_serverless-applications"]
[role="_additional-resources"]
== Additional resources
* xref:../../../serverless/cli_tools/serving_cli/kn-service.adoc#kn-service[Knative Serving CLI commands]
* xref:../../../serverless/knative-serving/config-access/serverless-ossm-with-kourier-jwt.adoc#serverless-ossm-with-kourier-jwt[Configuring JSON Web Token authentication for Knative services]
