// Module included in the following assemblies:
//
// * applications/deployments/route-based-deployment-strategies.adoc

[id="deployments-n1-compatibility_{context}"]
= N-1 compatibility

Applications that have new code and old code running at the same time must be
careful to ensure that data written by the new code can be read and handled (or
gracefully ignored) by the old version of the code. This is sometimes called
_schema evolution_ and is a complex problem.

This can take many forms: data stored on disk, in a database, in a temporary
cache, or that is part of a user's browser session. While most web applications
can support rolling deployments, it is important to test and design your
application to handle it.

For some applications, the period of time that old code and new code is running
side by side is short, so bugs or some failed user transactions are acceptable.
For others, the failure pattern may result in the entire application becoming
non-functional.

One way to validate N-1 compatibility is to use an A/B deployment: run the old
code and new code at the same time in a controlled way in a test environment,
and verify that traffic that flows to the new deployment does not cause failures
in the old deployment.
