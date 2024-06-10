// Module included in the following assemblies:
// * service_mesh/v2x/ossm-deploy-mod-v2x.adoc

:_mod-docs-content-type: CONCEPT
[id="ossm-deploy-multitenant_{context}"]
= Multitenant deployment model

{SMProductName} installs a `ServiceMeshControlPlane` that is configured for multitenancy by default. {SMProductName} uses a multitenant Operator to manage the {SMProductShortName} control plane lifecycle. Within a mesh, namespaces are used for tenancy.

{SMProductName} uses `ServiceMeshControlPlane` resources to manage mesh installations, whose scope is limited by default to namespace that contains the resource. You use `ServiceMeshMemberRoll` and `ServiceMeshMember` resources to include additional namespaces into the mesh. A namespace can only be included in a single mesh, and multiple meshes can be installed in a single OpenShift cluster.

Typical service mesh deployments use a single {SMProductShortName} control plane to configure communication between services in the mesh. {SMProductName} supports “soft multitenancy”, where there is one control plane and one mesh per tenant, and there can be multiple independent control planes within the cluster. Multitenant deployments specify the projects that can access the {SMProductShortName} and isolate the {SMProductShortName} from other control plane instances.

The cluster administrator gets control and visibility across all the Istio control planes, while the tenant administrator only gets control over their specific {SMProductShortName}, Kiali, and Jaeger instances.

You can grant a team permission to deploy its workloads only to a given namespace or set of namespaces. If granted the `mesh-user` role by the service mesh administrator, users can create a `ServiceMeshMember` resource to add namespaces to the `ServiceMeshMemberRoll`.
