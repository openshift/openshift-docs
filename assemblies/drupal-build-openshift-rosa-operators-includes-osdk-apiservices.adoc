// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

:_mod-docs-content-type: CONCEPT
[id="osdk-apiservices_{context}"]
= Understanding your API services

As with CRDs, there are two types of API services that your Operator may use: _owned_ and _required_.

[id="osdk-apiservices-owned_{context}"]
== Owned API services

When a CSV owns an API service, it is responsible for describing the deployment of the extension `api-server` that backs it and the group/version/kind (GVK) it provides.

An API service is uniquely identified by the group/version it provides and can be listed multiple times to denote the different kinds it is expected to provide.

.Owned API service fields
[cols="2a,5a,2",options="header"]
|===
|Field |Description |Required/optional

|`Group`
|Group that the API service provides, for example `database.example.com`.
|Required

|`Version`
|Version of the API service, for example `v1alpha1`.
|Required

|`Kind`
|A kind that the API service is expected to provide.
|Required

|`Name`
|The plural name for the API service provided.
|Required

|`DeploymentName`
|Name of the deployment defined by your CSV that corresponds to your API service (required for owned API services). During the CSV pending phase, the OLM Operator searches the `InstallStrategy` of your CSV for a `Deployment` spec with a matching name, and if not found, does not transition the CSV to the "Install Ready" phase.
|Required

|`DisplayName`
|A human readable version of your API service name, for example `MongoDB Standalone`.
|Required

|`Description`
|A short description of how this API service is used by the Operator or a description of the functionality provided by the API service.
|Required

|`Resources`
a|Your API services own one or more types of Kubernetes objects. These are listed in the resources section to inform your users of the objects they might need to troubleshoot or how to connect to the application, such as the service or ingress rule that exposes a database.

It is recommended to only list out the objects that are important to a human, not an exhaustive list of everything you orchestrate. For example, do not list config maps that store internal state that are not meant to be modified by a user.
|Optional

|`SpecDescriptors`, `StatusDescriptors`, and `ActionDescriptors`
|Essentially the same as for owned CRDs.
|Optional
|===

[id="osdk-apiservices-resource-creation_{context}"]
=== API service resource creation

Operator Lifecycle Manager (OLM) is responsible for creating or replacing the service and API service resources for each unique owned API service:

* Service pod selectors are copied from the CSV deployment matching the `DeploymentName` field of the API service description.

* A new CA key/certificate pair is generated for each installation and the base64-encoded CA bundle is embedded in the respective API service resource.

[id="osdk-apiservices-service-certs_{context}"]
=== API service serving certificates

OLM handles generating a serving key/certificate pair whenever an owned API service is being installed. The serving certificate has a common name (CN) containing the hostname of the generated `Service` resource and is signed by the private key of the CA bundle embedded in the corresponding API service resource.

The certificate is stored as a type `kubernetes.io/tls` secret in the deployment namespace, and a volume named `apiservice-cert` is automatically appended to the volumes section of the deployment in the CSV matching the `DeploymentName` field of the API service description.

If one does not already exist, a volume mount with a matching name is also appended to all containers of that deployment. This allows users to define a volume mount with the expected name to accommodate any custom path requirements. The path of the generated volume mount defaults to `/apiserver.local.config/certificates` and any existing volume mounts with the same path are replaced.

[id="osdk-apiservice-required_{context}"]
== Required API services

OLM ensures all required CSVs have an API service that is available and all expected GVKs are discoverable before attempting installation. This allows a CSV to rely on specific kinds provided by API services it does not own.

.Required API service fields
[cols="2a,5a,2",options="header"]
|===
|Field |Description |Required/optional

|`Group`
|Group that the API service provides, for example `database.example.com`.
|Required

|`Version`
|Version of the API service, for example `v1alpha1`.
|Required

|`Kind`
|A kind that the API service is expected to provide.
|Required

|`DisplayName`
|A human readable version of your API service name, for example `MongoDB Standalone`.
|Required

|`Description`
|A short description of how this API service is used by the Operator or a description of the functionality provided by the API service.
|Required
|===
