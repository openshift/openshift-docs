// Module included in the following assemblies:
//
// * security/container_security/security-build.adoc

[id="security-build-once_{context}"]
= Building once, deploying everywhere

Using {product-title} as the standard platform for container builds enables you
to guarantee the security of the build environment. Adhering to a "build once,
deploy everywhere" philosophy ensures that the product of the build process is
exactly what is deployed in production.

It is also important to maintain the immutability of your containers. You should
not patch running containers, but rebuild and redeploy them.

As your software moves through the stages of building, testing, and production, it is
important that the tools making up your software supply chain be trusted. The
following figure illustrates the process and tools that could be incorporated
into a trusted software supply chain for containerized software:

image::trustedsupplychain.png["", align="center"]

{product-title} can be integrated with trusted code repositories (such as GitHub)
and development platforms (such as Che) for creating and managing secure code.
Unit testing could rely on  
link:https://cucumber.io/[Cucumber] and link:https://junit.org/[JUnit].
You could inspect your containers for vulnerabilities and compliance issues
with link:https://anchore.com[Anchore] or Twistlock,
and use image scanning tools such as AtomicScan or Clair.
Tools such as link:https://sysdig.com[Sysdig] could provide ongoing monitoring
of your containerized applications.
