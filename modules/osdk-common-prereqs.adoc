// Module included in the following assemblies:
//
// * operators/operator_sdk/golang/osdk-golang-quickstart.adoc
// * operators/operator_sdk/golang/osdk-golang-tutorial.adoc
// * operators/operator_sdk/ansible/osdk-ansible-quickstart.adoc
// * operators/operator_sdk/ansible/osdk-ansible-tutorial.adoc
// * operators/operator_sdk/helm/osdk-helm-quickstart.adoc
// * operators/operator_sdk/helm/osdk-helm-tutorial.adoc
// * operators/operator_sdk/helm/osdk-hybrid-helm.adoc
// * operators/operator_sdk/osdk-working-bundle-images.adoc
// * operators/operator_sdk/java/osdk-java-quickstart.adoc
// * operators/operator_sdk/java/osdk-java-tutorial.adoc

ifeval::["{context}" == "osdk-ansible-quickstart"]
:ansible:
endif::[]
ifeval::["{context}" == "osdk-ansible-tutorial"]
:ansible:
endif::[]
ifeval::["{context}" == "osdk-golang-quickstart"]
:golang:
endif::[]
ifeval::["{context}" == "osdk-golang-tutorial"]
:golang:
endif::[]
ifeval::["{context}" == "osdk-java-quickstart"]
:java:
endif::[]
ifeval::["{context}" == "osdk-java-tutorial"]
:java:
endif::[]

[id="osdk-common-prereqs_{context}"]
= Prerequisites

* Operator SDK CLI installed
* OpenShift CLI (`oc`) {product-version}+ installed
ifdef::golang[]
* link:https://golang.org/dl/[Go] 1.19+
endif::[]
ifdef::ansible[]
* link:https://docs.ansible.com/ansible/latest/roadmap/ROADMAP_2_15.html[Ansible] 2.15.0
* link:https://ansible-runner.readthedocs.io/en/latest/install.html[Ansible Runner] 2.3.3+
* link:https://github.com/ansible/ansible-runner-http[Ansible Runner HTTP Event Emitter plugin] 1.0.0+
* link:https://www.python.org/downloads/[Python] 3.9+
* link:https://pypi.org/project/kubernetes/[Python Kubernetes client]
endif::[]
ifdef::java[]
* link:https://java.com/en/download/help/download_options.html[Java] 11+
* link:https://maven.apache.org/install.html[Maven] 3.6.3+
endif::[]
ifndef::openshift-dedicated,openshift-rosa[]
* Logged into an {product-title} {product-version} cluster with `oc` with an account that has `cluster-admin` permissions
endif::openshift-dedicated,openshift-rosa[]
ifdef::openshift-dedicated,openshift-rosa[]
* Logged into an {product-title} cluster with `oc` with an account that has `dedicated-admin` permissions
endif::openshift-dedicated,openshift-rosa[]
* To allow the cluster to pull the image, the repository where you push your image must be set as public, or you must configure an image pull secret

ifeval::["{context}" == "osdk-ansible-quickstart"]
:!ansible:
endif::[]
ifeval::["{context}" == "osdk-ansible-tutorial"]
:!ansible:
endif::[]
ifeval::["{context}" == "osdk-golang-quickstart"]
:!golang:
endif::[]
ifeval::["{context}" == "osdk-golang-tutorial"]
:!golang:
endif::[]
ifeval::["{context}" == "osdk-java-quickstart"]
:!java:
endif::[]
ifeval::["{context}" == "osdk-java-tutorial"]
:!java:
endif::[]
