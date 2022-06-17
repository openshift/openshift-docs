// Module included in the following assemblies:
//
// * authentication/configuring-ldap-failover.adoc

[id="sssd-configuring-apache_{context}"]
= Configuring Apache to use SSSD

.Procedure

.  Create a `/etc/pam.d/openshift` file that contains the
following contents:
+
----
auth required pam_sss.so
account required pam_sss.so
----
+
This configuration enables PAM, the pluggable authentication module, to use
`pam_sss.so` to determine authentication and access control when an
authentication request is issued for the `openshift` stack.

. Edit the `/etc/httpd/conf.modules.d/55-authnz_pam.conf` file and uncomment
 the following line:
+
----
LoadModule authnz_pam_module modules/mod_authnz_pam.so
----

. To configure the Apache `httpd.conf` file for remote basic authentication,
create the `openshift-remote-basic-auth.conf` file in the
`/etc/httpd/conf.d` directory. Use the following template to provide your
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
LoadModule php7_module modules/libphp7.so

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
  # openssl x509 -text -in /etc/pki/tls/certs/remote-basic.example.com.crt
  ServerName remote-basic.example.com

  DocumentRoot /var/www/html

  # Secure all connections with TLS
  SSLEngine on
  SSLCertificateFile /etc/pki/tls/certs/remote-basic.example.com.crt
  SSLCertificateKeyFile /etc/pki/tls/private/remote-basic.example.com.key
  SSLCACertificateFile /etc/pki/CA/certs/ca.crt

  # Require that TLS clients provide a valid certificate
  SSLVerifyClient require
  SSLVerifyDepth 10

  # Other SSL options that may be useful
  # SSLCertificateChainFile ...
  # SSLCARevocationFile ...

  # Send logs to a specific location to make them easier to find
  ErrorLog logs/remote_basic_error_log
  TransferLog logs/remote_basic_access_log
  LogLevel warn

  # PHP script that turns the Apache REMOTE_USER env var
  # into a JSON formatted response that OpenShift understands
  <Location /check_user.php>
    # all requests not using SSL are denied
    SSLRequireSSL
    # denies access when SSLRequireSSL is applied
    SSLOptions +StrictRequire
    # Require both a valid basic auth user (so REMOTE_USER is always set)
    # and that the CN of the TLS client matches that of the OpenShift master
    <RequireAll>
      Require valid-user
      Require expr %{SSL_CLIENT_S_DN_CN} == 'system:openshift-master'
    </RequireAll>
    # Use basic auth since OpenShift will call this endpoint with a basic challenge
    AuthType Basic
    AuthName openshift
    AuthBasicProvider PAM
    AuthPAMService openshift

    # Store attributes in environment variables. Specify the email attribute that
    # you confirmed.
    LookupOutput Env
    LookupUserAttr mail REMOTE_USER_MAIL
    LookupUserGECOS REMOTE_USER_DISPLAY_NAME

    # Other options that might be useful

    # While REMOTE_USER is used as the sub field and serves as the immutable ID,
    # REMOTE_USER_PREFERRED_USERNAME could be used to have a different username
    # LookupUserAttr <attr_name> REMOTE_USER_PREFERRED_USERNAME

    # Group support may be added in a future release
    # LookupUserGroupsIter REMOTE_USER_GROUP
  </Location>

  # Deny everything else
  <Location ~ "^((?!\/check_user\.php).)*$">
      Deny from all
  </Location>
</VirtualHost>
----

. Create the `check_user.php` script in the `/var/www/html` directory.
Include the following code:
+
----
<?php
// Get the user based on the Apache var, this should always be
// set because we 'Require valid-user' in the configuration
$user = apache_getenv('REMOTE_USER');

// However, we assume it may not be set and
// build an error response by default
$data = array(
    'error' => 'remote PAM authentication failed'
);

// Build a success response if we have a user
if (!empty($user)) {
    $data = array(
        'sub' => $user
    );
    // Map of optional environment variables to optional JSON fields
    $env_map = array(
        'REMOTE_USER_MAIL' => 'email',
        'REMOTE_USER_DISPLAY_NAME' => 'name',
        'REMOTE_USER_PREFERRED_USERNAME' => 'preferred_username'
    );

    // Add all non-empty environment variables to JSON data
    foreach ($env_map as $env_name => $json_name) {
        $env_data = apache_getenv($env_name);
        if (!empty($env_data)) {
            $data[$json_name] = $env_data;
        }
    }
}

// We always output JSON from this script
header('Content-Type: application/json', true);

// Write the response as JSON
echo json_encode($data);
?>
----

. Enable Apache to load the module. Modify the
`/etc/httpd/conf.modules.d/55-lookup_identity.conf` file and uncomment the
following line:
+
----
LoadModule lookup_identity_module modules/mod_lookup_identity.so
----

. Set an SELinux boolean so that SElinux allows Apache to connect to SSSD over
D-BUS:
+
----
# setsebool -P httpd_dbus_sssd on
----

. Set a boolean to tell SELinux that it is acceptable for Apache to contact the
PAM subsystem:
+
----
# setsebool -P allow_httpd_mod_auth_pam on
----

. Start Apache:
+
----
# systemctl start httpd.service
----
