// Module included in the following assemblies:
//
// * web_console/customizing-the-web-console.adoc

:_mod-docs-content-type: PROCEDURE
[id="customizing-the-login-page_{context}"]
= Customizing the login page

Create Terms of Service information with custom login pages. Custom login pages
can also be helpful if you use a third-party login provider, such as GitHub or
Google, to show users a branded page that they trust and expect before being
redirected to the authentication provider. You can also render custom error
pages during the authentication process.

[NOTE]
====
Customizing the error template is limited to identity providers (IDPs) that use redirects, such as request header and OIDC-based IDPs. It does not have an effect on IDPs that use direct password authentication, such as LDAP and htpasswd.
====

.Prerequisites

* You must have administrator privileges.

.Procedure

. Run the following commands to create templates you can modify:
+
[source,terminal]
----
$ oc adm create-login-template > login.html
----
+
[source,terminal]
----
$ oc adm create-provider-selection-template > providers.html
----
+
[source,terminal]
----
$ oc adm create-error-template > errors.html
----

. Create the secrets:
+
[source,terminal]
----
$ oc create secret generic login-template --from-file=login.html -n openshift-config
----
+
[source,terminal]
----
$ oc create secret generic providers-template --from-file=providers.html -n openshift-config
----
+
[source,terminal]
----
$ oc create secret generic error-template --from-file=errors.html -n openshift-config
----

. Run:
+
[source,terminal]
----
$ oc edit oauths cluster
----

. Update the specification:
+
[source,yaml]
----
apiVersion: config.openshift.io/v1
kind: OAuth
metadata:
  name: cluster
# ...
spec:
  templates:
    error:
        name: error-template
    login:
        name: login-template
    providerSelection:
        name: providers-template
----
+
Run `oc explain oauths.spec.templates` to understand the options.
