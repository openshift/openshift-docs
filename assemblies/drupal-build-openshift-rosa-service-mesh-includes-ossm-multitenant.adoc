////
Module included in the following assemblies:
-ossm-vs-community.adoc
////

[id="ossm-multitenant-install_{context}"]
= Multitenant installations

Whereas upstream Istio takes a single tenant approach, {SMProductName} supports multiple independent control planes within the cluster. {SMProductName} uses a multitenant operator to manage the control plane lifecycle.

{SMProductName} installs a multitenant control plane by default. You specify the projects that can access the {SMProductShortName}, and isolate the {SMProductShortName} from other control plane instances.

[id="ossm-mt-vs-clusterwide_{context}"]
== Multitenancy versus cluster-wide installations

The main difference between a multitenant installation and a cluster-wide installation is the scope of privileges used by istod. The components no longer use cluster-scoped Role Based Access Control (RBAC) resource `ClusterRoleBinding`.

Every project in the `ServiceMeshMemberRoll` `members` list will have a `RoleBinding` for each service account associated with the control plane deployment and each control plane deployment will only watch those member projects. Each member project has a `maistra.io/member-of` label added to it, where the `member-of` value is the project containing the control plane installation.

{SMProductName} configures each member project to ensure network access between itself, the control plane, and other member projects. The exact configuration differs depending on how {product-title} software-defined networking (SDN) is configured. See About OpenShift SDN for additional details.

If the {product-title} cluster is configured to use the SDN plugin:

* *`NetworkPolicy`*: {SMProductName} creates a `NetworkPolicy` resource in each member project allowing ingress to all pods from the other members and the control plane. If you remove a member from {SMProductShortName}, this `NetworkPolicy` resource is deleted from the project.
+
[NOTE]
====
This also restricts ingress to only member projects. If you require ingress from non-member projects, you need to create a `NetworkPolicy` to allow that traffic through.
====

* *Multitenant*: {SMProductName} joins the `NetNamespace` for each member project to the `NetNamespace` of the control plane project (the equivalent of running `oc adm pod-network join-projects --to control-plane-project member-project`). If you remove a member from the {SMProductShortName}, its `NetNamespace` is isolated from the control plane (the equivalent of running `oc adm pod-network isolate-projects member-project`).

* *Subnet*: No additional configuration is performed.

[id="ossm-cluster-scoped-resources_{context}"]
== Cluster scoped resources

Upstream Istio has two cluster scoped resources that it relies on. The `MeshPolicy` and the `ClusterRbacConfig`. These are not compatible with a multitenant cluster and have been replaced as described below.

* _ServiceMeshPolicy_ replaces MeshPolicy for configuration of control-plane-wide authentication policies. This must be created in the same project as the control plane.
* _ServicemeshRbacConfig_ replaces ClusterRbacConfig for configuration of control-plane-wide role based access control. This must be created in the same project as the control plane.
