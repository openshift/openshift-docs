// Module included in the following assemblies:
//
// * security/container_security/security-build.adoc

[id="security-build-designing_{context}"]
= Designing your build process

You can design your container image management and build process to use container layers so that you can separate control.

image::build_process2.png["Designing Your Build Process", align="center"]

For example, an operations team manages base images, while architects manage
middleware, runtimes, databases, and other solutions. Developers can then focus
on application layers and focus on writing code.

Because new vulnerabilities are identified daily, you need to proactively check
container content over time. To do this, you should integrate automated security
testing into your build or CI process. For example: 

* SAST / DAST – Static and Dynamic security testing tools.
* Scanners for real-time checking against known vulnerabilities. Tools like these
catalog the open source packages in your container, notify you of any known 
vulnerabilities, and update you when new vulnerabilities are discovered in
previously scanned packages.

Your CI process should include policies that flag builds with issues discovered
by security scans so that your team can take appropriate action to address those
issues. You should sign your custom built containers to ensure that nothing is
tampered with between build and deployment.

Using GitOps methodology, you can use the same CI/CD mechanisms to
manage not only your application configurations, but also your
{product-title} infrastructure.
