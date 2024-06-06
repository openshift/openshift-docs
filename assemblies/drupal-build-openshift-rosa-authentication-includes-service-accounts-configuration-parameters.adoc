// Module included in the following assemblies:
//
// * authentication/using-service-accounts.adoc

[id="service-accounts-configuration-parameters_{context}"]
= Service account configuration parameters

You can provide values for the following service account parameters in the 
*_/etc/origin/master/master-config.yml_* file on the control plane host.

.Service account configuration parameters
[cols="3a,3a,6a",options="header"]
|===

| Parameter Name | Type | Description

|`LimitSecretReferences`
|Boolean
|Controls whether or not to allow a service account to reference any secret in a
namespace without explicitly referencing them.

|`ManagedNames`
|String
|A list of service account names that is automatically created in each namespace.
If no names are specified, the `ServiceAccountsController` service does not
start.

|`MasterCA`
|String
|The CA that verifies the TLS connection back to the master. The service account
controller automatically injects the contents of this file into pods so they
can verify connections to the master.

|`PrivateKeyFile`
|String
|A file that contains a PEM-encoded private RSA key, which is used to sign
service account tokens. If no private key is specified, the service account
`TokensController` service does not start.

|`PublicKeyFiles`
|String
|A list of files, each of which contains a PEM-encoded public RSA key. If any file
contains a private key, the public portion of the key is used. The list of
public keys is used to verify presented service account tokens. Each key is
tried in order until the list is exhausted or verification succeeds. If no keys
are specified, no service account authentication is available.

|`ServiceAccountConfig`
|List
|The parameter that contains the other listed service account parameters.

|===
