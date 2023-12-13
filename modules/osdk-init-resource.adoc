// Module included in the following assemblies:
//
// * operators/operator_sdk/osdk-generating-csvs.adoc

:_mod-docs-content-type: PROCEDURE
[id="osdk-init-resource_{context}"]
= Initializing required custom resources

An Operator might require the user to instantiate a custom resource before the Operator can be fully functional. However, it can be challenging for a user to determine what is required or how to define the resource.

As an Operator developer, you can specify a single required custom resource by adding `operatorframework.io/initialization-resource` to the cluster service version (CSV) during Operator installation. You are then prompted to create the custom resource through a template that is provided in the CSV.
The annotation must include a template that contains a complete YAML definition that is required to initialize the resource during installation.

If this annotation is defined, after installing the Operator from the {product-title} web console, the user is prompted to create the resource using the template provided in the CSV.

.Procedure

* Add the `operatorframework.io/initialization-resource` annotation to the CSV of your Operator to specify a required custom resource. For example, the following annotation requires the creation of a `StorageCluster` resource and provides a full YAML definition:
+
.Initialization resource annotation
[source,yaml]
----
apiVersion: operators.coreos.com/v1alpha1
kind: ClusterServiceVersion
metadata:
  name: my-operator-v1.2.3
  annotations:
    operatorframework.io/initialization-resource: |-
        {
            "apiVersion": "ocs.openshift.io/v1",
            "kind": "StorageCluster",
            "metadata": {
                "name": "example-storagecluster"
            },
            "spec": {
                "manageNodes": false,
                "monPVCTemplate": {
                    "spec": {
                        "accessModes": [
                            "ReadWriteOnce"
                        ],
                        "resources": {
                            "requests": {
                                "storage": "10Gi"
                            }
                        },
                        "storageClassName": "gp2"
                    }
                },
                "storageDeviceSets": [
                    {
                        "count": 3,
                        "dataPVCTemplate": {
                            "spec": {
                                "accessModes": [
                                    "ReadWriteOnce"
                                ],
                                "resources": {
                                    "requests": {
                                        "storage": "1Ti"
                                    }
                                },
                                "storageClassName": "gp2",
                                "volumeMode": "Block"
                            }
                        },
                        "name": "example-deviceset",
                        "placement": {},
                        "portable": true,
                        "resources": {}
                    }
                ]
            }
        }
...
----
