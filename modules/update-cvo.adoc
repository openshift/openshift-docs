// Module included in the following assemblies:
//
// * updating/understanding_updates/how-updates-work.adoc

:_mod-docs-content-type: CONCEPT
[id="update-cvo_{context}"]
= The Cluster Version Operator

// adding a poorly written, technically inaccurate skeleton of a module for now, which can be replaced/refined by SMEs as they see fit

The Cluster Version Operator (CVO) is the primary component that orchestrates and facilitates the {product-title} update process.
During installation and standard cluster operation, the CVO is constantly comparing the manifests of managed cluster Operators to in-cluster resources, and reconciling discrepancies to ensure that the actual state of these resources match their desired state.
