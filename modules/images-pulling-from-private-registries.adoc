// Module included in the following assemblies:
// * openshift_images/using-image-pull-secrets

:_mod-docs-content-type: PROCEDURE
[id="images-pulling-from-private-registries_{context}"]
= Pulling from private registries with delegated authentication

A private registry can delegate authentication to a separate service. In these cases, image pull secrets must be defined for both the authentication and registry endpoints.

.Procedure

. Create a secret for the delegated authentication server:
+
[source,terminal]
----
$ oc create secret docker-registry \
    --docker-server=sso.redhat.com \
    --docker-username=developer@example.com \
    --docker-password=******** \
    --docker-email=unused \
    redhat-connect-sso

secret/redhat-connect-sso
----
+
. Create a secret for the private registry:
+
[source,terminal]
----
$ oc create secret docker-registry \
    --docker-server=privateregistry.example.com \
    --docker-username=developer@example.com \
    --docker-password=******** \
    --docker-email=unused \
    private-registry

secret/private-registry
----
