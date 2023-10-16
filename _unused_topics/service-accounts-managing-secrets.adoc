// Module included in the following assemblies:
//
// * authentication/using-service-accounts.adoc

[id="service-accounts-managing-secrets_{context}"]
= Managing allowed secrets

You can use the service account's secrets in your application's pods for:

* Image pull secrets, providing credentials used to pull images for the pod's containers
* Mountable secrets, injecting the contents of secrets into containers as files

.Procedure

. Create a secret:
+
----
$ oc create secret generic <secret_name> \
    --from-file=<file>.txt

secret/<secret_name>
----

. To allow a secret to be used as an image pull secret by a service account's
pods, run:
+
----
$ oc secrets link --for=pull <serviceaccount-name> <secret-name>
----

. To allow a secret to be mounted by a service account's pods, run:
+
----
$ oc secrets link --for=mount <serviceaccount-name> <secret-name>
----

. Confirm that the secret was added to the service account:
+
----
$ oc describe serviceaccount <serviceaccount-name>
Name:               <serviceaccount-name>
Labels:             <none>
Image pull secrets:	robot-dockercfg-624cx
                   	my-pull-secret

Mountable secrets: 	robot-token-uzkbh
                   	robot-dockercfg-624cx
                   	secret-plans

Tokens:            	robot-token-8bhpp
                   	robot-token-uzkbh
----

////
[NOTE]
====
Limiting secrets to only the service accounts that reference them is disabled by
default. This means that if `serviceAccountConfig.limitSecretReferences` is set
to `false` (the default setting) in the master configuration file, mounting
secrets to a service account's pods with the `--for=mount` option is not
required. However, using the `--for=pull` option to enable using an image pull
secret is required, regardless of the
`serviceAccountConfig.limitSecretReferences` value.
====
////
