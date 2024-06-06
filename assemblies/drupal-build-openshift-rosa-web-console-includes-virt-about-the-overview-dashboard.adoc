// Module included in the following assemblies:
//
// * web_console/using-dashboard-to-get-cluster-information.adoc

:_mod-docs-content-type: CONCEPT
[id="virt-about-the-overview-dashboard_{context}"]
= About the {product-title} dashboards page

Access the {product-title} dashboard, which captures high-level information
about the cluster, by navigating to *Home* -> *Overview* from
the {product-title} web console.

The {product-title} dashboard provides various cluster information, captured in
individual dashboard cards.

The {product-title} dashboard consists of the following cards:

* *Details* provides a brief overview of informational cluster details.
+
Status include *ok*, *error*, *warning*, *in progress*, and *unknown*. Resources can add custom status names.
+
** Cluster ID
** Provider
** Version
* *Cluster Inventory* details number of resources and associated statuses. It is helpful when intervention is required to resolve problems, including information about:
** Number of nodes
** Number of pods
** Persistent storage volume claims
** Bare metal hosts in the cluster, listed according to their state (only available in *metal3* environment)
* *Status* helps administrators understand how cluster resources are consumed. Click on a resource to jump to a detailed page listing pods and nodes that consume the largest amount of the specified cluster resource (CPU, memory, or storage).
* *Cluster Utilization* shows the capacity of various resources over a specified period of time, to help administrators understand the scale and frequency of high resource consumption, including information about:
** CPU time
** Memory allocation
** Storage consumed
** Network resources consumed
** Pod count
* *Activity* lists messages related to recent activity in the cluster, such as pod creation or virtual machine migration to another host.

