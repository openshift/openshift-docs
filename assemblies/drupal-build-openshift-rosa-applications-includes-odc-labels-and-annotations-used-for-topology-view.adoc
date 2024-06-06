[id="odc-labels-and-annotations-used-for-topology-view_{context}"]
= Labels and annotations used for the Topology view

The *Topology* view uses the following labels and annotations:

Icon displayed in the node:: Icons in the node are defined by looking for matching icons using the `app.openshift.io/runtime` label, followed by the `app.kubernetes.io/name` label. This matching is done using a predefined set of icons.
Link to the source code editor or the source:: The `app.openshift.io/vcs-uri` annotation is used to create links to the source code editor.
Node Connector:: The `app.openshift.io/connects-to` annotation is used to connect the nodes.
App grouping:: The `app.kubernetes.io/part-of=<appname>` label is used to group the applications, services, and components.

For detailed information on the labels and annotations {product-title} applications must use, see link:https://github.com/redhat-developer/app-labels/blob/master/labels-annotation-for-openshift.adoc[Guidelines for labels and annotations for OpenShift applications].
