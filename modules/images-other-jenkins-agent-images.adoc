// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins-agent.adoc

:_mod-docs-content-type: REFERENCE
[id="images-other-jenkins-agent-images_{context}"]
= Jenkins agent images

The {product-title} Jenkins agent images are available on link:https://quay.io[Quay.io] or link:https://registry.redhat.io[registry.redhat.io].

Jenkins images are available through the Red Hat Registry:

[source,terminal]
----
$ docker pull registry.redhat.io/ocp-tools-4/jenkins-rhel8:<image_tag>
----

[source,terminal]
----
$ docker pull registry.redhat.io/ocp-tools-4/jenkins-agent-base-rhel8:<image_tag>
----

To use these images, you can either access them directly from link:https://quay.io[Quay.io] or link:https://registry.redhat.io[registry.redhat.io] or push them into your {product-title} container image registry.
