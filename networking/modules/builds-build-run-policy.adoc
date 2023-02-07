// Module included in the following assemblies:
//
// * builds/advanced-build-operations.adoc

[id="builds-build-run-policy_{context}"]
= Build run policy

The build run policy describes the order in which the builds created from the build configuration should run. This can be done by changing the value of the `runPolicy` field in the `spec` section of the `Build` specification.

It is also possible to change the `runPolicy` value for existing build configurations, by:

* Changing `Parallel` to `Serial` or `SerialLatestOnly` and triggering a new build from this configuration causes the new build to wait until all parallel builds complete as the serial build can only run alone.
* Changing `Serial` to `SerialLatestOnly` and triggering a new build causes cancellation of all existing builds in queue, except the currently running build and the most recently created build. The newest build runs next.
