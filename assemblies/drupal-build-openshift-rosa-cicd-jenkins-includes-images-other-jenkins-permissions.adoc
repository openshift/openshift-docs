// Module included in the following assemblies:
//
// * cicd/jenkins/images-other-jenkins.adoc

:_mod-docs-content-type: CONCEPT
[id="images-other-jenkins-permissions_{context}"]
= Jenkins permissions

If in the config map the `<serviceAccount>` element of the pod template XML is the {product-title} service account used for the resulting pod, the service account credentials are mounted into the pod. The permissions are associated with the service account and control which operations against the {product-title} master are allowed from the pod.

Consider the following scenario with service accounts used for the pod, which is launched by the Kubernetes Plugin that runs in the {product-title} Jenkins image.

If you use the example template for Jenkins that is provided by {product-title}, the `jenkins` service account is defined with the `edit` role for the project Jenkins runs in, and the master Jenkins pod has that service account mounted.

The two default Maven and NodeJS pod templates that are injected into the Jenkins configuration are also set to use the same service account as the Jenkins master.

* Any pod templates that are automatically discovered by the {product-title} sync plugin because their image streams or image stream tags have the required label or annotations are configured to use the Jenkins master service account as their service account.
* For the other ways you can provide a pod template definition into Jenkins and the Kubernetes plugin, you have to explicitly specify the service account to use. Those other ways include the Jenkins console, the `podTemplate` pipeline DSL that is provided by the Kubernetes plugin, or labeling a config map whose data is the XML configuration for a pod template.
* If you do not specify a value for the service account, the `default` service account is used.
* Ensure that whatever service account is used has the necessary permissions, roles, and so on defined within {product-title} to manipulate whatever projects you choose to manipulate from the within the pod.
