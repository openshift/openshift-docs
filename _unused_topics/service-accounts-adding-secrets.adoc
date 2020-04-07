// Module included in the following assemblies:
//
// * authentication/using-service-accounts.adoc

[id="service-accounts-managing-secrets_{context}"]
== Managing secrets on a service account's pod

In addition to providing API credentials, a pod's service account determines
which secrets the pod is allowed to use.

Pods use secrets in two ways:

* image pull secrets, providing credentials used to pull images for the pod's containers
* mountable secrets, injecting the contents of secrets into containers as files

To allow a secret to be used as an image pull secret by a service account's
pods, run:

----
$ oc secrets link --for=pull <serviceaccount-name> <secret-name>
----

To allow a secret to be mounted by a service account's pods, run:

----
$ oc secrets link --for=mount <serviceaccount-name> <secret-name>
----

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

This example creates and adds secrets to a service account:

----
$ oc create secret generic secret-plans \
    --from-file=plan1.txt \
    --from-file=plan2.txt
secret/secret-plans

$ oc create secret docker-registry my-pull-secret \
    --docker-username=mastermind \
    --docker-password=12345 \
    --docker-email=mastermind@example.com
secret/my-pull-secret

$ oc secrets link robot secret-plans --for=mount

$ oc secrets link robot my-pull-secret --for=pull

$ oc describe serviceaccount robot
Name:               robot
Labels:             <none>
Image pull secrets:	robot-dockercfg-624cx
                   	my-pull-secret

Mountable secrets: 	robot-token-uzkbh
                   	robot-dockercfg-624cx
                   	secret-plans

Tokens:            	robot-token-8bhpp
                   	robot-token-uzkbh
----
