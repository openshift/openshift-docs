// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

[id="osdk-crds-owned_{context}"]
= Owned CRDs

The custom resource definitions (CRDs) owned by your Operator are the most important part of your CSV. This establishes the link between your Operator and the required RBAC rules, dependency management, and other Kubernetes concepts.

It is common for your Operator to use multiple CRDs to link together concepts, such as top-level database configuration in one object and a representation of replica sets in another. Each one should be listed out in the CSV file.

.Owned CRD fields
[cols="2a,5a,2",options="header"]
|===
|Field |Description |Required/optional

|`Name`
|The full name of your CRD.
|Required

|`Version`
|The version of that object API.
|Required

|`Kind`
|The machine readable name of your CRD.
|Required

|`DisplayName`
|A human readable version of your CRD name, for example `MongoDB Standalone`.
|Required

|`Description`
|A short description of how this CRD is used by the Operator or a description of the functionality provided by the CRD.
|Required

|`Group`
|The API group that this CRD belongs to, for example `database.example.com`.
|Optional

|`Resources`
a|Your CRDs own one or more types of Kubernetes objects. These are listed in the `resources` section to inform your users of the objects they might need to troubleshoot or how to connect to the application, such as the service or ingress rule that exposes a database.

It is recommended to only list out the objects that are important to a human, not an exhaustive list of everything you orchestrate. For example, do not list config maps that store internal state that are not meant to be modified by a user.
|Optional

|`SpecDescriptors`, `StatusDescriptors`, and `ActionDescriptors`
a|These descriptors are a way to hint UIs with certain inputs or outputs of your Operator that are most important to an end user. If your CRD contains the name of a secret or config map that the user must provide, you can specify that here. These items are linked and highlighted in compatible UIs.

There are three types of descriptors:

* `SpecDescriptors`: A reference to fields in the `spec` block of an object.
* `StatusDescriptors`: A reference to fields in the `status` block of an object.
* `ActionDescriptors`: A reference to actions that can be performed on an object.

All descriptors accept the following fields:

* `DisplayName`: A human readable name for the `Spec`, `Status`, or `Action`.
* `Description`: A short description of the `Spec`, `Status`, or `Action` and how it is used by the Operator.
* `Path`: A dot-delimited path of the field on the object that this descriptor describes.
* `X-Descriptors`: Used to determine which "capabilities" this descriptor has and which UI component to use. See the *openshift/console* project for a canonical link:https://github.com/openshift/console/tree/release-4.3/frontend/packages/operator-lifecycle-manager/src/components/descriptors/types.ts[list of React UI X-Descriptors] for {product-title}.

Also see the *openshift/console* project for more information on link:https://github.com/openshift/console/tree/release-4.3/frontend/packages/operator-lifecycle-manager/src/components/descriptors[Descriptors] in general.
|Optional

|===

The following example depicts a `MongoDB Standalone` CRD that requires some user input in the form of a secret and config map, and orchestrates services, stateful sets, pods and config maps:

[id="osdk-crds-owned-example_{context}"]
.Example owned CRD
[source,yaml]
----
      - displayName: MongoDB Standalone
        group: mongodb.com
        kind: MongoDbStandalone
        name: mongodbstandalones.mongodb.com
        resources:
          - kind: Service
            name: ''
            version: v1
          - kind: StatefulSet
            name: ''
            version: v1beta2
          - kind: Pod
            name: ''
            version: v1
          - kind: ConfigMap
            name: ''
            version: v1
        specDescriptors:
          - description: Credentials for Ops Manager or Cloud Manager.
            displayName: Credentials
            path: credentials
            x-descriptors:
              - 'urn:alm:descriptor:com.tectonic.ui:selector:core:v1:Secret'
          - description: Project this deployment belongs to.
            displayName: Project
            path: project
            x-descriptors:
              - 'urn:alm:descriptor:com.tectonic.ui:selector:core:v1:ConfigMap'
          - description: MongoDB version to be installed.
            displayName: Version
            path: version
            x-descriptors:
              - 'urn:alm:descriptor:com.tectonic.ui:label'
        statusDescriptors:
          - description: The status of each of the pods for the MongoDB cluster.
            displayName: Pod Status
            path: pods
            x-descriptors:
              - 'urn:alm:descriptor:com.tectonic.ui:podStatuses'
        version: v1
        description: >-
          MongoDB Deployment consisting of only one host. No replication of
          data.
----
