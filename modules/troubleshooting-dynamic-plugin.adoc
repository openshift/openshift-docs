// Module included in the following assemblies:
//
// * web_console/dynamic-plugin/dynamic-plugins-reference.adoc

:_mod-docs-content-type: REFERENCE
[id="troubleshooting-dynamic-plugin_{context}"]
= Troubleshooting your dynamic plugin

Refer to this list of troubleshooting tips if you run into issues loading your plugin.

* Verify that you have enabled your plugin in the console Operator configuration and your plugin name is the output by running the following command:
+
[source,terminal]
----
$ oc get console.operator.openshift.io cluster -o jsonpath='{.spec.plugins}'
----

** Verify the enabled plugins on the status card of the *Overview* page in the *Administrator* perspective. You must refresh your browser if the plugin was recently enabled.

* Verify your plugin service is healthy by:
** Verifying your plugin pod status is running and your containers are ready.
** Verifying the service label selector matches the pod and the target port is correct.
** Curl the `plugin-manifest.json` from the service in a terminal on the console pod or another pod on the cluster.

* Verify your `ConsolePlugin` resource name (`consolePlugin.name`) matches the plugin name used in `package.json`.

* Verify your service name, namespace, port, and path are declared correctly in the `ConsolePlugin` resource.

* Verify your plugin service uses HTTPS and service serving certificates.

* Verify any certificates or connection errors in the console pod logs.

* Verify the feature flag your plugin relys on is not disabled.

* Verify your plugin does not have any `consolePlugin.dependencies` in `package.json` that are not met.
** This can include console version dependencies or dependencies on other plugins. Filter the JS console in your browser for your plugin's name to see messages that are logged.

* Verify there are no typos in the nav extension perspective or section IDs.
** Your plugin may be loaded, but nav items missing if IDs are incorrect. Try navigating to a plugin page directly by editing the URL.

* Verify there are no network policies that are blocking traffic from the console pod to your plugin service.
** If necessary, adjust network policies to allow console pods in the openshift-console namespace to make requests to your service.

* Verify the list of dynamic plugins to be loaded in your browser in the *Console* tab of the developer tools browser.
** Evaluate `window.SERVER_FLAGS.consolePlugins` to see the dynamic plugin on the Console frontend.
