// Module included in the following assemblies:
//
// * authentication/identity_providers/configuring-request-header-identity-provider.adoc

:_mod-docs-content-type: PROCEDURE
[id="identity-provider-configuring-apache-request-header_{context}"]
= Configuring Apache authentication using request header

This example uses the `mod_auth_gssapi` module to configure an Apache
authentication proxy using the request header identity provider.

.Prerequisites

* Obtain the `mod_auth_gssapi` module from the
link:https://access.redhat.com/solutions/392003[Optional channel].
You must have the following packages installed on your local machine:
+
** `httpd`
** `mod_ssl`
** `mod_session`
** `apr-util-openssl`
** `mod_auth_gssapi`

* Generate a CA for validating requests that submit the trusted header. Define
an {product-title} `ConfigMap` object containing the CA. This is done by running:
+
[source,terminal]
----
$ oc create configmap ca-config-map --from-file=ca.crt=/path/to/ca -n openshift-config <1>
----
<1> The CA must be stored in the `ca.crt` key of the `ConfigMap` object.
+
[TIP]
====
You can alternatively apply the following YAML to create the config map:

[source,yaml]
----
apiVersion: v1
kind: ConfigMap
metadata:
  name: ca-config-map
  namespace: openshift-config
data:
  ca.crt: |
    <CA_certificate_PEM>
----
====

* Generate a client certificate for the proxy. You can generate this certificate
by using any x509 certificate tooling. The client certificate must be signed by
the CA you generated for validating requests that submit the trusted header.

* Create the custom resource (CR) for your identity providers.

.Procedure

This proxy uses a client certificate to connect to the OAuth server, which
is configured to trust the `X-Remote-User` header.

. Create the certificate for the Apache configuration. The certificate that you
specify as the `SSLProxyMachineCertificateFile` parameter value is the proxy's
client certificate that is used to authenticate the proxy to the server. It must
use `TLS Web Client Authentication` as the extended key type.

. Create the Apache configuration. Use the following template to provide your
required settings and values:
+
[IMPORTANT]
====
Carefully review the template and customize its contents to fit your
environment.
====
+
----
LoadModule request_module modules/mod_request.so
LoadModule auth_gssapi_module modules/mod_auth_gssapi.so
# Some Apache configurations might require these modules.
# LoadModule auth_form_module modules/mod_auth_form.so
# LoadModule session_module modules/mod_session.so

# Nothing needs to be served over HTTP.  This virtual host simply redirects to
# HTTPS.
<VirtualHost *:80>
  DocumentRoot /var/www/html
  RewriteEngine              On
  RewriteRule     ^(.*)$     https://%{HTTP_HOST}$1 [R,L]
</VirtualHost>

<VirtualHost *:443>
  # This needs to match the certificates you generated.  See the CN and X509v3
  # Subject Alternative Name in the output of:
  # openssl x509 -text -in /etc/pki/tls/certs/localhost.crt
  ServerName www.example.com

  DocumentRoot /var/www/html
  SSLEngine on
  SSLCertificateFile /etc/pki/tls/certs/localhost.crt
  SSLCertificateKeyFile /etc/pki/tls/private/localhost.key
  SSLCACertificateFile /etc/pki/CA/certs/ca.crt

  SSLProxyEngine on
  SSLProxyCACertificateFile /etc/pki/CA/certs/ca.crt
  # It is critical to enforce client certificates. Otherwise, requests can
  # spoof the X-Remote-User header by accessing the /oauth/authorize endpoint
  # directly.
  SSLProxyMachineCertificateFile /etc/pki/tls/certs/authproxy.pem

  # To use the challenging-proxy, an X-Csrf-Token must be present.
  RewriteCond %{REQUEST_URI} ^/challenging-proxy
  RewriteCond %{HTTP:X-Csrf-Token} ^$ [NC]
  RewriteRule ^.* - [F,L]

  <Location /challenging-proxy/oauth/authorize>
      # Insert your backend server name/ip here.
      ProxyPass https://<namespace_route>/oauth/authorize
      AuthName "SSO Login"
      # For Kerberos
      AuthType GSSAPI
      Require valid-user
      RequestHeader set X-Remote-User %{REMOTE_USER}s

      GssapiCredStore keytab:/etc/httpd/protected/auth-proxy.keytab
      # Enable the following if you want to allow users to fallback
      # to password based authentication when they do not have a client
      # configured to perform kerberos authentication.
      GssapiBasicAuth On

      # For ldap:
      # AuthBasicProvider ldap
      # AuthLDAPURL "ldap://ldap.example.com:389/ou=People,dc=my-domain,dc=com?uid?sub?(objectClass=*)"
    </Location>

    <Location /login-proxy/oauth/authorize>
    # Insert your backend server name/ip here.
    ProxyPass https://<namespace_route>/oauth/authorize

      AuthName "SSO Login"
      AuthType GSSAPI
      Require valid-user
      RequestHeader set X-Remote-User %{REMOTE_USER}s env=REMOTE_USER

      GssapiCredStore keytab:/etc/httpd/protected/auth-proxy.keytab
      # Enable the following if you want to allow users to fallback
      # to password based authentication when they do not have a client
      # configured to perform kerberos authentication.
      GssapiBasicAuth On

      ErrorDocument 401 /login.html
    </Location>

</VirtualHost>

RequestHeader unset X-Remote-User
----
+
[NOTE]
====
The `\https://<namespace_route>` address is the route to the OAuth server and
can be obtained by running `oc get route -n openshift-authentication`.
====

. Update the `identityProviders` stanza in the custom resource (CR):
+
[source,yaml]
----
identityProviders:
  - name: requestheaderidp
    type: RequestHeader
    requestHeader:
      challengeURL: "https://<namespace_route>/challenging-proxy/oauth/authorize?${query}"
      loginURL: "https://<namespace_route>/login-proxy/oauth/authorize?${query}"
      ca:
        name: ca-config-map
        clientCommonNames:
        - my-auth-proxy
        headers:
        - X-Remote-User
----

. Verify the configuration.

.. Confirm that you can bypass the proxy by requesting a token by supplying the
correct client certificate and header:
+
[source,terminal]
----
# curl -L -k -H "X-Remote-User: joe" \
   --cert /etc/pki/tls/certs/authproxy.pem \
   https://<namespace_route>/oauth/token/request
----

.. Confirm that requests that do not supply the client certificate fail by
requesting a token without the certificate:
+
[source,terminal]
----
# curl -L -k -H "X-Remote-User: joe" \
   https://<namespace_route>/oauth/token/request
----

.. Confirm that the `challengeURL` redirect is active:
+
[source,terminal]
----
# curl -k -v -H 'X-Csrf-Token: 1' \
   https://<namespace_route>/oauth/authorize?client_id=openshift-challenging-client&response_type=token
----
+
Copy the `challengeURL` redirect to use in the next step.

.. Run this command to show a `401` response with a `WWW-Authenticate` basic
challenge, a negotiate challenge, or both challenges:
+
[source,terminal]
----
# curl -k -v -H 'X-Csrf-Token: 1' \
   <challengeURL_redirect + query>
----

.. Test logging in to the OpenShift CLI (`oc`) with and without using a Kerberos
ticket:
... If you generated a Kerberos ticket by using `kinit`, destroy it:
+
[source,terminal]
----
# kdestroy -c cache_name <1>
----
+
<1> Make sure to provide the name of your Kerberos cache.
... Log in to the `oc` tool by using your Kerberos credentials:
+
[source,terminal]
----
# oc login -u <username>
----
+
Enter your Kerberos password at the prompt.
... Log out of the `oc` tool:
+
[source,terminal]
----
# oc logout
----
... Use your Kerberos credentials to get a ticket:
+
[source,terminal]
----
# kinit
----
+
Enter your Kerberos user name and password at the prompt.
... Confirm that you can log in to the `oc` tool:
+
[source,terminal]
----
# oc login
----
+
If your configuration is correct, you are logged in without entering separate
credentials.
