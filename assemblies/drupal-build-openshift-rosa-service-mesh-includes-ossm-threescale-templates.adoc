// Module included in the following assemblies:
//
// * service_mesh/v1x/threescale_adapter/threescale-adapter.adoc
// * service_mesh/v2x/threescale_adapter/threescale-adapter.adoc

:_mod-docs-content-type: PROCEDURE
[id="ossm-threescale-templates_{context}"]
= Generate templates from URL examples

[NOTE]
====
* Run the following commands via `oc exec` from the 3scale adapter container image in xref:ossm-threescale-manifests_{context}[Generating manifests from a deployed adapter].
* Use the `3scale-config-gen` command to help avoid YAML syntax and indentation errors.
* You can omit the `--service` if you use the annotations.
* This command must be invoked from within the container image via `oc exec`.
====

.Procedure

* Use the `3scale-config-gen` command to autogenerate templates files allowing the token, URL pair to be shared by multiple services as a single handler:
+
----
$ 3scale-config-gen --name=admin-credentials --url="https://<organization>-admin.3scale.net:443" --token="[redacted]"
----
+
* The following example generates the templates with the service ID embedded in the handler:
+
----
$ 3scale-config-gen --url="https://<organization>-admin.3scale.net" --name="my-unique-id" --service="123456789" --token="[redacted]"
----

[role="_additional-resources"]
.Additional resources
* link:https://access.redhat.com/documentation/en-us/red_hat_3scale_api_management/2.10/html-single/admin_portal_guide/index#tokens[Tokens].
