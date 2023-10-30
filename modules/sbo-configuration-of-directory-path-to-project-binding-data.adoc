// Module included in the following assemblies:
//
// * /applications/connecting_applications_to_services/projecting-binding-data.adoc

:_mod-docs-content-type: CONCEPT
[id="sbo-configuration-of-directory-path-to-project-binding-data_{context}"]
= Configuration of the directory path to project the binding data inside workload container

By default, {servicebinding-title} mounts the binding data as files at a specific directory in your workload resource. You can configure the directory path using the `SERVICE_BINDING_ROOT` environment variable setup in the container where your workload runs.

.Example: Binding data mounted as files
----
$SERVICE_BINDING_ROOT <1>
├── account-database <2>
│   ├── type <3>
│   ├── provider <4>
│   ├── uri
│   ├── username
│   └── password
└── transaction-event-stream <2>
    ├── type
    ├── connection-count
    ├── uri
    ├── certificates
    └── private-key
----
<1> Root directory.
<2> Directory that stores the binding data.
<3> Mandatory identifier that identifies the type of the binding data projected into the corresponding directory.
<4> Optional: Identifier to identify the provider so that the application can identify the type of backing service it can connect to.

To consume the binding data as environment variables, use the built-in language feature of your programming language of choice that can read environment variables.

.Example: Python client usage
----
import os
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
----

[WARNING]
====
.For using the binding data directory name to look up the binding data
{servicebinding-title} uses the `ServiceBinding` resource name (`.metadata.name`) as the binding data directory name. The spec also provides a way to override that name through the `.spec.name` field. As a result, there is a chance for binding data name collision if there are multiple `ServiceBinding` resources in the namespace. However, due to the nature of the volume mount in Kubernetes, the binding data directory will contain values from only one of the `Secret` resources.
====

[id="computation-of-the-final-path-for-projecting-the-binding-data-as-files_{context}"]
== Computation of the final path for projecting the binding data as files

The following table summarizes the configuration of how the final path for the binding data projection is computed when files are mounted at a specific directory:

.Summary of the final path computation
[cols="1,1",options="header"]
|===
| `SERVICE_BINDING_ROOT` | Final path

| Not available
| `/bindings/<ServiceBinding_ResourceName>`

| `dir/path/root`
| `dir/path/root/<ServiceBinding_ResourceName>`
|===

In the previous table, the `<ServiceBinding_ResourceName>` entry specifies the name of the `ServiceBinding` resource that you configure in the `.metadata.name` section of the custom resource (CR).

[NOTE]
====
By default, the projected files get their permissions set to 0644.  {servicebinding-title} cannot set specific permissions due to a bug in Kubernetes that causes issues if the service expects specific permissions such as `0600`.  As a workaround, you can modify the code of the program or the application that is running inside a workload resource to copy the file to the `/tmp` directory and set the appropriate permissions.
====

To access and consume the binding data within the existing `SERVICE_BINDING_ROOT` environment variable, use the built-in language feature of your programming language of choice that can read environment variables.

.Example: Python client usage
----
from pyservicebinding import binding
try:
    sb = binding.ServiceBinding()
except binding.ServiceBindingRootMissingError as msg:
    # log the error message and retry/exit
    print("SERVICE_BINDING_ROOT env var not set")
sb = binding.ServiceBinding()
bindings_list = sb.bindings("postgresql")
----

In the previous example, the `bindings_list` variable contains the binding data for the `postgresql` database service type.
