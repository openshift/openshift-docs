// Module is included in the following assemblies:
// * service_mesh/v2x/ossm-traffic-manage.adoc
//

[id="ossm-auto-route-annotations_{context}"]
= Route labels and annotations

Sometimes specific labels or annotations are needed in an OpenShift route.
ifdef::openshift-enterprise[]
For example, some advanced features in OpenShift routes are managed using special annotations. See "Route-specific annotations" in the following "Additional resources" section.
endif::[]

For this and other use cases, {SMProductName} will copy all labels and annotations present in the Istio gateway resource (with the exception of annotations starting with `kubectl.kubernetes.io`) into the managed OpenShift route resource.

If you need specific labels or annotations in the OpenShift routes created by {SMProductShortName}, create them in the Istio gateway resource and they will be copied into the OpenShift route resources managed by the {SMProductShortName}.
