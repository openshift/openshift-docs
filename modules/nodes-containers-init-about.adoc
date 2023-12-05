// Module included in the following assemblies:
//
// * nodes/nodes-containers-init.adoc

:_mod-docs-content-type: CONCEPT
[id="nodes-containers-init-about_{context}"]
= Understanding Init Containers

You can use an Init Container resource to perform tasks before the rest of a pod is deployed.

A pod can have Init Containers in addition to application containers. Init
containers allow you to reorganize setup scripts and binding code.

An Init Container can:

* Contain and run utilities that are not desirable to include in the app Container image for security reasons.
* Contain utilities or custom code for setup that is not present in an app image. For example, there is no requirement to make an image FROM another image just to use a tool like sed, awk, python, or dig during setup.
* Use Linux namespaces so that they have different filesystem views from app containers, such as access to secrets that application containers are not able to access.

Each Init Container must complete successfully before the next one is started. So, Init Containers provide an easy way to block or delay the startup of app containers until some set of preconditions are met.

For example, the following are some ways you can use Init Containers:

* Wait for a service to be created with a shell command like:
+
[source,terminal]
----
for i in {1..100}; do sleep 1; if dig myservice; then exit 0; fi; done; exit 1
----

* Register this pod with a remote server from the downward API with a command like:
+
[source,terminal]
----
$ curl -X POST http://$MANAGEMENT_SERVICE_HOST:$MANAGEMENT_SERVICE_PORT/register -d ‘instance=$()&ip=$()’
----

* Wait for some time before starting the app Container with a command like `sleep 60`.

* Clone a git repository into a volume.

* Place values into a configuration file and run a template tool to dynamically generate a configuration file for the main app Container. For example, place the POD_IP value in a configuration and generate the main app configuration file using Jinja.

See the link:https://kubernetes.io/docs/concepts/workloads/pods/init-containers/[Kubernetes documentation] for more information.
