// Text snippet included in the following modules:
//
// * modules/odc-importing-codebase-from-git-to-create-application.adoc

:_mod-docs-content-type: SNIPPET

Domain mapping:: If you are creating a *Serverless Deployment*, you can add a custom domain mapping to the Knative service during creation.
+
* In the *Advanced options* section, click *Show advanced Routing options*.
** If the domain mapping CR that you want to map to the service already exists, you can select it from the *Domain mapping* drop-down menu.
** If you want to create a new domain mapping CR, type the domain name into the box, and select the *Create* option. For example, if you type in `example.com`, the *Create* option is *Create "example.com"*.
