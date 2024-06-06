// Module included in the following assemblies:
//
// * applications/deployments/route-based-deployment-strategies.adoc

[id="deployments-ab-testing_{context}"]
= A/B deployments

The A/B deployment strategy lets you try a new version of the application in a
limited way in the production environment. You can specify that the production
version gets most of the user requests while a limited fraction of requests go
to the new version.

Because you control the portion of requests to each version, as testing
progresses you can increase the fraction of requests to the new version and
ultimately stop using the previous version. As you adjust the request load on
each version, the number of pods in each service might have to be scaled as well
to provide the expected performance.

In addition to upgrading software, you can use this feature to experiment with
versions of the user interface. Since some users get the old version and some
the new, you can evaluate the user's reaction to the different versions to
inform design decisions.

For this to be effective, both the old and new versions must be similar enough
that both can run at the same time. This is common with bug fix releases and
when new features do not interfere with the old. The versions require N-1
compatibility to properly work together.

{product-title} supports N-1 compatibility through the web console as well as
the CLI.
