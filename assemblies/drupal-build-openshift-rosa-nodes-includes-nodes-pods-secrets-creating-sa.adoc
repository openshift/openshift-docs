// Module included in the following assemblies:
//
// * nodes/nodes-pods-secrets.adoc

:_mod-docs-content-type: PROCEDURE
[id="nodes-pods-secrets-creating-sa_{context}"]
= Creating a service account token secret

As an administrator, you can create a service account token secret, which allows you to distribute a service account token to applications that must authenticate to the API.

[NOTE]
====
It is recommended to obtain bound service account tokens using the TokenRequest API instead of using service account token secrets. The tokens obtained from the TokenRequest API are more secure than the tokens stored in secrets, because they have a bounded lifetime and are not readable by other API clients.

You should create a service account token secret only if you cannot use the TokenRequest API and if the security exposure of a non-expiring token in a readable API object is acceptable to you.

See the Additional resources section that follows for information on creating bound service account tokens.
====

.Procedure

. Create a `Secret` object in a YAML file on a control plane node:
+
.Example `secret` object:
[source,yaml]
----
apiVersion: v1
kind: Secret
metadata:
  name: secret-sa-sample
  annotations:
    kubernetes.io/service-account.name: "sa-name" <1>
type: kubernetes.io/service-account-token <2>
----
<1> Specifies an existing service account name. If you are creating both the `ServiceAccount` and the `Secret` objects, create the `ServiceAccount` object first.
<2> Specifies a service account token secret.

. Use the following command to create the `Secret` object:
+
[source,terminal]
----
$ oc create -f <filename>.yaml
----

. To use the secret in a pod:

.. Update the pod's service account to reference the secret, as shown in the "Understanding how to create secrets" section.

.. Create the pod, which consumes the secret as an environment variable or as a file (using a `secret` volume), as shown in the "Understanding how to create secrets" section.
