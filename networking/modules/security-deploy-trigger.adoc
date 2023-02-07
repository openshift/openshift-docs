// Module included in the following assemblies:
//
// * security/container_security/security-deploy.adoc

[id="security-deploy-trigger_{context}"]
= Controlling container deployments with triggers

If something happens during the build process, or if a vulnerability is
discovered after an image has been deployed, you can use tooling for automated,
policy-based deployment to remediate. You can use triggers to rebuild and replace images,
ensuring the immutable containers process,
instead of patching running containers, which is not recommended.

image::secure_deployments.png["Secure Deployments", align="center"]

For example, you build an application using three container image layers: core,
middleware, and applications. An issue is discovered in the core image and that
image is rebuilt. After the build is complete, the image is pushed to your
OpenShift Container Registry. {product-title} detects that the image has changed
and automatically rebuilds and deploys the application image, based on the
defined triggers. This change incorporates the fixed libraries and ensures that
the production code is identical to the most current image.

You can use the `oc set triggers` command to set a deployment trigger.
For example, to set a trigger for a deployment called
deployment-example:

[source,terminal]
----
$ oc set triggers deploy/deployment-example \
    --from-image=example:latest \
    --containers=web
----
