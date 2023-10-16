// Module included in the following assemblies:
//
// * applications/deployments/route-based-deployment-strategies.adoc

[id="deployments-graceful-termination_{context}"]
= Graceful termination

{product-title} and Kubernetes give application instances time to shut down before removing them from load balancing rotations. However, applications must ensure they cleanly terminate user connections as well before they exit.

On shutdown, {product-title} sends a `TERM` signal to the processes in the container. Application code, on receiving `SIGTERM`, stop accepting new connections. This ensures that load balancers route traffic to other active instances. The application code then waits until all open connections are closed, or gracefully terminate individual connections at the next opportunity, before exiting.

After the graceful termination period expires, a process that has not exited is sent the `KILL` signal, which immediately ends the process. The
`terminationGracePeriodSeconds` attribute of a pod or pod template controls the graceful termination period (default 30 seconds) and can be customized per application as necessary.
