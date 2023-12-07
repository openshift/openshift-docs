// Module included in the following assemblies:
// * openshift_images/using-image-pull-secrets

:_mod-docs-content-type: PROCEDURE
[id="images-allow-pods-to-reference-images-across-projects_{context}"]
= Allowing pods to reference images across projects

When using the {product-registry}, to allow pods in `project-a` to reference images in `project-b`, a service account in `project-a` must be bound to the `system:image-puller` role in `project-b`.

[NOTE]
====
When you create a pod service account or a namespace, wait until the service account is provisioned with a docker pull secret; if you create a pod before its service account is fully provisioned, the pod fails to access the {product-registry}.
====

.Procedure

. To allow pods in `project-a` to reference images in `project-b`, bind a service account in `project-a` to the `system:image-puller` role in `project-b`:
+
[source,terminal]
----
$ oc policy add-role-to-user \
    system:image-puller system:serviceaccount:project-a:default \
    --namespace=project-b
----
+
After adding that role, the pods in `project-a` that reference the default service account are able to pull images from `project-b`.

. To allow access for any service account in `project-a`, use the group:
+
[source,terminal]
----
$ oc policy add-role-to-group \
    system:image-puller system:serviceaccounts:project-a \
    --namespace=project-b
----
