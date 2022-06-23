// Module included in the following assemblies:
//
// applications/projects/working-with-projects.adoc

[id="odc-customizing-available-cluster-roles-using-developer-perspective_{context}"]
= Customizing the available cluster roles using the Developer perspective

The users of a project are assigned to a cluster role based on their access control. You can access these cluster roles by navigating to the *Project* -> *Project access* -> *Role*. By default, these roles are *Admin*, *Edit*, and *View*.

To add or edit the cluster roles for a project, you can customize the YAML code of the cluster.

.Procedure
To customize the different cluster roles of a project:

. In the *Search* view, use the *Resources* drop-down list to search for `Console`.
. From the available options, select the *Console `operator.openshift.io/v1`*.
+
.Searching Console resource
image::odc_cluster_console.png[]
. Select *cluster* under the *Name* list.
. Navigate to the *YAML* tab to view and edit the YAML code.
. In the YAML code under `spec`, add or edit the list of `availableClusterRoles` and save your changes:
+
[source,yaml]
----
spec:
  customization:
    projectAccess:
      availableClusterRoles:
      - admin
      - edit
      - view
----
