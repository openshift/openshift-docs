// Module included in the following assemblies:
//
// * support/remote_health_monitoring/about-remote-health-monitoring.adoc

[id="insights-operator-what-information-is-collected_{context}"]
= Information collected by the Insights Operator

The following information is collected by the Insights Operator:

* General information about your cluster and its components to identify issues that are specific to your {product-title} version and environment
* Configuration files, such as the image registry configuration, of your cluster to determine incorrect settings and issues that are specific to parameters you set
* Errors that occur in the cluster components
* Progress information of running updates, and the status of any component upgrades
* Details of the platform that {product-title} is deployed on, such as Amazon Web Services, and the region that the cluster is located in
ifndef::openshift-dedicated[]
* Cluster workload information transformed into discreet Secure Hash Algorithm (SHA) values, which allows Red Hat to assess workloads for security and version vulnerabilities without disclosing sensitive details
endif::openshift-dedicated[]
* If an Operator reports an issue, information is collected about core {product-title} pods in the `openshift-&#42;` and `kube-&#42;` projects. This includes state, resource, security context, volume information, and more.
