// Module included in the following assemblies:
//
// * security/container_security/security-understanding.adoc

[id="security-understanding-openshift_{context}"]
= What is {product-title}?

Automating how containerized applications are deployed, run, and managed is the
job of a platform such as {product-title}. At its core, {product-title} relies
on the Kubernetes project to provide the engine for orchestrating containers
across many nodes in scalable data centers.

Kubernetes is a project, which can run using different operating systems
and add-on components that offer no guarantees of supportability from the project.
As a result, the security of different Kubernetes platforms can vary.

{product-title} is designed to lock down Kubernetes security and integrate
the platform with a variety of extended components. To do this,
{product-title} draws on the extensive Red Hat ecosystem of open source
technologies that include the operating systems, authentication, storage,
networking, development tools, base container images, and many other
components.

{product-title} can leverage Red Hat's experience in uncovering
and rapidly deploying fixes for vulnerabilities in the platform itself
as well as the containerized applications running on the platform.
Red Hat's experience also extends to efficiently integrating new
components with {product-title} as they become available and
adapting technologies to individual customer needs.
