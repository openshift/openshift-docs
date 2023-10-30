:_mod-docs-content-type: ASSEMBLY
[id="deploying-a-spring-boot-application-with-argo-cd"]
= Deploying a Spring Boot application with Argo CD
include::_attributes/common-attributes.adoc[]
:context: deploying-a-spring-boot-application-with-argo-cd

toc::[]

With Argo CD, you can deploy your applications to the OpenShift cluster either by using the Argo CD dashboard or by using the `oc` tool.

.Prerequisites

* Red Hat OpenShift GitOps is installed in your cluster.
* Logged into Argo CD instance.

include::modules/gitops-creating-an-application-by-using-the-argo-cd-dashboard.adoc[leveloffset=+1]

include::modules/gitops-creating-an-application-by-using-the-oc-tool.adoc[leveloffset=+1]

include::modules/gitops-verifying-argo-cd-self-healing-behavior.adoc[leveloffset=+1]
