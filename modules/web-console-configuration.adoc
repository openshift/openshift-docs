// Module included in the following assemblies:
//
// * web_console/configuring-web-console.adoc

[id="web-console-configuration_{context}"]
= Configuring the web console

You can configure the web console settings by editing the `console.config.openshift.io` resource.

* Edit the `console.config.openshift.io` resource:
+
[source,terminal]
----
$ oc edit console.config.openshift.io cluster
----
+
The following example displays the sample resource definition for the console:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: Console
metadata:
  name: cluster
spec:
  authentication:
    logoutRedirect: "" <1>
status:
  consoleURL: "" <2>
----
<1> Specify the URL of the page to load when a user logs out of the web console. If you do not specify a value, the user returns to the login page for the web console. Specifying a `logoutRedirect` URL allows your users to perform single logout (SLO) through the identity provider to destroy their single sign-on session.
<2> The web console URL. To update this to a custom value, see *Customizing the web console URL*.
