// Module included in the following assemblies:
//
// * applications/deployments/deployment-strategies.adoc

[id="deployments-canary-deployments_{context}"]
= Canary deployments

All rolling deployments in {product-title} are _canary deployments_; a new version (the canary) is tested before all of the old instances are replaced. If the readiness check never succeeds, the canary instance is removed and the `DeploymentConfig` object will be automatically rolled back.

The readiness check is part of the application code and can be as sophisticated as necessary to ensure the new instance is ready to be used. If you must implement more complex checks of the application (such as sending real user workloads to the new instance), consider implementing a custom deployment or using a blue-green deployment strategy.
