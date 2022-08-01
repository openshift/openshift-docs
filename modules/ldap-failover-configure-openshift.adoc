// Module included in the following assemblies:
//
// * authentication/configuring-ldap-failover.adoc

[id="sssd-for-ldap-configure-openshift_{context}"]
= Configuring {product-title} to use SSSD as the basic remote authentication server

Modify the default configuration of your cluster to use the new identity
provider that you created. Complete the following steps on the first control plane host
listed in the Ansible host inventory file.

.Procedure

. Open the `/etc/origin/master/master-config.yaml` file.

. Locate the `identityProviders` section and replace it with the following code:
+
----
  identityProviders:
  - name: sssd
    challenge: true
    login: true
    mappingMethod: claim
    provider:
      apiVersion: v1
      kind: BasicAuthPasswordIdentityProvider
      url: https://remote-basic.example.com/check_user.php
      ca: /etc/origin/master/ca.crt
      certFile: /etc/origin/master/openshift-master.crt
      keyFile: /etc/origin/master/openshift-master.key
----

. Start {product-title} with the updated configuration:
+
----
# openshift start \
    --public-master=https://openshift.example.com:8443 \
    --master-config=/etc/origin/master/master-config.yaml \
    --node-config=/etc/origin/node-node1.example.com/node-config.yaml
----

. Test a login by using the `oc` CLI:
+
----
$ oc login https://openshift.example.com:8443 -u user1
----
+
You can log in only with valid LDAP credentials.
. List the identities and confirm that an email address is displayed for each
user name. Run the following command:
+
----
$ oc get identity -o yaml
----
